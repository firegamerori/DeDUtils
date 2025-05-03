import typing

class Atributes:

    atrs = {"str": 0, "des": 0, "con": 0, "int": 0, "cha": 0}

    def __init__(self, str: int, des: int, con: int, int: int, cha: int):
        self.atrs["str"] = str
        self.atrs["des"] = des
        self.atrs["con"] = con
        self.atrs["int"] = int
        self.atrs["cha"] = cha

    def get_atribute(self, name: str):
        at = self.atrs.get(name[0:3])
        return at if at else None

    def set_atribute(self, name: str, value: int):
        if not name[0:3] in self.atrs:
            return

        self.atrs[name[0:3]] = value
    
    def to_json(self):
        pass

    pass


class Character:

    atributes: Atributes
    ac = 0
    speed = 0

    def __init__(self, str: int, des: int, con: int, int: int, cha: int, ac: int, speed: int):
        self.atributes = Atributes(str, des, con, int, cha)
        self.ac = ac
        self.speed = speed
        pass
    
    def to_json(self) -> dict[str, typing.Any]:
        js = {
            "atributes": self.atributes.to_json(),
            "ac": self.ac,
            "speed": self.speed
        }
        
        return js

    pass
