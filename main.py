from kivy.app import App
from kivy.uix.label import Label

class NexusBetApp(App):
    def build(self):
        return Label(text='NexusBet - Análise de Apostas')

if __name__ == '__main__':
    NexusBetApp().run()
