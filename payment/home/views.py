from django.shortcuts import render
import razorpay
from .models import Coffee
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        client = razorpay.Client(auth =("rzp_test_7xU3UbNrd1gV2i" , "GRZe0YkBzcl0YqwjedwxF98C"))
        payment = client.order.create({'amount':amount, 'currency':'INR',
                              'payment_capture':'1' })
        
        coffee = Coffee(name = name , amount =amount , order_id = payment['id'])
        coffee.save()
        
        return render(request, 'index.html' ,{'payment':payment})
    
    return render(request, 'index.html')


@csrf_exempt
def success(request):
      if request.method == "POST":
        a =  (request.POST)
        order_id = ""
        for key , val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
      return render(request, "success.html")
