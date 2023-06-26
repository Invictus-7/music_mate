from django.db.models import Q

from dialogs.models import Dialog
from feed.models import Match


class MatchChecker:

    def check_match(self, req_user, companion_user):
        """Вызвать эту функцию внутри метода create,
        чтобы при отсутствии Match процесс создания
        объекта не запускался."""
        return Match.objects.filter(Q(matcher=req_user, matched=companion_user) and
                                    Q(matcher=companion_user, matched=req_user)).exists()

    def check_if_dialog_exists(self, req_user, companion_user):
        """Проверяет существование диалога."""
        return Dialog.objects.filter(Q(started_by=req_user, to_whom=companion_user) or
                                     Q(to_whom=companion_user, started_by=req_user)).exists()


