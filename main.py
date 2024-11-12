import json
import re


# Leer el contenido desde el archivo
raw_string = ''
SETTINGS_STR = ';SETTING_3'

with open('gcode/file_001.gcode', 'r') as file:
    gcode_lines = file.read().splitlines()
    for line in gcode_lines:
        if re.search(SETTINGS_STR, line):
            raw_string += line.replace(SETTINGS_STR, '').strip()

# Paso 1: Procesar el contenido para convertirlo en JSON válido
# Reemplaza saltos de línea y escapa caracteres especiales
processed_string = raw_string.replace("\n", "\\n").replace("\\", "\\\\").replace('"', '\\"')

# Paso 2: Asegura que las claves estén entre comillas dobles si no lo están
processed_string = processed_string.replace('\\"', '"')

# Paso 3: Intenta parsear el JSON
print(processed_string)
try:
    parsed_json = json.loads(processed_string)
    print(parsed_json)
except json.JSONDecodeError as e:
    print("Error al parsear JSON:", e)
