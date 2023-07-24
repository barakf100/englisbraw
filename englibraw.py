from pynput import keyboard
import pyperclip
import keyboard

def change(a):
    if a=='e':
        return 'ק'
    elif a == 'r':
        return 'ר'
    elif a == 't':
        return 'א'
    elif a == 'y':
        return 'ט'
    elif a == 'u':
        return 'ו'
    elif a == 'i':
        return 'ן'
    elif a == 'o':
        return 'ם'
    elif a == 'p':
        return 'פ'
    elif a == 'a':
        return 'ש'
    elif a == 's':
        return 'ד'
    elif a == 'd':
        return 'ג'
    elif a == 'f':
        return 'כ'
    elif a == 'g':
        return 'ע'
    elif a == 'h':
        return 'י'
    elif a == 'j':
        return 'ח'
    elif a == 'k':
        return 'ל'
    elif a == 'l':
        return 'ך'
    elif a == ';':
        return 'ף'
    elif a == 'z':
        return 'ז'
    elif a == 'x':
        return 'ס'
    elif a == 'c':
        return 'ב'
    elif a == 'v':
        return 'ה'
    elif a == 'b':
        return 'נ'
    elif a == 'n':
        return 'מ'
    elif a == 'm':
        return 'צ'
    elif a == ',':
        return 'ת'
    elif a == '.':
        return 'ץ'
    elif a == ' ':
        return a
    else: return a
def englibraw(text):
    mod_text=""
    # keyboard.press_and_release('ctrl+c')
    # text = pyperclip.paste()
    for element in text:
        a = change(element)
        mod_text+= a
    pyperclip.copy(mod_text)
    # keyboard.press_and_release('ctrl+v')


# def on_hotkey_press():
#     marked_text = pyperclip.paste()
#     englibraw(marked_text)

hotkey = 'ctrl+shift+q'

keyboard.add_hotkey(hotkey, lambda: englibraw(pyperclip.paste()))

keyboard.wait('esc')