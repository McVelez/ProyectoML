import cv2

img = cv2.imread('Captcha.PNG',0)

(h, w) = img.shape[:2]
image_size = h*w
mser = cv2.MSER_create()
mser.setMaxArea(round(image_size/2))
mser.setMinArea(10)

ret, thresh2 = cv2.threshold(img,219,255,cv2.THRESH_BINARY_INV)
regions, rects = mser.detectRegions(thresh2)

print(rects)
sumW = 0
sumH = 0
for i in range(len(rects)):
    sumW = sumW + rects[i][2]
    sumH = sumH + rects[i][3]

print(sumW / len(rects))
print(sumH / len(rects))


rectsOrd = rects[rects[:, 0].argsort()]

cont = 0
for x,y,w,h in rectsOrd:
    if(h > ((sumH / len(rectsOrd)) - 4)):
        cv2.imwrite('{}.png'.format(cont), thresh2[y:y+h,x:x+w])
        cont += 1

