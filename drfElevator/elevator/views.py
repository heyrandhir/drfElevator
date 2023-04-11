from rest_framework import viewsets
from rest_framework.response import Response

from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer


# Create your views here.
class ElevatorView(viewsets.ViewSet):
    """
    A simple ViewSet for all Elevators
    """

    def list(self, request):
        queryset = Elevator.objects.all()
        serializer = ElevatorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Elevator.objects.get(pk=pk)
        serializer = ElevatorSerializer(queryset)
        return Response(serializer.data)


class RequestView(viewsets.ViewSet):
    """
    A simple ViewSet for all Requests
    """

    def list(self, request):
        queryset = Request.objects.all()
        serializer = RequestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = Request.objects.get(pk=pk)
        serializer = RequestSerializer(queryset)
        return Response(serializer.data)
