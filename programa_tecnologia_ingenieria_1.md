# Programa de la asignatura — Tecnología e Ingeniería I

## 1.º de Bachillerato · materia de modalidad · Comunidad de Madrid

Documento de referencia de los contenidos teóricos de la asignatura, organizado según los siete bloques de contenidos que el currículo de la Comunidad de Madrid enumera para la materia. Integra los bloques A, B, C, D, E, F y G en veintitrés temas. El proyecto es el eje metodológico de la materia: el currículo pide expresamente que los contenidos «se interrelacionen a través del desarrollo de actividades o proyectos de carácter práctico», de modo que la teoría acompaña al diseño, al cálculo, al montaje y a la comprobación de soluciones reales. No incluye prácticas ni instrumentos de evaluación, que se tratarán por separado.

En el bloque de programación se trabaja con **Python desde la primera sesión**, en **Jupyter Notebook** a través de **Google Colab**, y con **Thonny** como segundo entorno local para la ejecución de archivos `.py` y la depuración paso a paso. La **placa controladora** entra en escena en el Tema 14, con **MicroPython**, en cuanto el alumnado dispone de condicionales, bucles y funciones; a partir de ahí acompaña al resto del curso y es el soporte de los bloques F y G.

Los apartados de **conocimientos previos**, **temporalización orientativa**, **proyectos integradores** y **herramientas y entornos** cierran el documento: concretan qué se supone al empezar, cuántas sesiones recibe cada tema, qué proyectos atraviesan los bloques y con qué software se trabaja.

## Conocimientos previos

Tecnología e Ingeniería I es materia de modalidad de primer curso y **no exige haber cursado Tecnología en 4.º de la ESO**, que es optativa. El grupo llega, por tanto, con bases muy desiguales, y el Anexo III del Decreto 64/2022 la convierte además en requisito para cursar Tecnología e Ingeniería II. Conviene comprobar al empezar, con una evaluación inicial breve, los siguientes puntos:

| Procedencia | Qué conviene comprobar |
| --- | --- |
| Matemáticas | Sistema Internacional y cambio de unidades; notación científica; proporcionalidad y porcentajes; despeje de una ecuación de primer grado; trigonometría elemental. |
| Física y Química | Fuerza, trabajo, potencia y energía; formas de energía y sus transformaciones; nociones de calor y temperatura. |
| Tecnología de la ESO | Circuito eléctrico elemental: tensión, intensidad y resistencia, ley de Ohm, serie y paralelo; máquinas simples y mecanismos de transmisión; lectura de un croquis y noción de escala. |
| Digitalización | Procesador de textos y hoja de cálculo a nivel básico; búsqueda de información; uso de una carpeta compartida. |
| Lógica de programación | Secuencia, selección e iteración, aunque se hayan trabajado solo con bloques. |

Dos precisiones importantes:

- **No se supone ningún conocimiento de Python.** El Tema 12 arranca de cero y no da por sabida ninguna sintaxis. Tampoco se supone haber cursado Ciencias de la Computación I, con la que esta materia comparte lenguaje y entorno pero no objeto.
- **Hay contenidos que el alumnado recibirá en paralelo, no antes.** La trigonometría, la dinámica y el tratamiento de la energía se cursan simultáneamente en Matemáticas I y en Física y Química. El bloque C conviene situarlo, por eso, después del primer trimestre, y cualquier cálculo que dependa de una herramienta matemática aún no vista debe introducirse aquí desde cero o posponerse.
- **Nada de lo anterior es un requisito de acceso.** La materia no lo exige y la tabla no es un filtro: es un diagnóstico. Lo que la evaluación inicial revele que falta —y en un grupo que no cursó Tecnología en la ESO faltará el circuito eléctrico y la lógica de programación— se recupera dentro de los temas 10 y 12, que están redactados para poder arrancar de cero.

## Bloque A — Proyectos de investigación y desarrollo

Desde la investigación y la ideación hasta la gestión del proyecto, el ciclo de vida del producto, la expresión gráfica con CAD y la documentación y comunicación de los resultados.

### Tema 1. El proyecto tecnológico: investigación, ideación y gestión

Cómo se plantea un proyecto de investigación y desarrollo, cómo se generan ideas con método y cómo se organiza el trabajo de un equipo.

- proyectos de investigación y desarrollo (I+D+i): objeto, fases y resultados esperados.
- técnicas de investigación: búsqueda, selección, referenciación e interpretación de la información.
- técnicas de ideación y pensamiento de diseño (*Design Thinking*); divergencia y convergencia.
- planificación y organización: identificación de tareas, secuenciación y diagramas de Gantt.
- metodologías ágiles (*Agile*): iteraciones, solución mínima viable, priorización y seguimiento.
- técnicas de trabajo en equipo: roles asignados, escucha del razonamiento ajeno y reparto de tareas.
- relaciones saludables e inclusivas y bienestar del grupo como condición de trabajo.
- ruptura de estereotipos e ideas preconcebidas sobre las materias tecnológicas; vocaciones técnicas y brecha de género.
- emprendimiento, perseverancia y creatividad ante problemas de perspectiva interdisciplinar.
- autoconfianza e iniciativa; el error y la reevaluación como parte del proceso de aprendizaje.

### Tema 2. El producto: ciclo de vida, calidad, normalización y comercialización

Cómo nace, se fabrica, se distribuye y se retira un producto, y con qué criterios se mide que está bien hecho.

- el producto como respuesta a una necesidad; planificación y desarrollo del diseño.
- ciclo de vida del producto: introducción, crecimiento, madurez y declive.
- estrategias de mejora continua: ciclo de Deming (planificar, hacer, verificar, actuar) y planes de mejora.
- metrología: magnitudes, instrumentos de medida, incertidumbre y tolerancias.
- normalización: papel de las normas técnicas y de los organismos de normalización.
- control de calidad del producto en las distintas etapas, del diseño a la comercialización.
- logística, transporte y distribución; almacenamiento y trazabilidad.
- comercialización: coste, precio, mercado y responsabilidad social del producto.

