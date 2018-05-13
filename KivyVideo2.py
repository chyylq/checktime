from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


    
class SearchScreen(GridLayout):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text="Looking for"))
        self.loc_type = TextInput(multiline=False)
        self.add_widget(self.loc_type)
        
        self.add_widget(Label(text="Location:"))
        self.location = TextInput(multiline=False)
        self.add_widget(self.location)

        self.add_widget(Label(text="Miles:"))
        self.dist = TextInput(multiline=False)
        self.add_widget(self.dist)
        
        btn = Button(text="Search")
        btn.bind(on_press=self.callback)
        self.add_widget(btn)
        
    def callback(self, instance):
        print(instance.text)
        loc_type = int(self.loc_type.text)
        location = self.location.text
        dist = int(self.dist.text)
        
        
class SimpleKivy(App):
    def build(self):
        return SearchScreen()

if __name__ == "__main__":
    SimpleKivy().run()        