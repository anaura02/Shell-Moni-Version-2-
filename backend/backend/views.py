from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from banking.models import Customer


def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        # Get the incoming data from the request
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        try:
            # Look for the customer based on the username (email)
            customer = Customer.objects.get(email=username)  # Assuming username is email

            # Check if the password matches
            if customer.password == password:  # No hashing here for now
                # On successful login, redirect to the dashboard
                return JsonResponse({"success": True, "redirect_url": "/dashboard/"})
            else:
                return JsonResponse({"success": False, "message": "Invalid password"})
        except Customer.DoesNotExist:
            return JsonResponse({"success": False, "message": "Customer not found"})
        
        
def dashboard_view(request):
    return render(request, 'dashboard.html') 


