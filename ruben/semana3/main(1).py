import random
import string

# Importación del archivo de palabras
from ahorcado import lista
from vidas_ahorcado import vidas_ahorcado

def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def ahorcado():
    print("============================")
    print(" ¡Bienvenido(a) al juego del ahorcado!")
    print("============================")

    palabra = obtener_palabra_valida(lista)
    letras_por_adivinar = set(palabra)
    abecedario = set(string.ascii_uppercase)
    
    letras_adivinadas = set()

    vidas = 6  # Empezamos con 6 vidas para coincidir con el dibujo

    while len(letras_por_adivinar) > 0 and vidas >= 0:
        print(vidas_ahorcado[6 - vidas])  # Mostrar dibujo correspondiente
        print(f"\nTe quedan {vidas} vidas.")
        print("Letras usadas: ", ' '.join(sorted(letras_adivinadas)))

        palabra_mostrada = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print("Palabra: ", ' '.join(palabra_mostrada))

        letra_usuario = input("Escoge una letra: ").upper()

        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("¡Bien hecho!")
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario}, no está en la palabra.")
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

    # Resultado final
    if vidas < 0:
        print(vidas_ahorcado[0])  # Mostrar ahorcado final
        print(f"\n¡Ahorcado! Perdiste. La palabra era: {palabra}")
    else:
        print(f"\n¡Excelente! ¡Adivinaste la palabra {palabra}!")

if __name__ == '__main__':
    ahorcado()