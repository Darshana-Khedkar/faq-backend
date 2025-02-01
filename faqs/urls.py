from django.urls import path
from .views import faq_list

urlpatterns = [
    path('api/faqs/', faq_list, name='faq_list'),

]
