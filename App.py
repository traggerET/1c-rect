from Matrices.matrix_processing import read_matrix
from classes.parser import SimpleCLI
from ImagesProcess.image_processing import find_image

import sys

from ImagesProcess.metadata_processing import preprocess_image_description


def run_app():
    parser = SimpleCLI()
    params = parser.parse_args(sys.argv)

    source_image = read_matrix(sys.stdin)
    cut_image = read_matrix(sys.stdin)

    position = find_image(source_image, cut_image,
                         inaccuracy=params["inaccuracy"])

    description = dict(
        {
            "position": position,
            "rows_count": len(source_image),
            "rows_len_count": len(source_image[0])
        }
    )

    processed_descr = preprocess_image_description(description, params)

    print(processed_descr)
