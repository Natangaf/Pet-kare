from rest_framework.views import APIView, Request, Response, status
from pet_kare.pagination import CustomPageNumberPagination
from .models import Pet
from .serializers import PetSerializer
from groups.models import Group
from traits.models import Trait


class petsView(APIView, CustomPageNumberPagination):
    def get(self, req: Request) -> Response:
        pets = Pet.objects.all()
        result_page = self.paginate_queryset(pets, req, view=self)
        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, req: Request) -> Response:
        serializer = PetSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group")
        traits_data = serializer.validated_data.pop("traits")
        pet_data = serializer.validated_data

        group = Group.objects.filter(scientific_name__iexact= group_data["scientific_name"]).first()

        if not group:
            group = Group.objects.create(**group_data)

        instance_pets: Pet = Pet.objects.create(**pet_data, group=group)

        for trait_data in traits_data:
            trait = Trait.objects.filter(name__iexact=trait_data["name"]).first()
            if not trait:
                trait = Trait.objects.create(**trait_data)
            instance_pets.traits.add(trait)
        instance_pets.save()

        response = PetSerializer(instance_pets)

        return Response(response.data,status.HTTP_201_CREATED)