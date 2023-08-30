from setuptools import setup, find_packages
import os

# Obtén la lista de archivos en el directorio "cassette/utils"


def get_data_files(directory):
    data_files = []
    for root, _, files in os.walk(directory):
        for filename in files:
            data_files.append(os.path.relpath(
                os.path.join(root, filename), start=directory))
    return data_files


setup(
    name="cassette",
    version="1.0.0",
    description="Una aplicación de ejemplo de PyClick",
    author="Tu Nombre",
    author_email="tu@email.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyclick",
        # Lista de otras dependencias aquí
    ],
    entry_points={
        "console_scripts": [
            "cassette = cassette.main:main",
        ],
    },
    package_data={
        "": ["utils/.env"],
    },
)
