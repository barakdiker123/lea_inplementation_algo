#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import matplotlib.animation as animation
import imageio


def draw_pandas_machine(machine, ax=None):
    plt.cla()
    df = pd.DataFrame(machine)
    df.plot(ax=ax, title="Final Scheduling of program", kind="bar", stacked=True)


if __name__ == "__main__":
    draw_pandas_machine([[1, 2], [3, 4], [4], [4]])
    plt.show()


def create_animation(animation_address, animation_arr):
    # print(animation_arr[12])
    # print(len(animation_arr))
    fig, ax = plt.subplots()
    images = []
    for i, machine in enumerate(animation_arr):
        draw_pandas_machine(machine, ax)
        name_of_image_location = animation_address + "/iteration" + str(i) + ".png"
        plt.savefig(name_of_image_location)
        images.append(imageio.imread(name_of_image_location))

    imageio.mimsave(animation_address + "/movie.gif", images, duration=200)
