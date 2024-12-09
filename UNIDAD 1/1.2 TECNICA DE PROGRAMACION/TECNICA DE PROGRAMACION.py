import random


class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, energia):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.energia = energia

    def atributos(self):
        print(f"{self.nombre}:")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Inteligencia: {self.inteligencia}")
        print(f"· Defensa: {self.defensa}")
        print(f"· Vida: {self.vida}")
        print(f"· Energía: {self.energia}")

    def subir_nivel(self, fuerza=0, inteligencia=0, defensa=0, vida_extra=0, energia_extra=0):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.vida += vida_extra
        self.energia += energia_extra

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"⚔️ {self.nombre} ha muerto.")

    def atacar(self, enemigo):
        if self.energia <= 0:
            print(f"{self.nombre} está cansado y no puede atacar.")
            return

        daño = max(self.fuerza + random.randint(-2, 2) - enemigo.defensa, 0)
        enemigo.vida -= daño
        self.energia -= 5  # Coste de energía por ataque
        print(f"{self.nombre} inflige {daño} puntos de daño a {enemigo.nombre}.")
        if enemigo.esta_vivo():
            print(f"Vida restante de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()

    def descansar(self):
        self.energia += 10
        print(f"{self.nombre} descansa y recupera 10 puntos de energía.")


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, energia, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, energia)
        self.espada = espada

    def cambiar_arma(self):
        print("Opciones de espada:")
        print("(1) Acero Valyrio, daño +8")
        print("(2) Matadragones, daño +10")
        opcion = input("Elige tu arma: ")
        if opcion == "1":
            self.espada = 8
        elif opcion == "2":
            self.espada = 10
        else:
            print("Opción no válida. Mantienes tu arma actual.")

    def atacar(self, enemigo):
        daño = max(self.fuerza + self.espada - enemigo.defensa, 0)
        enemigo.vida -= daño
        print(f"⚔️ {self.nombre} usa su espada y causa {daño} de daño a {enemigo.nombre}.")
        if enemigo.esta_vivo():
            print(f"Vida restante de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, energia, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, energia)
        self.libro = libro

    def lanzar_hechizo(self, enemigo):
        if self.energia < 10:
            print(f"{self.nombre} no tiene suficiente energía para lanzar un hechizo.")
            return

        daño = max(self.inteligencia * self.libro - enemigo.defensa, 0)
        enemigo.vida -= daño
        self.energia -= 10  # Coste de energía del hechizo
        print(f"✨ {self.nombre} lanza un hechizo causando {daño} de daño a {enemigo.nombre}.")
        if enemigo.esta_vivo():
            print(f"Vida restante de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()


def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        if turno % 2 != 0:
            jugador_1.atacar(jugador_2)
        else:
            jugador_2.atacar(jugador_1)
        turno += 1

        # Opción para descansar y recuperar energía cada 5 turnos
        if turno % 5 == 0:
            jugador_1.descansar()
            jugador_2.descansar()

    if jugador_1.esta_vivo():
        print(f"\n🏆 ¡{jugador_1.nombre} ha ganado el combate!")
    elif jugador_2.esta_vivo():
        print(f"\n🏆 ¡{jugador_2.nombre} ha ganado el combate!")
    else:
        print("\n🤝 El combate terminó en empate.")


# Ejemplo de ejecución
personaje_1 = Guerrero("Guts", 20, 10, 8, 100, 50, 5)
personaje_2 = Mago("Vanessa", 5, 18, 6, 100, 50, 3)

personaje_1.atributos()
personaje_2.atributos()

combate(personaje_1, personaje_2)
