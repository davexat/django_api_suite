from django.shortcuts import render
from datetime import datetime

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Firebase Admin SDK
from firebase_admin import db

class LandingApi(APIView):
    name = 'Landing API'

    collection_name = 'comments'

    def get(self, request):
      # Referencia a la colección
      ref = db.reference(f'{self.collection_name}')

      # get: Obtiene todos los elementos de la colección
      data = ref.get()

      # Devuelve un arreglo JSON
      return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        ref = db.reference(f'{self.collection_name}')
        current_time  = datetime.now()
        iso_format = current_time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        data.update({"date": iso_format })

        new_resource = ref.push(data)
        return Response({"id": new_resource.key}, status=status.HTTP_201_CREATED)
