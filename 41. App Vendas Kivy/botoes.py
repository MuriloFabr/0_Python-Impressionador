from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior


class ImagemButton(ButtonBehavior, Image):
    pass

class LabelButton(ButtonBehavior, Label):
    pass