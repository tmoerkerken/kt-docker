from pyvirtualdisplay import Display
import matplotlib.pyplot as plt

Display().start()
plt.plot([0, 1, 2], [0, 1, 4])
plt.savefig("plot.png")
