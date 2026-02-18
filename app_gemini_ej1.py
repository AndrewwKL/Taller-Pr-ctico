import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")

# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)

configuration = types.GenerateContentConfig(
    max_output_tokens=100,  # límite bajo para asegurar respuestas cortas
    system_instruction="""Eres un asistente especializado en Inteligencia Artificial.
Responde de manera concisa y educativa.
No incluyas texto adicional fuera de la explicación."""
)

def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...")
    try:
        # 3. Llamada directa al servicio de modelos
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Explica qué es la 'Inferencia en IA' en menos de 50 palabras."
        )
        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")

if __name__ == "__main__":
    ejecutar_consulta()
