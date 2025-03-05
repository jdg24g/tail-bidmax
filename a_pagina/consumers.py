from channels.generic.websocket import WebsocketConsumer

class TicketConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        print(f"El usuario: {user} esta conectado")
        self.accept()

    def disconnect(self, close_code):
        user = self.scope['user']
        print(f"El usuario {user} se desconecto codigo de error {close_code}")
        pass
    