from django.shortcuts import get_object_or_404
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FAQ
from .serializers import FAQSerializer

@api_view(['GET'])
def faq_list(request):
    lang = request.GET.get('lang', 'en')
    cache_key = f'faqs_{lang}'
    faqs = cache.get(cache_key)

    if not faqs:
        faqs = FAQ.objects.all()
        data = [{ "question": faq.get_translated_question(lang), "answer": faq.answer } for faq in faqs]
        cache.set(cache_key, data, timeout=3600)  # Cache for 1 hour
    else:
        data = faqs

    return Response(data)
