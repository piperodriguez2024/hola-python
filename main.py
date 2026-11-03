def saludar(nombre):
    return f"Hola {nombre}, bienvenido a Python desde mi Steam Deck!"

def main():
    nombre = input("Como te llamas? ").strip()

    if not nombre:
        nombre = "Mundo"

    print(saludar(nombre))

if __name__ == "__main__":
    main()
