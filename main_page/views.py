from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect

# Create your views here.
def open_main_page(request):
    return HttpResponse("Hello, world. You're at the main page.")
def open_archive(request, year):
    if year > 2026:
        uri = reverse('', args=(year,))
        return render(request, "Main_page.html", {'uri': uri})
    return render(request, "main_page.html", )
def error_404(request, exception):
    return HttpResponseNotFound(f"<h1>404</ h1>")