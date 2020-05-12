from __future__ import print_function	# For Py2/3 compatibility
import eel
import random

eel.init('web')

@eel.expose
def py_random():
    return random.random()

@eel.expose
def py_exception(error):
    if error:
        raise ValueError("Test")
    else:
        return "No Error"

def print_num(n):
    print('Got this from Javascript:', n)

# Call Javascript function, and pass explicit callback function    
eel.js_random()(print_num)

# Do the same with an inline callback
eel.js_random()(lambda n: print('Got this from Javascript:', n))

eel.start('callbacks.html', size=(400, 300))
