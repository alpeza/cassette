import os
import sqlite3
import logging


class DatabaseAlreadyExistsError(Exception):
    pass


def createDB(name):
    if not os.path.exists(f"{name}.cst"):
        raise DatabaseAlreadyExistsError(
            f"El archivo {name}.cst no existe. Es necesario iniciar un proyecto cst previamente.")

    conn = sqlite3.connect(f"{name}.cst")
    # Crear un cursor para ejecutar comandos SQL
    cursor = conn.cursor()

    # Eliminar las tablas si ya existen
    cursor.execute('''DROP TABLE IF EXISTS CharacterDescriptor;''')
    cursor.execute('''DROP TABLE IF EXISTS Timeline;''')
    cursor.execute('''DROP TABLE IF EXISTS Tags;''')

    # Sentencia SQL para crear la tabla Character
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CharacterDescriptor (
        character_id INTEGER PRIMARY KEY,
        tts TEXT
    );
    ''')

    # Sentencia SQL para crear la tabla de Timeline
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Timeline (
        sequence_id INTEGER PRIMARY KEY,
        type TEXT,
        scene_id INTEGER,
        content TEXT
    );
    ''')

    # Sentencia SQL para crear la tabla de Timeline
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tags (
        tag_id INTEGER PRIMARY KEY,
        name TEXT,
        value TEXT
    );
    ''')

    cursor.execute('''
    CREATE VIEW VideoTimeView AS
    SELECT D.dialogue_id, D.audioDuration, DV.imagePath, D.scene_id,
        CASE WHEN D.audioDuration = MAX(D.audioDuration) OVER (PARTITION BY D.scene_id)
                THEN 'yes'
                ELSE 'no'
        END AS esMaximo
    FROM Dialogue D
    INNER JOIN DialogueVideo DV ON D.dialogue_id = DV.dialogue_id;
    ''')
    # Guardar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    logging.debug("Tablas de timeline creadas")
