# API Contracts

**Endpoint** : /api/elevator/

**Method** : GET
**Path Parameters** : None
**Body Parameters** : None

**Description** :
This endpoint allows retrieving all elevators

**Response**: 
```json
[
    {
        "id": "Elevator Object Id",
        "current_floor": "floorNumber",
        "direction": "N || S",
        "is_door_open": "true || false",
        "is_operational": "true || false"
    },
    "<Elevator Object 2>",
    ...
]
```
---
**Endpoint** : /api/request/

**Method** : GET
**Path Parameters** : None
**Body Parameters** : None

**Description** :
This endpoint allows retrieving all the requests

**Response**: 
```json
[
    {
        "id": "Request Object Id",
        "floor": "floor Number",
        "timestamp": "TimeStamp",
        "elevator": "Elevator Id",
    },
    "<Request Object 2>",
    "..."
]
```
---
**Endpoint** : /api/elevator/<int:pk>/

**Method** : GET
**Path Parameters** : Elevator Id
**Body Parameters** : None

**Description** :
Retrieves the current state of a specific elevator

**Response**: 
```json
{
    "id": "Elevator Object Id",
    "current_floor": "floorNumber",
    "direction": "N || S",
    "is_door_open": "true || false",
    "is_operational": "true || false"
}
```
---
**Endpoint** : /api/elevator/<int:pk>/requests/

**Method** : GET
**Path Parameters** : Elevator Id
**Body Parameters** : None

**Description** :
Retrieves the requests associated with a specific elevator

**Response**: 
```json
[
    {
        "id": "request identifier",
        "floor": "destination floor",
        "timestamp": "timestamp",
        "elevator": "request fullfilled elevator"
    },
    "<Request Object 2>",
    "..."
]
```
---
**Endpoint** : /api/elevator/request_elevator/

**Method** : POST
**Path** Parameters : None
**Body** Parameters : 
```json
{
    "floor" :  floorNumber
}
```


**Description** :
Sends a request to schedule an elevator to the desired floor

**Response**: 
```json
{
    "message": "Request full filled by elevator N from floor K"
}
```
---
**Endpoint** : /api/elevator/bulk_create_elevators/

**Method** : POST
**Path Parameters** : None
**Body Parameters** : 
```json
{
    "num_elevators" : "N"
}
```


**Description** :
Creates N number of elevators in bulk

**Response**: 
```json
{
    "message": "N elevators created successfully"
}
```
---
**Endpoint** : /api/elevator/<int:pk>/set_operational/<int:is_operational>/

**Method** : POST
**Path Parameters** : 
- [x] first param - Elevator Id (Integer)
- [x] second param - Operation State (Integer) 1 - Operational , 0 - Non-Operational
**Body Parameters** : None


**Description** :
Updates the operational state of a specific elevator

**Response**: 
```json
{
    "id": "Elevator Id",
    "current_floor": "Floor No",
    "direction": "N || S",
    "is_door_open": "true || false",
    "is_operational": "**desired Operation State (true || false)**",
}
```
---
**Endpoint** : /api/elevator/<int:pk>/set_door_status/<int:is_door_open>/

**Method** : POST
**Path Parameters** : 
- [x] first param - Elevator Id (Integer)
- [x] second param - Door State (Integer) 1 - open , 0 - Closed
**Body Parameters** : None


**Description** :
Updates the operational state of a specific elevator

**Response**: 
```json
{
    "id": "Elevator Id",
    "current_floor": "Floor No",
    "direction": "N || S",
    "is_door_open": "**desired door State (true || false)**",
    "is_operational": "true || false",
}
```
---
**Endpoint** : /api/elevator/<int:pk>/get_direction/

**Method** : POST
**Path Parameters** : Elevator Id (Integer)
**Body Parameters** : None


**Description** :
Gets the direction in which the specific elevator is moving i,e (North - N or South - S)

**Response**: 
```json
{
    "message": "The current direction of the elevator K is X"
}
```



