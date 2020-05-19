from kivy.app import App
from kivy.core.text import LabelBase
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.factory import Factory
import timeit
import random

Window.system_size = [500,600]
Window.clearcolor = (.83,.5,.5, .5)
LabelBase.register(name='Got',
                   fn_regular='BenguiatGothicC_Bold.ttf')

def predict(point, weights, P):
    s = 0
    for i in range(len(point)):
        s += weights[i] * point[i]
    return 1 if s > P else 0


def perceptron(speed_of_learning, deadline, iterations):
    P = 4
    data = [(0, 6), (1, 5), (3, 3), (2, 4)]
    n = len(data[0])
    weights = [0.001, -0.004]
    outputs = [0, 0, 0, 1]
    start_time = timeit.default_timer()

    for k in range(iterations):
        total_error = 0

        for i in range(len(outputs)):
            prediction = predict(data[i], weights, P)
            err = outputs[i] - prediction
            total_error += err

            for j in range(n):
                delta = speed_of_learning * data[i][j] * err
                weights[j] += delta

        if total_error == 0 or timeit.default_timer() - start_time > deadline:
            break
    return weights[0], weights[1], k

class MainWidget(BoxLayout):
    def train(self):
        speed = float(self.speed.text)
        deadline = int(self.deadline.text)
        iterations = int(self.iterations.text)
        if (speed <= 0) or (deadline <= 0) or (iterations <= 0):
            self.w1.text = 'Input is wrong.'
            self.w2.text = ''
            return
        w1, w2, iter = perceptron(speed, deadline, iterations)
        self.w1.text = 'w1 = {0:.2f}'.format(w1)
        self.w2.text = 'w2 = {0:.2f}'.format(w2)
        mypopup = Factory.MyPopup()
        mypopup.numiter.text = str(iter)
        mypopup.open()
        

class Lab3_2App(App):
    def build(self):
        return MainWidget()

if __name__ == "__main__":
    Lab3_2App().run()