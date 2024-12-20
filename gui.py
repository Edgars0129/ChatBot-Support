import tkinter as tk
from tkinter import ttk, scrolledtext
from src.chatbot import SupportChatbot
import threading


class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Soporte Técnico")
        self.root.geometry("800x600")

        # Configurar tema
        self.root.configure(bg='#f0f0f0')
        self.style = ttk.Style()
        self.style.configure('Main.TFrame', background='#f0f0f0')

        # Inicializar chatbot
        self.chatbot = SupportChatbot()

        # Crear interfaz
        self.create_gui_elements()
        self.setup_bindings()

    def create_gui_elements(self):
        # Marco principal
        self.main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Área de chat
        self.chat_display = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            font=("Segoe UI", 10),
            bg='white',
            height=30
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Marco para entrada y botón
        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(fill=tk.X, pady=5)

        # Campo de entrada
        self.input_field = ttk.Entry(
            input_frame,
            font=("Segoe UI", 10)
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        # Botón enviar
        self.send_button = ttk.Button(
            input_frame,
            text="Enviar",
            command=self.send_message
        )
        self.send_button.pack(side=tk.RIGHT)

        # Mostrar mensaje de bienvenida
        self.display_message(
            "Sistema de Soporte Técnico: ¡Bienvenido! ¿En qué puedo ayudarte hoy?\n",
            "sistema"
        )

    def setup_bindings(self):
        self.input_field.bind("<Return>", lambda e: self.send_message())
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def send_message(self):
        message = self.input_field.get().strip()
        if message:
            # Limpiar campo de entrada
            self.input_field.delete(0, tk.END)

            # Mostrar mensaje del usuario
            self.display_message(f"Tú: {message}\n", "usuario")

            # Obtener respuesta en un hilo separado
            threading.Thread(
                target=self.get_bot_response,
                args=(message,),
                daemon=True
            ).start()

    def get_bot_response(self, message):
        # Obtener respuesta del chatbot
        response = self.chatbot.get_response(message)

        # Mostrar respuesta en la interfaz
        self.display_message(f"Soporte Técnico: {response}\n", "bot")

    def display_message(self, message, sender):
        self.chat_display.configure(state='normal')

        # Configurar colores según el remitente
        if sender == "usuario":
            self.chat_display.tag_config("user_tag", foreground="green")
            self.chat_display.insert(tk.END, message, "user_tag")
        elif sender == "bot":
            self.chat_display.tag_config("bot_tag", foreground="blue")
            self.chat_display.insert(tk.END, message, "bot_tag")
        else:
            self.chat_display.tag_config("system_tag", foreground="purple")
            self.chat_display.insert(tk.END, message, "system_tag")

        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)

    def on_closing(self):
        self.root.destroy()


def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()