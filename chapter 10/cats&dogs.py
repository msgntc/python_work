try:    
    from pathlib import Path
    path = Path('cats.txt')
    contents = path.read_text()
    print(contents)
    path = Path('dogs.txt')
    contents = path.read_text()
    print(contents)
except FileNotFoundError:
    pass