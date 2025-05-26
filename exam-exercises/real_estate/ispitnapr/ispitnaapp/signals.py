# Кога еден оглас/недвижнина ќе се означи како продадена, потребно е сите агенти поврзани со неа да ја инкрементираат својата продажба
from django.db.models.signals import pre_save
from django.dispatch import receiver

from ispitnaapp.models import RealEstate, AgentRealEstate


@receiver(pre_save, sender=RealEstate)
def handle_saving_house(sender, instance, **kwargs):
    old_instance = sender.objects.filter(id=instance.id).first()
    if old_instance:
        if old_instance.is_sold != instance.is_sold:
            agents_real_estate = AgentRealEstate.objects.filter(real_estate=old_instance).all()
            for agent_real_estate in agents_real_estate:
                agent = agent_real_estate.agent
                agent.number_sales += 1
                agent.save()