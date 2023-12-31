import os
import csv
import shutil
import random


def get_rel(file_path: str, copy_path: str) -> str:
    
    """
    Файл принимает абсолютный путь на dataset и место куда создаётся копия с анатацией и возвращает относительный путь 
    
    """

    path = os.path.join(os.path.commonpath([file_path, copy_path]), "")
    rel = copy_path.replace(path, "")
    return rel


def main(dataset: str, copy_path: str, name: str) -> None:
    
    """
    Файл принимает абсолютный путь на dataset и абсолютный путь туда куда нужно сделать копию,
    и создаёт в соотвествуещей директории копию с анатацией к ней 
    
    """

    file_path = os.path.dirname(__file__)
    if not os.path.exists(copy_path):
        os.makedirs(copy_path)
    f = open(name, "w")
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    random_list = random.sample(list(range(1, 10000)), 3000)
    count = 0
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    for fold in os.listdir(dataset):
        for file in os.listdir(os.path.join(dataset, fold)):
            orig = os.path.join(dataset, fold, file)
            copy = os.path.join(copy_path, str(random_list[count]))
            count += 1
            relative = get_rel(orig, copy)
            shutil.copyfile(orig, copy)
            writer.writerow([orig, relative, fold])


if __name__ == "__main__":
    main(
        "C:\\Proganiy\\Git PP\\dataset",
        "C:\\Proganiy\\pp-laba2\\dataset_random",
        "annotation_for_random.csv",
    )
