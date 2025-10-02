# Prompts usados en el desarrollo

Este archivo documenta las interacciones con la IA que guiaron el diseño del proyecto.

---

## Diseño del Tablero

**Prompt:**  
> "¿Por qué hablamos de puntos? ¿Qué son los puntos? ¿Por qué 24? ¿Qué es la barra y el borne off?"

**Respuesta de la IA (resumen):**  
La IA explicó que el tablero de backgammon se compone de **24 puntos o agujas**, que son las posiciones posibles para colocar fichas.  
- Cada jugador tiene **15 fichas**.  
- Las **24 agujas** están divididas en 4 cuadrantes de 6 agujas cada uno.  
- La **barra** es el lugar donde van las fichas capturadas que deben reingresar al juego.  
- El **borne off (retirada)** es el sector donde se colocan las fichas que ya salieron del tablero, para contar la victoria.  

A partir de esa explicación, se diseñó la clase `Tablero` con:  
- Una lista de 24 agujas (`__agujas__`).  
- Un diccionario para la barra (`__barra__`).  
- A un diccionario para la retirada (`__retirada__`).  

---

## Creación de getters básicos

**Prompt:**  
> "¿Cómo puedo comenzar con `estado_aguja` y por qué?"

**Respuesta de la IA (resumen):**  
Se recomendó implementar métodos mínimos para **leer el estado del tablero sin tocar atributos internos**:  
- `estado_aguja(idx)` devuelve `(color, cantidad)` en la aguja indicada.  
- `fichas_en_barra(color)` devuelve cuántas fichas hay en la barra para un color.  
- `fichas_retiradas(color)` devuelve cuántas fichas retiró ese color.  

Estos métodos se justificaron como **getters**: funciones que exponen información del estado interno sin modificarlo.  

---

## Separar la lógica del juego de lo demás

**Prompt:**  
> "Pensaba hacer que las fichas estén en una base de datos."

**Respuesta de la IA (resumen):**  
La IA explicó que conviene mantener la **lógica del juego en memoria** (clases como `Tablero`, `Dados`, `Jugador`) y separar en otra capa la **persistencia** (JSON, SQLite o Redis) y la **presentación** (CLI, interfaz gráfica, etc.).  
- El core (`Tablero`) se encarga solo de reglas del backgammon.  
- La capa de persistencia guarda o carga el estado (`a_dict`, `desde_dict`, `json_store`).  
- La UI o CLI solo muestra información y recibe comandos del usuario.  

Esta separación permite testear la lógica del juego sin depender de la base de datos ni de la interfaz, y facilita cambios futuros (por ejemplo, reemplazar JSON por SQLite).  

## Uso y utilidad de type hints en Python


> "¿Cómo se usan los type hints en Python y para qué sirven?"

**Respuesta de la IA (resumen):**  
La IA explicó que los **type hints** son anotaciones opcionales que se colocan en parámetros y valores de retorno de funciones o métodos para indicar qué tipo de datos deberían usarse.  
- Ejemplo: `def sumar(a: int, b: int) -> int:`  
- No modifican la ejecución del programa (Python sigue siendo dinámico), pero sirven para:  
  - Mejorar la legibilidad del código.  
  - Obtener autocompletado más preciso en editores.  
  - Detectar errores con linters y herramientas de análisis estático como `mypy`.  

Se recomendó usarlos en proyectos medianos o grandes para hacer el código más claro y mantenible.

## Aplicar SRP en el método mover_ficha de Juego

**Prompt:**  
> "¿Cómo aplico una buena práctica o un principio SOLID en un método como mover_ficha del Juego?"

**Respuesta (resumen):**  
La IA explicó que el método `mover_ficha` en la clase `Juego` actualmente mezcla varias responsabilidades:  
- Validar si la ficha puede moverse (regla del color, si la aguja está bloqueada, captura).  
- Actualizar el estado del tablero (restar en 'desde', sumar en 'hasta', mandar ficha a la barra).  

Según el principio de **Responsabilidad Única (SRP)** conviene separar estas tareas:  
- `Tablero` debería proveer métodos como `puede_colocar(idx, color)` o `mover_simple(desde, hasta, color)` que encapsulen la lógica interna.  
- `Juego` debería encargarse de coordinar la acción (saber qué jugador juega y qué movimiento intenta), pero no manipular directamente las estructuras privadas de `Tablero`.  

Esto reduce acoplamiento, mejora la legibilidad y permite testear la lógica de movimiento en `Tablero` sin necesidad de pasar por toda la clase `Juego`.
