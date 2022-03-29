import sys

from classes.common import ReadMatrix
from classes.parser import SimpleCLI
from classes.findimage import FindImage


def MatchImages(source_image, cut_image, params):
    position = FindImage(source_image, cut_image)

    if not params["oriented"]:
        return position



def RunApp():
    parser = SimpleCLI()
    params = parser.ParseArgs(sys.argv)

    source_image = ReadMatrix(sys.stdin)
    cut_image = ReadMatrix(sys.stdin)

    position = FindImage(source_image, cut_image)

    ConvertParams(params, position, source_image, cut_image)

    print(position)
