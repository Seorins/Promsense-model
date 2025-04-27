from django.shortcuts import render
from .models import Message
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def chat_view(request):
    chat_history = Message.objects.order_by('timestamp')  # 또는 filter(user=request.user)
    return render(request, 'chat/chat.html', {
        'room_name': 'lobby',
        'chat_history': chat_history
    })

@csrf_exempt
def toggle_like(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        msg_id = data.get('msg_id')
        message = Message.objects.get(id=msg_id)
        message.liked = not message.liked
        message.save()
        return JsonResponse({'liked': message.liked})
    return JsonResponse({'error': 'Invalid method'}, status=400)
