from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, PostImageForm, PostVideoForm, PostPDFForm
from .models import  *
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = PostImageForm(request.POST, request.FILES)
        video_form = PostVideoForm(request.POST, request.FILES)
        pdf_form = PostPDFForm(request.POST, request.FILES)

        if post_form.is_valid() and image_form.is_valid() and video_form.is_valid() and pdf_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            images = image_form.cleaned_data['file_field']
            videos = video_form.cleaned_data['file_field']
            pdfs = pdf_form.cleaned_data['file_field']

            for image in images:
                Image.objects.create(post=post, image=image)

            for video in videos:
                Video.objects.create(post=post, video=video)

            for pdf in pdfs:
                PDF.objects.create(post=post, pdf=pdf)

            return redirect('post_detail', pk=post.pk)  # Redirect to post detail page

    else:
        post_form = PostForm()
        image_form = PostImageForm()
        video_form = PostVideoForm()
        pdf_form = PostPDFForm()

    return render(request, 'create_post.html', {
        'post_form': post_form,
        'image_form': image_form,
        'video_form': video_form,
        'pdf_form': pdf_form,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'post_detail.html', {
        'post': post,
    })

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            # Handle invalid login details
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render
from .models import Post

def search_posts(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(title__icontains=query) | Post.objects.filter(description__icontains=query)
    else:
        results = []
    default = Post.objects.all()[:10]
    return render(request, 'search.html', {'results': results, 'default': default, 'query': query})

def home(request):

    return render(request, 'home.html')
