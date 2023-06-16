from rest_framework.views import APIView, Request, Response, status
from pet_kare.pagination import CustomPageNumberPagination
from .models import Pet
from .serializers import PetSerializer
from groups.models import Group
from traits.models import Trait
from django.shortcuts import get_object_or_404


class petsView(APIView, CustomPageNumberPagination):
    def get(self, req: Request) -> Response:
        trait_params = req.query_params.get("trait", None)
        # trait = Trait.objects.filter(name__iexact=trait_params).first()

        if trait_params:
            pets = Pet.objects.filter(traits__name=trait_params)
        else:
            pets = Pet.objects.all().order_by("id")

        result_page = self.paginate_queryset(pets, req, view=self)
        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, req: Request) -> Response:
        serializer = PetSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group")
        traits_data = serializer.validated_data.pop("traits")
        pet_data = serializer.validated_data

        group = Group.objects.filter(
            scientific_name__iexact=group_data["scientific_name"]
        ).first()

        if not group:
            group = Group.objects.create(**group_data)

        instance_pets: Pet = Pet.objects.create(**pet_data, group=group)

        trait_list= []
        for trait_data in traits_data:
            trait = Trait.objects.filter(name__iexact=trait_data["name"]).first()
            if not trait:
                trait = Trait.objects.create(**trait_data)    
            trait_list.append(trait)

        instance_pets.traits.set(trait_list)
        instance_pets.save()

        response = PetSerializer(instance_pets)

        return Response(response.data, status.HTTP_201_CREATED)


class petsDetailView(APIView, CustomPageNumberPagination):
    def get (self, req: Request, pets_id: int) -> Response:

        pet = get_object_or_404(Pet, id=pets_id)

        respose = PetSerializer(instance=pet)

        return Response(data=respose.data, status=status.HTTP_200_OK)
    
    def patch(self, req: Request, pets_id: int) -> Response:

        pet = get_object_or_404(Pet, id=pets_id)

        serializer = PetSerializer(data=req.data ,partial=True)

        serializer.is_valid(raise_exception=True)

        group_data = serializer.validated_data.pop("group",None)
        traits_data = serializer.validated_data.pop("traits",None)

        for key, value in serializer.validated_data.items():
            setattr(pet, key, value)

        if group_data:
            group = Group.objects.filter(
                scientific_name__iexact=group_data["scientific_name"]
            ).first()
            if not group:
                group = Group.objects.create(**group_data)
            pet.group = group


        if traits_data:
            trait_list= []
            for trait_data in traits_data:
                trait = Trait.objects.filter(name__iexact=trait_data["name"]).first()
                if not trait:
                    trait = Trait.objects.create(**trait_data)    
                trait_list.append(trait)

            pet.traits.set(trait_list)

        pet.save()

        respose = PetSerializer(instance=pet)

        return Response(data=respose.data, status=status.HTTP_200_OK)

    def delete(self, req: Request, pets_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pets_id)
        pet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
