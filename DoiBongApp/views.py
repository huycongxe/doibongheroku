import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.db.models import Avg,Count
from .models import Doibong,Cauthu
from .serializers import DoiBongSerializer,CauThuSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def doibongApi(request,id=0):
    if request.method=='GET':
        doibongs = Doibong.objects.all()
        doibongs_serializer=DoiBongSerializer(instance=doibongs,many=True)
        return JsonResponse(doibongs_serializer.data,safe=False)
    elif request.method=='POST':
        doibong_data=JSONParser().parse(request)
        doibongs_serializer=DoiBongSerializer(data=doibong_data)
        print(doibongs_serializer);
        if doibongs_serializer.is_valid():
            doibongs_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        doibong_data=JSONParser().parse(request)
        doibong=Doibong.objects.get(id=doibong_data['id'])
        doibongs_serializer=DoiBongSerializer(doibong,data=doibong_data)
        if doibongs_serializer.is_valid():
            doibongs_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        print("123321312321",id)
        doibong=Doibong.objects.get(id=id)
        doibong.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def cauthuApi(request,id=0):
    if request.method=='GET':
        cauthus = Cauthu.objects.all()
        cauthus_serializer=CauThuSerializer(cauthus,many=True)
        return JsonResponse(cauthus_serializer.data,safe=False)
    elif request.method=='POST':
        print("fjhdsjkfh")
        cauthu_data=JSONParser().parse(request)
        cauthus_serializer=CauThuSerializer(data=cauthu_data)
        if cauthus_serializer.is_valid():
            cauthus_serializer.save()
            return JsonResponse({"status": 200}, safe=False)

        return JsonResponse({"status": 401}, safe=False)
    elif request.method=='PUT':
        cauthu_data=JSONParser().parse(request)
        cauthu=Cauthu.objects.get(id=cauthu_data['id'])
        cauthus_serializer=CauThuSerializer(cauthu,data=cauthu_data)
        if cauthus_serializer.is_valid():
            cauthus_serializer.save()
            return JsonResponse({"status": 200},safe=False)
        return JsonResponse({"status": 401})
    elif request.method=='DELETE':
        cauthu=Cauthu.objects.get(id=id)
        cauthu.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    print("abv")
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)

@csrf_exempt
def overallApi(request):
    doibongs = Doibong.objects.all().count()
    cauthus = Cauthu.objects.all().count()
    return JsonResponse({
        'doibongs' : doibongs,
        'cauthus': cauthus,
        'areas': 6
    },safe=False)

@csrf_exempt
def ageApi(request):
    list = []
    age = Doibong.objects.annotate(age_avg= Avg('cauthu__age'))
    for h in age:
        he = 0 if h.age_avg == None else h.age_avg
        list.append({'name': h.name, 'age': he})

    jsonStr = json.dumps(list)
    return HttpResponse(jsonStr, content_type='application/json')

@csrf_exempt
def areaApi(request):
    list = []
    age = Doibong.objects.values('area').annotate(count =Count('id'))
    for h in age:
        print(h)
        # he = 30 if h.age_avg == None else h.age_avg
        list.append(h)

    jsonStr = json.dumps(list)
    return HttpResponse(jsonStr, content_type='application/json')

@csrf_exempt
def heightweightApi(request):
    list = []
    height = Doibong.objects.annotate(height_avg= Avg('cauthu__height'))
    for h in height:
        he = 0 if h.height_avg == None else h.height_avg
        list.append({ 'name': 'Chiều cao','doibong': h.name, 'height_weight': he})

    weight = Doibong.objects.annotate(weight_avg=Avg('cauthu__weight'))
    for h in weight:
        he = 0 if h.weight_avg == None else h.weight_avg
        list.append({'name': 'Cân nặng', 'doibong': h.name, 'height_weight': he})

    jsonStr = json.dumps(list)
    return HttpResponse(jsonStr, content_type='application/json')
