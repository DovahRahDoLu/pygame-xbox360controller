from xbox360_controller import *

Controllers = list()
def JoystickDetection(max_controllers=4):
    global Controllers
    for num in range(0, max_controllers):
        try:
            c = XBox360Controller(num)
            Controllers.append(c)
        except ControllerNotFoundError:
            print("Controller {} not found".format(num+1))

    return Controllers
