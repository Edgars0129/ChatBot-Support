from config.settings import DIAGNOSTIC_QUESTIONS

def get_diagnostic_questions(problem_type):
    """Retorna preguntas diagnósticas según el tipo de problema"""
    return DIAGNOSTIC_QUESTIONS.get(problem_type, [])

def analyze_problem(description):
    """Analiza la descripción del problema para categorízarlo"""
    description = description.lower()
    if any(word in description for word in ['internet', 'wifi', 'red', 'conexión']):
        return 'internet'
    elif any(word in description for word in ['lento', 'lenta', 'rendimiento', 'velocidad']):
        return 'performance'
    return 'general'