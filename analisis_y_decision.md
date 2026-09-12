# Análisis y decisiones pedagógicas

Documento que justifica la estructura del programa de Tecnología e Ingeniería I: por qué se han elegido veintitrés temas, cómo se reparten entre los siete bloques de contenidos del currículo de la Comunidad de Madrid y qué criterios metodológicos rigen los bloques de programación, control y robótica. El apartado final recoge la revisión externa a la que se sometió el programa y qué se cambió a partir de ella.

## Criterios editoriales

- Solo se incluye teoría: no hay prácticas, cuestionarios ni ponderaciones. Las prácticas y las pruebas de evaluación se desarrollarán por separado.
- La temporalización, los proyectos integradores y las herramientas sí forman parte del programa: no son instrumentos de evaluación, sino las condiciones sin las que el temario no se puede juzgar viable.
- Las páginas son autónomas, adaptables a móvil, imprimibles y navegables con teclado.
- Cada tema incluye pregunta guía, objetivos, conceptos desarrollados, ejemplos, glosario o resumen.
- No se incluyen marcadores de imágenes inexistentes: no se publican materiales incompletos.
- Se incluyen enlaces a fuentes curriculares y técnicas.
- La estructura de bloques reproduce literalmente la del currículo oficial; la agrupación en temas es la decisión propia de esta asignatura.

## Una advertencia sobre el texto oficial

El currículo de Madrid contiene dos incoherencias internas que conviene tener localizadas, porque explican por qué circulan resúmenes distintos de esta materia:

- La introducción afirma que «la materia se articula en torno a **seis** bloques de contenidos» y a continuación describe seis: proyectos de investigación y desarrollo, materiales y fabricación, sistemas mecánicos, sistemas eléctricos y electrónicos, automatización y tecnología sostenible. Pero el apartado «Contenidos» enumera **siete** bloques, de la A a la G, porque añade «Sistemas informáticos. Programación» entre los sistemas eléctricos y los sistemas automáticos. El listado prescriptivo es el de «Contenidos», y es el que sigue este programa.
- El ejemplo de situación de aprendizaje que precede a las competencias específicas cita «el bloque **E. Automatización**», mientras que en el listado de contenidos el bloque E es «Sistemas informáticos. Programación» y la automatización es el bloque F. Se trata de un residuo de una versión anterior del texto.

Los resúmenes de esta materia que reducen el currículo a cinco bloques y funden los sistemas mecánicos y los eléctricos dentro de «Materiales y fabricación» proceden de esa confusión y dejan fuera dos bloques enteros con criterios de evaluación propios (4.1 y 4.2).

Además, el currículo de Madrid no es idéntico al estatal. Respecto del Real Decreto 243/2022, Madrid **añade** el criterio 3.3 (conocer programas CAD, CAE y CAM), precisa en el 5.1 que los lenguajes han de ser **textuales** y que se aplique **el paradigma de la programación estructurada**, y desarrolla los contenidos con mucho más detalle: propiedades físicas, químicas y mecánicas de los materiales, grafeno, estaneno, *shrilk*, tratamientos PVD y CVD, caja de cambios, junta Cardan, acoplamientos, motores de corriente continua, componentes y circuitos electrónicos, tipos de datos, bucles y estructuras de datos, inteligencia artificial aplicada al control, factura eléctrica, aireadores, grifos inteligentes, aguas grises y certificación energética. Madrid **omite**, en cambio, dos expresiones del texto estatal: la «resiliencia» y la «identificación y gestión de emociones». El programa sigue el texto de Madrid.

## Reparto general: veintitrés temas

El currículo de 1.º fija siete bloques con pesos muy desiguales. El reparto elegido es 4 + 2 + 3 + 2 + 5 + 3 + 4:

| Bloque | Temas | Nº | Sesiones |
| --- | --- | --- | --- |
| A. Proyectos de investigación y desarrollo | 1–4 | 4 | 20 |
| B. Materiales y fabricación | 5–6 | 2 | 8 |
| C. Sistemas mecánicos | 7–9 | 3 | 14 |
| D. Sistemas eléctricos y electrónicos | 10–11 | 2 | 13 |
| E. Sistemas informáticos. Programación | 12–16 | 5 | 24 |
| F. Sistemas automáticos | 17–19 | 3 | 16 |
| G. Tecnología sostenible | 20–23 | 4 | 14 |
| **Total** | **1–23** | **23** | **109** |

