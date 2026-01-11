from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from left_panel import models as l_models
from django.contrib.auth import models as auth_models
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class ExploreView(LoginRequiredMixin, generic.ListView):
    model = l_models.Identity
    template_name = 'index.html'
    context_object_name = 'pilots'
    paginate_by = 20
    extra_context = {
            'center_template' : 'center_panel/explore.html'
            }
    def get_queryset(self):
        return l_models.Identity.objects.exclude(user=self.request.user)

class IdentityView(LoginRequiredMixin,View):
    def get(self, request):
        pilot, created = l_models.Identity.objects.get_or_create(user=request.user)
        ctx =  {'center_template' : 'center_panel/identity.html', 'pilot' : pilot }
        return render(request, 'index.html', ctx)
    def post(self, request):
        pilot, created = l_models.Identity.objects.get_or_create(user=request.user)

        status = request.POST.get('pilot_status')
        image = request.FILES.get('pilot_image')
        about_h = request.POST.get('about_heading')
        about = request.POST.get('about')
        if status:
            pilot.status = status

        if image:
            pilot.profile_picture = image

        if about_h:
            pilot.about_heading = about_h

        if about:
            pilot.about = about

        pilot.save()
        return redirect('center_panel:identity')

class PilotProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'
    extra_context = {'center_template' : 'center_panel/center_panel.html'}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        username_from_url = self.kwargs.get('username')
        viewed_user = get_object_or_404(auth_models.User, username=username_from_url)

        context['display_user'] = viewed_user
        context['is_external_view'] = True

        return context

