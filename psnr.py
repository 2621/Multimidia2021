pgm_list = [
    "images/lena.pgm",
    "images/baboon.pgm" 
]

def get_image(fname):
    with open(fname) as f:
        lines = f.readlines()

    for l in list(lines):
        if l[0] == '#':
            lines.remove(l)

    data = []
    for line in lines[1:]:
        data.extend([int(c) for c in line.split()])

    vmax = data[2]
    dimensions = (data[1],data[0])
    image = data[3:]
    
    return image, dimensions, vmax

def calculate_psnr(original, decoded, vmax):
    MSE = 0
    for i in range(len(original)):
        MSE += (original[i] - decoded[i])**2
    
    if MSE == 0:
        return "infinite"
    else:
        return (vmax**2) / MSE


for pgm in pgm_list:
    image_original, _, vmax = get_image(pgm)
    image_decoded, *_ = get_image(f'{pgm}.huff.pgm')
    # assert np.array_equal(image_original, image_decoded)
    print(f"{pgm} PSNR: {calculate_psnr(image_original, image_decoded, vmax)}")

explanation = \
    "\nAs the Huffman compression is lossless, the corrupting noise is zero then the ratio between signal and noise, or the PSNR, in other words, tends to infinite"
print(explanation)
