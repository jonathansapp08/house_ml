from django.shortcuts import render

from .forms import HouseForm

from .load_model import predict_house
# from .ml import load_model

def index(request):
    form = HouseForm(request.POST or None)
    if form.is_valid():
        X_test = []
        X_test.append(request.POST.get('area'))

        if request.POST.get('fireplace') == 'on':
            fireplace = 1
        else:
            fireplace = 0
        X_test.append(fireplace)
        
        X_test.append(request.POST.get('baths'))
        X_test.append(request.POST.get('floors'))
        X_test.append(request.POST.get('city'))
    
        if request.POST.get('electric') == 'on':
            electric = 1
        else:
            electric = 0
        X_test.append(electric)

        form.save()
        form = HouseForm()

        price = predict_house(X_test)
        price = {
            'form': form,
            'price': price
        }

        return render(request, 'index.html', price)
    else:
        print(form.errors)

    context = {
        'form': form
    }

    return render(request, 'index.html', context)