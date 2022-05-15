#!/usr/bin/env python3

import json
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')

class GameView(BoxLayout):
    """docstring for GameView."""

    def __init__(self):
        super(GameView, self).__init__()
        self.from_json = None
        self.to_json = None

    def chooseFrom(self, lang):
        dict ={"Français":'fr', "English":'en', "Svenska":'sv'}
        fname = 'taxonomy_'+dict[lang]+'.json'
        str = ""
        with open(fname, 'r')as f:
            str = f.read()
        self.from_json=json.loads(str)
        return None

    def chooseTo(self, lang):
        dict ={"Français":'fr', "English":'en', "Svenska":'sv'}
        fname = 'taxonomy_'+dict[lang]+'.json'
        str = ""
        with open(fname, 'r')as f:
            str = f.read()
        self.to_json=json.loads(str)
        return None

    def main(self):
        speciesCode = ''
        for i in self.from_json:
            if i['comName'].lower() == self.name_input.text.lower():
                speciesCode = i['speciesCode']
        if speciesCode == '':
            self.translation.text = "The Input hasn't been found in the data base"
        comName=''
        for j in self.to_json:
            if j['speciesCode'] == speciesCode:
                comName = j['comName']
        if comName != "":
            self.translation.text = comName


class BirdTranslator(App):
    def build(self):
        return GameView()

# def load_json(lang):
#     fname = 'taxonomy_'+lang+'.json'
#     str = ""
#     with open(fname, 'r')as f:
#         str = f.read()
#     out_json=json.loads(str)
#     return out_json
#
# def main():
#     print('From:')
#     from_json= load_json(input())
#     print('To:')
#     to_json= load_json(input())
#     print('Name:')
#     name= input()
#     speciesCode = ''
#     for i in from_json:
#         if i['comName'].lower() == name.lower():
#             speciesCode = i['speciesCode']
#     for j in to_json:
#         if j['speciesCode'] == speciesCode:
#             print(j['comName'])


if __name__ == '__main__':
    app=BirdTranslator()
    app.run()
    # main()
