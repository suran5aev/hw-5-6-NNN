from django.core.management.base import BaseCommand
from apps.users.models import User

class Command(BaseCommand):
    help = 'Сжигает неиспользованные монеты всех пользователей'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            user.profile.balance = 0  # обнуляем баланс монет
            user.profile.save()
        self.stdout.write(self.style.SUCCESS('Неиспользованные монеты успешно сожжены'))
