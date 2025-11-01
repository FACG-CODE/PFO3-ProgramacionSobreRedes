import sqlite3

def inicializarBaseDatos():
    conn = sqlite3.connect("stockLibros.db")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                genero TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("Base de datos inicializada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")
    finally:
        if conn:
            conn.close()

def guardarLibro(titulo, autor, genero):
    conn = sqlite3.connect("stockLibros.db")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO libros (titulo, autor, genero) VALUES (?, ?, ?)
        ''', (titulo, autor, genero))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error al guardar el libro: {e}")
    finally:
        if conn:
            conn.close()

def obtenerUltimoLibro():
    conn = sqlite3.connect("stockLibros.db")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id FROM libros ORDER BY id DESC LIMIT 1
        ''')
        idLibro = cursor.fetchone()
        return idLibro
    except sqlite3.Error as e:
        print(f"Error al obtener el último libro: {e}")
        return None
    finally:
        if conn:
            conn.close()