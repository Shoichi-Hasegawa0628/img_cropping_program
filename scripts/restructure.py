import pprint
from pathlib import Path

if __name__ == '__main__':

    objects_dir = Path("./objects")
    for object_dir in objects_dir.iterdir():

        rgbs = object_dir.glob("rgb_*")
        masks = object_dir.glob("mask_*")
        rgb_dir = object_dir.joinpath("rgb")
        mask_dir = object_dir.joinpath("mask")
        rgb_dir.mkdir()
        mask_dir.mkdir()

        for rgb in rgbs:
            rgb.rename(rgb_dir.joinpath(rgb.name))

        for mask in masks:
            mask.rename(mask_dir.joinpath(mask.name))
