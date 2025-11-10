def make_shirt(size, text):
    """Display a message and the size of a shirt."""
    print(f"The size of your shirt is {size} and the text says: {text}.")
make_shirt('adult small', 'happy shawdow thoughts, angry echos beware')
make_shirt(size='adult small', text='happy shawdow thoughts, angry echos beware')

def make_large_shirt(text, size='large',):
    """Display a message and the size of a large shirt."""
    print(f"The size of your shirt is {size} and the text says: {text}.")
make_large_shirt('happy shawdow thoughts, angry echos beware')
make_large_shirt(size='medium', text='happy shawdow thoughts, angry echos beware')
make_large_shirt('its a keefe thing you wouldent understand')

def describe_city(city, country='switzerland'):
    """Display a message about a city and its country."""
    print(f"{city} is in {country}.")
describe_city('zürich')
describe_city('bern')
describe_city('dallas', 'the great country of texas')