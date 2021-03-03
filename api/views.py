from django.shortcuts import render


def nothing(request):
    return render(request, 'api/base.html', {})

