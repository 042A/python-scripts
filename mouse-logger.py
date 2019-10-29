from pynput import mouse

class MyException(Exception):pass

NumberOfMouseClicks = 0

def on_click(x, y, button, pressed):
    global NumberOfMouseClicks
    print(x, y)
    print(button)
    NumberOfMouseClicks = NumberOfMouseClicks + 1
    if (NumberOfMouseClicks==10):
        raise MyException(button)

with mouse.Listener(on_click=on_click) as listener:
    try:
        listener.join()
    except MyException as e:
        pass