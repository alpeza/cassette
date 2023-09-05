from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, concatenate_videoclips
from . import Dialogue


class VideoRenderer(Dialogue.DialogueDatabase):
    def generateVideoWithAudio(self, output_file, audio_input):
        dialogue_data_list = self.getDialogueData()

        if not dialogue_data_list:
            return

        image_files = [data["imagePath"] for data in dialogue_data_list]
        durations = [data["audioDuration"] /
                     1000.0 for data in dialogue_data_list]

        # Definir el tamaño de imagen deseado (por ejemplo, Full HD)
        desired_width = 1920
        desired_height = 1080

        # Crear una lista de clips de imagen con duraciones personalizadas
        clips = []
        for imagen, duracion in zip(image_files, durations):
            print(f"Añadiendo imagen: {imagen} Dur {str(duracion)}")
            imagen_clip = ImageClip(imagen)
            # Redimensionar la imagen al tamaño deseado
            imagen_clip = imagen_clip.resize((desired_width, desired_height))
            imagen_clip = imagen_clip.set_duration(duracion)
            imagen_clip.crossfadein(2.0)
            clips.append(imagen_clip)

        # Concatenar los clips para crear un único clip
        video_final = concatenate_videoclips(clips, method="compose")

        # Cargar el archivo de audio
        audio_clip = AudioFileClip(audio_input)

        # Añadir el audio al video
        video_with_audio = video_final.set_audio(audio_clip)

        # Exportar el video final con audio
        video_with_audio.write_videofile(
            output_file, codec='mpeg4', audio_codec='aac', fps=24)


"""
# Ejemplo de uso
db_url = "/Users/alvaroperis/Dropbox/draft/Idiotas.cst"
db = VideoRenderer(db_url)


# Reemplaza con el nombre del archivo de salida deseado
output_file = "output_with_audio.mp4"
# Reemplaza con la ubicación del archivo de audio deseado
audio_input = "/Users/alvaroperis/Dropbox/draft/Idiotas/film/Idiotas.mp3"
db.generateVideoWithAudio(output_file, audio_input)
print(f"Video generado con audio: {output_file}")
"""
