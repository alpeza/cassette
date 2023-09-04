import os
import logging
from ...lib.video import RenderDialogues


def run(params):
    logger = logging.getLogger(__name__)

    # 1. Mira si existe el directorio indicado en `params['storepath']`.
    # Si no existe, créalo y notifica con un logger.debug que lo ha creado.
    storepath = params['storepath']
    if not os.path.exists(storepath):
        os.makedirs(storepath)
        logger.debug(f"Created directory: {storepath}")

    # 2. Dentro de este directorio crea una carpeta llamada `scenes`
    scenes_dir = os.path.join(storepath, "video")
    if not os.path.exists(scenes_dir):
        os.makedirs(scenes_dir)

    # 3. Se conecta a la sqlite3 especificada en `params['pname']`.
    db_file = f"{params['pname']}.cst"
    if not os.path.exists(db_file):
        logger.error(f"The project {db_file} does not exist.")
        return

    db = RenderDialogues.VideoRenderer(db_file)

    # Reemplaza con el nombre del archivo de salida deseado
    output_file = f"{scenes_dir}/{params['pname']}.mp4"
    audio_input = params['audiopath']
    db.generateVideoWithAudio(output_file, audio_input)
    print(f"Video generado con audio: {output_file}")


"""
if __name__ == "__main__":
    # Example usage:
    params = {
        'storepath': "/path/to/store",
        'pname': "/path/to/project.db"
    }
    run(params)
"""
