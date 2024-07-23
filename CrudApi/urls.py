from django.contrib import admin
from django.urls import include, path

from CrudApi.views import create_data, retrieve_data, update_data,upload_file, delete_data

urlpatterns = [
    path('createData', create_data , name="createData"),
    path('RetrieveData', retrieve_data , name="RetrieveData"),
    path('UpdateData', update_data , name="UpdateData"),
    path('UploadFile', upload_file , name="UploadFile"),
    path('DeleteData', delete_data , name="DeleteData")
]
