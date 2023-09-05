import sqlite3
import json


class DialogueDatabase:
    def __init__(self, db_url):
        self.db_url = db_url
        self.conn = sqlite3.connect(db_url)
        self.cursor = self.conn.cursor()

    def getDialogue(self, dialogue_id):
        # Conectar a la base de datos SQLite3
        # Reemplaza 'tu_base_de_datos.db' con el nombre de tu base de datos
        self.conn = sqlite3.connect(self.db_url)
        self.cursor = self.conn.cursor()
        # Consulta para obtener imagePath, audioDuration y esMaximo de VideoTimeView
        self.cursor.execute("""
            SELECT imagePath, audioDuration, esMaximo, scene_id FROM VideoTimeView
            WHERE dialogue_id = ?;
        """, (dialogue_id,))

        result = self.cursor.fetchone()

        if result is None:
            self.conn.close()
            return None

        imagePath, audioDuration, esMaximo, scene_id = result

        if esMaximo == 'yes':
            # Consulta para obtener el contenido de Timeline
            self.cursor.execute("""
                SELECT content FROM Timeline
                WHERE scene_id = ? AND type = 'sound';
            """, (scene_id,))

            timeline_results = self.cursor.fetchall()

            if timeline_results:
                # Calcular la suma de las duraciones de sonido en milisegundos y agregarla a audioDuration
                for timeline_result in timeline_results:
                    content_json = json.loads(timeline_result[0])
                    if "duration" in content_json:
                        audioDuration += content_json["duration"] * 1000

        self.conn.close()

        return imagePath, audioDuration

    def getDialogueData(self):
        # Consulta para obtener los dialogue_id ordenados de manera ascendente
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT dialogue_id FROM Dialogue
            ORDER BY dialogue_id ASC;
        """)

        dialogue_ids = self.cursor.fetchall()

        dialogue_data_list = []

        for dialogue_id in dialogue_ids:
            dialogue_id = dialogue_id[0]  # Extraer el valor del tuple
            dialogue_data = self.getDialogue(dialogue_id)

            if dialogue_data:
                imagePath, audioDuration = dialogue_data
                dialogue_data_dict = {
                    "imagePath": imagePath,
                    "audioDuration": audioDuration
                }
                dialogue_data_list.append(dialogue_data_dict)

        self.conn.close()
        return dialogue_data_list


# Ejemplo de uso
"""
db_url = "/Users/alvaroperis/Dropbox/draft/Idiotas.cst"
db = DialogueDatabase(db_url)

try:
    imagePath, audioDuration = db.getDialogue(2)
    print("Imagen:" + imagePath + " Duración: " + str(audioDuration))
except Exception as e:
    print(str(e))
"""
