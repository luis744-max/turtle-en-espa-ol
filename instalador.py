import os
import shutil
import glob

# Usuario actual detectado automáticamente
usuario = os.getlogin()

# Rutas posibles del escritorio
desktop_local = fr"C:\Users\{usuario}\Desktop\timepython.py"
desktop_onedrive = fr"C:\Users\{usuario}\OneDrive\Desktop\timepython.py"

# Determinar cuál existe
if os.path.isfile(desktop_local):
    origen = desktop_local
elif os.path.isfile(desktop_onedrive):
    origen = desktop_onedrive
else:
    print("ERROR: No se encontró timepython.py ni en Desktop ni en OneDrive/Desktop.")
    print("Prueba dejar el archivo en alguna de estas rutas:")
    print(desktop_local)
    print(desktop_onedrive)
    exit()

print(f"Archivo encontrado en: {origen}")

# Buscar carpetas Lib de cualquier usuario + cualquier Python (universal)
rutas = glob.glob(r"C:\Users\*\AppData\Local\Programs\Python\Python*\Lib")

if not rutas:
    print("ERROR: No se encontró ninguna carpeta Lib en ninguna versión de Python.")
    exit()

print("\nCarpetas Lib encontradas:")
for r in rutas:
    print(" -", r)

# Copiar a cada carpeta Lib encontrada
for ruta in rutas:
    try:
        shutil.copy(origen, ruta)
        print("Copiado en:", ruta)
    except Exception as e:
        print("ERROR copiando en", ruta, ":", e)

print("\n--- PROCESO COMPLETADO ---")
