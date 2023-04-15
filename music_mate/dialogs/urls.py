from django.urls import path


from dialogs.views import DialogViewSet, MessageViewSet

urlpatterns = [
    path('<int:pk>', DialogViewSet.as_view({'post': 'create'}),
         name='start/get_dialog'),
    path('<int:pk>/messages', MessageViewSet.as_view({'post': 'create', 'get': 'list'}),
         name='write_message')
]