Con cuatro periodos lectivos semanales y 33 semanas efectivas, el curso tiene unas 132 sesiones. Las 109 asignadas a los temas dejan 23 —casi una sexta parte— para la evaluación inicial, las pruebas, la entrega y defensa de los proyectos y el margen de imprevistos que todo curso real consume. El programa recoge el reparto completo por tema y por evaluación; aquí interesa solo la consecuencia: **el número de temas no es el problema de viabilidad, el número de sesiones sí**, y por eso el documento declara las dos cifras.

Veintitrés temas es una granularidad más fina que las seis u ocho unidades didácticas de la mayoría de las programaciones de departamento. Es deliberado: este documento es el temario de referencia, del que después se derivan las unidades de aula agrupando temas contiguos. Un tema de cuatro o cinco sesiones es una unidad de trabajo reconocible; una unidad didáctica de treinta sesiones no dice nada sobre qué se enseña dentro.

La programación recibe el mayor número de temas porque es el único bloque cuyo aprendizaje se construye por acumulación —cada tema depende del anterior—, porque sostiene además los bloques F y G, y porque el criterio 5.3 exige que el alumnado siga paso a paso la ejecución de un programa y prediga su estado final, algo que no se consigue con una exposición breve.

## Bloque A — Decisión: cuatro temas

La secuencia responde a cuatro preguntas consecutivas:

1. **¿Cómo se pone en marcha y se organiza un proyecto?** Investigación, ideación, Agile, Gantt y equipo.
2. **¿Qué le ocurre al producto desde que se diseña hasta que se retira?** Ciclo de vida, calidad, normalización y comercialización.
3. **¿Cómo se dibuja lo que se quiere fabricar?** Croquis, esquemas, diagramas funcionales y CAD-CAE-CAM.
4. **¿Cómo se documenta y se cuenta?** Herramientas digitales, documentación técnica y comunicación.

### Por qué no tres o cinco

- **Tres temas** obligarían a meter la expresión gráfica y las aplicaciones CAD-CAE-CAM dentro del tema de gestión o dentro del de producto, cuando el criterio 3.3 les da entidad propia en Madrid.
- **Cinco temas** separarían la documentación técnica de la comunicación, que en la práctica se trabajan sobre el mismo entregable.
- **Cuatro temas** permiten que la competencia 3 —tres criterios de evaluación— tenga un lugar identificable sin convertirse en un bloque paralelo.

### Decisiones de contenido

- La competencia 3 no tiene bloque de contenidos propio: sus criterios se apoyan en «Expresión gráfica» del bloque A y en los simuladores y entornos de los bloques C a G. Por eso se ancla en los temas 3 y 4 y se recuerda después en cada bloque, en lugar de crear un bloque artificial de «herramientas digitales».
- El ciclo de vida del producto se estudia aquí (Tema 2) y no en el bloque B, porque el criterio 2.1 lo enuncia como planificación y control de calidad «desde el diseño a la comercialización», que es materia de proyecto, no de materiales.
- El emprendimiento, la autoconfianza, la iniciativa y el tratamiento del error se integran en el Tema 1 como criterios de trabajo del curso, no como un apartado final de buenas intenciones.
- **La ruptura de estereotipos sobre las materias tecnológicas tiene epígrafe propio en el Tema 1.** El Decreto 64/2022 la prescribe expresamente al comentar la competencia 1 —«debe fomentarse la ruptura de estereotipos e ideas preconcebidas sobre las materias tecnológicas asociadas a cuestiones individuales, como por ejemplo la aptitud para las materias tecnológicas»—, y la primera versión del programa solo la recogía de forma implícita, dentro de las «relaciones saludables e inclusivas». En una materia con la matrícula femenina que tiene esta, dejarla implícita equivale a no darla.
- CAE y CAM se tratan a nivel de reconocimiento —qué hacen y para qué sirven—, mientras que CAD se trabaja de forma operativa: es el único de los tres que el alumnado puede usar de verdad en el aula.

## Bloque B — Decisión: dos temas

La secuencia responde a dos preguntas consecutivas:

1. **¿Qué material elijo y por qué?** Propiedades, materiales técnicos, nuevos materiales y sostenibilidad.
2. **¿Cómo lo convierto en pieza y sin hacerme daño?** Técnicas de fabricación, prototipado, fabricación digital y seguridad.

### Por qué no uno o tres

- **Un tema** reuniría las propiedades de los materiales, los nuevos tratamientos, todas las técnicas de fabricación y la seguridad en una unidad larguísima y meramente enumerativa.
- **Tres temas** separarían las propiedades de los materiales técnicos, dejando dos unidades cortas que en el aula se explican encadenadas.
- **Dos temas** reproducen la partición del propio texto oficial: materiales, por un lado; fabricación y seguridad, por otro.

