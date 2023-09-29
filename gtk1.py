import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        super().__init__(application=app)
        # Add code

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="")
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(app)
        self.win.present()

app = MyApp()
app.run(sys.argv)


