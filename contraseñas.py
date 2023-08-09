import re

def check_password_strength(password):
    # Verificar la longitud mínima
    if len(password) < 8:
        return "La contraseña es demasiado corta."

    # Verificar al menos una letra mayúscula
    if not re.search(r'[A-Z]', password):
        return "La contraseña debe contener al menos una letra mayúscula."

    # Verificar al menos una letra minúscula
    if not re.search(r'[a-z]', password):
        return "La contraseña debe contener al menos una letra minúscula."

    # Verificar al menos un número
    if not re.search(r'[0-9]', password):
        return "La contraseña debe contener al menos un número."

    return "La contraseña es segura."

def main():
    password = input("Ingrese la contraseña a evaluar: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
