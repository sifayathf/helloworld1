#https://stackoverflow.com/questions/14706069/python-tkinter-with-a-simple-web-wrapper?noredirect=1&lq=1
#!/usr/bin/env python
import gtk
import webkit
import gobject

gobject.threads_init()
win = gtk.Window()
bro = webkit.WebView()
bro.open("http://www.google.com")
win.add(bro)
win.show_all()
gtk.main()