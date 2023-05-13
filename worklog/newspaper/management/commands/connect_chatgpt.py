import openai
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    openai.api_key = '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'


    def handle(self, *args, **options):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Please phrase 'Election Result 2023: All About Karnataka Election Results Time, Date And Coverage Online'"}
            ]
            )
        print(response['choices'][0]['message']['content'])
        
        