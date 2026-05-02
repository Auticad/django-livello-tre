from django.http import HttpResponse
from django.shortcuts import render

from blog.forms import BlogPostModelForm


def blog_post_editor(request):
    if request.method == "POST":
        form = BlogPostModelForm(request.POST)
        if form.is_valid():
            print("il form è valido!")
            new_post = form.save()
            print(f"Nuovo Post del Blog: {new_post}")
            return HttpResponse(f"<h1>Nuovo Post!</h1><p>{new_post.title}</p>")
    form = BlogPostModelForm()
    context = {"form": form}
    return render(request, "blog/post_editor.html", context)