### Decisiones de contenido

- Los ensayos de materiales se incorporan aunque el texto oficial no los enumere: sin ellos, las propiedades mecánicas quedan en una lista de palabras que el alumnado no sabe de dónde salen.
- Los nuevos materiales y los tratamientos PVD y CVD se estudian tal como los nombra el currículo, con ejemplos de aplicación actual, sin entrar en la química del proceso. Son contenido prescrito —el grafeno, el estaneno y el *shrilk* aparecen literalmente en el Decreto 64/2022—, de modo que no pueden suprimirse por muy específicos que resulten para el nivel; lo que sí se acota es la profundidad: **se piden a nivel de reconocimiento y como ejemplos de investigación en curso, no como contenido que haya que dominar ni memorizar**.
- La selección de materiales se plantea como decisión comparada sobre un caso concreto —qué material para la caja del KR-1, expuesta al sol y al agua— y no como una clasificación enciclopédica que recorra todas las familias.
- La seguridad e higiene no se imparte como tema aislado al principio del curso: se explica en el Tema 6, junto a las técnicas y máquinas a las que se refiere, y se recuerda en cada montaje.
- La selección de materiales se plantea siempre como decisión razonada de un proyecto concreto, que es como la formula el criterio 2.2.

## Bloque C — Decisión: tres temas

La secuencia responde a tres preguntas consecutivas:

1. **¿Cómo llega el movimiento de un sitio a otro?** Máquinas, engranajes, poleas, cadenas y caja de cambios.
2. **¿Cómo cambia de naturaleza el movimiento y cómo se sujetan las piezas?** Transformación, soportes, uniones y acoplamientos.
3. **¿Cómo se dimensiona y se comprueba?** Cálculo, diseño, montaje y experimentación.

### Por qué no dos o cuatro

- **Dos temas** dejarían el cálculo repartido en trozos dentro de los dos anteriores, justo el contenido que el criterio 4.1 pide «resolver» y el que conecta la materia con las matemáticas y la física.
- **Cuatro temas** fragmentarían la transmisión en dos unidades sin una frontera conceptual clara.
- **Tres temas** separan transmisión, transformación y cálculo, que son tres tipos de trabajo distintos en el aula.

### Decisiones de contenido

- El cigüeñal aparece en el texto oficial dentro de los elementos de transmisión, pero se estudia en el Tema 8 con la transformación del movimiento, que es lo que realmente hace. La decisión se hace explícita para que no parezca un olvido.
- El cálculo mecánico tiene tema propio (Tema 9) porque es donde se materializa la competencia 4: transferir matemáticas y física a un problema técnico.
- **El par, la potencia y el rendimiento aparecen en el Tema 7 y en el Tema 9, con papeles distintos y declarados.** En el 7 son conceptos: qué significan y por qué un mecanismo los modifica. En el 9 son cálculo: relaciones de transmisión en trenes compuestos, par transmitido y rendimiento del conjunto. El programa lo dice explícitamente en el epígrafe del Tema 7 para que la repetición no se lea como un descuido.
- El bloque se sitúa a partir de la segunda evaluación porque su cálculo depende de herramientas —trigonometría, dinámica— que el alumnado cursa en paralelo en Matemáticas I y en Física y Química, no antes.
- La experimentación se admite «física o simulada», tal como autoriza el currículo, lo que permite avanzar sin depender del material disponible en el aula-taller.
- La resistencia de materiales y las máquinas térmicas y fluidomecánicas no se tratan: son contenido de Tecnología e Ingeniería II.

## Bloque D — Decisión: dos temas

La secuencia responde a dos preguntas consecutivas:

1. **¿Cómo se calcula y se monta un circuito de corriente continua y cómo mueve un motor?** Circuitos y máquinas eléctricas de CC.
2. **¿Qué hacen los componentes electrónicos dentro de un circuito?** Componentes y circuitos electrónicos básicos.

### Por qué no uno o tres

- **Un tema** mezclaría el cálculo eléctrico con la electrónica de semiconductores, que tienen nivel de abstracción y método de trabajo distintos.
- **Tres temas** aislarían el motor de corriente continua en una unidad muy breve, cuando el propio currículo lo enuncia junto a los circuitos —«Circuitos y máquinas eléctricas de corriente continua»— y cuando su interés aquí es alimentar los proyectos de los bloques F y G.
- **Dos temas** reproducen los dos guiones del texto oficial.

