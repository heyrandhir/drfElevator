# Data Model
The following data model represents the entities and relationships in the elevator system:

## Elevator
The Elevator model represents an elevator in the system.

| **Field**            | **Type**       | **Description**                                                  |
| -------------------- | -------------- | ---------------------------------------------------------------- |
| `**id**`             | `AutoField`    | Unique identifier for the elevator.                              |
| ` **current_floor**` | `IntegerField` | The current floor of the elevator.                               |
| `**direction** `     | `CharField`    | The direction of the elevator - "N" for north and "S" for south. |
| `**is_door_open**`   | `BooleanField` | Indicates whether the door of the elevator is open or not.       |
| `**is_operational**` | `BooleanField` | Indicates whether the elevator is operational or not.            |

## Request
The Request model represents a request made by a user.

| **Field**       | **Type**       | **Description**                                  |
| --------------- | -------------- | ------------------------------------------------ |
| `**id**`        | `AutoField`    | Unique identifier for the request.               |
| `**elevator**`  | `IntegerField` | The elevator id that will full fill the request. |
| `**floor**`     | `IntegerField` | The floor number of the request.                 |
| `**timestamp**` | `TimeStamp`    | The time stamp of the request.                   |
