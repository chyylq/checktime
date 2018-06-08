from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from mapdetial import *

    
class SearchScreen(GridLayout):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text="Look for"))
        self.loc_name = TextInput(multiline=False)
        self.add_widget(self.loc_name)
        
        self.add_widget(Label(text="What type"))
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
        location = self.location.text
        loc_nm = self.loc_name.text
        loc_types = (self.loc_type.text).split(' ')
        dist = float(self.dist.text)*1609.34
        loc = get_loc(location, api_key)                
        nearby_place_ids = get_nearby(loc['coordinates']['lat'], loc['coordinates']['lng'], dist, loc_nm, loc_types, api_key)
        #print(nearby_place_ids)
        for i, place_id in enumerate(nearby_place_ids):
            print (i)            
            print(get_current_popular_times(api_key, place_id))                
        
        
class SimpleKivy(App):
    def build(self):
        return SearchScreen()

if __name__ == "__main__":
    SimpleKivy().run()        