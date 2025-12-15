from pathlib import Path

your_name = input("whats your name? ")
path = Path('guest.txt')
path.write_text(your_name)
