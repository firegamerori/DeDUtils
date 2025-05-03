import json
import random

PATH_TO_ARQ = "ress/tables"


class Item:
    prob = 0
    name = ""
    desc = ""

    def __init__(self, prob: int, name: str, desc: str):
        self.prob = prob
        self.name = name
        self.desc = desc

        pass

    def __str__(self):
        return "name: {0} \nprob: {1}\ndesc: {2}".format(
            self.name, self.prob, self.desc
        )
        pass

    def to_json(self):
        return {"name": self.name, "prob": self.prob, "desc": self.desc}
        pass

    pass


class Table:

    name = ""
    item_list : list[Item] = []
    prob_total = 0

    def __init__(self, name):
        self.name = name
        pass

    def add_item(self, prob: int, name: str, desc: str):
        self.prob_total += prob
        self.item_list.append(Item(prob, name, desc))
        pass

    @staticmethod
    def create_from_archive(name: str):
        arq = open("{0}/{1}.json".format(PATH_TO_ARQ, name), "r")
        js = json.loads(arq.read())

        table = Table(js["name"])

        for item in js["items"].values():
            table.add_item(item["prob"], item["name"], item["desc"])

        return table
        pass

    def roll(self):
        # roll from the dice
        r = random.randint(1, self.prob_total)
        actual = 1

        for item in self.item_list:
            item : Item = item
            if r >= actual and r <= item.prob + actual:
                return item
            actual += item.prob

        pass

    def save_in_archive(self, name: str):
        arq = open("{0}/{1}.json".format(PATH_TO_ARQ, name), "w")
        items = {}

        v = 0

        for i in self.item_list:
            items[str(v)] = i.to_json()
            v += 1
            pass

        jsn = {"name": name, "items": items}

        j = json.dumps(jsn)
        arq.write(j)
        pass

    pass