### Tema 3. Expresión gráfica del proyecto: croquis, esquemas y CAD, CAE y CAM

Cómo se representa una solución técnica para que otra persona pueda entenderla, calcularla y fabricarla.

- expresión gráfica aplicada a la planificación y al desarrollo de proyectos.
- croquis y bocetos a mano alzada; proporción, vistas y acotación.
- esquemas normalizados: mecánicos, eléctricos, electrónicos, neumáticos y de control.
- diagramas funcionales: representación del funcionamiento de un sistema por bloques.
- aplicaciones CAD (*Computer Aided Design*): diseño de la geometría y modelado en tres dimensiones.
- aplicaciones CAE (*Computer Aided Engineering*): análisis y simulación del funcionamiento.
- aplicaciones CAM (*Computer Aided Manufacturing*): definición y control de los procesos de fabricación.
- utilidad de la cadena CAD-CAE-CAM en el diseño, el dimensionado y la fabricación de un producto industrial.

### Tema 4. Herramientas digitales, documentación técnica y comunicación del proyecto

Qué herramientas digitales sostienen un proyecto técnico y cómo se documenta y se presenta el resultado con rigor.

- herramientas digitales de búsqueda, gestión y organización de la información.
- valoración de la procedencia de la información, contraste de veracidad y análisis crítico.
- configuración de las herramientas según la tarea y trabajo autónomo con ellas.
- entornos de trabajo colaborativo, almacenamiento compartido y control de versiones de los documentos.
- documentación técnica del proyecto: memoria, planos, esquemas, lista de materiales y presupuesto.
- precisión, rigor y terminología adecuada en la redacción técnica; referenciación de fuentes.
- presentación de proyectos con herramientas digitales: guion, soporte visual y tiempo.
- comunicación eficaz y organizada de ideas y soluciones tecnológicas; respuesta a preguntas técnicas.

## Bloque B — Materiales y fabricación

Propiedades y clasificación de los materiales técnicos, nuevos materiales y tratamientos, criterios de sostenibilidad y técnicas de fabricación, con las normas de seguridad del taller.

### Tema 5. Propiedades, clasificación y selección de los materiales técnicos

Qué distingue a un material de otro y con qué criterios técnicos y de sostenibilidad se elige el adecuado para un producto.

- propiedades físicas de los materiales: densidad, conductividad eléctrica y térmica, dilatación y punto de fusión.
- propiedades químicas: oxidación, corrosión y estabilidad frente al medio.
- propiedades mecánicas: dureza, resistencia, elasticidad, plasticidad, tenacidad, fragilidad y fatiga.
- ensayos de materiales y lectura de las curvas y valores característicos.
- materiales técnicos: metálicos, cerámicos, moleculares, poliméricos e híbridos, entre otros.
- nuevos materiales: grafeno, estaneno y *shrilk*, entre otros; propiedades y aplicaciones emergentes.
- nuevos tratamientos superficiales: PVD (*Physical Vapor Deposition*) y CVD (*Chemical Vapor Deposition*), entre otros.
- criterios de sostenibilidad: consumo energético y contaminación del ciclo completo, reciclabilidad y biodegradabilidad.
- selección del material y aplicaciones características; relación entre el material y quien usa el producto.

### Tema 6. Técnicas de fabricación, prototipado y seguridad en el trabajo

Cómo se transforma el material en pieza, qué aporta la fabricación digital y cómo se trabaja sin riesgo.

- técnicas de conformación: por deformación, por moldeo, por arranque de material y por unión.
- prototipado rápido: del modelo de comprobación al prototipo funcional.
- fabricación bajo demanda y series cortas; personalización del producto.
- fabricación digital aplicada a proyectos: impresión 3D, corte láser y mecanizado por control numérico.
- de la geometría al archivo de fabricación: preparación, parámetros y comprobación del resultado.
- criterios técnicos y de sostenibilidad en la elección de la técnica de fabricación.
- normas de seguridad e higiene en el trabajo: riesgos, equipos de protección y señalización.
- orden, mantenimiento y buenas prácticas en el aula-taller o laboratorio de fabricación.

## Bloque C — Sistemas mecánicos

Máquinas y mecanismos que transmiten y transforman el movimiento, elementos de soporte y unión, y el cálculo, el diseño y el montaje de sistemas mecánicos.

### Tema 7. Máquinas y mecanismos de transmisión del movimiento

Cómo se lleva el movimiento desde donde se genera hasta donde hace falta, y qué se gana y qué se pierde en el camino.

- máquinas y sistemas mecánicos: motor, transmisión, elemento de trabajo y bastidor.
- magnitudes del movimiento: velocidad de giro, par, potencia y rendimiento, en su sentido conceptual; su cálculo se aborda en el Tema 9.
- engranajes: tipos, relación de transmisión y trenes de engranajes.
- poleas y correas; relación de transmisión y deslizamiento.
- cadenas de rodillos y ruedas dentadas; transmisión sin deslizamiento.
- la caja de cambios como conjunto de relaciones seleccionables.
- criterios de elección del mecanismo de transmisión según la aplicación.
- representación esquematizada de una cadena cinemática.

### Tema 8. Transformación del movimiento, soportes, uniones y acoplamientos

Cómo se convierte un giro en un desplazamiento y cómo se sujetan y se enlazan las piezas de una máquina.

- mecanismos de transformación: biela-manivela, piñón-cremallera, leva-seguidor, tornillo-tuerca y excéntrica.
- el cigüeñal: transformación del movimiento alternativo en rotativo y viceversa.
- soportes y guiado: cojinetes, rodamientos y ejes.
- unión de elementos mecánicos: uniones desmontables y uniones fijas.
- acoplamientos rígidos y acoplamientos flexibles; función y criterios de uso.
- la junta Cardan y la transmisión entre ejes no alineados.
- lubricación, desgaste y mantenimiento de los elementos mecánicos.
- interpretación de un plano de conjunto y de su lista de piezas.

