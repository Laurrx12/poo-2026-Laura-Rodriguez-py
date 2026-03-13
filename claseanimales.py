class Animal:
    def __init__(self, nombre, sonido, movimiento):
        self.nombre = nombre
        self.sonido = sonido
        self.movimiento = movimiento

    def hacer_sonido(self):
        print(self.nombre, "dice:", self.sonido)

    def mover(self):
        print(self.nombre, "se mueve:", self.movimiento)


# Crear animales
vaca = Animal("Vaca", "Muuu", "caminando")
paloma = Animal("Paloma", "Coo coo", "volando")
cerdito = Animal("Cerdito", "Oink oink", "caminando")
pollito = Animal("Pollito", "Pío pío", "saltando")

# Usar los métodos
vaca.hacer_sonido()
vaca.mover()

paloma.hacer_sonido()
paloma.mover()

cerdito.hacer_sonido()
cerdito.mover()

pollito.hacer_sonido()
pollito.mover()