def test_run():
    code = """
from matplotlib import pyplot as plt

def polynomial(x, a, b, c):
  return a*(x**3) + b*(x**2) + c

def plot_me(a, b, c):
  x = tuple(range(-10, 10))
  y = [polynomial(x, a, b, c) for x in x]

  fig = plt.figure()
  ax = fig.add_subplot(1, 1, 1)
  ax.plot(x, y, color='tab:red')

  return fig

__chart_plotting_function__ = plot_me

"""

    comp = compile(code, "<string>", "exec")
    scope = {}

    # exec(comp, scope)
    #
    # scope['__chart_plotting_function__'](1, 2, 3)
