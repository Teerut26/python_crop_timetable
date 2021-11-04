import cv2
from pdf2image import convert_from_path
from os import path
import os

scale = 1

class Pdf2Image():
    def __init__(self):
        self.images = convert_from_path('M6.pdf', size=1000*scale, poppler_path=r'C:\poppler-0.67.0\bin')
        self.main()

    def main(self):
        print(self.images)
        if (path.exists("outputs")):
            for i in range(len(self.images)):
                self.saveImage(self.images[i], f"outputs/page_{i}.png")
        else:
            os.mkdir("outputs")
            for i in range(len(self.images)):
                self.saveImage(self.images[i], f"outputs/page_{i}.png")

    def saveImage(self, images, path):
        images.save(path, 'PNG')


class Crop():
    def __init__(self):
        self.pos1 = {
            "y": 84*scale,
            # "y": 50,
            "x": 43*scale,
            "h": 345*scale,
            "w": 620*scale,
        }
        self.pos2 = {
            "y": 580*scale,
            # "y": 500,
            "x": 43*scale,
            "h": 346*scale,
            "w": 620*scale,
        }
        self.pathSource = "outputs"
        self.pathResult = "results"
        self.index = 1
        self.main()

    def main(self):
        paths = next(os.walk(self.pathSource))[2]
        index = 1
        for i, path in enumerate(paths):
            self.pos1Work(path)
            self.pos2Work(path)

    def pos1Work(self, path):
        img = cv2.imread(f"outputs/{path}")
        crop_img = img[self.pos1["y"]:self.pos1["y"] + self.pos1["h"], self.pos1["x"]:self.pos1["x"] + self.pos1["w"]]
        # cv2.imshow(f"6_{self.index}.png", crop_img)
        # cv2.waitKey(0)
        self.saveImage(f"6_{self.index}.png", crop_img)
        self.index += 1

    def pos2Work(self, path):
        img = cv2.imread(f"outputs/{path}")
        crop_img = img[self.pos2["y"]:self.pos2["y"] + self.pos2["h"], self.pos2["x"]:self.pos2["x"] + self.pos2["w"]]
        # cv2.imshow(f"6_{self.index}.png", crop_img)
        # cv2.waitKey(0)
        self.saveImage(f"6_{self.index}.png", crop_img)
        self.index += 1

    def saveImage(self, filename, img):
        if (path.exists(self.pathResult) == False): os.mkdir(self.pathResult)
        cv2.imwrite(f"{self.pathResult}/{filename}", img)
        print(f"✔ {self.pathResult}/{filename}")


if __name__ == '__main__':
    Pdf2Image()
    Crop()
