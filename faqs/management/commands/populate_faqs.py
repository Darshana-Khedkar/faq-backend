from django.core.management.base import BaseCommand
from faqs.models import FAQ
from googletrans import Translator


class Command(BaseCommand):
    help = 'Populate or update FAQ data with translations'

    def handle(self, *args, **kwargs):
        faq_data = [
            {
                'question': 'What is Django?',
                'answer': 'Django is a high-level Python web framework that allows rapid development of secure and maintainable websites.'
            },
            {
                'question': 'How do I install Django?',
                'answer': 'You can install Django using pip: `pip install django`.'
            }
        ]

        # Instantiate a translator
        translator = Translator()

        for data in faq_data:
            # Check if FAQ already exists (based on question)
            faq, created = FAQ.objects.get_or_create(question=data['question'], defaults={'answer': data['answer']})

            if created:
                self.stdout.write(self.style.SUCCESS(f"FAQ '{data['question']}' created"))
            else:
                self.stdout.write(self.style.SUCCESS(f"FAQ '{data['question']}' already exists, updating answer"))

            # Translate the question
            faq.question_hi = translator.translate(data['question'], src='en', dest='hi').text
            faq.question_bn = translator.translate(data['question'], src='en', dest='bn').text

            # Save the FAQ with translations
            faq.save()

            self.stdout.write(self.style.SUCCESS(f"FAQ '{data['question']}' updated with translations"))

