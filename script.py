from PIL import Image
import random
import numpy as np


def convert_to_pure_bw(path):
    img = Image.open(path)
    thresh = 200
    fn = lambda x: 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')
    return r


def build_image_pair(img_a, img_b, img_c):
    width, height = img_a.size
    assert(width == height)
    assert((img_a.size == img_b.size) & (img_b.size == img_c.size))
    pixels_a = img_a.load()
    pixels_b = img_b.load()
    pixels_c = img_c.load()
    perm = [0,1,2,3]
    four_choose_two_blacks = [255,255,0,0]
    four_choose_three_blacks = [0,0,0,255]
    three_choose_one_black = [0,255,255]
    three_choose_two_blacks = [0,255,0]
    two_choose_one_black = [0,255]
    new_pixels_a = np.zeros((2*width,2*height), dtype=np.uint8) # new doubled size bitmap
    new_pixels_b = np.zeros((2 * width, 2 * height), dtype=np.uint8)  # new doubled size bitmap
    new_pixels_c = np.zeros((2 * width, 2 * height), dtype=np.uint8)  # new doubled size bitmap

    # fill new_pixels_a bitmap
    for i in range(width):
        for j in range(height):
            row = 2 * i
            col = 2 * j
            original_pixel_a = pixels_a[i,j]
            original_pixel_b = pixels_b[i, j]
            original_pixel_c = pixels_c[i, j]
            color_a = color_b = color_c = None
            if original_pixel_a < 128:
                color_a = "black"
            else:
                color_a = "white"
            if original_pixel_b < 128:
                color_b = "black"
            else:
                color_b = "white"
            if original_pixel_c < 128:
                color_c = "black"
            else:
                color_c = "white"

            entry_index = [(row,col), (row,col+1), (row+1,col), (row+1,col+1)]

            if (color_a == "white") & (color_b == "white") & (color_c == "white"):
                # (1) choose two black pixels for a.
                # (2) of the two black pixels of a, choose one black pixel for b.
                # (3) of the two white pixels of a, choose one black pixel for b.
                random.shuffle(four_choose_two_blacks)
                black_indices = []
                white_indices = []

                # (1)
                for k in range(len(four_choose_two_blacks)):
                    (r, c) = entry_index[k]
                    new_pixels_a[r][c] = four_choose_two_blacks[k]
                    if four_choose_two_blacks[k] == 0:
                        black_indices.append(k)
                    else:
                        white_indices.append(k)

                # (2)
                random.shuffle(two_choose_one_black)
                for k in range(len(two_choose_one_black)):
                    index = black_indices[k]
                    r, c = entry_index[index]
                    new_pixels_b[r][c] = two_choose_one_black[k]

                # (3)
                random.shuffle(two_choose_one_black)
                for k in range(len(two_choose_one_black)):
                    index = white_indices[k]
                    r, c = entry_index[index]
                    new_pixels_b[r][c] = two_choose_one_black[k]
            elif (color_a == "white") & (color_b == "white") & (color_c == "black"):
                # (1) choose two black pixels for a.
                # (2) each pixel of b is black iff the corresponding pixel of a is white
                random.shuffle(four_choose_two_blacks)
                for k in range(len(four_choose_two_blacks)):
                    (r, c) = entry_index[k]
                    new_pixels_a[r][c] = four_choose_two_blacks[k]
                    new_pixels_b[r][c] = 255 - four_choose_two_blacks[k]
            elif (color_a == "white") & (color_b == "black") & (color_c == "white"):
                # (1) choose two black pixels for a and b.
                # (2) of the two white pixels of a, choose one black pixel for b.
                random.shuffle(four_choose_two_blacks)
                black_indices = []
                white_indices = []

                # (1)
                for k in range(len(four_choose_two_blacks)):
                    (r, c) = entry_index[k]
                    new_pixels_a[r][c] = four_choose_two_blacks[k]
                    new_pixels_b[r][c] = four_choose_two_blacks[k]
                    if four_choose_two_blacks[k] == 0:
                        black_indices.append(k)
                    else:
                        white_indices.append(k)

                # (2)
                random.shuffle(two_choose_one_black)
                for k in range(len(two_choose_one_black)):
                    index = white_indices[k]
                    r, c = entry_index[index]
                    new_pixels_b[r][c] = two_choose_one_black[k]
            elif (color_a == "black") & (color_b == "white") & (color_c == "white"):
                # (1) choose two black pixels for a and b.
                # (2) of the two white pixels of b, choose one black pixel for a.
                random.shuffle(four_choose_two_blacks)
                black_indices = []
                white_indices = []

                # (1)
                for k in range(len(four_choose_two_blacks)):
                    (r, c) = entry_index[k]
                    new_pixels_a[r][c] = four_choose_two_blacks[k]
                    new_pixels_b[r][c] = four_choose_two_blacks[k]
                    if four_choose_two_blacks[k] == 0:
                        black_indices.append(k)
                    else:
                        white_indices.append(k)

                # (2)
                random.shuffle(two_choose_one_black)
                for k in range(len(two_choose_one_black)):
                    index = white_indices[k]
                    r, c = entry_index[index]
                    new_pixels_a[r][c] = two_choose_one_black[k]
            elif (color_a == "white") & (color_b == "black") & (color_c == "black"):
                # (1) choose three black pixels for b.
                # (2) the white pixel of b should be black in a
                # (3) of the three black pixels of b, choose one black pixel for a.
                random.shuffle(four_choose_three_blacks)
                black_indices = []
                white_indices = []

                # (1)
                for k in range(len(four_choose_three_blacks)):
                    (r, c) = entry_index[k]
                    new_pixels_b[r][c] = four_choose_three_blacks[k]
                    if four_choose_three_blacks[k] == 0:
                        black_indices.append(k)
                    else:
                        white_indices.append(k)

                # (2)
                assert(len(white_indices) == 1)
                r,c = entry_index[white_indices[0]]
                new_pixels_a[r][c] = 0

                # (3)
                random.shuffle(three_choose_one_black)
                for k in range(len(three_choose_one_black)):
                    index = black_indices[k]
                    r, c = entry_index[index]
                    new_pixels_a[r][c] = three_choose_one_black[k]
            elif (color_a == "black") & (color_b == "white") & (color_c == "black"):
                # (1) choose three black pixels for a.
                # (2) the white pixel of a should be black in b.
                # (3) of the three black pixels of a, choose one black pixel for b.
                random.shuffle(four_choose_three_blacks)
                black_indices = []
                white_indices = []

                # (1)
                for k in range(len(four_choose_three_blacks)):
                    (r, c) = entry_index[k]
                    new_pixels_a[r][c] = four_choose_three_blacks[k]
                    if four_choose_three_blacks[k] == 0:
                        black_indices.append(k)
                    else:
                        white_indices.append(k)

                # (2)
                assert(len(white_indices) == 1)
                r,c = entry_index[white_indices[0]]
                new_pixels_b[r][c] = 0

                # (3)
                random.shuffle(three_choose_one_black)
                for k in range(len(three_choose_one_black)):
                    index = black_indices[k]
                    r, c = entry_index[index]
                    new_pixels_b[r][c] = three_choose_one_black[k]
            elif (color_a == "black") & (color_b == "black") & (color_c == "black"):
                # (1) choose three black pixels for a.
                # (2) the white pixel of a should be black in b.
                # (3) of the three black pixels of a, choose two black pixel for b.
                random.shuffle(four_choose_three_blacks)
                black_indices = []
                white_indices = []

                # (1)
                for k in range(len(four_choose_three_blacks)):
                    (r, c) = entry_index[k]
                    new_pixels_a[r][c] = four_choose_three_blacks[k]
                    if four_choose_three_blacks[k] == 0:
                        black_indices.append(k)
                    else:
                        white_indices.append(k)

                # (2)
                assert(len(white_indices) == 1)
                r,c = entry_index[white_indices[0]]
                new_pixels_b[r][c] = 0

                # (3)
                random.shuffle(three_choose_two_blacks)
                for k in range(len(three_choose_two_blacks)):
                    index = black_indices[k]
                    r, c = entry_index[index]
                    new_pixels_b[r][c] = three_choose_two_blacks[k]
            elif (color_a == "black") & (color_b == "black") & (color_c == "white"):
                # (1) choose three black pixels for a and b.
                random.shuffle(four_choose_three_blacks)

                # (1)
                for k in range(len(four_choose_three_blacks)):
                    (r, c) = entry_index[k]
                    new_pixels_a[r][c] = four_choose_three_blacks[k]
                    new_pixels_b[r][c] = four_choose_three_blacks[k]

    a_new = Image.fromarray(new_pixels_a, 'L')
    b_new = Image.fromarray(new_pixels_b, 'L')

    for i in range(2*width):
        for j in range(2*height):
            if (new_pixels_a[i][j]) == 0 or (new_pixels_b[i][j] == 0):
                new_pixels_c[i][j] = 0
            else:
                new_pixels_c[i][j] = 255

    c_new = Image.fromarray(new_pixels_c, 'L')
    return a_new, b_new, c_new


