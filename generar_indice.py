# -*- coding: utf-8 -*-
import os, html

BLOQUES = [
 ("bloque_a", "Bloque A", "Proyectos de investigación y desarrollo",
  "Desde la investigación y la ideación hasta la gestión del proyecto, el ciclo de vida del producto, la expresión gráfica con CAD y la comunicación de los resultados.",
  [(1, "El proyecto tecnológico: investigación, ideación y gestión",
      "Cómo se plantea un proyecto de investigación y desarrollo, cómo se generan ideas con método y cómo se organiza el trabajo de un equipo."),
   (2, "El producto: ciclo de vida, calidad, normalización y comercialización",
      "Cómo nace, se fabrica, se distribuye y se retira un producto, y con qué criterios se mide que está bien hecho."),
   (3, "Expresión gráfica del proyecto: croquis, esquemas y CAD, CAE y CAM",
      "Cómo se representa una solución técnica para que otra persona pueda entenderla, calcularla y fabricarla."),
   (4, "Herramientas digitales, documentación técnica y comunicación del proyecto",
      "Qué herramientas digitales sostienen un proyecto técnico y cómo se documenta y se presenta el resultado con rigor.")]),
 ("bloque_b", "Bloque B", "Materiales y fabricación",
  "Propiedades y clasificación de los materiales técnicos, nuevos materiales y tratamientos, criterios de sostenibilidad y técnicas de fabricación, con las normas de seguridad del taller.",
  [(5, "Propiedades, clasificación y selección de los materiales técnicos",
      "Qué distingue a un material de otro y con qué criterios técnicos y de sostenibilidad se elige el adecuado para un producto."),
   (6, "Técnicas de fabricación, prototipado y seguridad en el trabajo",
      "Cómo se transforma el material en pieza, qué aporta la fabricación digital y cómo se trabaja sin riesgo.")]),
 ("bloque_c", "Bloque C", "Sistemas mecánicos",
  "Máquinas y mecanismos que transmiten y transforman el movimiento, elementos de soporte y unión, y el cálculo, el diseño y el montaje de sistemas mecánicos.",
  [(7, "Máquinas y mecanismos de transmisión del movimiento",
      "Cómo se lleva el movimiento desde donde se genera hasta donde hace falta, y qué se gana y qué se pierde en el camino."),
   (8, "Transformación del movimiento, soportes, uniones y acoplamientos",
      "Cómo se convierte un giro en un desplazamiento y cómo se sujetan y se enlazan las piezas de una máquina."),
   (9, "Cálculo, diseño y montaje de sistemas mecánicos",
      "Cómo se dimensiona un mecanismo con las herramientas de las matemáticas y la física, y cómo se comprueba que funciona.")]),
 ("bloque_d", "Bloque D", "Sistemas eléctricos y electrónicos",
  "Circuitos y máquinas eléctricas de corriente continua y componentes y circuitos electrónicos básicos, desde su interpretación y cálculo hasta el montaje o la simulación.",
  [(10, "Circuitos y máquinas eléctricas de corriente continua",
      "Cómo se representa, se calcula y se monta un circuito de corriente continua, y cómo funciona el motor que lo convierte en movimiento."),
   (11, "Componentes y circuitos electrónicos",
      "Qué hacen los componentes electrónicos dentro de un circuito y cómo se lee un esquema que los combina.")]),
 ("bloque_e", "Bloque E", "Sistemas informáticos. Programación",
  "Desde los primeros programas en Python con Jupyter Notebook hasta las funciones, la placa controladora con MicroPython, la depuración y la conexión de dispositivos.",
  [(12, "Fundamentos de la programación textual: del problema al programa",
      "Qué es programar con un lenguaje textual, cómo se estructura un programa y cómo se ejecuta el primero."),
   (13, "Datos, variables y operaciones",
      "Con qué datos trabaja un programa, cómo se guardan en variables y cómo se combinan para obtener resultados."),
   (14, "Estructuras de control, funciones y primer programa en la placa",
      "Cómo decide y cómo repite un programa, cómo se parte en piezas con nombre propio y cómo se hace que actúe sobre el mundo físico."),
   (15, "Estructuras de datos y proceso de desarrollo",
      "Cómo se guardan muchos datos en una sola variable y cómo se organiza, se comprueba y se corrige un programa que crece."),
   (16, "Internet de las cosas y redes de dispositivos",
      "Cómo se conectan entre sí los objetos que fabricamos y qué protocolos hacen posible que se entiendan.")]),
 ("bloque_f", "Bloque F", "Sistemas automáticos",
  "Sistemas de control y su modelización, automatización programada de procesos, supervisión y telemetría, robótica e inteligencia artificial aplicada al control.",
  [(17, "Sistemas de control: conceptos, elementos y modelización",
      "Qué es un sistema de control, de qué piezas consta y cómo se representa para poder estudiarlo."),
   (18, "Automatización programada de procesos, supervisión y telemetría",
      "Cómo se automatiza un proceso con una placa programable y cómo se vigila y se registra su funcionamiento a distancia."),
   (19, "Robótica e inteligencia artificial aplicadas al control",
      "Cómo se modela y se programa el movimiento de un robot y qué aportan las tecnologías emergentes al control de un sistema.")]),
 ("bloque_g", "Bloque G", "Tecnología sostenible",
  "Obtención y distribución de la energía, sistemas y mercados energéticos, instalaciones de la vivienda, climatización y aislamiento, domótica, renovables y certificación energética.",
  [(20, "Fuentes de energía, sistemas y mercados energéticos",
      "De dónde sale la electricidad que llega al enchufe, cómo se transporta y cómo se fija lo que cuesta."),
   (21, "Instalaciones de la vivienda: electricidad y agua",
      "Cómo llegan la electricidad y el agua a una vivienda, cómo se protegen esas instalaciones y cómo se reduce su consumo."),
   (22, "Climatización, aislamiento y arquitectura sostenible",
      "Cómo se acondiciona una vivienda y por qué la mejor instalación de climatización es la que casi no hace falta."),
   (23, "Domótica, energías renovables y certificación energética",
      "Cómo se automatiza el ahorro en una vivienda, cómo se produce energía en ella y cómo se acredita que es eficiente.")]),
]

