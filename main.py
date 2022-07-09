import os
import sys
import cv2
import matplotlib.pyplot as plt

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
INPUT_PATH  = os.path.join(BASE_PATH, "input")
OUTPUT_PATH = os.path.join(BASE_PATH, "output")

if not os.path.exists(OUTPUT_PATH): os.makedirs(OUTPUT_PATH)


def breaker(num: int = 50, char: str = "*") -> None:
    print("\n" + num*char + "\n")


def show_image(image, cmap: str = "gnuplot2", title: str=None) -> None:
    plt.figure()
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    if title: plt.title(title)
    figmanager = plt.get_current_fig_manager()
    figmanager.window.state("zoomed")
    plt.show()


def main():
    args_1: tuple = ("--file", "-f")
    args_2: tuple = ("--gray", "-g")
    args_3: tuple = ("--threshold", "-t")
    args_4: tuple = ("--save", "-s")

    filename: str = "Test_1.jpg"
    gray: bool = False
    threshold: int = 127
    save: bool = False

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv or args_2[1] in sys.argv: gray = True

    if args_3[0] in sys.argv: threshold = int(sys.argv[sys.argv.index(args_3[0]) + 1])
    if args_3[1] in sys.argv: threshold = int(sys.argv[sys.argv.index(args_3[1]) + 1])

    if args_4[0] in sys.argv or args_4[1] in sys.argv: save = True

    assert filename in os.listdir(INPUT_PATH), "File Not Found"
    assert threshold >= 0 and threshold < 255, "Threshold Out of Range"

    if gray: image = cv2.imread(os.path.join(INPUT_PATH, filename), cv2.IMREAD_GRAYSCALE)
    else: image = cv2.imread(os.path.join(INPUT_PATH, filename))
    
    image[image > threshold] = 255
    image[image <= threshold] = 0

    if save:
        cv2.imwrite(os.path.join(OUTPUT_PATH, filename.split(".")[0] + " - Binarized.png"), image)
    else:
        if gray: show_image(image=image, cmap="gray", title="Binarized Image")
        else: show_image(image=cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB), title="Binarized Image")


if __name__ == "__main__":
    sys.exit(main() or 0)