### Tema 9. Cálculo, diseño y montaje de sistemas mecánicos

Cómo se dimensiona un mecanismo con las herramientas de las matemáticas y la física, y cómo se comprueba que funciona.

- transferencia de conocimientos de matemáticas y física al cálculo mecánico.
- cálculo de relaciones de transmisión en trenes simples y compuestos.
- par, potencia transmitida y rendimiento del conjunto.
- fuerzas, momentos y equilibrio en elementos sencillos de una máquina.
- diseño de un sistema mecánico a partir de un requisito de movimiento.
- experimentación física o simulada: simuladores de mecanismos y montaje real.
- montaje, ajuste, medida y comprobación del comportamiento previsto.
- aplicación práctica a los proyectos de la asignatura.

## Bloque D — Sistemas eléctricos y electrónicos

Circuitos y máquinas eléctricas de corriente continua y componentes y circuitos electrónicos básicos, desde su interpretación y cálculo hasta el montaje o la simulación.

### Tema 10. Circuitos y máquinas eléctricas de corriente continua

Cómo se representa, se calcula y se monta un circuito de corriente continua, y cómo funciona el motor que lo convierte en movimiento.

- magnitudes eléctricas: tensión, intensidad, resistencia, potencia y energía.
- ley de Ohm y leyes de Kirchhoff; asociación de resistencias en serie, paralelo y mixta.
- interpretación y representación esquematizada de circuitos eléctricos con simbología normalizada.
- cálculo de circuitos de corriente continua; divisor de tensión y divisor de intensidad.
- efecto Joule, caída de tensión en los conductores y dimensionado del cableado.
- montaje y experimentación física o simulada; medida con polímetro y seguridad eléctrica.
- máquinas eléctricas de corriente continua: el motor de CC, características y funcionamiento.
- curva par-velocidad; control del sentido de giro con puente en H y de la velocidad por modulación de ancho de pulso (PWM).
- fuentes de alimentación, protección frente a sobrecorrientes y diferencia entre masa, alimentación y señal.
- aplicación del accionamiento a los proyectos de los bloques E, F y G.

### Tema 11. Componentes y circuitos electrónicos

Qué hacen los componentes electrónicos dentro de un circuito y cómo se lee un esquema que los combina.

- señal eléctrica y señal electrónica; niveles de tensión y corriente de trabajo.
- componentes pasivos: resistencias fijas y variables y condensadores; la bobina, en su única aplicación habitual en corriente continua, el relé.
- componentes semiconductores: diodo, diodo LED y transistor.
- el transistor y el MOSFET como interruptor de un actuador; el relé como interruptor aislado y el diodo de protección.
- sensores analógicos y digitales; divisores de tensión, resistencias de polarización y acondicionamiento de la señal.
- conversión analógico-digital: qué lee realmente una entrada de la placa controladora.
- lectura de hojas de características y seguridad eléctrica en el aula: tensiones admitidas, cortocircuito, polaridad y baterías.
- circuitos electrónicos básicos: rectificación, temporización, señalización y control de un actuador.
- interpretación de circuitos electrónicos básicos y de sus esquemas.
- montaje en placa de pruebas o simulación; comprobación del funcionamiento esperado.

## Bloque E — Sistemas informáticos. Programación

Fundamentos de la programación textual con Python, proceso de desarrollo de un programa y conexión de los dispositivos mediante el internet de las cosas.

### Tema 12. Fundamentos de la programación textual: del problema al programa

Qué es programar con un lenguaje textual, cómo se estructura un programa y cómo se ejecuta el primero.

- programación textual: características, elementos y lenguajes de programación más habituales.
- el paradigma de la programación estructurada: secuencia, selección e iteración.
- Python como lenguaje textual interpretado, de propósito general y de sintaxis legible.
- estructura de un programa: instrucciones, comandos, sintaxis, sangrado y comentarios.
- resolución de problemas mediante programación: del enunciado al programa.
- descripción de algoritmos en lenguaje natural, sin notaciones formales de pseudocódigo.
- diagramas de flujo: símbolos y lectura de un diagrama sencillo, de forma breve.
- Python en Jupyter Notebook con Google Colab: celdas, ejecución y estado de la sesión.
- seguimiento paso a paso de la ejecución: estado inicial, evolución y predicción del estado final.

### Tema 13. Datos, variables y operaciones

Con qué datos trabaja un programa, cómo se guardan en variables y cómo se combinan para obtener resultados.

- tipos de datos: enteros, reales, cadenas de texto y booleanos.
- constantes y variables: identificadores, asignación y nombres significativos.
- conversión de tipos y errores de tipo más frecuentes.
- operaciones básicas con variables: operadores aritméticos, relacionales y lógicos; precedencia.
- expresiones y evaluación paso a paso; traza del valor de las variables.
- entrada de datos y salida por pantalla; formato de la salida.
- cálculo de magnitudes técnicas con Python: unidades, redondeo y presentación de resultados.
- comprobación de los resultados con casos de prueba conocidos.

### Tema 14. Estructuras de control, funciones y primer programa en la placa

Cómo decide y cómo repite un programa, cómo se parte en piezas con nombre propio y cómo se hace que actúe sobre el mundo físico.

- expresiones condicionales: selección simple, doble y múltiple; condiciones compuestas.
- bucles con condición de parada y bucles de recorrido; contadores y acumuladores.
- bucles infinitos, interrupción de un bucle y continuación de la iteración.
- estructuras anidadas: combinación de selección e iteración.
- funciones: definición, llamada, parámetros y valor de retorno.
- ámbito de las variables: local y global; separación entre cálculo, entrada y presentación.
- seguimiento paso a paso de una función: estado inicial, traza y predicción del estado final.
- primer programa en la placa controladora con MicroPython: salida digital, entrada digital y lectura de un sensor.

### Tema 15. Estructuras de datos y proceso de desarrollo

