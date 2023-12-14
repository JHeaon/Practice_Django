from django.shortcuts import render


def echo_page(request):
    return render(request, "chat/echo_page.html")

