# -*- coding: utf-8 -*

'''
ソースは以下からコピーしました
github:https://github.com/diegodukao/calkvlator
説明スライド:https://speakerdeck.com/diegodukao/kivy-introducao-a-kv-lang
'''

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.core.window import Window
from kivy.properties import BooleanProperty
from kivy.utils import get_color_from_hex

from kivy.resources import resource_add_path


# 起動後"F1キー"を押すとデバック機能が開く
# ウィンドウサイズの初期設定(x,y)
Window.size = (450, 600)

# デフォルトに使用するフォントを変更する
resource_add_path('fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する


# フォントを直接指定する
#LabelBase.register(name='Roboto',
#                   fn_regular='./fonts/Roboto-Thin.ttf', # レギュラーの文字はM+で日本語表示する
#                   fn_bold='./fonts/Roboto-Medium.ttf')




class Calculator(App): 
    '''
    実際にボタンを押されたときの挙動を動かします
     .kvファイルは (クラス名).kv　とすると1対1対応で読み込まれます

    KV Languageはもう一つ、ファイルの中に記載して実行するやり方があります。
    
   <やり方>
    root = Builder.load_string(’’’(半角にする)
    FloatLayout:
         Color:
            rgba: 0, 1, 0, 1

    ’’’(半角にする))

    class MainApp(App):
        def build(self):
            return root

    '''

    clear_bool = BooleanProperty(False)

    def print_number(self, number):
        '''入力された値が入る'''
        if self.clear_bool:
            self.clear_display()

        text = "{}{}".format(self.root.display.text, number) # 今までの入力された文字列と入力された値が表示される
        self.root.display.text = text

        print("数字「{0}」が押されました".format(number))

    def print_operator(self, operator):
        if self.clear_bool:
            self.clear_bool = False

        text = "{} {} ".format(self.root.display.text, operator)
        self.root.display.text = text

        print("演算子「{0}」が押されました".format(operator))

    def clear_display(self):
        self.root.display.text = ""
        self.clear_bool = False

        print("「c」が押されました")
    def del_char(self):
        ''' "<x"を押された場合の計算結果を表示  '''

        self.root.display.text = self.root.display.text[:-1]

        print("「<x」が押されました")

    def calculate(self):
        ''' "="を押された場合の計算結果を表示  '''
        try:
            self.root.display.text = str(eval(self.root.display.text)) # 単一の式を評価  例：eval("5 + 10")　は15になる
            self.clear_bool = True

            print('計算完了')
        except:
            # 数字を入力せずに　'=’を押した場合などのエラー対策
            print('error　入力ミス')


if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#FFFFFF')
    Calculator().run()