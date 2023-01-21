import cv2
from matplotlib import pyplot as plt
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    image = cv2.imread('RX.jpg')
    # Recortar una imagen
    imageOut = image[80:250, 90:240]

    ret, thresh1 = cv2.threshold(imageOut, 127, 255, cv2.THRESH_BINARY)
    ret, thresh3 = cv2.threshold(image, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(imageOut, 127, 255, cv2.THRESH_TOZERO)

    titles = ['Original', 'Recorte', 'R1', 'R2']
    images = [thresh3, imageOut, thresh1, thresh4]
    for i in range(4):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray', vmin=0, vmax=255)
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()
    return  plt