Cómo se guardan muchos datos en una sola variable y cómo se organiza, se comprueba y se corrige un programa que crece.

- estructuras de datos: listas, índices, recorrido, búsqueda y modificación de elementos.
- tuplas y diccionarios como estructuras complementarias para los datos de un proyecto.
- cadenas de texto como secuencias: acceso, troceado y métodos habituales.
- elección de la estructura de datos adecuada para cada problema técnico.
- series de medidas: registro de lecturas de sensores, ficheros CSV y representación gráfica.
- proceso de desarrollo: edición, compilación o interpretación, ejecución, pruebas y depuración.
- diferencia entre compilar e interpretar; módulos y bibliotecas de la biblioteca estándar.
- tipos de error y depuración paso a paso con puntos de interrupción; batería de casos de prueba.

### Tema 16. Internet de las cosas y redes de dispositivos

Cómo se conectan entre sí los objetos que fabricamos y qué protocolos hacen posible que se entiendan.

- tecnologías emergentes: el internet de las cosas (IoT) y su aplicación a proyectos.
- arquitectura de una solución IoT: dispositivo, red, plataforma y aplicación.
- la placa controladora como nodo de red: identificación, alimentación y conectividad Wi-Fi.
- protocolos de mensajería de aplicación: MQTT y HTTP; publicación y suscripción.
- formato de los datos intercambiados y envío de las lecturas de un sensor a una plataforma.
- panorama de otras tecnologías de enlace —Bluetooth, Zigbee, LoRa—, a nivel de reconocimiento: para qué sirve cada una y por qué no se usan aquí.
- seguridad y privacidad de los dispositivos conectados; consumo energético del nodo.

## Bloque F — Sistemas automáticos

Sistemas de control y su modelización, automatización programada de procesos, supervisión y telemetría, robótica e inteligencia artificial aplicada al control.

### Tema 17. Sistemas de control: conceptos, elementos y modelización

Qué es un sistema de control, de qué piezas consta y cómo se representa para poder estudiarlo.

- concepto de sistema de control; entrada, salida y perturbación.
- elementos: controlador, sensor o transductor, comparador, actuador y planta.
- sistemas de lazo abierto y sistemas de lazo cerrado; realimentación.
- respuesta del sistema: estabilidad, precisión y tiempo de respuesta.
- modelización de sistemas sencillos mediante diagramas de bloques.
- función de cada bloque y recorrido de la señal por el sistema.
- control todo-nada, control proporcional e histéresis en aplicaciones sencillas.
- ejemplos de sistemas de control en máquinas, vehículos e instalaciones.

### Tema 18. Automatización programada de procesos, supervisión y telemetría

Cómo se automatiza un proceso con una placa programable y cómo se vigila y se registra su funcionamiento a distancia.

- automatización programada de procesos: del requisito al programa de control.
- entradas y salidas digitales y analógicas; lectura de sensores y activación de actuadores.
- diseño, programación, construcción y simulación o montaje de un proceso automatizado.
- programación estructurada del control: secuencia, condiciones y temporizaciones.
- máquinas de estados: estados, transiciones y su implementación en el programa de control.
- condiciones de seguridad, enclavamientos y comportamiento del automatismo ante un fallo.
- sistemas de supervisión SCADA (*Supervisory Control And Data Acquisition*): definición, características y ventajas.
- arquitectura de un SCADA: adquisición, comunicación, base de datos y interfaz de operador.
- telemetría y monitorización: registro de variables, alarmas y representación de la evolución.
- verificación, ajuste y documentación del sistema automatizado.

### Tema 19. Robótica e inteligencia artificial aplicadas al control

Cómo se modela y se programa el movimiento de un robot y qué aportan las tecnologías emergentes al control de un sistema.

- concepto de robot; estructura, grados de libertad y espacio de trabajo.
- modelización de movimientos y acciones mecánicas del robot.
- sensores y actuadores de un robot; percepción del entorno y respuesta.
- algoritmos sencillos de movimiento: desplazamiento, giro, seguimiento y evitación de obstáculos.
- programación y evaluación de los movimientos con herramientas informáticas y simuladores.
- aplicación de las tecnologías emergentes a los sistemas de control.
- inteligencia artificial aplicada al control: reconocimiento de patrones y decisión a partir de datos.
- uso responsable de los datos, límites de los sistemas automáticos y aplicación práctica a proyectos.

## Bloque G — Tecnología sostenible

Obtención y distribución de la energía, sistemas y mercados energéticos, instalaciones de la vivienda y criterios de eficiencia, certificación y sostenibilidad.

### Tema 20. Fuentes de energía, sistemas y mercados energéticos

De dónde sale la electricidad que llega al enchufe, cómo se transporta y cómo se fija lo que cuesta.

- obtención, transformación y distribución de las principales fuentes de energía.
- centrales de generación de energía eléctrica: térmicas, nucleares, hidráulicas, eólicas y solares.
- rendimiento de la conversión energética y cálculo de magnitudes en la generación.
- transporte y distribución: red de alta, media y baja tensión; pérdidas y transformadores.
- sistemas y mercados energéticos: agentes que intervienen y formación del precio.
- consumo energético sostenible: cálculo de costos, técnicas y criterios de ahorro.
- evaluación comparada de los sistemas de generación por eficiencia, coste e impacto.
- dependencia energética, seguridad de suministro y Objetivos de Desarrollo Sostenible.

### Tema 21. Instalaciones de la vivienda: electricidad y agua

Cómo llegan la electricidad y el agua a una vivienda, cómo se protegen esas instalaciones y cómo se reduce su consumo.

- suministros domésticos: acometida, contador y punto de entrega.
- instalación eléctrica interior: cuadro de distribución y circuitos independientes.
- elementos de protección: interruptor general, magnetotérmicos, diferencial y toma de tierra.
- esquemas de circuitos básicos de fuerza y de iluminación.
- control de potencia, consumo eléctrico y lectura e interpretación de la factura eléctrica.
- instalación de abastecimiento de agua: esquemas de distribución y tipos de válvulas.
- ahorro en el consumo de agua: aireadores, grifos inteligentes y recirculadores de agua caliente.
- reutilización de aguas grises y pluviales; saneamiento y evacuación.

