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

      # Filtra la lista para incluir solo los elementos donde 'is_active' es True
      active_items = [item for item in data_list if item.get('is_active', False)]
      return Response(active_items, status=status.HTTP_200_OK)
    
    def post(self, request):
      data = request.data

      # Validación mínima
      if 'name' not in data or 'email' not in data:
         return Response({'error': 'Faltan campos requeridos.'}, status=status.HTTP_400_BAD_REQUEST)

      data['id'] = str(uuid.uuid4())
      data['is_active'] = True
      data_list.append(data)

      return Response({'message': 'Dato guardado exitosamente.', 'data': data}, status=status.HTTP_201_CREATED)
    
class DemoRestApiItem(APIView):
    name = "Demo REST API Item"

    def put(self, request, item_id):
        # El item_id se pasa como argumento en la URL
        # Los datos para reemplazar se envían en el cuerpo de la solicitud
        data = request.data

        # Validación: El 'id' en el cuerpo debe coincidir con el 'item_id' de la URL
        if 'id' not in data or data['id'] != item_id:
            return Response({'error': 'El ID en el cuerpo de la solicitud no coincide con el ID de la URL o falta.'}, status=status.HTTP_400_BAD_REQUEST)

        for i, item in enumerate(data_list):
            if item['id'] == item_id:
                # Reemplazar completamente el elemento, manteniendo el mismo ID y 'is_active' si no se proporciona
                data['is_active'] = data.get('is_active', item.get('is_active', True)) # Mantener el is_active si no se envía, o si se envió en el body
                data_list[i] = data
                return Response({'message': 'Dato actualizado exitosamente (PUT).', 'data': data}, status=status.HTTP_200_OK)
        return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, item_id):
        # El item_id se pasa como argumento en la URL
        # Los campos a actualizar parcialmente se envían en el cuerpo de la solicitud
        data = request.data

        found = False
        for i, item in enumerate(data_list):
            if item['id'] == item_id:
                # Actualizar solo los campos proporcionados en la solicitud
                for key, value in data.items():
                    # No permitir la modificación del 'id' a través de PATCH
                    if key != 'id':
                        data_list[i][key] = value
                found = True
                return Response({'message': 'Dato actualizado parcialmente (PATCH).', 'data': data_list[i]}, status=status.HTTP_200_OK)
        if not found:
            return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, item_id):
        # El item_id se pasa como argumento en la URL
        found = False
        for i, item in enumerate(data_list):
            if item['id'] == item_id:
                # Eliminación lógica: marcar como inactivo
                data_list[i]['is_active'] = False
                found = True
                return Response({'message': 'Dato eliminado lógicamente (DELETE).'}, status=status.HTTP_200_OK)
        if not found:
            return Response({'error': 'Elemento no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
