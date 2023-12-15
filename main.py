
import datetime
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.utils.set_bars_colors import set_bars_colors
from kivymd.uix.tab import MDTabsBase
from kivy.animation import Animation

#https://scikit-maad.github.io/generated/maad.features.bioacoustics_index.html
#https://librosa.org/doc/latest/generated/librosa.feature.zero_crossing_rate.html
from kaki.app import App
import os

Window.size = (335,650)


class Bas(MDFloatLayout, MDTabsBase):
    pass

class Item(MDFloatLayout):
    pass

class Manager(ScreenManager):
    pass

class ThematisationApp(MDApp):
    a = 1
    nombre = 0
    anim_play = True
    def __init_(self, **kwargs):
        super().__init__(**kwargs)
        #Clock.schedule_interval(self.callback, 0.5)




    def callback(value, key, *largs):
        print("salut")


    def build(self):
        self.title = "Naudio"
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.set_bars_colors()
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("presentation.kv"))
        screen_manager.add_widget(Builder.load_file("parametre.kv"))
        screen_manager.add_widget(Builder.load_file("audio.kv"))
        return screen_manager

    def theme(self):
        self.theme_cls.primary_palette = (
            "Blue" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def on_start(self):
        Clock.schedule_once(self.login, 5)
        #Clock.schedule_interval(self.callback, 0.1)
        #self.defilement()
        self.screen_musique=screen_manager.get_screen("audio").screen_mic.idscreen_musique
        self.screen_music= screen_manager.get_screen("audio").screen_mic.idscreen_musique1
        self.screen_musique.height = dp(5)
        self.screen_musique.clear_widgets()


        for i in range(18):

            screen_manager.get_screen("audio").audio_item.children[0].item.add_widget(Item())


    def callback(self, dt):

        print(f'In callback{self.nombre}')
        self.nombre+=1


    def defilement(self,w,h):
        self.w = w

        self.screen_rail = screen_manager.get_screen("audio").screen_audio.rail
        #self.defile()
        Clock.schedule_interval(self.defile, .08)
        #while True:


    def defile(self, dt):
        #print(dt)
        if self.anim_play:
            couleur = "#581286"
        else:
            couleur = "#888888"
        self.ecran = MDBoxLayout(
            id="ide",
            size_hint=(None, None),
            height=dp(50),
            width=dp(2),
            md_bg_color=couleur,
            pos=(self.w, 50)
        )
        screen_manager.get_screen("audio").screen_audio.rail.add_widget(self.ecran)
        self.deplace = Animation(pos=(-2, 50), duration=4)
        #self.deplace.repeat = True
        self.deplace.start(self.ecran)

        #self.deplace.on_complete(self.ecran)

        if self.ecran.x <= -5:
            screen_manager.get_screen("audio").screen_audio.rail.remove_widget(self.ecran)

        if self.ecran.pos == (self.w*2/3,50):
            self.ecran.md_bg_color = "blue"
            print("ok")

    def mnu(self,s):
        self.menu_items = [
            {
                "text": f"renommer ",
                "viewclass": "OneLineListItem",


            } ,
            {
                "text": "suiprimer",
                "viewclass": "OneLineListItem",

            }
        ]
        self.menu = MDDropdownMenu(
            caller=s,
            items=self.menu_items,
            width_mult=3,
            max_height=dp(100),

        )
        self.menu.open()
    def push(self,nom):
        screen_manager.current = nom
    def login(self,*args):
        screen_manager.current = "audio"
        #self.screen_musique.height= dp(80)
        #self.screen_musique.add_widget(self.screen_music)
    def set_bars_colors(self):
        set_bars_colors(
            self.theme_cls.primary_color,  # status bar color
            self.theme_cls.primary_color,  # navigation bar color
            "Light",  # icons color of status bar
        )
    def anim(self,w,x,stop):

        if w.center_x == x.center_x:
            self.anim_play = True
            deplace = Animation(pos_hint={"center_x":0.3,"center_y":.05},duration=.5)
            deplace1 = Animation(pos_hint={"center_x": 0.5, "center_y": .12}, duration=.5)
            deplace.start(w)

            deplace1.start(x)
        elif stop:
            x.icon = "play"
            deplace = Animation(pos_hint={"center_x": 0.5, "center_y": .15}, duration=.5)
            deplace1 = Animation(pos_hint={"center_x": 0.5, "center_y": .15}, duration=.5)
            deplace.start(w)
            deplace1.start(x)

            date = datetime.datetime.now()
            self.date_str = (str(date))

    def enregistrer(self):
        self.deplace.stop_all(self.ecran)
        self.anim_play = False
        #self.screen_rail.clear_widgets()
        #self.deplace.
        self.dialog= MDDialog(
            title="enregistrer",
            type="custom",
            content_cls=MDTextField(text=self.date_str),
            buttons=[
                MDFlatButton(text="anuler",
                             on_release= lambda x="parametre":self.dialog.dismiss()),
                MDFlatButton(text="enregistrer",
                             on_release= lambda x="parametre":self.dialog.dismiss()
                ),
            ],

        )
        self.dialog.open()




if __name__ =="__main__":
    ThematisationApp().run()

