from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Post
from .forms import PostForm
from rest_framework import generics, filters, permissions
from .serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


def postList(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


@require_http_methods(["GET"])
def postDetailView(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Exception:
        return JsonResponse({"error": "post not found"}, 404)

    context = {
        "post": post
    }
    return render(request, 'blog/post_detail.html', context)


def postCreateView(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }

    return render(request, 'blog/post_form.html', context)


def postUpdateView(request, pk):
    form = PostForm()

    if request.method == "POST":
        try:
            post = Post.objects.get(id=pk)
        except:
            return JsonResponse({"error": "post not found"}, 404)

        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }

    return render(request, 'blog/post_form.html', context)


@require_http_methods(["GET", "POST"])
def postDeleteView(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {
        "post": post
    }

    if request.method == "POST":
        post.delete()
        return redirect("/")

    return render(request, 'blog/post_confirm_delete.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


# api views
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']
    permission_classes = [permissions.IsAuthenticated]


class PostRetriveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
