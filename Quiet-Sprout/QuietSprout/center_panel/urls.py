from django.urls import path
from django.views.generic import TemplateView
from center_panel import views

app_name = 'center_panel'
urlpatterns = [
        path('', TemplateView.as_view(template_name="index.html" , extra_context={'center_template' : 'center_panel/center_panel.html'}), name='default-panel'),
        path('identity/', views.IdentityView.as_view(), name='identity'),
        path('explore-pilots/', views.ExploreView.as_view(), name='explore-pilots'),
        path('pilot/<str:username>/', views.PilotProfileView.as_view(), name='view-pilot'),
        path('midnight-logs/<str:username>', views.MidnightLogListView.as_view(), name='midnight-logs')
        ]
