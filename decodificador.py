import json
import numpy as np

pgm_list = [
    "images/lena.pgm",
    "images/baboon.pgm"
]

def get_image_info(name):
    f = open(f"{name}.huff", "r")
    content = f.read()
    info = json.loads(content)
    return info["codewords"], info["dimensions"], info["vmax"], info["code"]

def dictionary(codewords):
    decoder = {}
    for key in codewords:
        decoder[codewords[key]] = key
    return decoder

def decode(code, decoder):
    max_code_length = 0
    for key in decoder:
        if max_code_length < len(key):
            max_code_length = len(key)

    decoded = []
    while (len(code) > 0):
        for i in range(1, max_code_length + 1):
            if decoder.get(code[:i], False):
                decoded.append(int(decoder[code[:i]]))
                code = code[i:]
                break
    
    return decoded

def save_decod(name, image, dimensions, vmax):
    image_copy = image.copy()
    content = f"P2\n{dimensions[0]} {dimensions[1]}\n{vmax}\n"
    for i in range(dimensions[0]):
        content += " ".join([str(el) for el in image_copy[:dimensions[1]]])
        content += "\n"
        image_copy = image_copy[dimensions[1]:]
    
    f = open(f"{name}.huff.pgm","w")
    f.write(content)
    f.close()
    print(f"{name}.huff.pgm saved")

for pgm in pgm_list:
    codewords, dimensions, vmax, code = get_image_info(pgm)
    decod = dictionary(codewords)
    image = decode(code, decod)
    save_decod(pgm, image, dimensions, vmax)
