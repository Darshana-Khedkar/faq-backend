from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    def test_translation(self):
        faq = FAQ.objects.get(question="What is Django?")
        self.assertTrue(faq.question_hi)
        self.assertTrue(faq.question_bn)