### Decisiones de contenido

- Las leyes de Kirchhoff y el efecto Joule se incorporan como ampliación: el criterio 4.2 pide «resolver problemas», y con la ley de Ohm sola no se resuelven circuitos mixtos ni se justifica el dimensionado del cableado que reaparece en el Tema 21.
- La corriente alterna no se estudia en este curso: el currículo de 1.º acota expresamente el bloque a la corriente continua y la alterna corresponde a 2.º. Solo se nombra en el Tema 20 al describir el transporte de la energía.
- La electrónica digital y las puertas lógicas no pertenecen a este curso.
- El transistor y el MOSFET se presentan sobre todo como interruptores de un actuador, porque es el papel que desempeñan en los montajes de control de los bloques E y F. Se añaden el relé, el diodo de protección, el puente en H y la modulación de ancho de pulso: son contenido de ampliación, pero sin ellos no se puede accionar un motor ni una electroválvula desde una placa, que es lo que los bloques E, F y G necesitan hacer.
- **Las bobinas se acotan a su única aplicación real en corriente continua: el relé.** Enunciarlas como componente pasivo general en un bloque que el currículo limita expresamente a la corriente continua era enseñar un componente sin sitio donde usarlo.
- **Los simuladores se nombran.** El currículo admite «experimentación física o simulada» sin concretar herramienta, y la primera versión del programa reprodujo esa indefinición en los bloques C y D mientras sí concretaba entornos en el bloque E. El programa nombra ahora Tinkercad Circuits y Falstad para circuitos y Algodoo o GeoGebra para mecanismos: no para cerrar la elección, sino para que el temario sea accionable y para no hacer depender el curso de que haya material de taller para todos los equipos.

## Bloque E — Decisión: cinco temas

La secuencia responde a cinco preguntas consecutivas:

1. **¿Qué es programar y cómo se ejecuta el primer programa?** Programación textual, estructura de un programa y Python en Jupyter Notebook.
2. **¿Con qué datos trabaja?** Tipos, constantes, variables y operaciones.
3. **¿Cómo decide, cómo repite y cómo se parte en piezas?** Condicionales, bucles, funciones y primer programa en la placa.
4. **¿Cómo guarda muchos datos y cómo se comprueba que funciona?** Estructuras de datos, series de medidas, pruebas y depuración.
5. **¿Cómo se conecta a la red?** Internet de las cosas y protocolos de comunicación.

### Por qué no tres o cuatro

- **Tres temas** obligarían a impartir condicionales, bucles, estructuras de datos y funciones en dos unidades muy densas, justo donde se produce la mayor parte del abandono en un primer curso de programación.
- **Cuatro temas** exigirían disolver el internet de las cosas dentro del tema de desarrollo o llevarlo al bloque F, contra la letra del currículo, que lo sitúa en el bloque E.
- **Cinco temas** permiten una progresión de dificultad regular y dejan la conectividad como puente natural hacia los sistemas automáticos.

### Por qué las funciones van en el Tema 14 y no en el 15

La primera versión del programa situaba la modularización en el último tema del bloque, después de las listas, las tuplas y los diccionarios. Era un error de secuencia: obligaba a escribir todos los programas de los temas 13 y 14 de una sola pieza y dejaba la descomposición en funciones como un añadido final, cuando es la herramienta que hace manejable todo lo anterior. Además, el criterio 5.3 —seguir la ejecución paso a paso y predecir el estado final— se trabaja mucho mejor trazando una función de seis líneas que un programa de sesenta. Las funciones se adelantan, por tanto, al Tema 14, junto a los condicionales y los bucles, y el Tema 15 queda para las colecciones y el proceso de desarrollo completo.

### Por qué la placa aparece en el Tema 14

La cabecera del programa prometía MicroPython sobre placa controladora y la secuencia no la usaba hasta el Tema 16. La contradicción se resuelve adelantando el hardware: en cuanto hay condicionales, bucles y funciones, ya se puede encender una salida, leer un pulsador y leer un sensor. Es el momento de máxima rentabilidad motivacional del bloque —el programa deja de imprimir texto y empieza a mover cosas— y permite que los temas 15 y 16 trabajen con datos reales medidos por el alumnado en lugar de con listas inventadas.

### Decisiones metodológicas

