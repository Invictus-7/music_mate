from django.urls import path

from forum.views import (
                        ForumIndexViewSet,
                        ForumSectionTopicsViewSet,
                        ForumTopicMessageView
                        )

urlpatterns = [
    # Действия с главной страницей форума (просмотр раздела + создание раздела + удаление раздела)
    path('', ForumIndexViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('delete_section/<int:pk>', ForumIndexViewSet.as_view({'delete': 'destroy'})),
    # Действия с темой внутри раздела (просмотр + создание + удаление)
    path('sections/<slug:slug>', ForumSectionTopicsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('delete_topic/<slug:slug>', ForumSectionTopicsViewSet.as_view({'delete': 'destroy'})),
    # Действия с сообщениями внутри топика (просмотр + создание + редактирование + удаление)
    path('topics/<slug:slug>/messages', ForumTopicMessageView.as_view({'get': 'list', 'post': 'create'})),
    path('topics/<slug:slug>/messages/<int:pk>',
         ForumTopicMessageView.as_view({'patch': 'update', 'delete': 'destroy'}))
]
