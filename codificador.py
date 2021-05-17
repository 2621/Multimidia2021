from heapq import heappush, heappop, heapify
from collections import defaultdict
import numpy as np
import json

pgm_list = [
    "images/lena.pgm",
    "images/baboon.pgm"
]

def get_image(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)

    data = []
    for line in lines[1:]:
        data.extend([int(c) for c in line.split()])

    vmax = data[2]
    dimensions = (data[1],data[0])
    image_flat = np.array(data[3:])
    
    return image_flat, dimensions, vmax

def word_frequencies(image):
    freqs = {}
    sum = 0

    for pixel in image:
        key = str(pixel)
        sum += 1
        if freqs.get(key, False):
            freqs[key] += 1
        else:
            freqs[key] = 1
    return freqs, sum

def huffman_tree(freqs):
    heap = [[wt, [sym, ""]] for sym, wt in freqs.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    codewords = {}
    for sym, wt in heap[0][1:]:
        codewords[sym] = wt
    return codewords

def avg_codeword(codewords, freqs, total):
    avg = 0
    for key in codewords:
        avg += len(codewords[key]) * freqs[key]
    return avg/total

def save_codf(name, image, codewords, dimensions, vmax):
    code = ""
    for pixel in image:
        key = str(pixel)
        code += codewords[key]
    
    content = json.dumps({
        "codewords": codewords,
        "dimensions": dimensions,
        "vmax": vmax,
        "code": code
    }, indent=4)

    f = open(f"{name}.huff","w")
    f.write(content)
    f.close()
    print(f"{name}.huff saved")

for pgm in pgm_list: 
    image, dimensions, vmax = get_image(pgm)
    frequencies, total = word_frequencies(image)
    codewords = huffman_tree(frequencies)
    save_codf(pgm, image, codewords, dimensions, vmax)
    print(f"{pgm} average code length: {avg_codeword(codewords, frequencies, total)}")
