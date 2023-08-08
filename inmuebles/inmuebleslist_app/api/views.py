from rest_framework.response import Response
from inmuebleslist_app.models import Inmueble
from inmuebleslist_app.api.serializers import InmuebleSerializer
# from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class InmuebleListAV(APIView):
    def get(self, request):
        inmuebles = Inmueble.objects.all()
        serializer = InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)

    def post(Self,request):
        serializer = InmuebleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class InmuebleDetalleAV(APIView):
    def get(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'INmueble no encontrado'}, status = status.HTTP_404_NOT_FOUND) #¿el inmueble existe o no existe?
        
        serializer = InmuebleSerializer(inmueble)
        return Response(serializer.data)
        
        
    def put(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'INmueble no encontrado'}, status = status.HTTP_404_NOT_FOUND)      
        serializer = InmuebleSerializer(inmueble, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            inmueble = Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response({'error': 'INmueble no encontrado'}, status = status.HTTP_404_NOT_FOUND)
        inmueble.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
        
        
        
        
# @api_view(['GET', 'POST'])
# def inmueble_list(request):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all()
#         serializer = InmuebleSerializer(inmuebles, many=True) #aca paso la data que quiero serializar, es decir inmueble
#         return Response(serializer.data)#aca tengo que pasarle la data serializada en formato json al cliente

            
    
#     if request.method == 'POST':#el cliente me envia la data en json, para registrar esta data en mi bdd tengo que
#         #realizar un proceso de DE-SERIALIZACION por lo tanto tengo que llamar al objeto serializer
#         de_serializer = InmuebleSerializer(data = request.data) #guardo en un objeto deserializado
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)

# # tengo tambien otra funcion que me devuelve el inmueble por el id
# @api_view(['GET','PUT','DELETE'])#actualizo para que soporte put para actualizar datos y delete para eliminar
# def inmueble_detalle(request,pk):
#     if request.method == 'GET':
#             try:
#                 inmueble = Inmueble.objects.get(pk=pk)
#                 serializer = InmuebleSerializer(inmueble)
#                 return Response(serializer.data) 
#             except Inmueble.DoesNotExist:
#                 return Response({'Error' : 'El inmueble no existe'}, status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk=pk)
#         de_serializer = InmuebleSerializer(inmueble, data = request.data)#esta deserilizacion va a comparar un valor nuevo con un valor existente en la bdd
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data)
#         else:
#             return Response(de_serializer.errors)
    
#     if request.method == 'DELETE':
#         inmueble = Inmueble.objects.get(pk=pk)
#         inmueble.delete()
#         #hasta aca ya estaria, pero algo le tengo que devolver al cliente...
        
#         data = {
#             "resultado" : True
#         }
#         return Response(data)


# #cuando devuelvo solo un record esta bien escrito asi, pero cuando devuelvo mas de uno debo poner en la
# #linea >> serializer = InmuebleSerializer(inmuebles) un many=True
# #quedando  serializer = InmuebleSerializer(inmuebles, many=True)


# #COMO ES CONSULTA DE DATOS SE TRATA DE UN METODO GET