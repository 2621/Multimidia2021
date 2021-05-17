from decoder_methods import image_scanner, huffman_decoder

pgm_list = [
    "images/lena.pgm",
    "images/baboon.pgm"
]

def save_decoded(name, image, dimensions, vmax):
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
    decoder = huffman_decoder.dictionary(codewords)
    image = huffman_decoder.decode(code, decoder)
    save_decoded(pgm, image, dimensions, vmax)
