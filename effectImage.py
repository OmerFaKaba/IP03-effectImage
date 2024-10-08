import cv2
import numpy as np


person = cv2.imread("saban.jpg")

#person[:,:,0] = 50 # Set the blue channel to 50
#person[:,:,1] = 200 # Set the green channel to 200
#person[:,:,2] = 0 # Set the red channel to 0 (resulting in a greenish color)

#person[200:450,200:300,1]=255 # Set the green channel to 255 for a specific region



section = person[200:400,150:400] # Extract a section of the image

#cv2.imshow("Kemal Sunal",person)   
cv2.imshow("section",section)

person[0:200,0:250] = section # Copy the extracted section to the top-left corner of the image
cv2.imshow("Kemal Sunal",person)   


cv2.waitKey(0)
cv2.destroyAllWindows()