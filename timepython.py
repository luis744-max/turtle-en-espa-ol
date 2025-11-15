import turtle

t = turtle.Turtle()

#definir final de turtle
def listo():
    turtle.done()

def adios():
    turtle.bye()

#definir movimientos
def avanzar(numero):
    t.forward(numero)

def retroceder(numero):
    t.backward(numero)

#definir giros
def derecha(angulo):
    t.right(angulo)

def izquierda(angulo):
    t.left(angulo)

#definir bucles
def repetir(hasta):
    return range(hasta)

#definir formas y sellos
def punto(tamaño, color):
    color_ingles = colores.get(color.lower(),color)
    t.dot(tamaño, color_ingles)
    
def circulo(radio ,angulo=360):
    t.circle(radio ,angulo)

def triangulo(a):
    for z in repetir(3):
        derecha(120)
        avanzar(a)

def cuadrado(e):
    for z in repetir(4):
        derecha(90)
        avanzar(e)

def pentagono(i):
    for z in repetir(5):
        derecha(72)
        avanzar(i)

def hexagono(o):
    for z in repetir(6):
        derecha(60)
        avanzar(o)

def sellar():
    t.stamp()

def borrarSellos():
    t.clearstamps()

#definir rellenar
def colorDeRelleno(color):
    # Traduce el color si está en el diccionario
    color_ingles = colores.get(color.lower(), color)
    t.fillcolor(color_ingles)

def empezarRelleno():
    t.begin_fill()

def finalizarRelleno():
    t.end_fill()

#definir colores
colores = {
    "rojo": "red",
    "azul": "blue",
    "verde": "green",
    "amarillo": "yellow",
    "negro": "black",
    "blanco": "white",
    "morado": "purple",
    "naranja": "orange",
    "gris": "gray",
    "rosado": "pink"
}

#def pociciones
def ir(x,y):
    t.goto(x,y)

def irCentro():
    t.home()

def ubicacion():
    return t.pos()

def dejarAngulo(angulo):
    t.seth(angulo)

def anguloActual():
    return t.heading()

def arribaActual():
    return t.ycor()

def derechaActual():
    return t.xcor()

def distancia(x, y):
    return t.distance(x, y)

def direccionHasta(x, y):
    return t.towards(x, y)
#Pantalla y apariencia
def mostrarTortuga():
    t.st()

def ocultarTortuga():
    t.ht()

def reiniciar():
    t.reset()
    
def borrar():
    t.clear()

def titulo(texto):
    turtle.title(texto)

def ColorPantalla(color):
    # Traduce el color si está en el diccionario
    color_ingles = colores.get(color.lower(), color)
    turtle.bgcolor(color_ingles)

#definir lapiz
def lapizArriba():
    t.pu()

def lapizAbajo():
    t.pd()

def lapizColor(color):
    # Traduce el color si está en el diccionario
    color_ingles = colores.get(color.lower(), color)
    t.pencolor(color_ingles)

def velocidad(numero):
    t.speed(numero)

def formaTortuga(forma):
    t.shape(forma)

def tamañoTortuga(alto, ancho):
    t.shapesize(alto, ancho)

def colorLineaYRelleno(linea, relleno):
    linea = colores.get(linea.lower(), linea)
    relleno = colores.get(relleno.lower(), relleno)
    t.color(linea, relleno)

def anchoLinea(ancho):
    t.pensize(ancho)

def estaAbajo():
    return t.isdown()

#definir Tiempo
def esperar(tiempo):
    turtle.delay(tiempo)

def NoAnimacion():
    turtle.tracer(0)

def actualizar():
    turtle.update()
