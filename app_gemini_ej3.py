import os
import google.genai as genai
from dotenv import load_dotenv
from google.genai import types

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
client = genai.Client(api_key=clave_api)

# Configuración con system_instruction
configuration = types.GenerateContentConfig( 
    max_output_tokens=1012,
    system_instruction="""Eres un vendedor amable de una tienda de tecnología. Responde con especificaciones claras y útiles, siempre manteniendo un tono cordial y profesional. Sigue el formato de los ejemplos: Usuario: '¿Qué características tiene el portátil Lenovo ThinkPad X1 Carbon?'
Vendedor: 'El Lenovo ThinkPad X1 Carbon cuenta con pantalla de 14'' Full HD, procesador Intel Core i7, 16 GB de RAM y 512 GB SSD. Es ligero y muy resistente.'

Usuario: '¿Qué especificaciones tiene el iPhone 15 Pro?'
Vendedor: 'El iPhone 15 Pro incluye pantalla OLED de 6.1'', chip A17 Pro, cámara triple de 48 MP, y cuerpo de titanio.'

Usuario: '¿Qué opciones de televisores tienen disponibles?'
Vendedor: 'Tenemos televisores Samsung y LG con pantallas entre 50'' y 75'', resolución 4K UHD, HDR10+, y sistemas operativos inteligentes como Tizen y webOS.'

Usuario: '¿Qué beneficios ofrece la tablet Samsung Galaxy Tab S9?'
Vendedor: 'La Galaxy Tab S9 ofrece pantalla AMOLED de 11'', procesador Snapdragon 8 Gen 2, 8 GB de RAM, 256 GB de almacenamiento y compatibilidad con S Pen.'
""" )




def chat_soporte():
    try:
        # Inicialización del chat
        chat = client.chats.create(
            model="gemini-3-flash-preview",
            config=configuration,
            
        )

        print("--- Bienvenido al Chat de Soporte de la Tienda de Tecnología ---")
        print("(Escribe 'finalizar' para terminar)\n")

        while True:
            user_input = input("Cliente: ")

            if user_input.lower() in ["salir", "exit", "quit", "finalizar"]:
                print("Vendedor: Gracias por visitar nuestra tienda! Que tengas un excelente día.")
                break

            try:
                # 3. Envío del mensaje
                response =chat.send_message(user_input)

                # En el nuevo SDK, el acceso al texto es response.text
                print(f"\nAsistente: {response.text}\n")
            except Exception as e:
                # Es recomendable implementar reintentos con backoff exponencial en producción
                print(f"Error al procesar la solicitud: {e}")

    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")



if __name__ == "__main__":
    chat_soporte()
   
