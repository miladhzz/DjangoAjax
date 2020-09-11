from django.http import HttpResponse
from django.shortcuts import render, reverse
from . import forms
from . import models
from django.http import JsonResponse
from django.core import serializers


def index(request):
    form = forms.TestForm()
    if request.method == 'POST':
        form = forms.TestForm(request.POST)
        if form.is_valid():
            print('ok', request.POST.get('name'))
    return render(request, 'index.html', {'form': form})


def friend_view(request):
    form = forms.FriendForm()
    friends = models.Friend.objects.all()

    return render(request, 'friend.html', {'form': form, 'friends': friends,
                                           'post_address': reverse('post_friend'),
                                           'validate_nickname_address': reverse('validate_nickname')})


def post_friend(request):
    # request should be ajax and method should be POST.
    # is_ajax() Deprecated since version 3.1
    if request.is_ajax and request.method == "POST":
        # get the form data
        form = forms.FriendForm(request.POST)
        # save the data and after fetch the object in instance
        if form.is_valid():
            instance = form.save()
            print('ok', instance.first_name)
            # serialize in new friend object in json
            ser_instance = serializers.serialize('json', [instance, ])
            # send to client side.
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            # some form errors occurred.
            return JsonResponse({"error": form.errors}, status=400)

    # some error occurred
    return JsonResponse({"error": ""}, status=400)


def check_nickname(request):
    # request should be ajax and method should be GET.
    #  is_ajax() Deprecated since version 3.1
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        nick_name = request.GET.get("nick_name", None)
        # check for the nick name in the database.
        if models.Friend.objects.filter(nick_name=nick_name).exists():
            # if nick_name found return not valid new friend
            return JsonResponse({"valid": False}, status=200)
        else:
            # if nick_name not found, then user can create a new friend.
            return JsonResponse({"valid": True}, status=200)

    return JsonResponse({}, status=400)
