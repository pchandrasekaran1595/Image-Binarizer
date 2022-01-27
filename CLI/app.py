import os
import sys
import cv2
import matplotlib.pyplot as plt


READ_PATH = "Files"
SAVE_PATH = "Processed"
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


def show(image, cmap: str = "gnuplot2") -> None:
    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    figmanager = plt.get_current_fig_manager()
    figmanager.window.state("zoomed")
    plt.show()


def run():
    args_1: tuple = ("--file", "-f")
    args_2: tuple = ("--gray", "-g")
    args_3: tuple = ("--threshold", "-t")
    args_4: tuple = ("--save", "-s")

    filename: str = None
    gray: bool = False
    threshold: int = 127
    save: bool = False

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv or args_2[1] in sys.argv: gray = True

    if args_3[0] in sys.argv: threshold = int(sys.argv[sys.argv.index(args_3[0]) + 1])
    if args_3[1] in sys.argv: threshold = int(sys.argv[sys.argv.index(args_3[1]) + 1])

    if args_4[0] in sys.argv or args_4[1] in sys.argv: save = True

    assert filename is not None, "Enter an argument for --file | -f"

    if gray: image = cv2.imread(os.path.join(READ_PATH, filename), cv2.IMREAD_GRAYSCALE)
    else: image = src=cv2.imread(os.path.join(READ_PATH, filename), cv2.IMREAD_COLOR)
    
    image[image > threshold] = 255
    image[image <= threshold] = 0

    if save:
        cv2.imwrite(os.path.join(SAVE_PATH, filename.split(".")[0] + " - Binarized.jpg"), image)
    else:
        if gray: show(image, "gray")
        else: show(cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB))
