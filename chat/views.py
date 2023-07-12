from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Chat, User

# Create your views here.


class StartChat(ListView):
    model = User
    template_name = 'start_chat.html'
    context_object_name = 'users'

class Chat(TemplateView):
    template_name = 'chat.html'

    def post(self, request, **kwargs):
        chat = Chat(name='')
        chat.members.add(self.request.user)
        chat.members.add(User.objects.get(id=kwargs['id']))