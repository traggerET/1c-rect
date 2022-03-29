from collections import defaultdict
from itertools import chain


def matrix_relative_position(idx, matrix_row_len):
    x_offset = idx % matrix_row_len
    y_offset = (idx - x_offset) // matrix_row_len
    return x_offset, y_offset


def find_image_position(matrix_occurences, pattern_image, inaccuracy=1):
    position = [-1, -1]
    for x, y in matrix_occurences[pattern_image[0]]:
        matching_lines = 1
        for i in range(1, len(pattern_image), inaccuracy):
            if (x, y + i) not in matrix_occurences[pattern_image[i]]:
                matching_lines = 1
                break
            else:
                matching_lines += 1 + inaccuracy - 1
        if  len(pattern_image) == 1 or matching_lines != 1:
            position = [x, y]
            break
    return position


def FindImage(source_image, pattern_image, **params):
    flat_image = flatten(source_image)
    flat_occurrences = defaultdict(set)
    for batch in pattern_image:
        flat_occurrences[batch] = KMPSearch(batch, flat_image)

    source_row_len = len(source_image[0])

    # splitting image in batches by lines
    matrix_occurences = defaultdict(set)

    # set in order to not iterate over the same lines
    for batch in set(pattern_image):
        for occurence in flat_occurrences[batch]:
            x, y = matrix_relative_position(occurence, source_row_len)
            if x + len(batch) <= source_row_len:
                matrix_position = (x, y)
                matrix_occurences[batch].add(matrix_position)

    position = find_image_position(matrix_occurences, pattern_image,
                                   inaccuracy=params["inaccuracy"])

    return position


def KMPSearch(pat, txt):
    pattern_len = len(pat)
    source_len = len(txt)

    lps = [0] * pattern_len
    j = 0

    computeLPSArray(pat, pattern_len, lps)
    occurences = set()
    i = 0
    while i < source_len:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == pattern_len:
            occurences.add(i - j)
            j = lps[j - 1]

        # mismatch after j matches
        elif i < source_len and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return occurences


def computeLPSArray(pat, M, lps):
    len = 0
    i = 1

    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def flatten(source_image):
    return list(chain.from_iterable(source_image))
