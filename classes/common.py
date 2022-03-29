from typing import Tuple, List

def ReadMatrix(input) -> List[Tuple[int]]:
    matrix = []
    try:
        for line in input:
            matrix.append(tuple(map(int, line.split())))
    except ValueError:
        return matrix
    return matrix
