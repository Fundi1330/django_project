from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView, CreateView, FormView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .models.post import Post
from .models.comment import Comment
from .models.like import Like
from .models.user import Profile
from .models.base import User
from .forms import AddPost, Register, Search, EditProfile
from django.http import JsonResponse
from django.core.files import File
from pathlib import Path

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        posts = Post.objects.all()

        context['posts'] = posts
        context['form'] = AddPost()
        context['search_form'] = Search()
        
        return context
    
    def post(self, request, **kwargs):
        data = request.POST
        if 'title' in data.keys():
            with open('new_app/static/images/upload.png', 'rb') as file:
                img = File(file, name=file.name)
                print(img)
                post = Post(title=data['title'], body=data['body'], author=request.user, image=img)
                post.save()
        if 'input' in data.keys():
            search = Post.objects.filter(title__contains=data['input'])
            result = render_to_string('search_result.html', {'posts': search})
            return JsonResponse(result, safe=False)
        return JsonResponse({'title': post.title, 'id': post.id}, safe=False)    

class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = Register
    success_url = '/login'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        usernames = []
        for i in User.objects.all():
            usernames.append(i.username)
        if not form.cleaned_data['username'] in usernames: 
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User(username=name, password=password, email=email)
            user.save()
            return redirect('/')
        return form

class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'

    def post(self, request):
        file = request.FILES['file']
        with open('new_app/static/images/upload.png', 'wb') as img:
            img.write(file.read())

        return JsonResponse({'status': 200}, safe=False)

class EditProfileView(TemplateView):
    template_name = 'edit_profile.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = EditProfile()
        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        data = request.POST
        user = request.user
        profile = Profile.objects.get(author=user)
        if 'edit' in data.keys():
            user.username = data['username']
            user.email = data['email']
            profile.bio = data['bio']
            user.save()
            profile.save()
            return JsonResponse({'success': True}, safe=False)
        if 'get_data' in data.keys():
            return JsonResponse({'username': user.username, 'email': user.email, 'bio': profile.bio, 'avatar': profile.avatar.url}, safe=False)

class PostView(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        post = Post.objects.get(id=self.kwargs['id'])
        comments = Comment.objects.filter(post=post)
        likes = len(Like.objects.filter(post=post))
        is_liked = False
        for like in Like.objects.filter(post=post):
            if like.author == self.request.user:
                is_liked = True
                break
        context['post'] = post
        context['comments'] = comments
        context['likes'] = likes
        context['is_liked'] = is_liked
        return context
    
    def post(self, request, **kwargs):
        if (request.user.is_authenticated and request.POST['action'] == 'comment'):
            data = request.POST
            comment = Comment(body=data['comment'], post=Post.objects.get(id=kwargs['id']), author=request.user)
            comment.save()
            return JsonResponse(f'<p>{comment.body}</p>', safe=False)
        if (request.user.is_authenticated and request.POST['action'] == 'like'):
            data = request.POST
            post = Post.objects.get(id=kwargs['id'])
            likes = Like.objects.filter(post=post)
            is_liked = False
            for like in likes:
                if like.author == request.user:
                    like.delete()
                    is_liked = True
                    break
            else:
                like = Like(post=post, author=request.user)
                like.save()
            
            return JsonResponse({'likes': len(Like.objects.filter(post=post)), 'is_liked': is_liked }, safe=False)
        return JsonResponse('<h3>Error</h3>', safe=False)

class ProfileView(ListView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        return context