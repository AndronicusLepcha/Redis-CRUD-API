import json
from django.shortcuts import render
from redis import Redis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .forms import dummy_data_form
from .models import dummy_model_data
from django.core.files import File
# Create your views here.

#landing page
@api_view(['GET'])
def load_data(request):
    
    return HttpResponse("API create_data added the new data in the DB and REDIS !")

# CREATE
@api_view(['POST'])
def create_data(request):
    try:
        redis_connection=Redis(host='redis', port=6379, db=1)
        print("connection success!")
    except Exception as e:
        print("Redis connection failed ! || Exception",e)
    
    payload=request.data
    redis_connection.lpush("media_files_list", json.dumps(payload))
    return HttpResponse("API create_data added the new data in the DB and REDIS !")


# RETRIEVE
@api_view(['POST'])
def retrieve_data(request):
    
    payload=request.data
    inital_page = payload.get('page', 1)
    items_per_page = 20
    
    try:
        page = int(inital_page)
    except ValueError:
        page = 1
    
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page - 1
    
    try:
        redis_connection=Redis(host='redis', port=6379, db=1)
        print("connection success!")
    except Exception as e:
        print("Exception",e)
        print("Redis connection failed ! ")
    
    redis_data_chunk = redis_connection.lrange("media_files_list",start_index,end_index)
    if not redis_data_chunk:
        media_data=dummy_model_data.objects.all().values()
        for item in media_data:
            redis_connection.rpush("media_files_list", json.dumps(item))
        redis_data_chunk = redis_connection.lrange("media_files_list",start_index,end_index)
    redis_data = [json.loads(item) for item in redis_data_chunk]
    
    return Response(redis_data)
    
    

# UPDATE
@api_view(['GET'])
def update_data(request):
    data=None
    return Response(data)

# DELETE 
@api_view(['GET'])
def delete_data(request):
    data=None
    return Response(data)

def upload_file(request):
    if request.method == 'POST':
        form = dummy_data_form(request.POST, request.FILES)
        uploaded_instances = []
        if form.is_valid():
            form.save()
            # for _ in range(200000): 
            #     uploaded_data = form.save(commit=False)
            #     uploaded_instances.append(uploaded_data)
            # dummy_model_data.objects.bulk_create(uploaded_instances)
            return HttpResponse("Upload Successfull")
    else:
        form = dummy_data_form()
    return render(request, 'UploadForm.html', {'form': form})
