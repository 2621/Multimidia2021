import json

def get_image_info(name):
    f = open(f"{name}.huff", "r")
    content = f.read()
    info = json.loads(content)
    return info["codewords"], info["dimensions"], info["vmax"], info["code"]