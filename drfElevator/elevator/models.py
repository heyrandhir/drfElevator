from django.db import models


# Create your models here.
class Elevator(models.Model):
    current_floor = models.IntegerField(default=0)
    direction = models.CharField(
        max_length=10, default="N"
    )  # N for north and S for south
    is_door_open = models.BooleanField(default=False)
    is_operational = models.BooleanField(default=True)

    def __str__(self):
        return f"Elevator {self.id}"

    def add_request(self, request):
        self.request.add(request)

    def get_nearest_elevator(floor_no):
        nearest_elevator = None
        nearest_distance = float("inf")
        elevators = Elevator.objects.filter(is_operational=True)

        if not elevators.exists():
            return None
        elevator_distances = []
        for elevator in elevators:
            distance = abs(elevator.current_floor - floor_no)
            elevator_distances.append(distance)

        for elevator in elevators:
            distance = abs(elevator.current_floor - floor_no)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_elevator = elevator
        print(
            {"nearest_elevator": nearest_elevator, "nearest_distance": nearest_distance}
        )
        return nearest_elevator

    def set_current_floor(self, floor):
        self.current_floor = floor
        self.save()

    def set_direction(self, desired_floor):
        if desired_floor == self.current_floor:
            return
        self.direction = "N" if desired_floor > self.current_floor else "S"
        self.save()


class Request(models.Model):
    elevator = models.ForeignKey(
        Elevator,
        related_name="requests",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    floor = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
