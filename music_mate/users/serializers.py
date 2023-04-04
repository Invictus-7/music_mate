from djoser.serializers import UserSerializer as UserHandleSerializer
from users.models import CustomUser


class UserSerializer(UserHandleSerializer):
    """Сериализатор для модели пользователя."""

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'is_staff',
                  'is_admin', 'is_ensemble')
