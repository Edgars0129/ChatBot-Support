import time
import uuid

class TicketSystem:
    def __init__(self):
        self.tickets = {}

    def create_ticket(self, problem_description, priority='media'):
        """Crea un nuevo ticket de soporte"""
        ticket_id = f"TCK-{str(uuid.uuid4())[:8]}"
        ticket = {
            "id": ticket_id,
            "description": problem_description,
            "status": "creado",
            "priority": priority,
            "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tickets[ticket_id] = ticket
        return ticket

    def get_ticket(self, ticket_id):
        """Obtiene información de un ticket específico"""
        return self.tickets.get(ticket_id)