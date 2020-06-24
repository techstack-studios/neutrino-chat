from django.http import HttpResponse
from django.shortcuts import render
from .models import Users


# Create your views here.

def search(request, search_id):
    return HttpResponse("You're looking for user: %s." % search_id)


def add(request, add_id):
    return HttpResponse("You're adding user: %s." % add_id)


def index(request):
    UserList = Users.objects.order_by('-name')
    context = {'UserList': UserList}
    return render(request, 'user/index.html', context)


def detail(request, gid):
    user = Users.objects.all()
    context = {
        'user': user,
        'gid': gid,
    }
    return render(request, 'user/detail.html', context)
# TODO: BIG BUG