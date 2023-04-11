from django.db import models


# Create your models here.
class Elevator(models.model):
    current_floor = models.IntegerField(default=0)
    direction = models.CharField(
        max_length=10, default="N"
    )  # N for north and S for south
    request = models.ManyToManyField("Request", blank=True)
    is_door_open = models.BooleanField(default=False)
    is_operational = models.BooleanField(default=True)

    def __str__(self):
        return f"Elevator {self.id}"


class Request(models.model):
    floor_no = models.IntegerField(default=0)

    def __str__(self):
        return f"Request to floor {self.floor_no}"
