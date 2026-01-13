def sandwiches(*ingredients):
    """
    Docstring for sandwiches
    
    :param ingredients: Description
    """
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
sandwiches('ham', 'cheese', 'lettuce')
sandwiches('turkey', 'bacon', 'avocado', 'tomato')
sandwiches('peanut butter', 'jelly', 'bacon')
