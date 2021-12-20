import numpy as np
from pymoo.core.problem import ElementwiseProblem
import cv2

class ImageToAscii(ElementwiseProblem):

    def __image_to_array(self, image):
        arr = []
        for y in range(self.I_height):
            for x in range(self.I_width):
                fromH = y*self.C_height
                untilH = (y+1)*self.C_height
                fromW = x*self.C_width
                untilW = (x+1)*self.C_width
                print(fromW, untilW, fromH, untilH)
                crop_img = image[fromH:untilH, fromW:untilW]

                # show Crops
                # cv2.imshow('image',crop_img)
                # cv2.waitKey(2000)

                arr.append(crop_img)

        return arr

    def __init__(self, ascii, image):
        print(ascii[0].shape[:2])
        self.C_height, self.C_width = ascii[0].shape[:2]
        self.ascii = ascii
        h_img, w_img = image.shape[:2]
        self.I_height, self.I_width = (h_img // self.C_height) , (w_img // self.C_width)
        self.image = self.__image_to_array(image)

        vars = self.I_height * self.I_width
        super().__init__(n_var=vars,
                         n_obj=2,
                         n_constr=0,
                         xl=0, 
                         xu=94, 
                         type_var=int)


    def __compare(self, vec):

        tot = 0
        for coord in range(len(vec)):
            img1 = self.ascii[vec[coord]] # ascii char
            img2 = self.image[coord]

            hist1 = cv2.calcHist([img1],[0],None,[256],[0,256])
            hist2 = cv2.calcHist([img2],[0],None,[256],[0,256])
            tot += (cv2.compareHist(hist1,hist2,cv2.HISTCMP_CORREL))
            

        return tot / len(vec)
        

    def _evaluate(self, x, out, *args, **kwargs):
        metric = - self.__compare(x)
        out["F"] = [ metric , metric]

