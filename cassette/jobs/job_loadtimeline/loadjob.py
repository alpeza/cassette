import sqlite3
import yaml
import json


def load_tags(name, yaml_data):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    for key, value in yaml_data.get("tags", {}).items():
        cursor.execute(
            "INSERT INTO Tags (name, value) VALUES (?, ?);", (key, value))

    conn.commit()
    conn.close()


def load_video_data(name, yaml_data):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    # cursor.execute('PRAGMA foreign_keys = ON;')  # Habilitar claves foráneas

    for video_entry in yaml_data.get("video", []):
        dialogue_id = video_entry.get("id")
        video_type = video_entry.get("type")
        image_path = video_entry.get("imagePath")

        cursor.execute(
            "INSERT INTO DialogueVideo (dialogue_id, type, imagePath, rendered) VALUES (?, ?, ?, 0);",
            (dialogue_id, video_type, image_path)
        )

    conn.commit()
    conn.close()


def load_characters(name, yaml_data):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    for character in yaml_data.get("characters", []):
        character_id = character.get("id")
        tts = json.dumps(character)
        cursor.execute(
            "INSERT INTO CharacterDescriptor (character_id, tts) VALUES (?, ?);", (character_id, tts))

    conn.commit()
    conn.close()


def load_timeline(name, yaml_data):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()

    timeline = yaml_data.get("timeline", [])
    scene_id = 1
    for sequence_id, item in enumerate(timeline):
        sequence_type = item.get("type")
        if sequence_type == "scene":
            scene_id = item.get("scene_id")

        content = json.dumps(item)
        cursor.execute("INSERT INTO Timeline (sequence_id, type, content, scene_id) VALUES (?, ?, ?,?);",
                       (sequence_id, sequence_type, content, scene_id))

    conn.commit()
    conn.close()


def runloader(timeline_file, pname):

    # Cargar datos desde el archivo YAML
    nombre_base_de_datos = f"{pname}.cst"
    yaml_file = timeline_file

    with open(yaml_file, 'r') as f:
        yaml_data = yaml.safe_load(f)

    # Cargar los datos en las tablas
    load_tags(nombre_base_de_datos, yaml_data)
    load_characters(nombre_base_de_datos, yaml_data)
    load_timeline(nombre_base_de_datos, yaml_data)
    load_video_data(nombre_base_de_datos, yaml_data)
