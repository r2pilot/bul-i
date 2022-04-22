import cv2

# reading the images
diff_img = cv2.imread('images\\a_7.jpg')
ref_img = cv2.imread('images\\a_ref.jpg')

# subtract the images
subtracted = cv2.subtract(ref_img, diff_img)

# TO show the output
cv2.imshow('image', subtracted)

# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()