### Tema 22. Climatización, aislamiento y arquitectura sostenible

Cómo se acondiciona una vivienda y por qué la mejor instalación de climatización es la que casi no hace falta.

- instalaciones de climatización: calefacción, refrigeración y ventilación.
- transmisión del calor en la vivienda: conducción, convección y radiación.
- aislamiento térmico, puentes térmicos y estanqueidad al aire.
- balance energético sencillo de una vivienda: pérdidas, ganancias y demanda.
- uso eficiente de los sistemas de climatización y regulación de la temperatura.
- arquitectura sostenible: bioconstrucción y ecoarquitectura.
- orientación, protección solar, inercia térmica y ventilación natural.
- rehabilitación energética de un edificio existente: medidas y prioridades.

### Tema 23. Domótica, energías renovables y certificación energética

Cómo se automatiza el ahorro en una vivienda, cómo se produce energía en ella y cómo se acredita que es eficiente.

- instalaciones de comunicación y domóticas: sensores, actuadores, red y escenas.
- sistemas domóticos para la contribución al ahorro energético.
- energías renovables en la vivienda: solar fotovoltaica, solar térmica, biomasa y geotérmica.
- autoconsumo: dimensionado elemental de una instalación fotovoltaica y excedentes.
- periodo de retorno de una medida de ahorro: inversión, ahorro anual y amortización.
- eficiencia energética y certificación energética de edificios y de aparatos.
- lectura e interpretación de una etiqueta energética real.
- análisis de la sostenibilidad de una vivienda y propuesta razonada de mejoras.

## Competencias específicas de la materia

El currículo de Tecnología e Ingeniería I define seis competencias específicas. El programa las desarrolla de forma integrada en los siete bloques. Entre corchetes se recogen los descriptores operativos del perfil de salida con los que el propio Decreto 64/2022 conecta cada una:

- **Competencia 1.** Coordinar y desarrollar proyectos de investigación con actitud crítica y emprendedora, implementando estrategias y técnicas eficientes de resolución de problemas y comunicando los resultados. Bloque A, con aplicación en todos los demás. [CCL1, STEM3, STEM4, CD1, CD3, CD5, CPSAA1.1, CE3]
- **Competencia 2.** Seleccionar materiales y elaborar estudios de impacto, aplicando criterios técnicos para fabricar productos de calidad desde un enfoque responsable y ético. Bloques A y B. [STEM2, STEM5, CD1, CD2, CPSAA1.1, CPSAA4, CC4, CE1]
- **Competencia 3.** Utilizar las herramientas digitales adecuadas, configurándolas según las necesidades, para resolver tareas y presentar los resultados de manera óptima. Bloque A, temas 3 y 4, con apoyo de los simuladores y entornos de los bloques C a G. [STEM1, STEM4, CD1, CD2, CD3, CD5, CPSAA5, CE3]
- **Competencia 4.** Generar conocimientos y mejorar destrezas técnicas transfiriendo conocimientos de otras disciplinas científicas para calcular y resolver problemas de los distintos ámbitos de la ingeniería. Bloques C y D. [STEM1, STEM2, STEM3, STEM4, CD2, CD5, CPSAA5, CE3]
- **Competencia 5.** Diseñar, crear y evaluar sistemas tecnológicos aplicando programación, regulación automática y control, así como las tecnologías emergentes. Bloques E y F. [STEM1, STEM2, STEM3, CD2, CD3, CD5, CPSAA1.1, CE3]
- **Competencia 6.** Analizar y comprender sistemas tecnológicos estudiando sus características, consumo y eficiencia energética, para evaluar el uso responsable y sostenible de la tecnología. Bloque G. [STEM2, STEM5, CD1, CD2, CD4, CPSAA2, CC4, CE1]

## Cobertura curricular

Los siete bloques del programa reproducen los siete bloques de contenidos que el Decreto 64/2022 enumera para Tecnología e Ingeniería I y conservan todos sus núcleos expresos, en su mismo orden.

**Bloque A (temas 1–4).** Los cuatro temas cubren las estrategias de gestión y desarrollo de proyectos con metodologías Agile, la identificación y secuenciación de tareas, los diagramas de Gantt y el seguimiento, las técnicas de investigación e ideación y las de trabajo en equipo, el ciclo de vida del producto, la planificación y el desarrollo del diseño y la comercialización, la metrología, la normalización y el control de calidad, la logística, el transporte y la distribución, las estrategias de mejora continua con el ciclo de Deming, la expresión gráfica con diagramas funcionales, esquemas y croquis, las aplicaciones CAD, CAE y CAM, el emprendimiento, la perseverancia y la creatividad, la autoconfianza y la iniciativa y el error y la reevaluación como parte del aprendizaje. El Tema 4 recoge además la competencia 3 —uso y configuración de herramientas digitales y presentación de proyectos—, que el currículo formula como competencia pero cuyo contenido se apoya en este bloque.

**Bloque B (temas 5–6).** Los dos temas cubren las propiedades físicas, químicas y mecánicas de los materiales, los materiales técnicos metálicos, cerámicos, moleculares, poliméricos e híbridos, los nuevos materiales —grafeno, estaneno y *shrilk*— y los nuevos tratamientos PVD y CVD, la clasificación y los criterios de sostenibilidad, la selección y las aplicaciones características, las técnicas de fabricación con prototipado rápido y bajo demanda, la fabricación digital aplicada a proyectos y las normas de seguridad e higiene en el trabajo.

