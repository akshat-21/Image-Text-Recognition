# GrayScale Image Convertor
# https://extr3metech.wordpress.com
 
import cv2
image = cv2.imread('img.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grey.jpg',gray_image)
cv2.imshow('color_image',image)
cv2.imshow('grey.jpg',gray_image) 
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
 
#End of Code