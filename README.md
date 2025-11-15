timepython — Turtle en Español

timepython es una librería que traduce al español los comandos del módulo turtle de Python, permitiendo programar sin necesidad de conocer los nombres originales en inglés.
Está diseñado para estudiantes, principiantes y entornos educativos.

Características

Comandos 100% en español.

Traducción automática de colores.

Compatible con cualquier versión de Python.

Conserva toda la funcionalidad de turtle.

Facilita el aprendizaje para quienes no dominan el inglés.

Instalación

Coloca el archivo timepython.py en Desktop junto a instalador.py . Al hacer doble click sobre instalador.py se copiara en la dirección lib en las carpetas de python 

Ejemplo en Windows:

C:\Users\TU_USUARIO\AppData\Local\Programs\Python\Python313\Lib\


Luego impórtalo así:

from timepython import *

Ejemplo rápido de uso

from timepython import *

import turtle

ColorPantalla("azul")

lapizColor("rojo")

avanzar(100)

derecha(90)

cuadrado(80)

listo()

## Requisito importante

Para que el instalador funcione correctamente:

- Debe tener importado turtle con `import turtle`
- El archivo `timepython.py` debe estar directamente en el Escritorio.
- El archivo `instalador.py` también debe estar directamente en el Escritorio.
- No deben estar dentro de ninguna carpeta.

Esto se debe a que el instalador busca los archivos automáticamente en:
- `C:\Users\USUARIO\Desktop\`
- `C:\Users\USUARIO\OneDrive\Desktop\`

Si los archivos no están en estas rutas, el instalador no podrá encontrarlos.


Documentación de comandos

A continuación se listan todos los comandos disponibles y su equivalente original en turtle.

Finalización
Español	Turtle original

listo()	turtle.done()

adios()	turtle.bye()

Movimientos

Español	Turtle original

avanzar(n)	t.forward(n)

retroceder(n)	t.backward(n)

Giros

Español	Turtle original

derecha(a)	t.right(a)

izquierda(a)	t.left(a)

Bucles

Español	Turtle original

repetir(n)	range(n)

Figuras y sellos

Español	Turtle original

punto(tamaño, color)	t.dot()

circulo(radio, a)	t.circle()

triangulo(lado)	3 veces: derecha(120) + avanzar(lado)

cuadrado(lado)	4 veces: derecha(90) + avanzar(lado)

pentagono(lado)	5 veces: derecha(72) + avanzar(lado)

hexagono(lado)	6 veces: derecha(60) + avanzar(lado)

sellar()	t.stamp()

borrarSellos()	t.clearstamps()

Relleno

Español	Turtle original

colorDeRelleno(c)	t.fillcolor(c)

empezarRelleno()	t.begin_fill()

finalizarRelleno()	t.end_fill()

Posición y orientación

Español	Turtle original

ir(x, y)	t.goto(x, y)

irCentro()	t.home()

ubicacion()	t.pos()

dejarAngulo(a)	t.seth(a)

anguloActual()	t.heading()

arribaActual()	t.ycor()

derechaActual()	t.xcor()

distancia(x, y)	t.distance(x, y)

direccionHasta(x, y)	t.towards(x, y)

Pantalla y apariencia

Español	Turtle original

mostrarTortuga()	t.showturtle()

ocultarTortuga()	t.hideturtle()

reiniciar()	t.reset()

borrar()	t.clear()

titulo(texto)	turtle.title(texto)

ColorPantalla(color)	turtle.bgcolor(color)

Lápiz

Español	Turtle original

lapizArriba()	t.penup()

lapizAbajo()	t.pendown()

lapizColor(c)	t.pencolor(c)

velocidad(n)	t.speed(n)

formaTortuga(f)	t.shape(f)

tamañoTortuga(h, a)	t.shapesize(h, a)

colorLineaYRelleno(l, r)	t.color(l, r)

anchoLinea(n)	t.pensize(n)

estaAbajo()	t.isdown()

Tiempo y animación

Español	Turtle original

esperar(ms)	turtle.delay(ms)

NoAnimacion()	turtle.tracer(0)

actualizar()	turtle.update()

Colores disponibles


Los siguientes colores en español se traducen a su equivalente en inglés:

rojo → red


azul → blue

verde → green

amarillo → yellow

negro → black

blanco → white

morado → purple

naranja → orange

gris → gray

rosado → pink

Contribuciones

Si deseas reportar errores o proponer mejoras para futuras actualizaciones, por favor abre un issue en el repositorio.

Licencia

MIT License.
## Licencia

Este proyecto está licenciado bajo los términos de la **MIT License**.  
Puedes encontrar el archivo de licencia en el repositorio con el nombre **LICENSE**.







