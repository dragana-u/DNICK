from django.shortcuts import render, redirect, get_object_or_404

from ispitnaapp.forms import RealEstateForm
from ispitnaapp.models import RealEstate, RealEstateCharacteristic


# Create your views here.

def index(request):
    re = RealEstate.objects.filter(is_sold=False,area__gte=100).all()
    re_context = []
    for r in re:
        price = 0
        hc = RealEstateCharacteristic.objects.filter(real_estate=r)
        for h in hc:
            price += h.characteristic.price
        re_context.append({'house': r, 'price': price})
    return render(request, 'index.html', context={'houses': re_context})


def edit(request, r_id):
    real_estate = get_object_or_404(RealEstate, pk=r_id)

    if request.method == 'POST':
        form = RealEstateForm(request.POST, request.FILES, instance=real_estate)
        if form.is_valid():
            form.save()

        return redirect('index')

    form = RealEstateForm(instance=real_estate)
    return render(request, "edit.html", context={'form': form, 'r_id': r_id,'house': real_estate})
