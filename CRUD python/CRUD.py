import mysql.connector

# Establecer la conexión a la base de datos
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crud_python'
)

cursor = conn.cursor()

def crear_usuario(nombre, edad):
    query = "INSERT INTO Usuarios (nombre, edad) VALUES (%s, %s)"
    valores = (nombre, edad)
    cursor.execute(query, valores)
    conn.commit()

def obtener_usuarios():
    query = "SELECT * FROM Usuarios"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

def actualizar_usuario(id, nuevo_nombre):
    query = "UPDATE Usuarios SET nombre = %s WHERE id = %s"
    valores = (nuevo_nombre, id)
    cursor.execute(query, valores)
    conn.commit()

def eliminar_usuario(id):
    query = "DELETE FROM Usuarios WHERE id = %s"
    valores = (id,)
    cursor.execute(query, valores)
    conn.commit()

# Ejemplo de uso
crear_usuario("Juan", 25)
crear_usuario("Maria", 30)

obtener_usuarios()

actualizar_usuario(1, "Pedro")

eliminar_usuario(2)

obtener_usuarios()


""" CREATE DATABASE IF NOT EXISTS NombreDeTuBaseDeDatos;

USE NombreDeTuBaseDeDatos;

CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    edad INT
); """