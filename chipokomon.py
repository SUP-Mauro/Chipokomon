from random import randint
# Ascii alt + 254 = ■
vida_inicial_pikachu = 80
vida_inicial_squirtle = 90
vida_actual_pikachu = 80
vida_actual_squirtle = 90 

def mostrar_vida(nombre, vida_actual, vida_max):
    if vida_actual < 0:
        vida_actual = 0
    porcentaje = vida_actual / vida_max #69 / 80 = 0.8625
    barras_llenas = int(porcentaje * 10) # 0.8625 * 10 = int(8.625) = 8
    barras_vacias = 10 - barras_llenas # 10 - 8 = 2
    barra = '■' * barras_llenas + " " * barras_vacias # ■■■■■■■■ + "  " = "■■■■■■■■  "
    print(f'{nombre}: [{barra}] {vida_actual} HP')


while vida_actual_pikachu > 0 and vida_actual_squirtle > 0:
    #Se desenvuelven los turnos de combate

    #Turno de Pikachu
    print('Turno de Pikachu ⚡')
    ataque_pikachu = randint(1,2)
    if ataque_pikachu == 1:
        # Bola voltio
        print('Pikachu ataca con Bola Voltio')
        vida_actual_squirtle -= 10
    
    else:
        print('Pikachu ataca con Onda Trueno')
        vida_actual_squirtle -= 11

    mostrar_vida('Pikachu', vida_actual_pikachu, vida_inicial_pikachu)
    mostrar_vida('Squirtle', vida_actual_squirtle, vida_inicial_squirtle)
    input('Enter para continuar...\n\n')

    #Turno de Squirtle
    if vida_actual_squirtle <= 0:
        break
    print('Turno de Squirtle 🌊')
    ataque_squirtle = None


    while ataque_squirtle != 'P' and ataque_squirtle != 'A' and ataque_squirtle != 'B':
        ataque_squirtle = input('¿Que ataque deseas realizar? [P]lacaje, Pistola [A]gua, [B]urbuja \n')

    else:
        if ataque_squirtle == 'P':
            print('Squirtle ataca con Placaje')
            vida_actual_pikachu -= 10
        elif ataque_squirtle == 'A':
            print('Squirtle ataca con Pistola Agua')
            vida_actual_pikachu -= 12
        elif ataque_squirtle == 'B':
            print('Squirtle ataca con Burbuja')
            vida_actual_pikachu -= 9
    
    mostrar_vida('Pikachu', vida_actual_pikachu, vida_inicial_pikachu)
    mostrar_vida('Squirtle', vida_actual_squirtle, vida_inicial_squirtle)    
    input('Enter para continuar...\n\n')


if vida_actual_pikachu > vida_actual_squirtle:
    print('\n🏆 Pikachu Gana! ⚡')
else:
    print('\n🏆 Squirtle Gana! 🌊')