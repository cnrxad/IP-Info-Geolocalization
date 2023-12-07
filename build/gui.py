# cnrxad puto amo

import requests
import tkinter as tk
import os

# Función para geolocalizar la dirección IP
def get_ip_details():
    ip_address = ip_entry.get()
    access_token = "5d24aff3325639"  # Reemplazar con tu propio token

    url = f"https://ipinfo.io/{ip_address}?token={access_token}"
    response = requests.get(url)
    data = response.json()

    if 'city' in data:
        result_text = f"IP: {data['ip']}\nciudad: {data['city']}\nregión: {data['region']}\npaís: {data['country']}\ncódigo Postal: {data['postal']}\ncoordenadas: {data['loc']}"
        result_label.config(text=result_text, fg="#1E90FF")
        submit_button.pack_forget()  # Ocultar el botón de consulta
        download_button.pack(pady=10, side="bottom")  # Mostrar el botón de descarga
        return result_text
    else:
        result_label.config(text="no se encontraron detalles para la dirección IP proporcionada", fg="#ef6666")

# Función para guardar los datos en un archivo .txt
def save_data():
    result_text = get_ip_details()
    if result_text:
        file_name = f"IP_{ip_entry.get()}.txt"
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(download_folder, file_name)

        with open(file_path, "w") as file:
            file.write(result_text)

        result_label.config(text=f"datos guardados en {file_path}", fg="#85B865")

# Crear ventana de Tkinter | 5d24aff3325639
window = tk.Tk()
window.title("cnrxad | geolocalizador de IP")

# Obtener las dimensiones de la pantalla
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calcular la posición para centrar la ventana
x = (screen_width - 800) // 2  # La ventana tiene un ancho de 800
y = (screen_height - 450) // 2  # La ventana tiene una altura de 450

# Establecer la geometría de la ventana para que se posicione en el centro de la pantalla
window.geometry("800x450+{}+{}".format(x, y))
window.resizable(0, 0)


# Crear widgets
title_label = tk.Label(window, text="ingresa la dirección IP:", font=("Arial", 14), wraplength=780)
ip_entry = tk.Entry(window, font=("Arial", 12), width=50)
submit_button = tk.Button(window, text="consultar", command=get_ip_details, font=("Arial", 12))
result_label = tk.Label(window, text="", font=("Arial", 12), justify="left", wraplength=780)
download_button = tk.Button(window, text="descargar datos", command=save_data, font=("Arial", 12))

# Colocar widgets en la ventana
title_label.pack(pady=10)
ip_entry.pack(pady=5)
submit_button.pack(pady=10)
result_label.pack(pady=5)

# Ejecutar la ventana
window.mainloop()
