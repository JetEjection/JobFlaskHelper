import os
from config.config import INTERNAL_PATH

PATH = os.path.normpath(INTERNAL_PATH)


def create_new_directory(name):
    """
    Creates a new directory
    :param name: name from a form
    :return: str path to created directory
    """
    folder_name = name.split()[0]
    if os.path.exists(os.path.normpath(f"{PATH}/{folder_name}")):
        folder_name = name.replace(" ", "")

    os.makedirs(f"{PATH}/{folder_name}")
    return f"{PATH}/{folder_name}"
