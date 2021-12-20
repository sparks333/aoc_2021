
import numpy as np

def enhance_img(img, alg):

    img_binary = []
    for i in img:
        img_binary_line = []
        for j in i:
            if j == '.':
                img_binary_line.append(0)
            else:
                img_binary_line.append(1)
        img_binary.append(img_binary_line)

    img_binary = np.pad(np.array(img_binary), 2, mode='edge')
    kernel = np.array([[256, 128, 64], [32, 16, 8], [4, 2, 1]])

    indices = np.zeros([img_binary.shape[0]-2, img_binary.shape[1]-2])
    for i in range(1, img_binary.shape[1]-1):
        for j in range (1, img_binary.shape[0]-1):
            indices[i-1, j-1] = np.sum(kernel * img_binary[i-1:i+2,j-1:j+2])

    out_img = []
    for i in indices:
        out_img_line = ''
        for j in i:
            out_img_line += alg[int(j)]
        out_img.append(out_img_line)
    return out_img


with open('input.txt') as file:
    isAlg = True
    alg = ''
    img = []
    for line in file:
        if line == '\n':
            isAlg = False
        elif isAlg:
            alg += line.strip()
        else:
            img.append(line.strip())
     
    img_null_line = ''
    for i in range(len(img[0])+6):
        img_null_line += '.'
    
    for i in range(len(img)):
        img[i] = '...' + img[i] + '...'

    img.insert(0, img_null_line)
    img.insert(0, img_null_line)
    img.insert(0, img_null_line)
    img.insert(len(img), img_null_line)
    img.insert(len(img), img_null_line)
    img.insert(len(img), img_null_line)

    img = enhance_img(img, alg)
    img = enhance_img(img, alg)
    
    num_bright = 0

    for i in img:
        for j in i:
            if j == '#':
                num_bright += 1
    

    print('Part 1: ' + str(num_bright))

    for i in range(48):
        img = enhance_img(img, alg)

    num_bright = 0

    for i in img:
        for j in i:
            if j == '#':
                num_bright += 1
    

    print('Part 2: ' + str(num_bright))
