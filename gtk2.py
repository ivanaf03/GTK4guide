import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)

        #Tamaño y título de la ventana
        self.set_default_size(600, 250)
        self.set_title("Título")

        # Caja céntrica
        center_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        center_box.set_halign(Gtk.Align.CENTER)

        # Botón
        button = Gtk.Button(label="Botón")
        button.set_size_request(100, 40)

        # Conectar el click del botóna  una función
        button.connect('clicked', self.hello)

        # Agregar el botón a la caja
        center_box.append(button)

        # Agregar la caja a la ventana
        self.set_child(center_box)

    def hello(self, button):
        print("Hello world")

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="")
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(app)
        self.win.present()

app = MyApp()
app.run(sys.argv)

