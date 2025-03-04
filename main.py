import re

def limpiar_chat(archivo):
    """Lee un archivo de WhatsApp y extrae los mensajes con los remitentes.
       Retorna una lista de tuplas (remitente, mensaje)."""
    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    mensajes_limpios = []
    
    # Expresión regular para extraer remitente y mensaje
    patron_mensaje = regex = r"^(\d{1,2}/\d{1,2}/\d{2,4}),\s+(\d{1,2}:\d{2}\s*(?:a\.?\s*m\.?|p\.?\s*m\.?))\s*-\s*(.+?):\s(.+)$"
    
    for linea in lineas:
        match = re.match(patron_mensaje, linea)
        if match:
            remitente = match.group(3)  # Nombre del remitente
            mensaje = match.group(4).strip()  # Mensaje limpio
            mensajes_limpios.append((remitente, mensaje))

    return mensajes_limpios

# Prueba con un archivo "chat.txt"
mensajes = limpiar_chat("chat.txt")

# Muestra los primeros mensajes procesados
for remitente, msg in mensajes[:5]:
    print(f"{remitente}: {msg}")





