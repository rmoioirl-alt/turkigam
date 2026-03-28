from django.contrib import admin
from django.urls import path, register_converter, converters
from main_page.converters import FourDigitYearConverter
from main_page.views import open_main_page, open_archive
register_converter(FourDigitYearConverter, "year4")
urlpatterns = [
    path('', open_main_page, name= "main_page1"),
    path("archive/<year4:year>", open_archive),
]