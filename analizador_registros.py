import re

def analizar_registro_resumido(archivo_registro, palabra_clave):
    """
    Analiza un archivo de registro, contando registros por tipo,
    identificando IPs únicas y buscando una palabra clave 

    Args:
        archivo_registro (str): Nombre del archivo de registro.
        palabra_clave (str): Palabra clave a buscar en los registros.

    Returns:
        str: Informe con el análisis.
         """