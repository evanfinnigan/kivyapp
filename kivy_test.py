from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation="vertical")
        self.content = BoxLayout(orientation="vertical")
        self.bottom_nav = BoxLayout()
        self.button1 = Button(text = "S1" , font_size='16sp')
        self.button1.on_press = self.toScreen1
        self.button2 = Button(text = "S2" , font_size='16sp')
        self.button2.on_press = self.toScreen2
        self.button3 = Button(text = "S3" , font_size='16sp')
        self.button3.on_press = self.toScreen3
        self.bottom_nav.add_widget(self.button1)
        self.bottom_nav.add_widget(self.button2)
        self.bottom_nav.add_widget(self.button3)
        self.main_layout.add_widget(self.content)
        self.main_layout.add_widget(self.bottom_nav)
        self.add_widget(self.main_layout)

    def toScreen1(self):
        self.manager.current = 'Screen 1'

    def toScreen2(self):
        self.manager.current = 'Screen 2'

    def toScreen3(self):
        self.manager.current = 'Screen 3'



class Screen1(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content.add_widget(Label(text="Screen 1"))



class Screen2(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content.add_widget(Label(text="Screen 2"))
        self.content.add_widget(Button(text="Some button", font_size='16sp'))
        
class Screen3(BaseScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content.add_widget(Label(text="Screen 3"))
        for i in range(5):
            self.content.add_widget(Label(text="blah blah blah"))


class MyApp(App):

    def on_click(self):
        print("clicked")
    
    def build(self):
        sm = ScreenManager()
        screen1 = Screen1(name="Screen 1")
        screen2 = Screen2(name="Screen 2")
        screen3 = Screen1(name="Screen 3")
        sm.add_widget(screen1)
        sm.add_widget(screen2)
        sm.add_widget(screen3)
        sm.current = "Screen 1"
        return sm

app = MyApp()
app.run()