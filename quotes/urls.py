from django.urls import path, include
from . import views

urlpatterns = [
    # TODO 12: Add template view patterns
    #   - '' -> home view, name='home'
    #   - 'all/' -> all_quotes view, name='all_quotes'
    path('', views.home, name='home'),
    path('all/', views.all_quotes, name='all_quotes'),

    
    # TODO 13: Use include() to add all API routes under 'api/'
    path('api/', include('quotes.api_urls')),
]