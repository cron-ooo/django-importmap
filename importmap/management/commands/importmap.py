from django.core.management.base import BaseCommand

from ...importmap import Importmap


class Command(BaseCommand):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.importmap = Importmap()

    def add_arguments(self, parser) -> None:
        parser.add_argument('--add', nargs='+', type=str)
        parser.add_argument('--list', action='store_true')

    def handle(self, *args, **options):
        if options['add']:
            packages = []
            for package in options['add']:
                packages.append(package)
            self.importmap.add(packages)

        if options['list']:
            for item in self.importmap.imports():
                self.stdout.write(item)
