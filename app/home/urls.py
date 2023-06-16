from django.urls import path

import home.views as home

urlpatterns = [
    path('', home.home_view, name='home'),
    path('support/', home.support_view, name='support'),
    path('privacy/', home.privacy_view, name='privacy'),
    path('success/', home.success_view, name='success'),
    path('error/', home.error_view, name='error'),
    path('cancel/', home.cancel_view, name='cancel'),
    path('addtoslack/', home.add_to_slack, name='addtoslack'),
    path('callback/', home.callback, name='callback'),
]
