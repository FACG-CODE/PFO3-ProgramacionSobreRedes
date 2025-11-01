import socket
import json
from models.funcionesSocket import conectarSocket

HOST = 'localhost'
PORT = 5000

def ejecutarCliente():
    socketServidor = conectarSocket(HOST, PORT)
    if socketServidor is None:
        print("No se pudo conectar al socket del servidor.")
        return
    print (f"Conectado al servidor {HOST}:{PORT}")
    while True:
        opcion = input("Ingrese 'y' para registrar un libro o 'off' para salir: ")
        if not opcion:
            print("La opcion no puede estar vacia.")
            continue
        elif opcion.lower() == 'off':
            print("Cerrando conexion con el servidor.")
            socketServidor.send("off".encode('utf-8'))
            print(socketServidor.recv(1024).decode("utf-8"))
            break
        elif opcion == 'y':
            print("Ingrese de manera secuencial titulo, autor y genero del libro que desea registrar.")
            while True:
                titulo = input("Titulo: ")
                if not titulo:
                    print("El titulo no puede estar vacio. Intente nuevamente.")
                    continue
                else:
                    while True:
                        autor = input("Autor: ")
                        if not autor:
                            print("El autor no puede estar vacio. Intente nuevamente.")
                            continue
                        else:
                            while True:
                                genero = input("Genero: ")
                                if not genero:
                                    print("El genero no puede estar vacio. Intente nuevamente.")
                                    continue
                                libro = {"titulo": titulo, "autor": autor, "genero": genero}
                                mensaje = json.dumps(libro)
                                socketServidor.send(mensaje.encode('utf-8')) # Enviar nuevo libro al servidor como JSON
                                respuesta = socketServidor.recv(1024).decode('utf-8') # Recibir ID del libro registrado
                                print(f"Resultado: {respuesta}")