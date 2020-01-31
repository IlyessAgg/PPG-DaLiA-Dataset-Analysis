from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from .models import Patient
from .serializers import PatientSerializer
from django.views.decorators.csrf import csrf_exempt

def index(request):
    # This is a view
    return HttpResponse("Your are on the main page: isn't it beautiful ?")

def predict_activity(unscaled_data):
    from sklearn.externals import joblib
    colonnes        = ['chest_ACC_x', 'chest_ACC_y', 'chest_ACC_z', 'chest_Resp', 'chest_ECG', 'wrist_ACC_x', 
                       'wrist_ACC_y', 'wrist_ACC_z', 'wrist_BVP', 'wrist_TEMP', 'WEIGHT', 'Gender', 'AGE', 
                       'HEIGHT', 'SKIN', 'SPORT', 'Rpeaks', 'Label']
    path_to_model   = "./ipynb/final_model.sav"
    donnees         = [[unscaled_data[colonne] for colonne in colonnes]]
    model           = joblib.load(path_to_model)
    activity        = model.predict(donnees)
    return activity

@csrf_exempt
def predict(request):
    """
    Renvoie une Patient avec la activity completee
    (Attend une activity innexistante == null)
    """
    if request.method == 'GET':
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = PatientSerializer(data=data)
        if serializer.is_valid():
            data["Activity"]        = predict_activity(data)
            serializer          = PatientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)