- **Python desde la primera sesión.** El criterio 5.1 de Madrid exige lenguajes de programación **textuales** y el paradigma de la **programación estructurada**: Python cumple ambos, es el lenguaje con el que el alumnado seguirá trabajando en la placa controladora mediante MicroPython y da continuidad a las materias de Ciencias de la Computación.
- **Jupyter Notebook con Google Colab como entorno principal.** No requiere instalación, funciona desde cualquier equipo del centro o de casa y permite alternar explicación y código ejecutable en el mismo documento.
- **Thonny como segundo entorno.** Se utiliza para la ejecución de archivos `.py`, para la depuración paso a paso con puntos de interrupción e inspección de variables —que es exactamente lo que pide el criterio 5.3— y para grabar programas MicroPython en la placa controladora de los bloques F y G.
- **Diagramas de flujo: tratamiento breve.** Se presentan sus símbolos y se practica la lectura de un diagrama sencillo, lo suficiente para reconocer la notación cuando aparezca en un esquema ajeno. No se convierten en método de diseño.
- **Pseudocódigo en lenguaje natural, nunca en un lenguaje formal.** Los algoritmos se describen de viva voz o por escrito en español corriente, con entradas y salidas esperadas. No se enseña ninguna notación formal de pseudocódigo ni herramientas del tipo PSeInt: obligan a aprender una sintaxis intermedia que después hay que abandonar. Ese esfuerzo se invierte en Python, ejecutable desde el primer día.
- **La compilación se explica, no se practica.** El texto oficial menciona «compilación o interpretación»; en un curso basado en Python se aborda como concepto, comparando ambos caminos en el Tema 15.
- **Las estructuras de datos incluyen listas, tuplas y diccionarios.** El currículo habla de «estructuras de datos» sin concretar; los diccionarios son necesarios en el Tema 16 para dar forma a los datos que un dispositivo IoT publica, y el registro de series de medidas en ficheros CSV se incorpora en el Tema 15 porque es lo que permite que los bloques F y G trabajen con datos propios y no con cifras de catálogo.
- **La programación se concentra en el bloque E.** No se reparte en dosis pequeñas dentro de los bloques anteriores: cada bloque conserva su objeto propio y Python se trabaja de forma continuada, donde la progresión puede sostenerse sesión a sesión. Los bloques F y G la aplican, no la reexplican.
- **La placa del curso es el ESP32 DevKit, y la decisión está cerrada.** El criterio que la determina es el mismo que rige todo el bloque: un solo lenguaje textual de principio a fin. Eso descarta el Arduino UNO del taller, que **no puede ejecutar MicroPython** —2 KB de RAM frente a los 16 KB mínimos, y no existe puerto para AVR—, y descarta el micro:bit, que **no tiene Wi-Fi** y deja el Tema 16 sin soporte nativo. El Arduino UNO R4 WiFi tampoco sirve: su procesador principal es un Renesas y el ESP32-S3 va solo de radio. La única alternativa equivalente era la Raspberry Pi Pico 2 W, descartada por material didáctico y ecosistema de módulos, no por capacidad.
- **Las placas Arduino del taller no se jubilan.** El periférico se reutiliza íntegro y el UNO conserva el bloque D —donde el objeto son los circuitos, no la placa, y donde Tinkercad Circuits lo simula con exactitud— y la vía opcional en C++. El gasto de la decisión es de unos 50 € por grupo, una placa por equipo de cuatro: no es una reinversión de taller.
- **Alternativa considerada y descartada para el curso:** gobernar un Arduino UNO desde Python en el ordenador mediante Firmata. Mantendría las placas y el lenguaje único, pero ata la placa al USB del PC: no puede funcionar de forma autónoma en el huerto ni comunicarse por Wi-Fi. Sirve como demostración puntual, no como soporte del proyecto.
- **Cinco temas de programación no son un curso de Python.** Es la objeción más repetida a este bloque, y la respuesta es curricular: el criterio 5.1 de Madrid añade al texto estatal la exigencia de lenguajes textuales y de paradigma estructurado, el 5.3 pide trazar la ejecución, y **en 2.º de Bachillerato no hay bloque de programación** —el bloque informático de Tecnología e Ingeniería II es «Sistemas informáticos emergentes»: inteligencia artificial, *big data* y ciberseguridad—. Este bloque es el único lugar de la materia donde se aprende a programar, y además sostiene los bloques F y G. Recortarlo a tres temas dejaría el control y la robótica apoyados en un conocimiento que nadie habría enseñado.

## Bloque F — Decisión: tres temas

La secuencia responde a tres preguntas consecutivas:

