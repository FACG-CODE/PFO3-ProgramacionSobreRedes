# 📚 PFO3 - Sistema de Stock de Libros (Cliente-Servidor con Workers)

## 📝 Descripción
Este proyecto es un sistema distribuido para registrar libros en una base de datos SQLite.  
Está compuesto por:

- 🖥 **Servidor:** centraliza las solicitudes del cliente y coordina la comunicación con los workers.  
- ✏️ **Worker de escritura:** recibe datos de libros y los guarda en la base de datos.  
- 🔍 **Worker de lectura:** devuelve el último ID de libro registrado al servidor.  
- 🧑‍💻 **Cliente:** permite registrar libros o salir del sistema.

La comunicación entre servidor y workers se realiza mediante **sockets TCP**.

## ⚙️ Requisitos
- Python 3.x
- Módulos:
  - `sqlite3`
  - `socket`
  - `threading`
  - `json`

## 🚀 Instrucciones
- Posicionarse dentro de la carpeta 'src' del repositorio y ejectur en consola:
    ``` python main.py ```

## ⚠️ Notas
- El servidor principal utiliza el puerto 5000
- Cada worker corre en su propio puerto:
    - 6000 para escritura ✏️
    - 7000 para lectura 🔍
- Cada conexión con cliente se maneja en un hilo separado, permitiendo múltiples clientes simultáneos.
- Cada solicitud del servidor principal a los workers se maneja en un hilo separado, permitiendo múltiples consultas simultáneas.

## 👤 Autor
Francisco Agustin Cruz Guantay