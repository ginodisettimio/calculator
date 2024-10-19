# Calculator
Primer proyecto integrador del curso "Python+FastAPI".

Este proyecto presenta una calculadora que contiene operaciones aritméticas, un conversor de temperaturas, un actualizador de decimales, un historial de operaciones y la posibilidad de borrar el historial. Cumpliendo así las funciones básicas de un CRUD (Create, Read, Update, Delete).

## Dependencias
- **Termcolor:** Dependencia para agregar colores al texto en la consola.

## Puesta en marcha
1. Instalar Python version 3.12.6

    Hay dos opciones validas:
    - Desde la `Microsoft Store`

        `Buscar Python` - `Elegir Python 3.12` - `Pulsar Obtener`

    - Desde `https://www.python.org/ (la web oficial de Python)`
    
        `Downloads` -> `Tu sistema operativo` -> `Download installer(bits de tu sistema)`
        
        Instalar como cualquier otro programa.

    Para comprobar si se instalo correctamente:
    1. Abrir en Terminal
    2. Escribir `python` o `py`
    Si se imprime `Python 3.12.6` y/o se muestran `>>>`, signfica que se instaló correctamente.

2. Crear un entorno virtual y activarlo
    
    - Crear una `Nueva Terminal` o utilizar el shortcut Ctrl+Shift+ñ
    - En la consola, escribir `python -m venv env` ó `python -m venv venv`
    - Pasos para activarlo:

        Si tienes Windows:
        ```
        env\Scripts\activate
        venv\Scripts\activate
        ```

        Si tienes Linux:
        ```
        source env/bin/activate
        source venv/bin/activate
        ```

    - Para comprobar que se activó correctamente tendría que salir `(env)` ó `(venv)` detras de la ubicación del archivo en la terminal.

    - Para desactivar el entorno virtual, escribir en la terminal:
        ```
        deactivate
        ```

3. Instalar dependencia del archivo `requirements.txt`

    - Dentro del entorno virtual, escribir en la terminal:
        ```
        pip install -r requirements.txt
        ```

    - También se puede usar para actualizar las dependencias o si agregaron nuevas.

4. Ejecutar con Python el archivo `main.py`
    
    Escribir en la términal
    ```
    py main.py
    python main.py
    ```

    Le saldrá una interfaz donde podrá elegir escribiendo el número correspondiente a la opción.

    ```
    CALCULADORA

    1.Operaciones aritmeticas
    2.Conversor de unidades
    3.Mostrrar historial
    4.Borar historial
    5.Actualizar cuenta
    0.Salir

    Elija una opción =
    ```
    
    - Para deplegar la lista de operaciones aritmeticas disponibles, escribir `1`
    - Para deplegar la lista de unidades a convertir disponibles, escribir `2`
    - Para mostrar las operaciones realizadas, escribir `3`
    - Para borrar el historial de las operaciones, escribir `4`
    - Para actualizar la cantidad de decimales visibles de una operacion, escribir `5`
    - Para salir del programa, escribir `0`

    `Opción 1`: Lista de operaciones aritmeticas:

    ```
    1.Suma
    2.Resta
    3.División
    4.Multiplicación
    5.Potencia
    0.Volver

    Elija el tipo de operación =
    ```

    - Para volver al menu anterior, escribir `0`
    - Para realizar una operación matemática, escribir el número correspondiente a la operación aritmetica
        - Ingresar `primer operando` de la cuenta
        - Ingresar `segundo operando` de la cuenta
        - Se mostrará el `Resultado:` y se guardará automaticamente en el historial.

    `Opción 2`: Lista de unidades a convertir:

    ```
    1.Fahrenheit
    2.Celsius
    3.Kelvin
    0.Volver

    Elija el tipo de conversión =
    ```
    - Para volver al menu anterior, escribir `0`
    - Para elegir la unidad a convertir, escribir el número correspondiente
        - Ingresar la `temperatura` a convertir 
        - Ingresar la `unidad a convertir` escribiendo la `primer letra`, es decir `f`, `c` ó `k`
        - Se mostrará el `Resultado:` y se guardará automaticamente en el historial.

    `Opción 5`: Actualizar cuenta
    ```
    CALCULADORA

    1.Operaciones aritmeticas
    2.Conversor de unidades
    3.Mostrrar historial
    4.Borrar historial
    5.Actualizar cuenta
    0.Salir

    Elija una opción =
    ```

    - Para volver al menu anterior, escribir cualquier cosa menos los números correspondientes al índice.
    - Para elegir la operación a realizar, escribir el número del índice de la `operación a actualizar`:
        - Ingresar cuantos `decimales` quiere ver en el resultado
        - Se mostrará el `Resultado actualizado` y se reemplazará automaticamente en el historial.

## Agradecimientos
Al profe por revisar, responder dudas y dar clase

Al creador de Python por su lenguaje
