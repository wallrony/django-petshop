from rest_framework import serializers
from petshop.core.models import Pet

class PetSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pet
    fields = ('id', 'nome', 'raca', 'idade')