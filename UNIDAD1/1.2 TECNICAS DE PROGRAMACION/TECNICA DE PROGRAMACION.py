class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha caído en combate.")

    def daño(self, enemigo):
        return max(1, self.fuerza - enemigo.defensa)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "inflige", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida restante de", enemigo.nombre, ":", enemigo.vida)
        else:
            enemigo.morir()


class Arquero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arco):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arco = arco

    def cambiar_arco(self):
        opcion = int(input("Elige un arco: (1) Largo, daño x2. (2) Compuesto, daño x3: "))
        if opcion == 1:
            self.arco = 2
        elif opcion == 2:
            self.arco = 3
        else:
            print("Opción incorrecta, mantienes el arco actual.")

    def atributos(self):
        super().atributos()
        print("·Arco (multiplicador de daño):", self.arco)

    def daño(self, enemigo):
        return max(1, (self.fuerza * self.arco) - enemigo.defensa)


class Hechicero(Personaje):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, bastón):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.bastón = bastón

    def mejorar_baston(self):
        opcion = int(input("Elige una mejora para el bastón: (1) Fuego, daño +3. (2) Hielo, daño +5: "))
        if opcion == 1:
            self.bastón += 3
        elif opcion == 2:
            self.bastón += 5
        else:
            print("Opción incorrecta, mantienes el bastón actual.")

    def atributos(self):
        super().atributos()
        print("·Bastón (potencia mágica):", self.bastón)

    def daño(self, enemigo):
        return max(1, (self.inteligencia * self.bastón) - enemigo.defensa)


def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\n--- Turno", turno, "---")
        print("Acción de", jugador_1.nombre)
        jugador_1.atacar(jugador_2)
        if not jugador_2.esta_vivo():
            break
        print("Acción de", jugador_2.nombre)
        jugador_2.atacar(jugador_1)
        turno += 1

    if jugador_1.esta_vivo():
        print("\n¡El ganador es", jugador_1.nombre + "!")
    elif jugador_2.esta_vivo():
        print("\n¡El ganador es", jugador_2.nombre + "!")
    else:
        print("\n¡Es un empate!")


# Crear personajes
personaje_1 = Arquero("Legolas", 18, 8, 5, 90, 2)
personaje_2 = Hechicero("Gandalf", 6, 20, 4, 100, 4)

# Mostrar atributos iniciales
personaje_1.atributos()
personaje_2.atributos()

# Combate
combate(personaje_1, personaje_2)
