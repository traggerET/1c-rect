from collections import defaultdict

from Matrices.matrix_processing import matrix_relative_position, flatten
from Algorithm.kmp import kmp_search


def find_image_position(matrix_occurences, pattern_image, inaccuracy=1):
    position = [-1, -1]
    for x, y in matrix_occurences[pattern_image[0]]:
        matching_lines = 1
        for i in range(1, len(pattern_image), inaccuracy):
            # check if next lines correspond to fist line's relative position
            if (x, y + i) not in matrix_occurences[pattern_image[i]]:
                matching_lines = 1
                break
            else:
                matching_lines += 1 + inaccuracy - 1

        # by decreasing accuracy we can't guarantee all lines matching
        # but if counter is greater than 1, then last time we didn't break
        if len(pattern_image) == 1 or matching_lines != 1:
            position = [x, y]
            break
    return position


def find_image(source_image, pattern_image, **params):
    flat_image = flatten(source_image)
    flat_occurrences = defaultdict(set)

    # running kmp for each line of pattern
    for batch in pattern_image:
        flat_occurrences[batch] = kmp_search(batch, flat_image)

    source_row_len = len(source_image[0])

    # splitting image in batches by lines
    matrix_occurences = defaultdict(set)

    # set in order to not iterate over the same lines ... just a little optimuzation
    for batch in set(pattern_image):
        for occurrence in flat_occurrences[batch]:
            x, y = matrix_relative_position(occurrence, source_row_len)
            if x + len(batch) <= source_row_len:
                matrix_position = (x, y)
                matrix_occurences[batch].add(matrix_position)

    position = find_image_position(matrix_occurences, pattern_image,
                                   inaccuracy=params["inaccuracy"])

    return position


