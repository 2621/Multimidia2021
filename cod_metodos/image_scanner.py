import numpy as np

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