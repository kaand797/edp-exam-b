class EventHandlerQueue(EventQueue):
    def __init__(self):
        super().__init__()
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
