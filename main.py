
class EventQueue:
    def init(self):
        self.queue = []

    def add_event(self, event):
        """Add an event to the queue."""
        self.queue.append(event)

    def get_events(self):
        """Return all events in the queue."""
        return self.queue

eq = EventQueue()
eq.add_event({"key": "event_a", "payload": {"data": "Hello from A"}})
eq.add_event({"key": "event_b", "payload": {"data": "Hello from B"}})

print(eq.get_events())

class EventQueue:
    def init(self):
        self.queue = []

    def add_event(self, event):
        """Add an event to the queue."""
        self.queue.append(event)

    def add_child_event(self, parent_event_key, child_event):
        """Add a child event to a specific parent event."""
        for event in self.queue:
            if event["key"] == parent_event_key:
                if "children" not in event:
                    event["children"] = []
                event["children"].append(child_event)
                return
        raise ValueError(f"Parent event with key '{parent_event_key}' not found.")


eq = EventQueue()
eq.add_event({"key": "event_a", "payload": {"data": "Hello from A"}})
eq.add_child_event("event_a", {"key": "child_event_a", "payload": {"data": "Child of A"}})

print(eq.queue)


class EventQueue:
    def init(self):
        self.queue = []

    def emit(self, event):
        """Emit an event."""
        print(f"Event Emitted: {event}")
        self.queue.append(event)


eq = EventQueue()
eq.emit({"key": "event_a", "payload": {"data": "Hello from A"}})
eq.emit({"key": "event_b", "payload": {"data": "Hello from B"}})

print(eq.queue)


class EventQueue:
    def init(self):
        self.queue = []
        self.handlers = {}

    def add_handler(self, event_key, handler):
        """Add a handler for a specific event key."""
        if event_key not in self.handlers:
            self.handlers[event_key] = []
        self.handlers[event_key].append(handler)

    def emit(self, event):
        """Emit an event and call associated handlers."""
        self.queue.append(event)
        if event["key"] in self.handlers:
            for handler in self.handlers[event["key"]]:
                handler(event["payload"])

def on_event_a(payload):
    print(f"Handled Event A with payload: {payload}")

eq = EventQueue()
eq.add_handler("event_a", on_event_a)
eq.emit({"key": "event_a", "payload": {"data": "Hello from A"}})

class EventQueue:
    def init(self):
        self.functions = {}

    def add_function(self, key, func):
        """Assign a function to a string key."""
        self.functions[key] = func

    def call_function(self, key, *args, **kwargs):
        """Call the function associated with the string key."""
        if key in self.functions:
            return self.functions[key](*args, **kwargs)
        raise KeyError(f"No function found for key '{key}'.")

def example_function(x, y):
    return x + y

eq = EventQueue()
eq.add_function("add", example_function)
result = eq.call_function("add", 5, 3)

print(f"Result: {result}")