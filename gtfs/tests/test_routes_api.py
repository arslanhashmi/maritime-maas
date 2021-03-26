import json

import pytest
from model_bakery import baker

from gtfs.models import Route, Stop, StopTime, Trip


@pytest.mark.django_db
def test_routes(maas_api_client):

    endpoint = "/v1/routes/"

    route = baker.make(Route)
    trip = baker.make(Trip, route=route)
    stop = baker.make(Stop)
    baker.make(StopTime, trip=trip, stop=stop)

    response = maas_api_client.get(endpoint)

    assert response.status_code == 200
    assert len(json.loads(response.content)) == 1


@pytest.mark.django_db
def test_routes_with_stop_id(maas_api_client):

    routes = baker.make(Route, _quantity=3)
    trip = baker.make(Trip, route=routes[0])
    stop = baker.make(Stop)
    baker.make(StopTime, trip=trip, stop=stop)

    endpoint = "/v1/routes/"
    url = f"{endpoint}?stop_id={stop.api_id}"

    response = maas_api_client.get(url)

    assert response.status_code == 200
    assert len(json.loads(response.content)) == 1
