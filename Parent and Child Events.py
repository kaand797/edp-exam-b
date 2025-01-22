class EventWithChildrenQueue(EventQueue):
    def add_child_event(self, parent_event_key, child_event):
        """Add a child event to a specific parent event."""
        for event in self.queue:
            if event["key"] == parent_event_key:
                if "children" not in event:
                    event["children"] = []
                event["children"].append(child_event)
                return
        raise ValueError(f"Parent event with key '{parent_event_key}' not found.")
