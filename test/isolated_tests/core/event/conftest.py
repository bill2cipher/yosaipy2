import pytest

from yosaipy2.core import (
    EventLogger,
)


@pytest.fixture(scope='function')
def event_logger(event_bus):
    return EventLogger(event_bus)