**Bloque C (temas 7–9).** Los tres temas cubren las máquinas y los sistemas mecánicos, los mecanismos de transmisión —engranajes, poleas y correas, cadenas de rodillos, cigüeñal y caja de cambios—, los mecanismos de transformación de movimientos, los soportes y la unión de elementos mecánicos, los acoplamientos rígidos y flexibles, la junta Cardan, y el diseño, el cálculo, el montaje y la experimentación física o simulada, con aplicación práctica a proyectos.

**Bloque D (temas 10–11).** Los dos temas cubren los circuitos y las máquinas eléctricas de corriente continua, la interpretación y la representación esquematizada de circuitos eléctricos, su cálculo, montaje y experimentación física o simulada, los motores eléctricos de corriente continua con sus características y funcionamiento, los componentes y circuitos electrónicos y la interpretación de circuitos básicos, con aplicación a proyectos.

**Bloque E (temas 12–16).** Los cinco temas cubren los fundamentos de la programación textual con sus características, elementos y lenguajes, los tipos de datos, las constantes y las variables, la estructura de un programa con sus instrucciones, comandos y sintaxis, las operaciones básicas con variables, los bucles, las expresiones condicionales y las estructuras de datos, el proceso de desarrollo completo —edición, compilación o interpretación, ejecución, pruebas y depuración—, la creación de programas para la resolución de problemas, la modularización, el internet de las cosas aplicado a proyectos y los protocolos de comunicación de redes de dispositivos. La modularización se adelanta al Tema 14, junto a las estructuras de control, para que ningún programa del bloque tenga que escribirse de una sola pieza y para que el criterio 5.3 —seguir la ejecución paso a paso y predecir el estado final— pueda trabajarse sobre funciones pequeñas.

**Bloque F (temas 17–19).** Los tres temas cubren los sistemas de control con sus conceptos y elementos y la modelización de sistemas sencillos, la automatización programada de procesos con su diseño, programación, construcción y simulación o montaje, los sistemas de supervisión SCADA con su definición, características y ventajas, la telemetría y la monitorización, la aplicación de las tecnologías emergentes a los sistemas de control, la robótica con la modelización de movimientos y acciones mecánicas y su aplicación práctica a proyectos, y la inteligencia artificial aplicada a los sistemas de control.

**Bloque G (temas 20–23).** Los cuatro temas cubren la obtención, la transformación y la distribución de las principales fuentes de energía, los sistemas y mercados energéticos, el consumo energético sostenible con el cálculo de costes —«costos» en el texto oficial— y las técnicas y criterios de ahorro, los suministros domésticos, las instalaciones eléctricas de la vivienda con sus elementos de protección, el cuadro de distribución, los esquemas de circuitos básicos de fuerza e iluminación, el control de potencia, el consumo eléctrico y la factura eléctrica, las instalaciones de abastecimiento de agua con sus esquemas de distribución, tipos de válvulas y medidas de ahorro —aireadores, grifos inteligentes, recirculadores y reutilización de aguas grises y pluviales—, las instalaciones de climatización, el aislamiento térmico, la arquitectura sostenible con la bioconstrucción y la ecoarquitectura, el uso eficiente de los sistemas de climatización, las instalaciones de comunicación y domóticas con su contribución al ahorro energético, y las energías renovables, la eficiencia energética, la certificación energética y la sostenibilidad. El último tema se desdobla en dos —climatización y arquitectura sostenible, por un lado; domótica, renovables y certificación, por otro— porque reunía en una sola unidad seis núcleos de contenido independientes.

### Contenidos de ampliación

Los siguientes contenidos no figuran literalmente en el texto oficial y se incorporan de forma deliberada porque sostienen otros saberes del propio curso o los hacen enseñables. Se señalan aquí para que puedan distinguirse en cualquier momento de los contenidos prescritos:

- ensayos de materiales y lectura de sus valores característicos (Tema 5).
- técnicas de conformación por deformación, moldeo, arranque de material y unión (Tema 6).
- magnitudes del movimiento —velocidad de giro, par, potencia y rendimiento— y cálculo de relaciones de transmisión (temas 7 y 9).
- cojinetes, rodamientos, lubricación y mantenimiento de los elementos mecánicos (Tema 8).
- leyes de Kirchhoff, efecto Joule y dimensionado del cableado (Tema 10).
- puente en H, modulación de ancho de pulso (PWM) y protección frente a sobrecorrientes (Tema 10).
- el MOSFET y el relé como interruptores de un actuador, el diodo de protección y la conversión analógico-digital (Tema 11).
- acondicionamiento de señal con divisores de tensión y resistencias de polarización (Tema 11).
- tuplas y diccionarios como estructuras complementarias a las listas (Tema 15).
- registro de series de medidas en ficheros CSV y su representación gráfica (Tema 15).
- arquitectura de una solución IoT y protocolos MQTT y HTTP (Tema 16).
- control todo-nada, control proporcional e histéresis (Tema 17).
- máquinas de estados y condiciones de seguridad e interbloqueo en un automatismo (Tema 18).
- rendimiento de la conversión energética y pérdidas en el transporte (Tema 20).
- toma de tierra, saneamiento y evacuación de aguas (Tema 21).
- balance energético de una vivienda y rehabilitación energética (Tema 22).
- autoconsumo fotovoltaico y periodo de retorno de una medida de ahorro (Tema 23).

Todo lo demás procede de los contenidos enumerados en el Decreto 64/2022: el ciclo de Deming, la metrología, la normalización, la logística, las aplicaciones CAD, CAE y CAM, el grafeno, el estaneno, el *shrilk*, los tratamientos PVD y CVD, la caja de cambios, la junta Cardan, los acoplamientos rígidos y flexibles, el SCADA, la telemetría, la inteligencia artificial aplicada al control, los aireadores, los grifos inteligentes, los recirculadores de agua caliente, las aguas grises y pluviales, la bioconstrucción, la ecoarquitectura y la certificación energética aparecen en el texto oficial y no son añadidos de este programa.

## Alineación con los criterios de evaluación

Los dieciocho criterios de evaluación de la materia para 1.º de Bachillerato se trabajan en los temas indicados:

