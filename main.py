# ------------------- instal in terminal ----------------------
# py -m pip install cython
# py -m pip install pygame
# py -m pip install Pillow
# Poté nainstalujeme samotný Kivy framework:
#
# py -m pip install kivy



import kivy
kivy.require("1.10.1")
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# builder nacte ze souboru whatever.kv vsechno je lepsi pouzivat toto
from kivy.lang import Builder

Builder.load_file('whatever.kv')
# ///////////////////////////////////////////////////////////////


class MyGridLayout(Widget):
	name = ObjectProperty(None)
	pizza = ObjectProperty(None)
	color = ObjectProperty(None)


	def press(self):
		name = self.name.text
		pizza = self.pizza.text
		color = self.color.text

		#self.add_widget(text=f'Hello{name} your favorite pizza is {pizza} and color is {color}')
		print(f'Hello{name} your favorite pizza is {pizza} and color is {color}')
		# clear the input boxes

		self.name.text = ""
		self.pizza.text = ""
		self.color.text = ""

class AwesomeApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == "__main__":
	AwesomeApp().run()
