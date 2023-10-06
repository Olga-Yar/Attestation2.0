from django.core.management import BaseCommand

from user.models import UserCustom, UserRoles


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = UserCustom.objects.create(
            pk=0,
            email='admin@admin.ru',
            is_active=True,
            role=UserRoles.MODERATOR,
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123098')
        user.save()
