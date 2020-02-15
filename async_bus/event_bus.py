import asyncio
from collections import defaultdict
from functools import wraps


class EventBus:
    """
    EventBus class to run async subscribers
    """

    def __init__(self):
        self.__events = defaultdict(set)

    def __str__(self):
        return 'EventBus'

    def __repr__(self):
        return f'<EventBus: {len(self.__events.items())} events>'

    @property
    def events(self):
        """
        Property for returning events and their respective subscribers

        :return: Events and their respective subscribers
        """
        return self.__events

    def subscribe(self, event_name):
        """
        Decorator for subscribing a handler to an event

        :param event_name: Event name for subscribing
        """
        def wrapper(subscriber):
            self.add_event(event_name, subscriber)

            @wraps(subscriber)
            def wrapped(*args, **kwargs):
                return subscriber(*args, **kwargs)

            return wrapped

        return wrapper

    def add_event(self, event_name, subscriber):
        """
        Method for subscribing a handler to an event

        :param event_name: Event name for subscribing
        :param subscriber: Subscriber of the event
        """
        self.__events[event_name].add(subscriber)

    def emit(self, event_name, *args, **kwargs):
        """
        Method for emitting an event

        :param event_name: Event name for emitting their subscribers
        """
        asyncio.run(self.__run_subscribers(event_name, *args, **kwargs))

    async def __run_subscribers(self, event_name, *args, **kwargs):
        subscribers = self.__events[event_name]

        await asyncio.wait(
            [subscriber(*args, **kwargs) for subscriber in subscribers]
        )
