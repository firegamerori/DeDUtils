import random
import tables

v = tables.Table()
v.add_item(10, "Lorem ipsum dolor sit amet", "Lorem")
v.add_item(40, "adipiscing elit quisque faucibus", "ipsum")

for i in range(0, 10):
    print(v.roll().name)

v.save_in_arquive("table1")
