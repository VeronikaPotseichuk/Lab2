from ..json_serializer import json_serializer

class pickle_serializer:
    
    def __init__(self):
        self.s = json_serializer()

    def loads(self, bin_string):
        return self.s.loads(self.from_hex(bin_string))

    def dumps(self, obj):
        return self.to_hex(self.s.dumps(obj))

    def load(self, string):
        return self.loads(string)  

    def dump(self, obj):
        return self.dumps(obj)

    def to_hex(self, s):
        return r"\x".join("{:02x}".format(c) for c in s.encode())

    def from_hex(self, hex):
        return r"".join("{}".format(chr(int(c, 16))) for c in hex.split(r'\x'))

    