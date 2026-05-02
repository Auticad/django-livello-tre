from django.forms import ModelForm

from blog.models import BlogPost


class BlogPostModelForm(ModelForm):

    class Meta:
        model = BlogPost
        fields = "__all__"