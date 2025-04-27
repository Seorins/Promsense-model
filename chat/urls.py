from django.urls import path
from .views import chat_view
from chat.views import chat_view, toggle_like

urlpatterns = [
    path('chat/', chat_view, name='chat'),
    path('like/', toggle_like, name='toggle_like'),
]
