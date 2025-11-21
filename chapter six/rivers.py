"""nortoha:
take a look at line 2, your loop var is rive_r 
but your print statement prints the whole river list, instead of each item.
"""
river = {'nile': 'Egypt', 'missisipy': 'USA', 'amazon': 'Brizil'}
for rive_r, country in river.items():
    print(f"The {river} river is in {country}")

for ri_ver in river.keys():
    print(ri_ver)
for countr_y in river.values():
    print(countr_y)