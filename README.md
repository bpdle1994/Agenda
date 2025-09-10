# 📂 Proyecto: Agenda de Contactos

## 📝 Descripción del Proyecto
Este es un programa simple de consola, escrito en Python, que simula una agenda de contactos. El objetivo principal de este proyecto es aplicar y demostrar el uso de una **estructura de datos** fundamental para la organización de la información: el **diccionario**. A través de sus funcionalidades, se puede entender cómo los diccionarios permiten un acceso rápido y eficiente a los datos.

## 🧭 Tabla de Contenidos
- [Descripción del Proyecto](#descripción-del-proyecto)
- [Funcionalidades](#funcionalidades)
- [Estructuras de Datos y Algoritmos](#estructuras-de-datos-y-algoritmos)
- [Cómo ejecutar el programa](#cómo-ejecutar-el-programa)
- [Cómo subir el proyecto a GitHub](#cómo-subir-el-proyecto-a-github)
- [Autor](#autor)

## 🚀 Funcionalidades
El programa ofrece un menú interactivo con las siguientes opciones para que el usuario pueda gestionar sus contactos:
1.  **Agregar un contacto**: Permite al usuario guardar un nuevo contacto (nombre y número de teléfono).
2.  **Buscar un contacto**: Encuentra y muestra el número de teléfono de un contacto existente usando su nombre.
3.  **Mostrar todos los contactos**: Lista todos los contactos guardados en la agenda en orden alfabético.
4.  **Salir**: Termina la ejecución del programa.

## 🧠 Estructuras de Datos y Algoritmos
-   **Diccionario (`dict`)**: Es la estructura de datos central del proyecto. Se utiliza para almacenar los contactos en pares de **clave-valor**. La **clave** es el nombre del contacto, lo que permite una **búsqueda extremadamente rápida** y eficiente.

-   **Algoritmo de Ordenamiento**: Para la funcionalidad de "Mostrar todos los contactos", el programa utiliza la función `sorted()` de Python. Esta función ordena las claves del diccionario (los nombres de los contactos) para que se muestren de manera alfabética, lo que mejora la experiencia del usuario.

## 🛠️ Cómo ejecutar el programa
1.  Asegúrate de tener **Python** instalado en tu computadora. Puedes verificarlo abriendo una terminal y ejecutando `python --version` (o `python3 --version` en algunos sistemas).
2.  Guarda el código del proyecto en un archivo llamado `agenda.py` y el contenido de este README en un archivo `README.md`.
3.  Abre tu terminal o la consola de VS Code.
4.  Navega hasta el directorio donde guardaste los archivos.
5.  Ejecuta el siguiente comando para iniciar la agenda:
    ```sh
    python agenda.py
    ```
    El programa se ejecutará y te presentará el menú interactivo en la consola.

## 🔗 Cómo subir el proyecto a GitHub
Sigue estos pasos para subir tu proyecto a un nuevo repositorio en GitHub usando la línea de comandos:
1.  **Inicializa un repositorio Git local:**
    ```sh
    git init
    ```
2.  **Agrega los archivos:**
    ```sh
    git add .
    ```
3.  **Realiza el primer commit:**
    ```sh
    git commit -m "Primer commit: proyecto de agenda de contactos"
    ```
4.  **Conecta con tu repositorio en GitHub:**
    ```sh
    git remote add origin [URL_DEL_REPOSITORIO]
    ```
    (Reemplaza `[URL_DEL_REPOSITORIO]` con la URL que GitHub te proporciona al crear el repositorio.)
5.  **Sube los archivos:**
    ```sh
    git push -u origin main
    ```

## ✍️ Autor
* **[Tu Nombre Completo]** - [Tu perfil de GitHub](URL_de_tu_perfil)