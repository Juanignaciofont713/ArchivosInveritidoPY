from collections import defaultdict
import string

# Función para preprocesar el texto (eliminar puntuación y convertir a minúsculas)
def preprocesar_texto(texto):
    # Eliminamos puntuación
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    # Convertimos a minúsculas
    return texto.lower()

# Función para crear un archivo invertido
def crear_archivo_invertido(documentos):
    archivo_invertido = defaultdict(list)
    
    for doc_id, texto in documentos.items():
        palabras = preprocesar_texto(texto).split()
        
        for palabra in palabras:
            if doc_id not in archivo_invertido[palabra]:
                archivo_invertido[palabra].append(doc_id)
    
    return archivo_invertido

# Función para buscar en el archivo invertido
def buscar(archivo_invertido, palabra):
    palabra = preprocesar_texto(palabra)
    return archivo_invertido.get(palabra, [])

# Conjunto de documentos de ejemplo (doc_id: texto)
documentos = {
    1: "El gato negro corre rapido",
    2: "El perro duerme todo el dia",
    3: "El gato y el perro son amigos",
    4: "El día es soleado y cálido"
}

# Crear archivo invertido
archivo_invertido = crear_archivo_invertido(documentos)

# Mostrar archivo invertido
print("Archivo Invertido:")
for palabra, doc_ids in archivo_invertido.items():
    print(f"{palabra}: {doc_ids}")

# Búsqueda de ejemplo
palabra_a_buscar = "gato"
resultados = buscar(archivo_invertido, palabra_a_buscar)
print(f"\nDocumentos que contienen la palabra '{palabra_a_buscar}': {resultados}")