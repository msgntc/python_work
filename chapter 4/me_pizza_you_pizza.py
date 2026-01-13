pizzas = ['barbecue chicken', 'plain cheese', 'sausage']
for pizza in pizzas:
   print(f"I like {pizza.title()} pizza.")
print("pizza is yummy.")
freind_pizzas = pizzas[:]
pizzas.append('yummy')
freind_pizzas.append('cheese')
print(pizzas)
print(freind_pizzas)