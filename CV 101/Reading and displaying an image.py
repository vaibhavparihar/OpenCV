import cv2
import numpy as np

#reading the image and assigning it to a variable 
img = cv2.imread("images/cats.jpg",cv2.IMREAD_COLOR)

#diplaying the image
cv2.imshow("cat",img)

#Free any associated memory usage  
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()