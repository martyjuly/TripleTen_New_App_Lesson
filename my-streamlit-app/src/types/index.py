class CustomType:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"CustomType(name={self.name}, value={self.value})"

def example_function(data):
    return [CustomType(name, value) for name, value in data.items()]