- Bloque A (temas 1–4): criterios 1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 3.1, 3.2 y 3.3.
- Bloque B (temas 5–6): criterios 2.2 y 2.3.
- Bloque C (temas 7–9): criterio 4.1, con apoyo de 3.3.
- Bloque D (temas 10–11): criterio 4.2.
- Bloque E (temas 12–16): criterios 5.1 y 5.3, con apoyo de 3.1.
- Bloque F (temas 17–19): criterios 5.1 y 5.2.
- Bloque G (temas 20–23): criterios 6.1 y 6.2.

## Temporalización orientativa

La materia tiene **cuatro periodos lectivos semanales**. Con 33 semanas efectivas resultan unas **132 sesiones**, cifra coherente con la de las programaciones de departamento de la Comunidad de Madrid, que cuentan entre 125 y 135 sesiones para esta materia.<sup>1</sup> El reparto siguiente asigna 109 sesiones a los temas y reserva las 23 restantes para la evaluación inicial, las pruebas, la entrega y defensa de los proyectos y un margen de imprevistos que cualquier curso real consume:

| Bloque | Tema | Sesiones | Bloque | Tema | Sesiones |
| --- | --- | --- | --- | --- | --- |
| A | 1. El proyecto tecnológico | 6 | E | 12. Fundamentos de la programación textual | 6 |
| A | 2. El producto | 5 | E | 13. Datos, variables y operaciones | 5 |
| A | 3. Expresión gráfica y CAD-CAE-CAM | 5 | E | 14. Control, funciones y placa | 5 |
| A | 4. Herramientas, documentación y comunicación | 4 | E | 15. Estructuras de datos y desarrollo | 5 |
| B | 5. Propiedades y selección de materiales | 5 | E | 16. Internet de las cosas | 3 |
| B | 6. Fabricación, prototipado y seguridad | 3 | F | 17. Sistemas de control | 4 |
| C | 7. Transmisión del movimiento | 5 | F | 18. Automatización, SCADA y telemetría | 6 |
| C | 8. Transformación, soportes y uniones | 4 | F | 19. Robótica e inteligencia artificial | 6 |
| C | 9. Cálculo, diseño y montaje | 5 | G | 20. Fuentes de energía y mercados | 4 |
| D | 10. Circuitos y máquinas de CC | 7 | G | 21. Instalaciones: electricidad y agua | 4 |
| D | 11. Componentes y circuitos electrónicos | 6 | G | 22. Climatización y arquitectura sostenible | 3 |
| | | | G | 23. Domótica, renovables y certificación | 3 |

Reparto por evaluaciones, de 44 sesiones cada una:

| Evaluación | Contenido | Sesiones |
| --- | --- | --- |
| **1.ª** | Evaluación inicial (2) · Bloque A, temas 1–4 (20) · **Tema 20**, fuentes de energía y mercados (4) · Bloque B, temas 5–6 (8) · prueba (2) · entrega y defensa del Proyecto 1 (3) · reserva (5) | 44 |
| **2.ª** | Bloque C, temas 7–9 (14) · Bloque D, temas 10–11 (13) · **Tema 21**, instalaciones de la vivienda (4) · Bloque E, temas 12–13 (11) · prueba (2) | 44 |
| **3.ª** | Bloque E, temas 14–16 (13) · Bloque F, temas 17–19 (16) · Bloque G, temas 22–23 (6) · entrega y defensa del Proyecto 2 (3) · prueba (2) · reserva (4) | 44 |

Dos decisiones de calendario merecen explicación, porque **el orden de los bloques en este documento reproduce el del currículo oficial y no obliga a impartirlos en ese orden**:

- **El Bloque G se reparte entre las tres evaluaciones.** Los temas 20 y 21 se adelantan a la primera y a la segunda porque no dependen de nada previo, conectan con lo que el alumnado trae de la ESO y son los que en la práctica se quedan sin impartir cuando el bloque energético se deja entero para junio. Solo los temas 22 y 23 permanecen al final.
- **El Bloque E se parte entre la segunda y la tercera evaluación.** No es lo ideal para una progresión acumulativa, pero es preferible a la alternativa: concentrar los 24 periodos de programación y los 16 de automatización en un mismo trimestre, que es el más corto del curso. Los temas 12 y 13 —sintaxis, datos y operaciones— toleran mejor el corte que los temas 14 a 16.

## Proyectos integradores

El currículo exige que los contenidos «se interrelacionen a través del desarrollo de actividades o proyectos de carácter práctico». Para que eso no quede en una declaración, el curso se articula en torno a **un solo proyecto desarrollado en dos fases**, el **KR-1**: un kit de riego automatizado y monitorizado para el huerto del centro y, por extensión, para huertos urbanos. La elección no es arbitraria: es el ejemplo de situación de aprendizaje que el propio Decreto 64/2022 propone para esta materia, al ilustrar la competencia 5.1 con «un sistema de control automático para el riego de unas plantas mediante una placa controladora programable, capaz de regular la humedad de la tierra y monitorizar su estado en tiempo real».

**Proyecto 1 — El KR-1 como producto** (1.ª evaluación; bloques A y B)

| Fase | Bloque y tema | Entregable |
| --- | --- | --- |
| Necesidad, investigación e ideación | A · 1 | Informe de necesidad, dosier de fuentes y matriz de decisión |
| Requisitos, calidad y coste | A · 2 | Especificación priorizada, cotas con tolerancia y presupuesto |
| Planos y modelo 3D | A · 3 | Planos acotados, modelo paramétrico y diagrama funcional |
| Documentación y defensa | A · 4 | Memoria, manual y presentación de diez minutos |
| Material y fabricación | B · 5 y 6 | Caja y soporte fabricados, con material justificado |

**Proyecto 2 — El KR-1 como sistema** (2.ª y 3.ª evaluación; bloques C a G)

