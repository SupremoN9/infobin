import requests
from colorama import Fore, Style

# URL base de la API
url_base = "https://lookup.binlist.net/"

# Función que toma el número de BIN como argumento y devuelve la información correspondiente
def obtener_info_bin(bin_num):
    # Concatenar el número de BIN con la URL base de la API
    url = url_base + bin_num

    # Establecer los headers para indicar que se espera una respuesta en formato JSON
    headers = {
        "Accept-Version": "3",
        "Accept": "application/json"
    }

    # Hacer la petición GET a la API
    response = requests.get(url, headers=headers)

    # Si la respuesta fue exitosa, extraer la información necesaria del JSON
    if response.status_code == 200:
        data = response.json()
        return {
            "Banco emisor": data["bank"]["name"] if "bank" in data else "Desconocido",
            "País": data["country"]["name"] if "country" in data else "Desconocido",
            "Tipo de tarjeta": data["type"] if "type" in data else "Desconocido",
            "Categoría de tarjeta": data["scheme"] if "scheme" in data else "Desconocido",
            "Moneda": data["country"]["currency"] if "country" in data and "currency" in data["country"] else "Desconocido",
            "Estado de la tarjeta": "Válido" if response.status_code == 200 else "Inválido"
        }
    else:
        # Si la respuesta no fue exitosa, devolver un diccionario vacío
        return {}

# Print inicial con información del creador y las redes sociales
print(Fore.GREEN + Style.BRIGHT + """
==================================================
|              Verificador de BINs                |
|                                                 |
|              Creado por: SupremoN9              |
|                                                 |
| Instagram: https://www.instagram.com/supremon9  |
|                                                 |
==================================================
""" + Style.RESET_ALL)

# Solicitar al usuario el número de BIN
bin_num = input("Ingresa los primeros 6 dígitos de tu tarjeta (BIN): ")

# Obtener la información del BIN y mostrarla en pantalla
info_bin = obtener_info_bin(bin_num)
if info_bin:
    print("\n" + Fore.YELLOW + Style.BRIGHT + "La información del BIN es la siguiente:\n" + Style.RESET_ALL)
    for key, value in info_bin.items():
        print(f"{key}: {Fore.BLUE + Style.BRIGHT}{value}{Style.RESET_ALL}")
else:
    print("\n" + Fore.RED + Style.BRIGHT + "No se pudo obtener la información del BIN. Verifica que el número sea correcto." + Style.RESET_ALL)
