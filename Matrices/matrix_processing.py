from itertools import chain


def read_matrix(input_):
    matrix = []
    try:
        for line in input_:
            matrix.append(tuple(map(int, line.split())))
    except ValueError:
        return matrix
    return matrix


def matrix_relative_position(idx, matrix_row_len):
    x_offset = idx % matrix_row_len
    y_offset = (idx - x_offset) // matrix_row_len
    return x_offset, y_offset


def flatten(source_image):
    return list(chain.from_iterable(source_image))