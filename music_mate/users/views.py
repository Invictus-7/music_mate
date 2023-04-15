from djoser.views import UserViewSet as UserHandleSet
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['User'])
class UserViewSet(UserHandleSet):
    """Вьюсет для модели пользователя."""
    pass
