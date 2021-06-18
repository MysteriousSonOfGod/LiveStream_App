from django.shortcuts import render


def HomeView(request):
    return render(request, "channels/channels_list.html")
