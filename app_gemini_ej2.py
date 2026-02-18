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
    max_output_tokens=512,
    system_instruction="""Eres un Editor Editorial de prestigio.
Tu tarea es procesar textos largos según la instrucción recibida.
Si la tarea es 'resumir', debes devolver un resumen ejecutivo claro y conciso.
Si la tarea es 'profesionalizar', debes editar el texto para que suene formal y técnico.
Responde únicamente con el texto procesado, sin explicaciones adicionales."""
)

def procesar_articulo(texto, tarea):
    try:
        # Construimos el prompt según la tarea
        prompt = f"Tarea: {tarea}\n\nTexto:\n{texto}"

        # Enviamos la consulta al modelo
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=configuration,
            contents=prompt
        )

        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")
        
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")


# Ejemplo de uso
if __name__ == "__main__": 
    texto_usuario = input("📄 Ingresa el texto a procesar:\n") 
    tarea_usuario = input("\n⚙️ Ingresa la tarea (ej: resumir, profesionalizar, traducir al inglés, simplificar): ") 
    resultado = procesar_articulo(texto_usuario, tarea_usuario) 
   
