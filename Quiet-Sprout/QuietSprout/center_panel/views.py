from django.shortcuts import render, redirect
from django.views import View
from left_panel import models
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class IdentityView(LoginRequiredMixin,View):
    def get(self, request):
        pilot, created = models.Identity.objects.get_or_create(user=request.user)
        ctx =  {'center_template' : 'center_panel/identity.html', 'pilot' : pilot }
        return render(request, 'index.html', ctx)
    def post(self, request):
        pilot, created = models.Identity.objects.get_or_create(user=request.user)

        status = request.POST.get('pilot_status')
        image = request.FILES.get('pilot_image')
        if status:
            pilot.status = status

        if image:
            pilot.profile_picture = image

        pilot.save()
        return redirect('center_panel:identity')

