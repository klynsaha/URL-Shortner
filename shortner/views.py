from django.shortcuts import render, redirect, HttpResponse
import uuid
from .models import URL

# Create your views here.
def index(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        if(link not in [None, ""]):
            uid = str(uuid.uuid4())[:5]
            # if uuid already exits, get a new uid
            while(URL.objects.filter(uuid=uid).count()):
                uid = str(uuid.uuid4())[:5]

            # if link not exits, save to db
            if(not URL.objects.filter(link=link).count()):
                new_url = URL(link=link, uuid=uid)
                new_url.save()
            else:  # if link already exits, return uid from db
                obj = URL.objects.get(link=link)
                uid = obj.uuid

            return HttpResponse(uid)
    return render(request, 'index.html', context=None)


def new_url(request, id):
    url_details = URL.objects.get(uuid=id)
    return redirect(url_details.link)
