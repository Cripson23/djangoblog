from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def blog_home(request):
    posts = Posts.objects.order_by('-date')
    return render(request, 'blog/blog_home.html', {'posts': posts})


class PostDetailView(DetailView):
    model = Posts
    template_name = 'blog/details_view.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Posts
    template_name = 'blog/update.html'

    form_class = PostsForm


class PostDeleteView(DeleteView):
    model = Posts
    success_url = '/blog'
    template_name = 'blog/delete.html'

    form_class = PostsForm


def create(request):
    error = ''
    if request.method == 'POST':
        form = PostsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
        else:
            error = "Неверное заполнение формы"

    form = PostsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'blog/create.html', data)
