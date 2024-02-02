from django.shortcuts import render


def frontdoor(request):
    return render(request, './frontdoor/index.html')
