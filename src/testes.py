import random
import tables
import manager

v = tables.Table("foda")
v.add_item(10, "Lorem ipsum dolor sit amet", "Lorem")
v.add_item(40, "adipiscing elit quisque faucibus", "ipsum")

v2 = tables.Table("foda2")
v2.add_item(100, "foda", "Lorem")
v2.add_item(40, "adipiscing elit quisque faucibus", "ipsum")

m = manager.Manager()
m.tables.append(v)
m.tables.append(v2)

m.start()