1. **¿Qué es un sistema de control y cómo se representa?** Conceptos, elementos, lazo abierto y cerrado, modelización.
2. **¿Cómo se automatiza y cómo se vigila a distancia?** Automatización programada, SCADA, telemetría y monitorización.
3. **¿Cómo se mueve un robot y qué aporta la inteligencia artificial?** Robótica y tecnologías emergentes aplicadas al control.

### Por qué no dos o cuatro

- **Dos temas** dejarían el SCADA y la telemetría como apéndice de la robótica o del control, cuando el currículo los enuncia con «definición, características y ventajas», es decir, como contenido con entidad propia.
- **Cuatro temas** aislarían la inteligencia artificial en una unidad que a este nivel sería divulgativa y no operativa.
- **Tres temas** siguen el orden natural del trabajo: entender el sistema, programarlo y supervisarlo, y después moverlo.

### Decisiones de contenido

- La modelización se hace con diagramas de bloques, no con funciones de transferencia ni transformadas: eso es Tecnología e Ingeniería II.
- El control proporcional y la histéresis se incorporan como ampliación mínima para que el lazo cerrado no se reduzca a un esquema en la pizarra.
- El SCADA se estudia sobre una maqueta propia: la placa publica sus lecturas y un panel las representa. Así, «definición, características y ventajas» deja de ser una lista y pasa a ser una experiencia.
- La inteligencia artificial se trata aplicada al control —reconocimiento de patrones y decisión a partir de datos— y no como panorama general del campo, que no es objeto de esta materia.

## Bloque G — Decisión: cuatro temas

La secuencia responde a cuatro preguntas consecutivas:

1. **¿De dónde viene la energía y cuánto cuesta?** Fuentes, generación, transporte, mercados y ahorro.
2. **¿Cómo llegan la electricidad y el agua a una vivienda?** Suministros, protecciones, esquemas, factura y ahorro de agua.
3. **¿Cómo se acondiciona una vivienda y cómo se evita tener que acondicionarla?** Climatización, transmisión del calor, aislamiento y arquitectura sostenible.
4. **¿Cómo se automatiza el ahorro, cómo se produce energía en casa y cómo se acredita?** Domótica, renovables, autoconsumo y certificación.

### Por qué no tres

La primera versión del programa usaba tres temas y el último acumulaba seis núcleos de contenido independientes —climatización, aislamiento, arquitectura sostenible, domótica, renovables y certificación— en ocho epígrafes. Era, con diferencia, el tema más denso del programa. El desdoblamiento separa lo pasivo de lo activo: primero reducir la demanda —aislar, orientar, ventilar—, después cubrirla con instalaciones eficientes, energía propia y automatización. Ese es además el orden correcto de intervención en una rehabilitación real.

### Decisiones de contenido

- **El bloque no se imparte al final del curso.** Los temas 20 y 21 se adelantan a la primera y la segunda evaluación. El orden de este documento reproduce el del currículo, pero el calendario no tiene por qué: cuando el bloque energético entero se deja para junio es el que se queda sin dar, y es justamente el que sostiene la competencia 6 y la conexión con los Objetivos de Desarrollo Sostenible.
- **El análisis es cuantitativo, no descriptivo.** Los temas incorporan balance energético de la vivienda, cálculo de costes, dimensionado elemental de una instalación fotovoltaica y periodo de retorno de una medida de ahorro. Estudiar tipos de centrales sin calcular nada convierte el bloque en cultura general; con los cálculos se convierte en la aplicación de la competencia 4 a un problema doméstico real.
- La factura eléctrica se trabaja como documento real: es lo que convierte el criterio 6.2 en algo comprobable y conecta el cálculo de costes del Tema 20 con la instalación del Tema 21.
- Las energías renovables se estudian dos veces con niveles distintos: como sistemas de generación en el Tema 20 y como autoconsumo de la vivienda en el Tema 23.
- Las máquinas térmicas, que la introducción del currículo menciona al describir la competencia 6, no aparecen en los contenidos de 1.º y sí en los de 2.º: no se adelantan.
- La certificación energética se trabaja leyendo e interpretando etiquetas reales de edificios y de aparatos.

## Revisión externa del programa (septiembre de 2026)

La primera versión del programa —veintidós temas— se sometió a la revisión de siete sistemas de inteligencia artificial, a los que se pidió contrastarla con el currículo oficial y con programaciones de departamento reales. Este apartado registra qué se aceptó, qué se rechazó y por qué, para que ninguna de las dos decisiones tenga que volver a discutirse desde cero.

### Cambios aceptados

