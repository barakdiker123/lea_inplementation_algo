#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import matplotlib.animation as animation
import imageio


def draw_pandas_machine(machine, disp_text=""):
    fig, ax = plt.subplots()

    plt.cla()
    df = pd.DataFrame(machine)
    # print(df.sum())
    # df.index = df.index + df.sum()
    df.plot(
        ax=ax,
        title="Final Scheduling of program\n" + disp_text,
        kind="bar",
        stacked=True,
        legend=False,
    )

    ## This for annotating the bars in the bar chart !
    for c in ax.containers:
        # Optional: if the segment is small or 0, customize the labels
        labels = [v.get_height() if v.get_height() > 0 else "" for v in c]
        # remove the labels parameter if it's not needed for customized labels
        ax.bar_label(c, labels=labels, label_type="center")


if __name__ == "__main__":
    draw_pandas_machine([[1, 2], [3, 4], [4], [4]])
    plt.show()


def create_animation(animation_address, animation_arr, k):
    # print(animation_arr[12])
    # print(len(animation_arr))
    fig, ax = plt.subplots()
    images = []
    for i, machine in enumerate(animation_arr):
        draw_pandas_machine(machine, "Current step:" + str(i) + "\n")
        name_of_image_location = animation_address + "/iteration" + str(i) + ".png"
        plt.savefig(name_of_image_location)
        images.append(imageio.imread(name_of_image_location))

    imageio.mimsave(animation_address + "/movie.gif", images, duration=200)
