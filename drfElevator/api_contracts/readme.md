# API Contracts

**Endpoint** : /api/elevator/<br />

**Method** : GET<br />
**Path Parameters** : None<br />
**Body Parameters** : None<br />

**Description** :<br />
This endpoint allows retrieving all elevators<br />

**Response**:<br />
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
**Endpoint** : /api/request/<br />

**Method** : GET<br />
**Path Parameters** : None<br />
**Body Parameters** : None<br />

**Description** :<br />
This endpoint allows retrieving all the requests

**Response**:<br />
```json
[
    {
        "id": "Request Object Id",
        "floor": "floor Number",
        "timestamp": "TimeStamp",
        "elevator": "Elevator Id",
    },
    "<Request Object 2>",
    "...",
    "<Request Object N>",
]
```
---
**Endpoint** : /api/elevator/<int:pk>/<br />

**Method** : GET<br />
**Path Parameters** : Elevator Id<br />
**Body Parameters** : None<br />

**Description** :<br />
Retrieves the current state of a specific elevator

**Response**:<br />
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
**Endpoint** : /api/elevator/<int:pk>/requests/<br />

**Method** : GET<br />
**Path Parameters** : Elevator Id<br />
**Body Parameters** : None<br />

**Description** :<br />
Retrieves the requests associated with a specific elevator<br />

**Response**:<br />
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
**Endpoint** : /api/elevator/request_elevator/<br />

**Method** : POST<br />
**Path** Parameters : None<br />
**Body** Parameters :<br />
```json
{
    "floor" :  "floorNumber"
}
```


**Description** :<br />
Sends a request to schedule an elevator to the desired floor

**Response**:<br />
```json
{
    "message": "Request full filled by elevator N from floor K"
}
```
---
**Endpoint** : /api/elevator/bulk_create_elevators/<br />

**Method** : POST<br />
**Path Parameters** : None<br />
**Body Parameters** : 
```json
{
    "num_elevators" : "N"
}
```


**Description** :<br />
Creates N number of elevators in bulk

**Response**:<br />
```json
{
    "message": "N elevators created successfully"
}
```
---
**Endpoint** : /api/elevator/<int:pk>/set_operational/<int:is_operational>/<br />

**Method** : POST<br />
**Path Parameters** :<br />
- [x] first param - Elevator Id (Integer)<br />
- [x] second param - Operation State (Integer) 1 - Operational , 0 - Non-Operational<br />
**Body Parameters** : None<br />


**Description** :<br />
Updates the operational state of a specific elevator<br />

**Response**:<br />
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
**Endpoint** : /api/elevator/<int:pk>/set_door_status/<int:is_door_open>/<br />

**Method** : POST<br />
**Path Parameters** :<br />
- [x] first param - Elevator Id (Integer)<br />
- [x] second param - Door State (Integer) 1 - open , 0 - Closed<br />
**Body Parameters** : None<br />


**Description** :<br />
Updates the operational state of a specific elevator<br />

**Response**: <br />
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
**Endpoint** : /api/elevator/<int:pk>/get_direction/<br />

**Method** : POST<br />
**Path Parameters** : Elevator Id (Integer)<br />
**Body Parameters** : None<br />


**Description** :<br />
Gets the direction in which the specific elevator is moving i,e (North - N or South - S)

**Response**:<br /> 
```json
{
    "message": "The current direction of the elevator K is X"
}
```