DOCS = "/Users/mag/Documents/ti1/ti1/docs"

def card(num, titulo, resumen):
    archivo = "tema%02d.html" % num
    existe = os.path.exists(os.path.join(DOCS, archivo))
    etiqueta = "Tema %02d" % num
    cuerpo = ('<span class="topic-number">%s</span><h2>%s</h2><p>%s</p>'
              % (etiqueta, html.escape(titulo), html.escape(resumen)))
    if existe:
        return ('<a class="topic-card" href="%s">%s<span class="go">Abrir tema →</span></a>'
                % (archivo, cuerpo))
    return ('<div class="topic-card is-pending">%s<span class="go">En preparación</span></div>'
            % cuerpo)

secciones = []
for sid, kicker, titulo, intro, temas in BLOQUES:
    tarjetas = "".join(card(*t) for t in temas)
    secciones.append(
        '<section class="index-section" aria-labelledby="%s"><p class="kicker index-kicker">%s</p>'
        '<h2 id="%s" class="index-heading">%s</h2><p class="index-intro">%s</p>'
        '<div class="topic-grid">%s</div></section>' % (sid, kicker, sid, titulo, intro, tarjetas))

doc = (
'<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
'<meta name="description" content="Materiales de Tecnología e Ingeniería I para 1.º de Bachillerato">'
'<title>Tecnología e Ingeniería I · 1.º de Bachillerato</title>'
'<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">\n'
'<link rel="stylesheet" href="assets/estilos.css"></head><body><a class="skip" href="#contenido">Saltar al contenido</a>\n'
'<div class="progress" aria-hidden="true"><span></span></div>\n'
'<header class="site-header"><div class="header-inner">\n'
'  <a class="brand" href="index.html"><span class="brand-mark">TI1</span><span>Tecnología e Ingeniería I<small>1.º de Bachillerato · 2026–2027</small></span></a>\n'
'</div></header>\n'
'<main id="contenido"><section class="hero"><div class="hero-inner hero-index"><div>'
'<p class="kicker">1.º de Bachillerato · Curso 2026–2027</p><h1>Tecnología e Ingeniería I</h1>'
'<p class="hero-lead">Materiales de teoría organizados por bloques y temas para acompañar el trabajo de la asignatura.</p>'
'</div></div></section>\n'
'<div class="index-shell">' + "\n\n".join(secciones) + '</div></main>\n'
'<footer class="site-footer">Tecnología e Ingeniería I · 1.º de Bachillerato · Comunidad de Madrid</footer></body></html>\n')

open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(doc)
print("index.html escrito:", len(doc), "bytes")
