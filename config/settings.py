import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la API
API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Configuración del chatbot
SYSTEM_PROMPT = """Eres un asistente de soporte técnico profesional y amigable. Tu rol es:
1. Identificar problemas técnicos de computadoras
2. Realizar diagnósticos mediante preguntas específicas
3. Proporcionar soluciones paso a paso
4. Crear tickets cuando sea necesario
5. Mantener un tono profesional pero accesible"""

# Configuración de diagnósticos
DIAGNOSTIC_QUESTIONS = {
    "internet": [
        "¿El problema es con WiFi o conexión por cable?",
        "¿Otros dispositivos tienen conexión a internet?",
        "¿Ha reiniciado el módem y router?",
        "¿Puede ver la red WiFi en la lista de redes disponibles?"
    ],
    "performance": [
        "¿Cuándo empezó a notar la lentitud?",
        "¿Ha instalado programas nuevos recientemente?",
        "¿Cuánto espacio libre tiene en el disco duro?",
        "¿Ha ejecutado el antivirus recientemente?"
    ]
}