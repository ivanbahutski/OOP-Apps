import wikipedia
import requests
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("frontend.kv")


class FirstScreen(Screen):
    def get_image_link(self):
        user_input = self.manager.current_screen.ids.word.text
        # Set wikipedia page and first image link
        page = wikipedia.page(user_input)
        link = page.images[0]  # Is image link
        return link

    def download_image(self):
        # Download the image
        response = requests.get(self.get_image_link())
        image_path = "files/image.jpg"
        with open(image_path, "wb") as file:
            file.write(response.content)
        return image_path

    def set_image(self):
        # Set the image in the Image widget
        self.manager.current_screen.ids.image.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
