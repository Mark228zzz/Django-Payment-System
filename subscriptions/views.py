import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Subscription

stripe.api_key = settings.STRIPE_SECRET_KEY

def pricing(request):
    """Render the subscription pricing page."""
    return render(request, "subscriptions/pricing.html", {
        "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY,
        "stripe_price_id": settings.STRIPE_PRICE_ID
    })

@csrf_exempt
def create_checkout_session(request):
    if request.method == "POST":
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                mode="subscription",
                line_items=[{
                    "price": settings.STRIPE_PRICE_ID,  # Using Stripe price ID
                    "quantity": 1
                }],
                success_url=request.build_absolute_uri("/success/"),
                cancel_url=request.build_absolute_uri("/cancel/"),
            )
            return JsonResponse({"sessionId": session.id})
        except Exception as e:
            print("Stripe Error:", str(e))  # Debugging error
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)


def success(request):
    """Subscription success page."""
    return render(request, "subscriptions/success.html")

def cancel(request):
    """Subscription cancellation page."""
    return render(request, "subscriptions/cancel.html")

@csrf_exempt
def webhook(request):
    """Handle Stripe webhooks for subscription events."""
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session["customer_details"]["email"]
        subscription_id = session["subscription"]
        customer_id = session["customer"]

        Subscription.objects.create(
            email=customer_email,
            stripe_subscription_id=subscription_id,
            stripe_customer_id=customer_id
        )

    return HttpResponse(status=200)
