import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)

        # Tamaño y título de la ventana
        self.set_default_size(600, 250)
        self.set_title("Título")

        # Caja céntrica
        center_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        center_box.set_halign(Gtk.Align.CENTER)

        # Botón
        button = Gtk.Button(label="Botón")
        button.set_size_request(100, 40)

        # Conectar el click del botón a una función
        button.connect('clicked', self.hello)

        # Agregar el botón a la caja
        center_box.append(button)

        # Agregar la caja a la ventana
        self.set_child(center_box)

        # Nueva caja con otras cajas dentro
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        center_box.append(self.box2)
        self.box2.append(self.box3)
        self.box2.append(self.box4)

        # Botón de check
        self.check = Gtk.CheckButton(label="Prueba a marcarme y a desmarcarme")
        self.box3.append(self.check)

    def hello(self, button):
        if self.check.get_active():
            print("La casilla está marcada")
        else: 
            print("La casilla no está marcada")

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="")
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(app)
        self.win.present()

app = MyApp()
app.run(sys.argv)