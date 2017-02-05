from django.core.management.base import BaseCommand
from lib.utils import *
from importtxt.management.commands.lib.Say import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Hello")
        Say()
        Say().some()
        utils().sample()
