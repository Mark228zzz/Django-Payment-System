from django.urls import path
from .views import pricing, create_checkout_session, success, cancel, webhook

urlpatterns = [
    path("", pricing, name="pricing"),
    path("create-checkout-session/", create_checkout_session, name="create_checkout_session"),
    path("success/", success, name="success"),
    path("cancel/", cancel, name="cancel"),
    path("webhook/", webhook, name="webhook"),
]
