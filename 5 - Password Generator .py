import random
import string

print('Welcome to the Password Generator!')

# Pedir ao usuário quantas letras, símbolos e números eles querem em sua senha
num_up_letters = int(input("How many upper letters would you like in your password? "))
num_low_letters = int(input("How many lower letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

# Gerar listas de caracteres aleatórios
letters_up = [random.choice(string.ascii_uppercase) for _ in range(num_up_letters)]
letters_low = [random.choice(string.ascii_lowercase) for _ in range(num_low_letters)]
symbols = [random.choice(string.punctuation) for _ in range(num_symbols)]
numbers = [random.choice(string.digits) for _ in range(num_numbers)]

# Combinar as listas e embaralhar a ordem
password_list = letters_up + letters_low + symbols + numbers
random.shuffle(password_list)

# Juntar os elementos da lista em uma string
password = ''.join(password_list)

print(f'Your password is: {password}')
