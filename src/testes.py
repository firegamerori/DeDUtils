import random
from tables import Table
import manager

v = Table.create_from_arquive("tabela1")
v2 = Table.create_from_arquive("teste2")

m = manager.Manager()
m.tables.append(v)
m.tables.append(v2)

m.start()