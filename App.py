import sys

from classes.common import ReadMatrix
from classes.parser import SimpleCLI
from classes.findimage import FindImage


def OrientPosition(description):
    if description["position"][1] < description["rows_count"] // 2:
        if description["position"][0] < description["rows_len_count"] // 2:
            description["oriented_pos"] = "северо-запад"

        else:
            description["oriented_pos"] = "северо-воcток"
    else:
        if description["position"][0] < description["rows_len_count"] // 2:
            description["oriented_pos"] = "юго-запад"

        else:
            description["oriented_pos"] = "юго-воcток"

def preprocessImageDescription(description, params):
    processed_description = dict(description)
    if params["oriented"]:
        OrientPosition(processed_description)

    return processed_description



def RunApp():
    parser = SimpleCLI()
    params = parser.ParseArgs(sys.argv)

    source_image = ReadMatrix(sys.stdin)
    cut_image = ReadMatrix(sys.stdin)

    position = FindImage(source_image, cut_image,
                         inaccuracy=params["inaccuracy"])

    description = dict(
        {
            "position": position,
            "rows_count": len(source_image),
            "rows_len_count": len(source_image[0])
        }
    )

    processed_descr = preprocessImageDescription(description, params)

    print(processed_descr)
