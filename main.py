import os
from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'resizable', 0)
Config.set('kivy', 'exit_on_escape', 0)
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang.builder import Builder
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner

Builder.load_string(open(os.path.join("config", "kvfile.kv"), encoding="utf-8").read(), rulesonly=True)


class Manager(ScreenManager):
    pass


class PopupWarning(Popup):
    # PopUp do Login
    pass

#order details to be fetched
#check <OrderWindow> in .kv file
class OrderWindow(Screen):
    def displayorder(self):
        self.ids.repairorder.text =''
        self.ids.sellorder.text=''


class Sellwindow(Screen):

    def price(self, values):
        global cost
        global phone
        cost = 1000
        phone = self.ids.brand.text
        if phone == 'OnePlus':
            cost= cost +1000
        elif phone =='Apple':
            cost = cost + 3000
        elif phone =='Samsung':
            cost = cost + 2000
        else:
            cost = cost +0

        global damage
        damage = self.ids.damage.text

        if damage =='Flawless':
            cost = cost + 4000
        elif damage=='Dents':
            cost = cost + 3000
        elif damage=='Not Working':
            cost = cost + 2000
        else:
            cost = cost + 0
        print(damage)

        global age
        age = self.ids.years.text

        if age=='1':
            cost = cost + 3000
        elif age=='3':
            cost = cost + 2000
        elif age=='5':
            cost = cost + 1000
        else:
            cost = cost + 0
        print(age)

        global warrant
        warrant = self.ids.warrant.text
        if warrant== 'Yes':
            cost = cost + 3000
        elif warrant =='No':
            cost = cost + 1000
        else:
            cost = cost + 0
        print(warrant)


    def pickup(self, values):
        global day
        day = self.ids.day.text

        print(day)
        global month
        month = self.ids.month.text
        print(month)

    def display(self):

        self.ids.brandchoosen.text = phone
        self.ids.damagedone.text = damage
        self.ids.yearsold.text = age
        self.ids.warranty.text = warrant
        self.ids.date.text = day+' '+month
        self.ids.resale.text = 'Rs.'+str(cost)

        pass

class RepairWindow(Screen):
    def price(self, values):
        global cost
        global phone
        cost = 1000
        phone = self.ids.brand.text
        if phone == 'OnePlus':
            cost= cost +1000
        elif phone =='Apple':
            cost = cost + 3000
        elif phone =='Samsung':
            cost = cost + 2000
        else:
            cost = cost +0

        global damage
        damage = self.ids.damage.text

        if damage =='Battery':
            cost = cost + 4000
        elif damage=='Screen':
            cost = cost + 3000
        elif damage=='Body':
            cost = cost + 2000
        elif damage=='Camera':
            cost = cost + 1000
        else:
            cost = cost + 0
        print(damage)

        global age
        age = self.ids.years.text

        if age=='1':
            cost = cost + 3000
        elif age=='3':
            cost = cost + 2000
        elif age=='5':
            cost = cost + 1000
        else:
            cost = cost + 0
        print(age)

        global warrant
        warrant = self.ids.warrant.text
        if warrant== 'Yes':
            cost = cost + 3000
        elif warrant =='No':
            cost = cost + 1000
        else:
            cost = cost + 0
        print(warrant)


    def pickup(self, values):
        global day
        day = self.ids.day.text

        print(day)
        global month
        month = self.ids.month.text
        print(month)

    def display(self):

        self.ids.brandchoosen.text = phone
        self.ids.damagedone.text = damage
        self.ids.yearsold.text = age
        self.ids.warranty.text = warrant
        self.ids.date.text = day+' '+month
        self.ids.resale.text = 'Rs.'+str(cost)

        pass


class LoginScreen(Screen):
    def login_verification(self):
        if self.ids.email.text == '1234' and self.ids.passw.text == '1234':
            self.clean_inputs()  # Remove os texto digitados nos campos de Login e Senha
            self.ids.dica.text = ''  # Remove o texto que informa o login da conta
            App.get_running_app().root.current = 'mobifysell'

        else:
            self.incorrect_login()
            self.clean_inputs()

    def openaccountpage(self):
        App.get_running_app().root.current = 'accountpage'

    def clean_inputs(self):
        if self.ids.checkbox.active:
            self.ids.passw.text = ''
        else:
            self.ids.email.text = self.ids.passw.text = ''

    def incorrect_login(self):
        popup = PopupWarning()
        popup.open()


    def istab_pressed(self, text):
        if len(text) > 0 and text[-1] == '\t':
            self.ids.passw.text = text[:-1]


class AccountPage(Screen):
    def openloginpage(self):
        App.get_running_app().root.current = 'loginscreen'

    def openaccountpage(self):
        App.get_running_app().root.current = 'accountpage'

    def clean_inputs(self):
        if self.ids.checkbox.active:
            self.ids.passw.text = ''
        else:
            self.ids.email.text = self.ids.passw.text = ''

    def incorrect_login(self):
        popup = PopupWarning()
        popup.open()


    def istab_pressed(self, text):
        if len(text) > 0 and text[-1] == '\t':
            self.ids.passw.text = text[:-1]


class MobifySell(Screen):
    def on_leave(self, *args):
        self.ids.content.clear_widgets()

class MobifyRepair(Screen):
    def on_leave(self, *args):
        self.ids.content.clear_widgets()

class MobifyOrder(Screen):
    def on_leave(self, *args):
        self.ids.content.clear_widgets()


