import variables
#first it will check if __name__ == __main__ (in this case module name is variables from variables.py)

Username = input("Введите ваше имя: ")

def print_hi(name):
    print(f'Hi, {name}') 

if __name__ == '__main__':
    print_hi(Username)