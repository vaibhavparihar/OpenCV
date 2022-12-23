import cv2
#location of the image on your local machine 
path = r'C:/Users/vaibh/Desktop/f_r/images/dog.jpg'

img = cv2.imread(path)

#specifying name , font and font properties
name  = "Animal"
font  = cv2.FONT_HERSHEY_COMPLEX
org = (180,40)
font_scale = 1
color = (255,255,255)
thickness = 1
#using putText function to put text over an image
text = cv2.putText(img,"dog :)" , org , font, font_scale , color , thickness, cv2.LINE_AA)
nimg = cv2.cvtColor(text, cv2.COLOR_BGR2BGRA)
cv2.imshow(name , nimg)

#Free any associated memory usage  
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()