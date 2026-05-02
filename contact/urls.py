from django.urls import path

from contact.views import contact_page

urlpatterns = [
    path("contact-page/", contact_page, name="contact-page")
]