from django.contrib import admin
from django.urls import include, path

from CrudApi.views import create_data, retrieve_data,upload_file, delete_data

urlpatterns = [
    path('createData', create_data , name="createData"),
    path('RetrieveData', retrieve_data , name="RetrieveData"),
    path('UploadFile', upload_file , name="UploadFile"),
    path('DeleteFile', delete_data , name="DeleteFile")
]
