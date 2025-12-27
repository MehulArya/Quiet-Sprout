from left_panel import models
from django.contrib.auth import models as auth_model
def pilot_context(request):
    if request.user.is_authenticated:
        pilot, created = models.Identity.objects.get_or_create(user=request.user)
        return {'pilot' : pilot}
    return {}

def current_profile(request):
    if request.user.is_authenticated:
        profile_user = auth_model.User.objects.get(user=request.user)
        return {'profile_user' : profile_user}
    return {}
