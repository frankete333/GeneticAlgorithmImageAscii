import cv2
import os

print('Starting character extraction tool')
for i in range(0, 7):
    print('██'*15 + '█')
    for j in range(0, 15):
        print('█' + chr((i*15 + j + 32) if (i*15 + j + 32) <= 126 else 32), end='')
    print('█')
print('██'*15 + '█')

print('Take a screenshot of the table above')
print('Save the white square as extract.png in the ascii folder')
print('If the image is saved:')
charH = int(input('Height in pixels of a character: '))
charW = int(input('Width in pixels of a character: '))

print(os.path.dirname(os.path.realpath(__file__))) 
img = cv2.imread("extract.png")
for Vofset in range(0, 7):
    for Hofset in range(0,15):
        fromH = charH+(2*charH*Vofset)
        fromV = charW+(2*charW*Hofset)
        untilH = 2*charH+(2*charH*Vofset)
        untilV = 2*charW+(2*charW*Hofset)
        num = Vofset*15 + Hofset + 32
        if num <= 126:
            print(f'Saved Image {num}')
            crop_img = img[fromH:untilH, fromV:untilV]
            cv2.imwrite(f'{num}.png', crop_img)
