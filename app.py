from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton
from kivy.lang import Builder
import idee_repas
from functools import partial

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

import sqlite3
import pymysql

# database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", database="recettes")

cursor = connection.cursor()
# some other statements  with the help of cursor

class Demo(App):
    buttons = {"1": {"Name": "Pour un repas", "Action": idee_repas.fct(2,cursor)},
               "2": {"Name": "Pour la journée", "Action": idee_repas.fct(2,cursor) +idee_repas.fct(2,cursor)},
               "3": {"Name": "Pour la semaine", "Action": idee_repas.fct(2,cursor)+idee_repas.fct(2,cursor)+idee_repas.fct(2,cursor)+idee_repas.fct(2,cursor)+idee_repas.fct(2,cursor)+idee_repas.fct(2,cursor)+idee_repas.fct(2,cursor)}
               }

    def build(self):
        layout = BoxLayout(padding=10, spacing=10)
        for key, value in self.buttons.items():
            layout.add_widget(Button(text=value["Name"], on_press=partial(print, value["Action"])))

        return layout
        

Demo().run()

