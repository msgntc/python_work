from pathlib import Path
list_name = []
while True:
    your_name = input("What is your name? ")
    list_name.append(your_name + '\n')
    print(f"Welcome to the guest list {your_name}!")

    
    if your_name.lower() == 'q':
        list_name.pop()
        
        break
contnents = ''.join(list_name)   
path = Path('guest_book.txt')
path.write_text(contnents) 