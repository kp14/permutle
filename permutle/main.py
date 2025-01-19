from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import itertools
import string

class MainApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.text_input = TextInput(hint_text='Enter text here')
        self.button = Button(text='Generate Permutations')
        self.button.bind(on_press=self.on_button_press)
        self.output_label = Label(text='Permutations will be shown here', valign='top', halign='left', text_size=(self.layout.width, None))
        
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.output_label)
        
        return self.layout
    
    def on_button_press(self, instance):
        input_text = self.text_input.text
        # Strip whitespace and punctuation
        cleaned_text = ''.join(char for char in input_text if char.isalnum())
        # Generate permutations
        permutations = [''.join(p) for p in itertools.permutations(cleaned_text)]
        self.output_label.text = '\n'.join(permutations)

if __name__ == '__main__':
    MainApp().run()
