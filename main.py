# foundational code
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import kivy
kivy.require('1.9.1')

#class Calculator
class MyInterface(BoxLayout):
    def __init__(self):
        super(MyInterface, self).__init__()

    def calc_value(self, value):
        self.calc_field.text += value

    def calc_clear(self):
        self.calc_field.text = ""

    def calc_result(self):
        try:
            self.calc_field.text = str(eval(self.calc_field.text))
        except:
            self.calc_field.text = "error"

class Calculator(App):
    def build(self):
        return MyInterface()

calculator = Calculator()
calculator.run()