| Observación | Cambio realizado |
| --- | --- |
| La modularización llegaba después de las colecciones, y todos los programas de los temas 13 y 14 quedaban monolíticos | Las funciones se adelantan al Tema 14; el Tema 15 recoge colecciones y proceso de desarrollo |
| La cabecera prometía MicroPython sobre placa y la secuencia no la usaba hasta el Tema 16 | La placa entra en el Tema 14, con salida digital, entrada digital y lectura de un sensor |
| El último tema del bloque G acumulaba seis núcleos independientes | Se desdobla en Tema 22 (climatización, aislamiento y arquitectura sostenible) y Tema 23 (domótica, renovables y certificación) |
| El Tema 16 era un curso de telecomunicaciones: cuatro tecnologías de enlace más dos protocolos de aplicación | Se prioriza Wi-Fi con MQTT y HTTP; Bluetooth, Zigbee y LoRa quedan a nivel de reconocimiento |
| «Par, potencia y rendimiento» aparecía en los temas 7 y 9 sin decir en qué se diferencian | El epígrafe del Tema 7 declara que el cálculo corresponde al Tema 9 |
| Las bobinas no tienen aplicación en un bloque limitado a corriente continua | Se acotan a su uso real: el relé |
| Faltaban el relé, el puente en H, la modulación de ancho de pulso y la conversión analógico-digital, imprescindibles para accionar algo desde la placa | Se incorporan a los temas 10 y 11 como contenido de ampliación declarado |
| No había temporalización ni reparto por evaluaciones | Se añade la temporalización orientativa: 132 sesiones, 109 de temas, reparto por tema y por evaluación |
| No se declaraban los conocimientos previos, y la materia no exige haber cursado Tecnología en 4.º de la ESO | Se añade el apartado de conocimientos previos, con lo que aporta cada materia de procedencia y lo que se cursa en paralelo |
| El programa declaraba el proyecto como eje metodológico sin concretar ninguno | Se añade el apartado de proyectos integradores con las dos fases del KR-1 y el entregable de cada bloque |
| Los simuladores de los bloques C y D quedaban sin nombre mientras el bloque E sí concretaba entornos | Se añade el apartado de herramientas y entornos, con la placa propuesta y sus alternativas |
| La ruptura de estereotipos sobre las materias tecnológicas, prescrita en el currículo, solo estaba implícita | Epígrafe propio en el Tema 1 |
| Las competencias específicas no citaban los descriptores operativos del perfil de salida | Se añaden entre corchetes, tomados del propio Decreto 64/2022 |
| Faltaban las máquinas de estados y las condiciones de seguridad de un automatismo | Se incorporan al Tema 18 |
| El bloque G, entero al final del curso, es el que se queda sin impartir | Los temas 20 y 21 se adelantan a la primera y segunda evaluación |
| El bloque energético era descriptivo | Se incorporan balance energético de la vivienda, dimensionado fotovoltaico elemental y periodo de retorno |
| El texto alternaba «costos» y «costes» | Se unifica en «costes», citando una vez el «costos» del texto oficial |

### Propuestas rechazadas, y por qué

