from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import uuid

# Simulación de base de datos local en memoria
data_list = []

# Añadiendo algunos datos de ejemplo para probar el GET
data_list.append({'id': str(uuid.uuid4()), 'name': 'User01', 'email': 'user01@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User02', 'email': 'user02@example.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'User03', 'email': 'user03@example.com', 'is_active': False}) # Ejemplo de item inactivo

class DemoRestApi(APIView):
    name = "Demo REST API"

    def get(self, request):
        active_items = [item for item in data_list if item.get('is_active', False)]
        return Response(active_items, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        if not data.get('name') or not data.get('email'):
            return Response({'error': 'Campos requeridos faltantes','message': 'Los campos name y email son obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

        data['id'] = str(uuid.uuid4())
        data['is_active'] = True
        data_list.append(data)

        return Response({'message': 'Usuario creado exitosamente', 'data': data}, status=status.HTTP_201_CREATED)

class DemoRestApiItem(APIView):
    name = "Demo REST API Item"

    def get_item_by_id(self, id):
        for item in data_list:
            if item['id'] == id:
                return item
        return None
    
    def get(self, request, id):
        item = self.get_item_by_id(id)
        if not item:
            return Response({'error': 'Item no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(item, status=status.HTTP_200_OK)

    def put(self, request, id):
        data = request.data
        item = self.get_item_by_id(id)

        if not item:
            return Response({'error': 'Item no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        if not data.get('name') or not data.get('email'):
            return Response({'error': 'Campos requeridos faltantes', 'message': 'Los campos name y email son obligatorios'}, status=status.HTTP_400_BAD_REQUEST)
        
        item.update({
            'name': data['name'],
            'email': data['email'],
            'is_active': data.get('is_active', True)
        })

        return Response({'message': 'Item actualizado', 'data': item}, status=status.HTTP_200_OK)

    def patch(self, request, id):
        data = request.data
        item = self.get_item_by_id(id)

        if not item:
            return Response({'error': 'Item no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        if 'name' in data:
            item['name'] = data['name']
        if 'email' in data:
            item['email'] = data['email']
        if 'is_active' in data:
            item['is_active'] = data['is_active']
        
        return Response({'message': 'Item actualizado', 'data': item}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = self.get_item_by_id(id)
        if not item:
            return Response({'error': 'Item no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        item['is_active'] = False

        # MAUSKE HERRAMIENTA MISTERIOSA: Si se desea eliminar físicamente, usar:
        # data_list.remove(item)

        return Response(status=status.HTTP_204_NO_CONTENT)