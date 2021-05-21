import numpy as np
import matplotlib.pyplot as plt
import util


def model(x, a0=3, a1=2, a2=0):
    return a0 + (a1 * x) + (a2 * x ** 2)


def model_component():
    x = np.linspace(-10, 10, 21)
    y = model(x)

    fig = util.plot_prediction(x, y)


def model_parameters():
    xd = np.array([0.0,  0.5,  1.0,  1.5,  2.0,
                   2.5,  3.0,  3.5,  4.0,  4.5,
                   5.0,  5.5,  6.0,  6.5,  7.0,
                   7.5,  8.0,  8.5,  9.0,  9.5,  10.0, ])
    yd = np.array([161.78587909,  132.72560763,  210.81767421,  179.6837026,  181.98528167,
                   234.67907351,  246.48971034,  221.58691239,  250.3924093,  206.43287615,
                   303.75089312,  312.29865056,  323.8331032,  261.9686295,  316.64806585,
                   337.55295912,  360.13633529,  369.72729852,  408.0289548,  348.82736117,  394.93384188, ])

    a0 = 150
    a1 = 25
    ym = model(xd, a0, a1)
    fig = util.plot_data_with_model(xd, yd, ym)


#model_component()
model_parameters()
