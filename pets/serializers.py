from rest_framework import serializers
from .models import CategorySex
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer

class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=CategorySex.choices, default=CategorySex.Not_Informed
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

