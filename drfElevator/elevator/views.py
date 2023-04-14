from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Elevator, Request
from .serializers import ElevatorSerializer, RequestSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows elevators to be viewed or edited.
    """

    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=False, methods=["post"])
    def bulk_create_elevators(self, request):
        num_elevators = int(request.data.get("num_elevators"))
        elevators = []
        for i in range(num_elevators):
            elevator = Elevator()
            elevators.append(elevator)
        Elevator.objects.bulk_create(elevators)
        return Response({"message": f"{num_elevators} elevators created successfully"})

    @action(detail=True, methods=["post"])
    def set_operational(self, request, pk=None, is_operational=None):
        elevator = self.get_object()
        elevator.is_operational = bool(is_operational)
        elevator.save()
        serializer = self.get_serializer(elevator)
        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def set_door_status(self, request, pk=None, is_door_open=None):
        elevator = self.get_object()
        elevator.is_door_open = bool(is_door_open)
        elevator.save()
        serializer = self.get_serializer(elevator)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def requests(self, request, pk=None):
        elevator = self.get_object()
        requests = Request.objects.filter(elevator=elevator)
        serializer = RequestSerializer(requests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def request_elevator(self, request):
        desired_floor = request.data.get("floor")
        nearest_elevator = Elevator.get_nearest_elevator(desired_floor)
        current_floor = nearest_elevator.current_floor

        if nearest_elevator:
            nearest_elevator.set_direction(desired_floor)
            nearest_elevator.set_current_floor(desired_floor)
            request_obj = Request(floor=desired_floor, elevator=nearest_elevator)
            request_obj.save()

            return Response(
                {
                    "message": f"Request full filled by elevator {nearest_elevator.id} from floor {current_floor}"
                }
            )
        else:
            return Response(
                {"message": "No available elevators."}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=True, methods=["get"])
    def get_direction(self, request, pk=None):
        elevator = self.get_object()
        return Response(
            {
                "message": f"The current direction of the elevator {elevator.id} is {elevator.direction}"
            }
        )


class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows requests to be viewed or edited.
    """

    queryset = Request.objects.all()
    serializer_class = RequestSerializer
