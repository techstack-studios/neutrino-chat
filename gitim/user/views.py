from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def search(request, search_id):
    return HttpResponse("You're looking for user: %s." % search_id)


def add(request, add_id):
    return HttpResponse("You're adding user: %s." % add_id)


def look(request, look_id):
    return HttpResponse("You're looking user: %s." % look_id)
