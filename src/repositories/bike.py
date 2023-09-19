from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# from . import models
# from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.bike import Bike
from ..schemas.bike import BikeSerializer


class BikeViewset(APIView):
    def get(self, request, id=None):
        if id:
            item = Bike.objects.get(id=id)
            serializer = BikeSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Bike.objects.all()
        serializer = BikeSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Bike.objects.get(id=id)
        serializer = BikeSerializer(
            item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = Bike.objects.filter(id=id)
        print(item)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
