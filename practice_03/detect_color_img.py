import matplotlib.pylab as plt
import cv2
from PIL import Image, ImageStat


# First I thought the problem can be solved by detecting some simple patterns in the
# image's histogram. However, the real solution is much more complicated than what I thought.
# The rule to distinguish colored images and black-white images are quite complex. You will see one
# solution below, in which I copied from Stack Overflow. To distinguish paintings and colored photographs,
# which is way more difficult, we may use machine learning. Obviously it is out of the scope of this course.
# I apologize since I did not check the solutions in advance.

# This histogram solution does not work. There is no clear rule to tell different types of images based on
# their histograms.
def show_histogram(img_path):
    """
    Display a histogram of pixel intensity values in an image.
    Note: The image is resized to 60% of its original size.
    :param img_path: (str): The file path of the image.
    :return: None
    """
    img = cv2.imread(img_path)
    scale_percent = 60  # percent of original size, just to make the image smaller
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    plt.hist(resized.ravel(), bins = 256, range=(0, 256))
    plt.show(block=True)
    # plt.interactive(False)


# This solution I took it from https://stackoverflow.com/a/23035464
# It works very well on a few examples I tried. You may take a look at the function and test it
# with your own images. However, since it is very complicated, you do not have to understand it.
def detect_color_image(file, thumb_size=40, MSE_cutoff=22, adjust_color_bias=True):
    pil_img = Image.open(file)
    bands = pil_img.getbands()
    if bands == ('R','G','B') or bands== ('R','G','B','A'):
        thumb = pil_img.resize((thumb_size,thumb_size))
        SSE, bias = 0, [0,0,0]
        if adjust_color_bias:
            bias = ImageStat.Stat(thumb).mean[:3]
            bias = [b - sum(bias)/3 for b in bias ]
        for pixel in thumb.getdata():
            mu = sum(pixel)/3
            SSE += sum((pixel[i] - mu - bias[i])*(pixel[i] - mu - bias[i]) for i in [0,1,2])
        MSE = float(SSE)/(thumb_size*thumb_size)
        if MSE <= MSE_cutoff:
            print("grayscale\t")
        else:
            print("Color\t\t\t")
        print("( MSE=",MSE,")")
    elif len(bands)==1:
        print("Black and white", bands)
    else:
        print("Don't know...", bands)


if __name__ == '__main__':
    detect_color_image('./img/Paolo_De_Matteis.jpg')
