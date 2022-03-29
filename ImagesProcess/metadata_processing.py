def orient_position(description):
    orientations = ["северо-запад", "север", "северо-восток",
                    "запад", "центр", "восток",
                    "юго-запад", "юг", "юго-восток"
                    ]
    rows = description["rows_count"]
    row_len = description["rows_len_count"]
    current = description["position"]

    # just splitted matrix into a grid
    x_grid = [x for x in range(rows // 3, rows + 1, rows // 3)]
    y_grid = [y for y in range(row_len // 3, row_len + 1, row_len // 3)]
    x_left = y_left = 0

    for i, x_right in enumerate(x_grid):
        y_left = 0
        for j, y_right in enumerate(y_grid):

            # check if left-upper corner fits into grid dividers
            if x_left <= current[1] <= x_right \
                    and y_left <= current[0] <= y_right:
                description["oriented_pos"] = orientations[i + j]
                break

            y_left = y_right
        x_left = x_right


def preprocess_image_description(descr, params):
    if params["oriented"]:
        orient_position(descr)
        return descr["oriented_pos"]

    return descr["position"]
