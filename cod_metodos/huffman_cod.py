from heapq import heappush, heappop, heapify

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