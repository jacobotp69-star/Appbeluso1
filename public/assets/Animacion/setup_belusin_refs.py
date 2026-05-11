import bpy
import os

# Ruta a la carpeta con las imágenes de Belusín
image_dir = r"F:\conrutas\AppBeluso\public\assets\Animacion"

# Limpiar la escena por defecto (opcional, elimina el cubo inicial)
bpy.ops.object.select_all(action='DESELECT')
if "Cube" in bpy.data.objects:
    bpy.data.objects['Cube'].select_set(True)
    bpy.ops.object.delete()

# Imágenes que queremos usar como referencia (puedes ajustar los nombres)
reference_images = {
    "Frontal": "belusin_wave.png",
    "Lateral_Derecho": "belusin_camina_derecha.gif",
    "Lateral_Izquierdo": "belusin_camina_izquierda.gif"
}

# Configuración inicial de posiciones y rotaciones para las referencias
positions = {
    "Frontal": (0, 5, 0),
    "Lateral_Derecho": (5, 0, 0),
    "Lateral_Izquierdo": (-5, 0, 0)
}

rotations = {
    "Frontal": (1.5708, 0, 0),          # Rotado 90 grados en X
    "Lateral_Derecho": (1.5708, 0, 1.5708), # Rotado 90 en X y 90 en Z
    "Lateral_Izquierdo": (1.5708, 0, -1.5708)
}

for name, filename in reference_images.items():
    img_path = os.path.join(image_dir, filename)
    
    if os.path.exists(img_path):
        # Cargar la imagen
        img = bpy.data.images.load(img_path)
        
        # Crear un objeto Empty tipo imagen
        bpy.ops.object.empty_add(type='IMAGE', location=positions[name], rotation=rotations[name])
        empty_obj = bpy.context.active_object
        empty_obj.name = f"Ref_{name}"
        
        # Asignar la imagen al Empty
        empty_obj.data.image = img
        empty_obj.color[3] = 0.5  # Transparencia al 50% para que sea más fácil modelar
        
        print(f"Cargada referencia {name}: {filename}")
    else:
        print(f"No se encontró la imagen: {img_path}")

print("¡Imágenes de referencia de Belusín cargadas con éxito!")
