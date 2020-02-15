# Py Async Bus

A simple async event bus in Python

Installing
----------

Install with **pip**:

```sh
$ pip install py-async-bus
```


Usage
----------

```py
from async_bus import EventBus

bus = EventBus()

@bus.subscribe('event_name')
async def subscriber(param):
    print(param)


bus.emit('event_name', param='test_param')
```

Tests
----------
```sh
$ python -m unittest
```
