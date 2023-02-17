import numpy as np
import matplotlib.pyplot as plt
import functions

fig, (ax1, ax2) = plt.subplots(2, 1)
fig.subplots_adjust(hspace=0.5)

# getting the information for ax1, "terms" can be modified for arbitrary precision
terms = 100
x = range(0, terms)
y1 = functions.get_y_ax1(x)

ax1.plot(x, y1)
ax1.axhline(np.pi, color='red', linestyle='dotted')
ax1.set_ylim(np.pi - 1, np.pi + 1)

ax1.set_ylabel("Approximated value for PI")
ax1.set_xlabel("Number of terms used in the Leibniz infinite sum")

x2 = range(0, int(terms/5))
y2 = functions.get_y_ax2(x2)

ax2.plot(x2, y2)
ax2.axhline(np.e, color='red', linestyle='dotted')
ax2.set_ylim(np.e - 1, np.e + 1)
ax2.set_ylabel("Approximated value for e")
ax2.set_xlabel("Number of terms used in the infinite sum")
plt.show()
