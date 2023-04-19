# Api Bondis SUBE

## Endpoints

Los posibles endpoints son los de la appi [onebusaway](http://developer.onebusaway.org/modules/onebusaway-application-modules/current/api/where/index.html)

```
agencies-with-coverage - list all supported agencies along with the center of their coverage area
agency - get details for a specific agency
arrival-and-departure-for-stop - details about a specific arrival/departure at a stop
arrivals-and-departures-for-stop - get current arrivals and departures for a stop
arrivals-and-departures-for-location - get current arrivals and departures for a stops near location
block - get block configuration for a specific block
cancel-alarm - cancel a registered alarm
current-time - retrieve the current system time
register-alarm-for-arrival-and-departure-at-stop - register an alarm for an arrival-departure event
report-problem-with-stop - submit a user-generated problem for a stop
report-problem-with-trip - submit a user-generated problem for a trip
route-ids-for-agency - get a list of all route ids for an agency
route - get details for a specific route
routes-for-agency - get a list of all routes for an agency
routes-for-location - search for routes near a location, optionally by route name
schedule-for-route - get the full schedule for a route on a particular day
schedule-for-stop - get the full schedule for a stop on a particular day
shape - get details for a specific shape (polyline drawn on a map)
stop-ids-for-agency - get a list of all stops for an agency
stop - get details for a specific stop
stops-for-location - search for stops near a location, optionally by stop code
stops-for-route - get the set of stops and paths of travel for a particular route
trip-details - get extended details for a specific trip
trip-for-vehicle - get extended trip details for current trip of a specific transit vehicle
trip - get details for a specific trip
trips-for-location - get active trips near a location
trips-for-route - get active trips for a route
```

## URL base

```
http://cuandosubo.sube.gob.ar/onebusaway-api-webapp/api/where/
```

## Endpoints Validas:

