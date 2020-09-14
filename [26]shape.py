Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> a=turtle.Pen()
>>> a.shape("turtle")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a.shape("turtle")
  File "C:\Program Files\Python37\lib\turtle.py", line 2778, in shape
    self._update()
  File "C:\Program Files\Python37\lib\turtle.py", line 2660, in _update
    self._update_data()
  File "C:\Program Files\Python37\lib\turtle.py", line 2646, in _update_data
    self.screen._incrementudc()
  File "C:\Program Files\Python37\lib\turtle.py", line 1292, in _incrementudc
    raise Terminator
turtle.Terminator
>>> a.fordword(100)