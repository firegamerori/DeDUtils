import json
from character import Character

PATH_TO_CREATURE = "ress/creature"


class Creature(Character):

    actions: dict[str, str] = {}
    hitPoints: str = ''
    lang = ''
    senses = ''
    challange = ''
    about = ""

    def __init__(
        self, str: int, des: int, con: int, int: int, cha: int, ac: int, speed: str
    ):
        super().__init__(str, des, con, int, cha, ac, speed)

    def change_about(self, about: str):
        self.about = about

    def add_action(self, name: str, desc: str):
        self.actions[name] = desc

    def save_on_archive(self, name: str):
        dic = self.to_json()
        js = json.dumps(dic)
        arq = open("{0}/{1}.json".format(PATH_TO_CREATURE, name), "w")
        arq.write(js)
        pass

    def to_json(self):
        old = super().to_json()
        old["actions"] = self.actions
        old["senses"] = self.senses
        old["challange"] = self.challange
        old["about"] = self.about
        old["lang"] = self.lang

        return old
        pass

    pass
