import random
import string

def generate_password(length):
    # Possible characters for the password (you can customize them) (Caracteres posibles para la contraseña (puedes personalizarlos))
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the random password (Genera la contraseña aleatoria)
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Define the desired password length (Definir la longitud de la contraseña deseada)
password_length = 15

# Generate and display the random password (Generar y mostrar la contraseña aleatoria)
for i in range(10):
    random_password = generate_password(password_length)
    print("Random Password:", random_password)
