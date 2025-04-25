from django.shortcuts import render
from .models import Message

def chat_view(request):
    chat_history = Message.objects.order_by('timestamp')  # 또는 filter(user=request.user)
    return render(request, 'chat/chat.html', {
        'room_name': 'lobby',
        'chat_history': chat_history
    })
