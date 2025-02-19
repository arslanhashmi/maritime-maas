import datetime
from dataclasses import dataclass
from typing import List

import pytest
from model_bakery import baker, seq

from gtfs.models import (
    Agency,
    Departure,
    Fare,
    FareRiderCategory,
    FareRule,
    Feed,
    RiderCategory,
    Route,
)
from gtfs.tests.conftest import *  # noqa
from gtfs.tests.utils import get_feed_for_maas_operator


@dataclass
class FareTestData:
    feed: Feed
    routes: List[Route]
    fares: List[Fare]
    rider_categories: List[RiderCategory]
    departures: List[Departure]


@pytest.fixture
def fare_test_data(maas_operator, api_id_generator):
    """Basically two routes, two fares, two rider_categories and two departures."""
    feed = get_feed_for_maas_operator(maas_operator, True)

    agency = baker.make(
        Agency,
        name="Test agency"
    )
    routes = baker.make(
        Route,
        agency=agency,
        feed=feed,
        source_id=seq("source_id of route "),
        long_name="Name of route",
        _quantity=2,
    )

    # Fares
    fares = [
        baker.make(
            Fare,
            feed=feed,
            source_id="source_id of test fare 1",
            api_id=api_id_generator,
            name="Name of test fare 1",
            description="Description of test fare 1",
            instructions="Instructions of test fare 1",
        ),
        baker.make(
            Fare,
            feed=feed,
            source_id="source_id of test fare 2",
            api_id=api_id_generator,
            name="Name of test fare 2",
            description="Description of test fare 2",
            instructions="Instructions of test fare 2",
        ),
    ]

    baker.make(FareRule, feed=feed, fare=iter(fares), route=iter(routes))
    # Rider categories
    rider_categories = [
        baker.make(
            RiderCategory,
            feed=feed,
            source_id="source_id of test rider category 1",
            api_id=api_id_generator,
            name="name of test rider category 1",
            description="description of test rider category 1",
        ),
        baker.make(
            RiderCategory,
            feed=feed,
            source_id="source_id of test rider category 2",
            api_id=api_id_generator,
            name="name of test rider category 2",
            description="description of test rider category 2",
        ),
    ]

    baker.make(
        FareRiderCategory,
        feed=feed,
        fare=iter(fares),
        rider_category=iter(rider_categories),
        currency_type="EUR",
        price=seq(1),
        _quantity=2,
    )
    departures = baker.make(
        Departure,
        trip__feed=feed,
        trip__source_id=seq("source_id of trip "),
        trip__route=iter(routes),
        api_id=api_id_generator,
        date=datetime.date(2021, 4, 28),
        _quantity=2,
    )

    return FareTestData(
        feed,
        routes,
        fares,
        rider_categories,
        departures,
    )
