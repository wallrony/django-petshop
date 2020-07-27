from django.http.response import JsonResponse
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from petshop.core import serializers
from petshop.core.models import Pet

@api_view(['GET', 'POST'])
def pet_list(request):
  if request.method == 'GET':
    try:
      pets = Pet.objects.all()
    except:
      pets = []

    serializer = serializers.PetSerializer(pets, many=True)

    return Response(serializer.data)
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = serializers.PetSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'DELETE', 'PUT'])
def unique_pet(request, pet_id):
  try:
    pet = Pet.objects.get(id=pet_id)
  except Pet.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = serializers.PetSerializer(pet, many=False)

    return Response(serializer.data)
  elif request.method == 'DELETE':
    pet.delete()

    return Response(status=status.HTTP_200_OK)
  elif request.method == 'PUT':
    serializer = serializers.PetSerializer(pet, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)

  return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
