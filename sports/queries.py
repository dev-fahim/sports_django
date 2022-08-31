from sports.models import Event


def get_all_events():
    return Event.objects.all()