| Fase | Bloque y tema | Entregable |
| --- | --- | --- |
| Accionamiento mecánico | C · 7 a 9 | Cálculo del mecanismo de apertura y su montaje |
| Circuito de control | D · 10 y 11 | Esquema, montaje y medidas con polímetro |
| Programa de control | E · 12 a 15 | Programa en Python y MicroPython, con su batería de pruebas |
| Conexión y datos | E · 16 · F · 18 | Publicación de lecturas y panel de monitorización |
| Lazo cerrado y robustez | F · 17 a 19 | Diagrama de bloques, ensayos de fallo y registro de incidencias |
| Balance de agua y energía | G · 20 a 23 | Consumo medido, ahorro estimado y periodo de retorno |

Cada tema del programa aporta al proyecto una pieza concreta, y el proyecto devuelve a cada tema un motivo para estudiarlo. Los temas cuyo contenido no cabe en el KR-1 —la caja de cambios, la junta Cardan, los mercados energéticos, el SCADA industrial— se trabajan como análisis de sistemas existentes, no como partes del prototipo.

## Herramientas y entornos

El currículo no impone ningún software, y la competencia 3 pide precisamente saber elegirlo y configurarlo. Los criterios de esta materia son tres: **que sea gratuito o de licencia educativa**, **que funcione en los equipos del centro y en casa** y **que no obligue a aprender dos sintaxis distintas para lo mismo**. Con ellos, la propuesta es:

| Función | Herramienta | Bloques |
| --- | --- | --- |
| CAD paramétrico y planos | FreeCAD; alternativas: Onshape o Fusion con licencia educativa | A, B |
| CAM y fabricación digital | Laminador de la impresora 3D del centro; software de la cortadora | B |
| Simulación de mecanismos | Algodoo o GeoGebra | C |
| Simulación de circuitos | Tinkercad Circuits o el simulador de Falstad | D, F |
| Programación general | Python en Jupyter Notebook a través de Google Colab | E |
| Ejecución local y depuración paso a paso | Thonny | E |
| Placa controladora | ESP32 con MicroPython; alternativas: Raspberry Pi Pico W o micro:bit | E, F, G |
| Simulación de la placa | Wokwi, cuando no hay hardware para todos los equipos | E, F |
| Telemetría y panel de supervisión | Cliente y *broker* MQTT con un panel web sencillo | F |
| Documentación y gestión | Procesador de textos, hoja de cálculo, tablero de tareas y carpeta compartida con historial de versiones | A, y todo el curso |

Sobre la placa: se propone **ESP32** porque integra Wi-Fi, lo que hace viable el Tema 16 sin módulos añadidos, y porque admite MicroPython, de modo que el lenguaje del curso es uno solo de principio a fin. Los temas 14, 16, 18 y 19 están redactados para poder impartirse igualmente con Raspberry Pi Pico W o con micro:bit, y la decisión concreta corresponde al departamento según el material disponible.

## Continuidad con Tecnología e Ingeniería II

El programa se diseña para enlazar con el de 2.º de Bachillerato:

- El Bloque A deja asentadas la gestión de proyectos, la documentación técnica y la expresión gráfica, que en 2.º se reorientan hacia proyectos de investigación e innovación, pliegos de condiciones y presupuestos.
- El Bloque B se queda en las propiedades y la selección de materiales; la estructura interna, los procedimientos de ensayo y medida, los tratamientos de modificación y las técnicas de fabricación industrial son contenido de 2.º.
- El Bloque C prepara el cálculo de estructuras, las máquinas térmicas y la neumática y la hidráulica que 2.º incorpora a su bloque de sistemas mecánicos.
- El Bloque D queda acotado a la corriente continua: la corriente alterna y la electrónica digital combinacional y secuencial corresponden a 2.º.
- El Bloque E asienta la programación textual estructurada en Python y la conexión de dispositivos; en 2.º el bloque informático cambia de objeto y pasa a la inteligencia artificial, el *big data* y la ciberseguridad, para los que este curso deja preparados el internet de las cosas y el tratamiento de datos.
- El Bloque F introduce el control en el nivel de los diagramas de bloques y la programación de la placa; el álgebra de bloques, la simplificación de sistemas y el estudio de la estabilidad se abordan en 2.º.
- El Bloque G trabaja la energía y las instalaciones; los informes de evaluación de impacto ambiental y la valoración crítica de las tecnologías desde la sostenibilidad se desarrollan en 2.º.

## Fuentes curriculares mantenidas

- [Decreto 64/2022, de 20 de julio, del Consejo de Gobierno, por el que se establecen para la Comunidad de Madrid la ordenación y el currículo del Bachillerato](https://www.bocm.es/boletin/CM_Orden_BOCM/2022/07/26/BOCM-20220726-1.PDF) (BOCM de 26 de julio de 2022). Currículo de Tecnología e Ingeniería: introducción, competencias específicas 1 a 6, criterios de evaluación de Tecnología e Ingeniería I y contenidos A a G (páginas 379 a 385 del boletín).
- [Real Decreto 243/2022, de 5 de abril, por el que se establecen la ordenación y las enseñanzas mínimas del Bachillerato](https://www.boe.es/buscar/act.php?id=BOE-A-2022-5521). Marco estatal, perfil de salida y descriptores operativos de las competencias clave.
- [Picuino: transcripción navegable del currículo de Tecnología e Ingeniería](https://www.picuino.com/es/ley-tecnologia-ingenieria.html). Recurso de consulta que presenta enfrentados el currículo de Madrid y el estatal.
- <sup>1</sup> [IES El Carrascal (Arganda del Rey) — Programación didáctica de Tecnología e Ingeniería I, curso 2025-2026](https://site.educa.madrid.org/ies.elcarrascal.arganda//wp-content/uploads/ies.elcarrascal.arganda/2025/11/PROGRAMACION-TECNOLOGIA-E-INGENIERIA-1o-BACH-25-26.pdf) (PDF). Consultada para contrastar la carga horaria real: cuatro horas semanales y 130 sesiones repartidas en seis unidades didácticas.
