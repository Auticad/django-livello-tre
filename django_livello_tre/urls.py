"""
URL configuration for django_livello_tre project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from blog.views import blog_post_editor
from forms_app.views import contact_view, HomeTemplateView, register_account

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeTemplateView.as_view(), name="homepage"),
    # path("contact-us/", contact_view, name="contact-page"),
    path("blog-post-editor/", blog_post_editor, name="post-editor"),
    path("contact/", include("contact.urls")),
]

urlpatterns += [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/new/", register_account, name="register-account"),
]