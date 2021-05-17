from cod_metodos import image_scanner, huffman_cod
from collections import defaultdict
import json

pgm_list = [
    "images/lena.pgm",
    "images/baboon.pgm"
]

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
    image, dimensions, vmax = image_scanner.get_image(pgm)
    frequencies, total = huffman_cod.word_frequencies(image)
    codewords = huffman_cod.huffman_tree(frequencies)
    save_codf(pgm, image, codewords, dimensions, vmax)
    print(f"{pgm} average code length: {huffman_cod.avg_codeword(codewords, frequencies, total)}")
