from django.shortcuts import get_object_or_404, render, redirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.conf import settings
from .models import Payment

def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name= request.POST.get('name')
        email = request.user.email
        amount= 100
        fee_type= request.POST.get('fee')
        state_ID= request.POST.get('state')
        pay = Payment(name=name,email=email,amount=amount,fee_type=fee_type,state_ID=state_ID).save()
        pays = Payment.objects.filter(email=email).last()
        return render(request, 'payment.html', {'payment': pays, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})

    return render(request, "connector.html")

def verify_payment(request, ref: str):
    trxref = request.GET["trxref"]
    if trxref != ref:
        messages.error(
            request,
            "The transaction reference passed was different from the actual reference. Please do not modify data during transactions",
        )
    payment: Payment = get_object_or_404(Payment, ref=ref)
    if payment.verify_payment():
        messages.success(
            request, f"Payment Completed Successfully, NGN #{payment.amount}."
        )
  
    else:
        messages.warning(request, "Sorry, your payment could not be confirmed.")
    return render(request, "connector.html")