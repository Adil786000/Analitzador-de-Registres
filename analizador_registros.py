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
    total_registros = 0
    tipos_registros = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    ips_unicas = set()
    conteo_palabra_clave = 0

    try:
        with open(archivo_registro, 'r') as archivo:
            for linea in archivo:
                total_registros += 1
                linea_lower = linea.lower() #Para no repetir la operacion

                # Contar registros por tipo
                for tipo in tipos_registros:
                    if tipo.lower() in linea_lower:
                        tipos_registros[tipo] += 1
                        break #Evitar contar un registro en varios tipos
# Identificar IPs (más robusto)
                ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', linea)
                if ip:
                    ips_unicas.add(ip.group(0))

                # Contar la palabra clave
                if palabra_clave.lower() in linea_lower:
                    conteo_palabra_clave += 1
                    
                except FileNotFoundError:
        return "Error: Archivo no encontrado."
        # Crear el informe
    informe = (
        "Informe d'Anàlisi de Fitxer de Registre\n"
        "---------------------------------------\n"
        f"Nombre total de registres: {total_registros}\n"
        "Registres per tipus:\n"
        f"\tINFO: {tipos_registros['INFO']}\n"
        f"\tWARNING: {tipos_registros['WARNING']}\n"
        f"\tERROR: {tipos_registros['ERROR']}\n"
        "Adreces IP úniques detectades:\n"
        f"\t{chr(10).join(ips_unicas)}\n"
        f"Recurrence de la paraula clau '{palabra_clave}':
        {conteo_palabra_clave}\n"
        "---------------------------------------"
    )

    return informe

        # Ejemplo de uso:
        archivo_registro = "register.log"
        palabra_clave = "error"
        informe = analizar_registro_resumido(archivo_registro, palabra_clave)
        print(informe)

        # Guardar el informe (opcional):
        with open("informe.txt", "w") as f:
            f.write(informe) 
