import json
import requests
from django.http import JsonResponse
from django.views import View


class NumbersView(View):
    def get(self, request, *args, **kwargs):
        urls = request.GET.getlist('url')
        merged_numbers = set()

        for url in urls:
            try:
                response = requests.get(url, timeout=0.5)
                if response.status_code == 200:
                    data = response.json()
                    merged_numbers.update(data['numbers'])
            except requests.Timeout:
                pass

        response_data = {
            'numbers': sorted(merged_numbers)
        }
        print(response_data)
        return JsonResponse(response_data)
