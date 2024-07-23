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
@api_view(['POST'])
def update_data(request):
    try:
        redis_connection=Redis(host='redis', port=6379, db=1)
        print("connection success!")
    except Exception as e:
        print("Exception",e)
        print("Redis connection failed ! ")
        
    page=request.data.get('page')
    start_index = (page - 1) * 20
    end_index = start_index + 20 - 1
    new_data=request.data.get('new_data')
    id=new_data["id"]
    
    redis_data_chunk = redis_connection.lrange("media_files_list", start_index, end_index)
    redis_data = [json.loads(item) for item in redis_data_chunk]
        
    for item in redis_data:
        if id == int(item.get('id')):
            item.update(new_data)
        
    updated_redis_data_chunk = [json.dumps(item) for item in redis_data]
    for index, item_json in enumerate(updated_redis_data_chunk):
        # The list indices are assumed to start from start_index.
        redis_connection.lset("media_files_list", start_index + index, item_json)
    
    return Response(redis_connection.lrange("media_files_list", start_index, end_index))

# DELETE 
@api_view(['POST'])
def delete_data(request):
    try:
        redis_connection=Redis(host='redis', port=6379, db=1)
        print("connection success!")
    except Exception as e:
        print("Exception",e)
        print("Redis connection failed ! ")
        
    redis_connection.lrem("media_files_list", 0, json.dumps(request.data))  
    return HttpResponse("Item Deleted!")

def upload_file(request):
    if request.method == 'POST':
        form = dummy_data_form(request.POST, request.FILES)
        # uploaded_instances = []
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
