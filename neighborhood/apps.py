from django.apps import AppConfig


class NeighborhoodConfig(AppConfig):
    name = 'neighborhood'

    def ready(self):
        import neighborhood.signals
