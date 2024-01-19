"""Base de datos para DnD que recoge los stats de cada personaje como objetos"""


class Personaje:

    def __init__(self, nombre: str, clase: str, fuerza, destreza, constitucion, intelecto,
                 sabiduria, carisma, vida, ataque, defensa, ins, mov, alerta,
                 comunicacion, manipulacion,
                 erudicion, subterfugio, superviviencia):
        """Clase consructora, donde se introducen los atributos"""
        self.nombre = nombre
        self.clase = clase
        self.fuerza = fuerza
        self.destreza = destreza
        self.constitucion = constitucion
        self.intelecto = intelecto
        self.sabiduria = sabiduria
        self.carisma = carisma
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.ins = ins
        self.mov = mov
        self.alerta = alerta
        self.comunicacion = comunicacion
        self.manipulacion = manipulacion
        self.erudicion = erudicion
        self.subterfugio = subterfugio
        self.superviviencia = superviviencia

    def atributos(self):
        """Devuelve los atributos del personaje"""
        print("---------------------------")
        print(f"Atributos de {self.nombre}\n")
        print(f"-Nombre: {self.nombre}")
        print(f"-Clase: {self.clase}")
        print(f"-Fuerza: {self.fuerza}")
        print(f"-Destreza: {self.destreza}")
        print(f"-Constitución: {self.constitucion}")
        print(f"-Intelecto: {self.intelecto}")
        print(f"-Sabiduría: {self.sabiduria}")
        print(f"-Carisma: {self.carisma}")
        print(f"-Vida: {self.vida}")
        print("--------------------------")
        return None

    def combathability(self):
        """Devuelve las habilidades de combate del personaje"""
        print("--------------------------")
        print(f"-Estadísticas de combate de {self.nombre}\n")
        print(f"-Ataque: {self.ataque}")
        print(f"-Defensa: {self.defensa}")
        print(f"-Instinto: {self.ins}")
        print(f"-Movimiento: {self.mov}")
        print("--------------------------")
        return None

    def standardhability(self):
        """Devuelves las habilidades no ideadas para combate del personaje"""
        print("--------------------------")
        print(f"-Habilidades de {self.nombre}\n")
        print(f"-Alerta: {self.alerta}")
        print(f"-Comunicación: {self.comunicacion}")
        print(f"-Manipulación: {self.manipulacion}")
        print(f"-Erudición: {self.erudicion}")
        print(f"-Subterfugio: {self.subterfugio}")
        print(f"-Supervivencia: {self.superviviencia}")
        print("--------------------------")
        return None

    def fullcharinfo(self):
        """Devuelve todas las estadísticas del personaje"""
        Personaje.atributos(self)
        Personaje.standardhability(self)
        Personaje.combathability(self)

# (ಠ_ಠ) Microwavedd