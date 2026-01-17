"""Utilidades para la aplicación."""

import io
import zipfile


def create_zip_from_files(files: list[dict]) -> io.BytesIO:
    """
    Crea un archivo ZIP en memoria a partir de una lista de archivos.

    Args:
        files: Lista de diccionarios con 'filename' y 'data' (BytesIO)

    Returns:
        BytesIO con el archivo ZIP
    """
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for file_info in files:
            filename = file_info['filename']
            file_data = file_info['data']

            # Asegurar que el cursor está al inicio
            file_data.seek(0)

            # Agregar archivo al ZIP
            zip_file.writestr(filename, file_data.read())

    zip_buffer.seek(0)
    return zip_buffer
