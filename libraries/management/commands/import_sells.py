# from django.core.management.base import BaseCommand, CommandError

# from ox_plugin.models import Sell
# from ox_plugin.forms import SellForm
# from ox_plugin.sell import SellListManager

'''
class Command(BaseCommand):
    args = 'None'
    help = 'Импорт списка продаж'
    sells = SellListManager()

    def handle(self, *args, **options):
        for item in self.sells:
            form = SellForm(item)
            if form.is_valid():
                Sell.objects.update_or_create(**form.clean())

        self.stdout.write('Импорт списка продаж ЗАВЕРШЕН!!!')
'''
