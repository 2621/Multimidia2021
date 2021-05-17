from decod_metodos import image_scanner, huffman_decod

pgm_list = [
    "images/lena.pgm",
    "images/baboon.pgm"
]

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
    codewords, dimensions, vmax, code = image_scanner.get_image_info(pgm)
    decod = huffman_decod.dictionary(codewords)
    image = huffman_decod.decode(code, decoder)
    save_decod(pgm, image, dimensions, vmax)
