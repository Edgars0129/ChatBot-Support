import anthropic
from config.settings import API_KEY, SYSTEM_PROMPT
from .diagnostics import analyze_problem, get_diagnostic_questions
from .ticket_system import TicketSystem

class SupportChatbot:
    def __init__(self):
        self.client = anthropic.Client(api_key=API_KEY)  # Cambia api_key=API_KEY
        self.ticket_system = TicketSystem()
        self.conversation_history = []

    def get_response(self, user_input):
        """Obtiene respuesta del modelo de Claude"""
        try:
            # Analizar el problema
            problem_type = analyze_problem(user_input)
            questions = get_diagnostic_questions(problem_type)

            # Preparar el mensaje para Claude
            message = f"{SYSTEM_PROMPT}\n\nProblema del usuario: {user_input}"
            if questions:
                message += "\n\nPreguntas de diagnóstico sugeridas:\n" + "\n".join(questions)

            # Obtener respuesta de Claude
            response = self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0.7,
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )

            return response.content[0].text
        except Exception as e:
            return f"Error en el sistema: {str(e)}"

    def create_support_ticket(self, description):
        """Crea un ticket de soporte"""
        return self.ticket_system.create_ticket(description)