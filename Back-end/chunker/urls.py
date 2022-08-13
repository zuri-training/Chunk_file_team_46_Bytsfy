from django.urls import path 
from .views import splitCSV, csvToJson, save, delete, jsonToCsv, splitJSON

urlpatterns = [
    path('csvsplit/', splitCSV, name="csvsplitter"),
    path('jsonsplit/', splitJSON, name="jsonsplitter"),
    path('csv2json/', csvToJson, name="csv2json"),
    path('json2csv/', jsonToCsv, name="json2csv"),
    path('save/<str:pk>/', save, name="save"),
    path('delete/<str:pk>/', delete, name="delete"),
]

