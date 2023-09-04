from ...utils import Job
from . import jtask

description = "Renderiza el video."
configMap = {
    "type": "object",
    "properties": {
        "pname": {
            "type": "string",
            "description": "Nombre del fichero del proyecto sin extension."
        },
        "audiopath": {
            "type": "string",
            "description": "Nombre del audio del proyecto."
        },
        "storepath": {
            "type": "string",
            "description": "Ruta donde se almacenará la salida."
        }
    },
    "required": ["pname", "audiopath", "storepath"]
}


class MJob(Job.Job):
    def __init__(self):
        super().__init__(description,
                         configMap)

    def task(self):
        jtask.run(self.params)


def get():
    return MJob()
