import numpy as np

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