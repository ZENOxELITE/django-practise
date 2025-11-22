from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'page_title': 'Home'})


def services(request):
    return render(request, 'services.html', {'page_title': 'Services'})


def sections(request):
    return render(request, 'sections.html', {'page_title': 'Sections'})
