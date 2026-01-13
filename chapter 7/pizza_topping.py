order = input("What would you like on your pizza? ")
while True:
    print(f"Adding {order} to your pizza.")
    order = input("Anything else? (type \"done\" to finish) ")
    if order.lower() == 'done':
        break
print(f"Your pizza is ready!")