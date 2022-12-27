import cv2
#location of the image on your local machine 
path = r'C:/Users/vaibh/Desktop/f_r/images/dog.jpg'

img = cv2.imread(path)

name = "doggo"

color = (0,255,0)

start_point = (80,50)
end_point = (400,350)
thickness = 4

rect  = cv2.rectangle(img,start_point,end_point,color,thickness)
cv2.imshow(name,rect)

#Free any associated memory usage  
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()