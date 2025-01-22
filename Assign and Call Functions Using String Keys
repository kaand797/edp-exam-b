class FunctionCallQueue:
    def __init__(self):
        self.functions = {}

    def add_function(self, key, func):
        """Assign a function to a string key."""
        self.functions[key] = func

    def call_function(self, key, *args, **kwargs):
        """Call the function associated with the string key."""
        if key in self.functions:
            return self.functions[key](*args, **kwargs)
        raise KeyError(f"No function found for key '{key}'.")
