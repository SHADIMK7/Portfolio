from django.urls import path
from . import views

urlpatterns = [
    path('', views.modals, name='modals'),
    path('tsa/', views.modals, name='tsa'),  # Include the 'tsa/' URL pattern
    # Other URL patterns for your app...
    path('send_email', views.send_email, name='send_email'),
]
