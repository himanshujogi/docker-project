from locale import currency
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.

def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        amount=50000
        client=razorpay.Client(
            auth=("rzp_test_tQ2y8Du41bhF39","BZZQlEIb5pQ6dnC9cUkdlAb6")
        )
        payment=client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    return render(request, 'index.html')
@csrf_exempt
def success(request):
    return render(request,'success.html')
