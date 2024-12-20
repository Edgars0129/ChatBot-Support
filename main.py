from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.style import Style
from rich.text import Text
from src.chatbot import SupportChatbot
import time

console = Console()


def show_typing_indicator():
    """Muestra un indicador de 'escribiendo...'"""
    with console.status("[bold green]Pensando...") as status:
        time.sleep(1.5)


def print_welcome():
    """Muestra el mensaje de bienvenida"""
    console.print(Panel(
        "[bold cyan]¡Bienvenido al Sistema de Soporte Técnico![/]\n\n"
        "[green]👨‍💻 Estoy aquí para ayudarte con tus problemas técnicos[/]\n"
        "[yellow]📝 Describe tu problema y te ayudaré a resolverlo[/]\n"
        "[red]❌ Escribe 'salir' para terminar la conversación[/]",
        title="Soporte Técnico",
        border_style="blue"
    ))


def print_user_message(message):
    """Formatea y muestra el mensaje del usuario"""
    console.print(Panel(
        message,
        title="👤 Tú",
        style="green",
        border_style="green"
    ))


def print_bot_message(message):
    """Formatea y muestra la respuesta del bot"""
    show_typing_indicator()
    console.print(Panel(
        message,
        title="🤖 Soporte Técnico",
        style="cyan",
        border_style="blue"
    ))


def print_goodbye():
    """Muestra el mensaje de despedida"""
    console.print(Panel(
        "[bold cyan]¡Gracias por usar nuestro servicio de soporte técnico![/]\n"
        "[green]¡Que tengas un excelente día![/]",
        title="👋 Hasta luego",
        border_style="blue"
    ))


def main():
    console.clear()
    print_welcome()
    chatbot = SupportChatbot()

    while True:
        user_input = console.input("\n[bold green]📝 Escribe tu mensaje:[/] ")

        if user_input.lower() == 'salir':
            print_goodbye()
            break

        print_user_message(user_input)
        response = chatbot.get_response(user_input)
        print_bot_message(response)


if __name__ == "__main__":
    main()