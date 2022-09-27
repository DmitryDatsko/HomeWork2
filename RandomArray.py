from tkinter import DOTBOX
import numpy as np

rand_int = np.int64(np.arange(1, 21))

for i in range(0, len(rand_int)):
    rand_int[i] = rand_int[i] + 1

print(rand_int)


