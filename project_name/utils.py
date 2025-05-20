import json


class PrettyLog:
    """
    Nice print for configuration dicts.
    """

    def __init__(self, obj):
        self.obj = dict(obj)

    def __repr__(self):
        return json.dumps(self.obj, indent=4, default=str)