class NetflixHome(Screen):
    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.isupdate)
        self.ids.scroll_home.scroll_y = 1
        self.add_content()

    def on_leave(self, *args):
        self.ids.content.clear_widgets()

    def isupdate(self, window, key, *args):
        if key == 286:
            self.on_pre_enter()
            if App.get_running_app().root.current == 'resultpage':
                App.get_running_app().root.current = 'netflixmenu'

    def add_content(self):
        self.ids.content.clear_widgets()

        self.ids.content.add_widget(Banner())

        for folder in os.listdir('Content'):
            files = os.listdir(os.path.join('Content', folder))
            content = ContentList()
            content.create(folder, files)
            self.ids.content.add_widget(content)


class Banner(BoxLayout):
    pass


class SearchBox(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda *_: self.ids.searchbtn.bind(on_press=self.open_animation_search_box), 1)
        self.search_input = TextInput(multiline=False, hint_text='Search Phones', background_color=[0, 0, 0, .1],
                                      on_text_validate=self.search, foreground_color=[1, 1, 1, 1])

    def search(self, *args):
        if self.search_input.text != '':
            if App.get_running_app().root.current != 'resultpage':
                App.get_running_app().root.current = 'resultpage'

            App.get_running_app().root.get_screen('resultpage').pre_search(self.search_input.text.lower().strip())

        self.search_input.text = ''

    def open_animation_search_box(self, *args):

        self.btn = self.ids.searchbtn

        self.search_input.size_hint = [.02, .4]
        self.search_input.pos_hint = {'center_y': .5, 'center_x': .57}
        Clock.schedule_once(self.searchinput_focus, .3)

        anim_btn = Animation(size_hint=[.15, .45], duration=.01) + Animation(size_hint=[.08, .35], duration=.01) + \
                   Animation(pos_hint={'center_x': .1}, duration=.05)
        anim_txt = Animation(size_hint=[.8, .4], d=.15, t='in_sine')

        anim_btn.start(self.btn)
        self.add_widget(self.search_input)
        anim_txt.start(self.search_input)

        self.btn.unbind(on_press=self.open_animation_search_box)
        self.btn.bind(on_press=self.search)

        Clock.schedule_once(lambda *_: Clock.schedule_interval(self.isdefocused, 0), .4)

    def close_animation_search_box(self, *args):

        anim_btn = Animation(size_hint=[.15, .45], duration=.01) + Animation(size_hint=[.08, .35], duration=.01) + \
                   Animation(pos_hint={'center_x': .9}, duration=.1)

        self.remove_widget(self.search_input)  # Remove o TextInput
        anim_btn.start(self.btn)  # Inicia a animação

        self.btn.unbind(on_press=self.search)
        self.btn.bind(on_press=self.open_animation_search_box)

    def searchinput_focus(self, *args):
        self.search_input.focus = True

    def isdefocused(self, *args):
        if not self.search_input.focus:
            self.close_animation_search_box()
            Clock.unschedule(self.isdefocused)


class ContentList(BoxLayout):
    def create(self, foldername, images):
        self.padding = 0, 0, 0, 50
        self.ids.label.text = foldername
        self.ids.grid.cols = len(images)
        if len(images) > 0:
            # Adiciona as séries de acordo com as imagens dentro da categoria(pasta)
            for image in images:
                image_path = os.path.join('Content', foldername, image)
                image_content = ImageContent(image_path)
                self.ids.grid.add_widget(image_content)


class ImageContent(Button):
    def __init__(self, image_path, **kwargs):
        super().__init__(**kwargs)
        self.image_path = image_path
        self.size_hint = None, None
        self.size = 240, 151

        self.background_normal = self.background_down = self.image_path

    def on_press(self):
        print(self.image_path)


class ResultPage(Screen):
    def pre_search(self, text):
        if len(text) > 0:
            all_images = []
            for folder, subfolders, files in os.walk('Content'):
                for file in files:
                    if file[:-4] not in all_images:
                        all_images.append(file[:-4])

            self.search_files(text, all_images)

    def search_files(self, text, all_images):
        # Faz a pesquisa
        results = []
        for individual_word in text.split(' '):
            for image in all_images:
                if individual_word in image.lower():
                    results.append(image + '.jpg')

        folders = os.listdir('Content')
        paths = []
        for result in results:
            for folder in folders:
                folder_path = os.path.join('Content', folder)
                images = os.listdir(folder_path)
                if result in images:
                    img_index = images.index(result)
                    paths.append(os.path.join(folder_path, images[img_index]))
                    break

        self.add_content(text, paths)

    def add_content(self, text, paths=None):
        self.ids.stack.clear_widgets()
        self.ids.scroll_result.scroll_y = 1
        if len(paths) > 0:
            self.ids.searchtext.text = 'The results for ' + text.title()
            for path in paths:
                self.ids.stack.add_widget(ImageContent(path))
        else:
            self.ids.searchtext.text = ' No results found for ' + text.title()


class Mobify(App):
    app_icon = os.path.join('config', 'M.png')
    netflix_logo = os.path.join('config', 'logo.png')
    background_login = os.path.join('config', 'bg.jpg')
    dropmenu_icon = os.path.join('config', 'user.png')
    search_btn = os.path.join('config', 'search_btn.png')
    roundborder = os.path.join('config', 'roundborder.png')
    banner = os.path.join('config', 'banner_1.jpg')
    netflix_font = os.path.join('config', 'net_font.ttf')

    def build(self):
        self.icon = self.app_icon
        return Manager()


Mobify().run()
