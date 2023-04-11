import json
import random
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import create_excel_file

# Create your views here.
def home(request):
    return render(request, 'home.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

@csrf_exempt
def generate_menu(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ingredients = data['ingredients']
        month = int(data['month'])

        # Generate a random menu
        menu = "Random menu for month " + str(month) + ":\n"
        for i in range(1, 31):  # Assuming a 30-day month
            menu += "Day " + str(i) + ":\n"
            menu += "  Breakfast: " + random.choice(ingredients) + "\n"
            menu += "  Lunch: " + random.choice(ingredients) + "\n"
            menu += "  Dinner: " + random.choice(ingredients) + "\n\n"

        # Create an Excel file and save it to the server
        filename = create_excel_file(menu, month)

        return JsonResponse({'menu': menu, 'filename': filename})

def download_menu(request, filename):
    with open(f'app/generated_files/{filename}', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response

def menu_generator(request):
    return render(request, 'app/menu_generator.html')