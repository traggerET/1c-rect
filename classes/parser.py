import typing
from collections import defaultdict


class SimpleCLI:
    def __init__(self):
        self.resp = defaultdict()
        self.resp["inaccuracy"] = 1
        self.resp["oriented"] = False

    def parse_args(self, args: typing.List) -> defaultdict:
        if len(args) == 1:
            return self.resp
        if args[1] == "oriented":
            self.resp["oriented"] = True
            self.resp["inaccuracy"] = 2

        return self.resp
