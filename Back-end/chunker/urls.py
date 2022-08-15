from django.urls import path 
from .views import splitCSV, save, delete, splitJSON, dashboard, downloadFile

urlpatterns = [
    path('csvsplit/', splitCSV, name="csvsplitter"),
    path('jsonsplit/', splitJSON, name="jsonsplitter"),
    path('save/<str:pk>/', save, name="save"),
    path('download/<str:pk>/', downloadFile, name="download-save"),
    path('delete/<str:pk>/', delete, name="delete"),
    path('saved-files/', dashboard, name='dashboard'),
]

