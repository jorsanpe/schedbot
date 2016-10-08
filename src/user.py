class User:
    def __init__(self, **kwargs):
        self.props = {}
        self.props.update(kwargs)

    def __setitem__(self, key, value):
        self.props[key] = value

    def __getitem__(self, item):
        if self.props.has_key(item):
            return self.props[item]
        return None
