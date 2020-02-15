import unittest
from unittest.mock import create_autospec
from async_bus import EventBus


async def mock_subscribe(param):
    pass


class TestEventBus(unittest.TestCase):

    def test_add_event(self):
        bus = EventBus()

        bus.add_event('event_test', lambda x: x)

        self.assertEqual(len(bus.events['event_test']), 1)

    def test_subscribe_decorator(self):
        bus = EventBus()

        @bus.subscribe('event_test')
        def test_subscriber():
            pass

        self.assertEqual(len(bus.events['event_test']), 1)

    def test_emit(self):
        bus = EventBus()
        subscriber = create_autospec(mock_subscribe)
        bus.add_event('event_test', subscriber)

        bus.emit('event_test', param='test_param')

        subscriber.assert_called_once_with(param='test_param')