- **Reducir el temario a 15–17 temas o reorganizarlo en cinco o seis «proyectos» que sustituyan a los bloques.** Este documento es el temario de referencia de la materia, no la programación de aula: su valor está precisamente en la granularidad, porque es lo que permite comprobar epígrafe por epígrafe la cobertura del Decreto 64/2022. Las unidades didácticas se derivan de él agrupando temas contiguos, y los proyectos integradores ya atraviesan los bloques sin disolverlos. Sustituir los bloques por proyectos rompería además la trazabilidad con el currículo, que es lo que sostiene el documento ante una revisión.
- **Recortar el bloque de programación de cinco temas a tres.** Fue la propuesta más repetida y es la que menos se sostiene: el criterio 5.1 de Madrid añade al texto estatal la exigencia de lenguajes **textuales** y de **programación estructurada**, el 5.3 pide trazar la ejecución paso a paso, y **en 2.º de Bachillerato no existe bloque de programación** —el bloque informático de Tecnología e Ingeniería II es «Sistemas informáticos emergentes»—. Es el único lugar de la materia donde se aprende a programar, y encima sostiene los bloques F y G. Lo que sí se ha hecho es reordenarlo por dentro.
- **Introducir Blender antes que un CAD paramétrico.** El modelado poligonal no es expresión gráfica de ingeniería: no tiene cotas, ni restricciones, ni tolerancias, ni genera planos, y el criterio 3.3 pide justamente CAD, CAE y CAM para «diseño, dimensionado y fabricación de un producto industrial». La fase divergente del diseño ya está cubierta, y mejor, por el croquis a mano alzada del Tema 3.
- **Suprimir el grafeno, el estaneno, el *shrilk*, el PVD y el CVD por demasiado específicos.** Son contenido literal del Decreto 64/2022. Lo que se puede decidir es la profundidad, y se ha decidido: nivel de reconocimiento.
- **Suprimir o rebajar el SCADA.** También es contenido literal, y con sus tres exigencias explícitas: «definición, características y ventajas». Se mantiene, trabajado sobre la maqueta propia —la placa publica, un panel representa— en lugar de sobre un sistema industrial que el alumnado no puede tocar.
- **Desdoblar el Tema 3 en un tema de dibujo a mano sin ordenador y otro de CAD.** La preocupación es legítima —el CAD tiende a comerse el lápiz—, pero la secuencia interna del tema ya va croquis → vistas → acotación → esquemas → CAD, y sus tres primeros apartados son manuales. Convertirlo en dos temas gastaría una sesión en una frontera artificial. La garantía es metodológica, no estructural: **el croquis del Proyecto 1 se entrega a mano, fechado y firmado, antes de abrir el CAD**.
- **Añadir corriente alterna, mapas de Karnaugh, diagramas de fases o neumática.** Varias revisiones criticaron su presencia o pidieron su tratamiento; no están en el programa y no deben estarlo: son contenido de Tecnología e Ingeniería II, y el documento ya lo declara en el apartado de continuidad.

### Una advertencia sobre este tipo de revisión

Conviene saber que una parte apreciable de las observaciones recibidas no se refería al documento real:

- Una de las revisiones declaró expresamente que **no había podido acceder al archivo** y a continuación afirmó que «la carencia más importante» era la ausencia de un bloque de sistemas informáticos y programación, que el programa desarrolla en cinco temas.
- Otra criticó la inclusión de **corriente alterna con impedancias y triángulos de potencia, de mapas de Karnaugh y de diagramas de fases**: ninguno de los tres figura en el programa, que los asigna explícitamente a 2.º.
- Otra afirmó que el programa fija **FreeCAD como herramienta prioritaria** y, en la misma página, que **no concreta qué software de CAD se usa**. La segunda afirmación era la correcta: la primera versión no nombraba ninguno. También citó números de saberes básicos —«1.9» y «1.10»— que no existen en el Decreto 64/2022, cuyos contenidos se enumeran por bloques de la A a la G sin numerar.

Las observaciones que sí resultaron útiles fueron, sin excepción, las que se podían verificar contra el texto del documento o contra el del decreto. Es el mismo criterio que el Tema 1 pide aplicar a cualquier fuente: ir al original, comprobar y no dar por bueno lo plausible.

## Relación con Tecnología e Ingeniería II

El programa se ha escrito comprobando el currículo de 2.º curso para evitar solapamientos y huecos:

- La corriente alterna, la electrónica digital combinacional y secuencial y los sistemas neumáticos e hidráulicos no se tratan en 1.º.
- El cálculo de estructuras y las máquinas térmicas pertenecen al bloque de sistemas mecánicos de 2.º.
- La estructura interna de los materiales, los ensayos normalizados y las técnicas de fabricación industrial corresponden a 2.º.
- El control se queda en 1.º en el nivel de diagramas de bloques y programación de placa; el álgebra de bloques, la simplificación y el estudio de la estabilidad corresponden a 2.º.
- La programación no vuelve a aparecer como bloque en 2.º: el bloque informático de 2.º es «Sistemas informáticos emergentes» —inteligencia artificial, *big data* y ciberseguridad—. Por eso el Bloque E de 1.º no puede tratarse como una introducción que ya se completará después: es el único lugar de la materia donde se aprende a programar.

## Relación con las demás asignaturas del departamento

- **Tecnología de 4.º de la ESO** deja trabajados los mecanismos, la electricidad básica, la electrónica digital, el control programado y la robótica en un nivel introductorio. Tecnología e Ingeniería I no los repite: los retoma desde el cálculo, la simbología y la interpretación de circuitos y esquemas.
- **Ciencias de la Computación I** comparte con esta materia el lenguaje, el entorno y el método de trabajo en programación, pero no el objeto: allí la programación es el fin y aquí es una herramienta al servicio del control de sistemas. Los temas 12 a 15 se redactan de modo que funcionen para quien no curse aquella materia.
