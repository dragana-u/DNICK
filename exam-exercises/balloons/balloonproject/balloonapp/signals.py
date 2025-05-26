import random

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from balloonapp.models import Pilot, Flight


@receiver(pre_delete, sender=Pilot)
def reassign_flights(sender, instance, **kwargs):
    print("test")
    flights = Flight.objects.filter(pilot=instance)
    other_pilots = Pilot.objects.exclude(id=instance.id)

    if other_pilots.exists():
        for flight in flights:
            new_pilot = random.choice(other_pilots)
            flight.pilot = new_pilot
            flight.save()
