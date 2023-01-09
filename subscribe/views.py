from django.shortcuts import render,redirect
from django.urls import reverse
from subscribe.form import SubscribeForm

# Create your views here.
def subscribe(request):
    if request.POST:
        sf = SubscribeForm(request.POST)
        if sf.is_valid():
            sf.save()
            return redirect(reverse('thankyou'))
    else:
        sf = SubscribeForm()

    return render(request, 'subscribe/subscribe.html', {'name':'subscribe','sf':sf,})

# ----------

def thankyou(request):
    return render(request, 'subscribe/thankyou.html', {'name':'thankyou',})