def create_new_image(img_a, w, b):
    width, height = img_a.size
    assert(width == height)
    pixels = img_a.load()
    perm = [0,1,2,3]
    white = [255,255,255,255]
    black = [255,255,255,255]
    for i in range(w):
        white[i] = 0
    for i in range(b):
        black[i] = 0
    new_pixels = np.zeros((2*width,2*height), dtype=np.uint8) # new doubled size bitmap

    for i in range(width):
        for j in range(height):

            random.shuffle(white)
            original_pixel = pixels[i,j]
            select = None
            if original_pixel < 128: # original_pixel is black
                select = black
            else: # original_pixel is white
                select = white
            random.shuffle(select)
            row = 2*i
            col = 2*j
            new_pixels[row][col] = select[0]
            new_pixels[row][col + 1] = select[1]
            new_pixels[row + 1][col] = select[2]
            new_pixels[row + 1][col + 1] = select[3]

    new_img = Image.fromarray(new_pixels, 'L')
    return new_img


# TODO: We first compute A. Later we compute B such that A XOR B = C.
a_bw = convert_to_pure_bw('a.jpg').rotate(90)
b_bw = convert_to_pure_bw('b.jpg').rotate(90)
c_bw = convert_to_pure_bw('c.jpg').rotate(90)
(new_a, new_b, new_c) = build_image_pair(a_bw, b_bw, c_bw)
new_a.save('A.bmp')
new_b.save('B.bmp')
new_c.save('C.bmp')