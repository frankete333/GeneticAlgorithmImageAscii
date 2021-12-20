from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.factory import get_termination
from pymoo.optimize import minimize
from problem import ImageToAscii
import matplotlib.pyplot as plt
import cv2

# Pseudo-Code 8x16 px
# - Load table of Ascii from /ascii
# - Open Image
# - Image to gray scale
# - Trunc to multiple of char size
# - 

# Vars
pop = 40
max_gens = 500

ascii = []
for i in range(95):  # Cargar los ascii en el array (offset -32)
    im = cv2.cvtColor(cv2.imread(f'../ascii/{i+32}.png'), cv2.COLOR_BGR2GRAY)
    ascii.append(im)

C_height, C_width = ascii[0].shape[:2]
# cv2.imshow('image',arr[0])
# cv2.waitKey(5000)

img = cv2.imread("../in_out/in.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

I_height, I_width = img.shape[:2]

new_height = I_height - (I_height % C_height) 
new_width = I_width - (I_width % C_width)

resized = cv2.resize(img, (new_width, new_height), interpolation = cv2.INTER_AREA)
cv2.imshow('image',resized)
cv2.waitKey(3000)

# Manual compare ONLY with images size 1 character
# max = -1000
# m = 0
# for i in range(95):
#     hist1 = cv2.calcHist([ascii[i]],[0],None,[256],[0,256])
#     hist2 = cv2.calcHist([resized],[0],None,[256],[0,256])
#     h = cv2.compareHist(hist1,hist2,cv2.HISTCMP_CORREL)
#     print(f'{chr(i+32)} = {h}')
#     if h > max:
#         max = h
#         m = i
# print(f'MEJOR: {chr(m)} = {max}')


algorithm = NSGA2(
    pop_size=pop,
    n_offsprings=10,
    sampling= get_sampling("int_random"),
    crossover=get_crossover("int_sbx", prob=0.9, eta=15),
    mutation=get_mutation("int_pm", eta=20),
    eliminate_duplicates=True
)

termination = get_termination("n_gen", max_gens)

problem = ImageToAscii(ascii, resized)

res = minimize(problem,
               algorithm,
               termination,
               seed=1,
               save_history=True,
               verbose=True)

X = res.X
F = res.F


with open('Solutions.txt', 'w') as f:
    iter = 0
    for arr in X.astype(int):
        f.write(f'Metric: {-F[iter][0]}\n')
        for y in range(0,(I_height // C_height)):
            for x in range(0, (I_width // C_width)):
                f.write(f'{chr(arr[y*(I_width // C_width) + x] + 32)}')
            f.write('\n')
        f.write('\n')
        f.write('\n')
        iter += 1



# xl, xu = problem.bounds()
# plt.figure(figsize=(7, 5))
# plt.scatter(F[:, 0], F[:, 1], s=20, facecolors='none', edgecolors='blue')
# plt.title("Soluciones no Dominadas")
# plt.show()