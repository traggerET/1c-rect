import typing
from collections import defaultdict


class SimpleCLI:
    def __init__(self):
        self.resp = defaultdict()

    def ParseArgs(self, args: typing.List) -> dict:
        if len(args) == 1:
            return self.resp
        if args[1] == "oriented":
            self.resp["oriented"] = True

        return self.resp
