from django.shortcuts import get_object_or_404

from .models import BoardsAndUsers, BoardAndColumn


def check_input_data_in_db(post_data):
    obj_1 = get_object_or_404(BoardsAndUsers, user_name=post_data["user_name"],
                              board_title=post_data["board_title"])
    obj_2 = get_object_or_404(BoardAndColumn, board_title=post_data["board_title"],
                              column_title=post_data["column_title"])
    if obj_1 is not None and obj_2 is not None:
        return True
    else:
        return False
