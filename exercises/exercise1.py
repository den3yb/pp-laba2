import os
import csv


def get_rel(absolut: str, file: str) -> str:

    """
    Файл принимает абсолютный путь на dataset и место куда создаётся анатация и возвращает относительный путь  
    
    """

    path = os.path.join(os.path.commonpath([absolut, file]))
    rel = absolut.replace(path, "")
    return rel


def main(dataset: str) -> None:
    
    """
    Файл принимает абсолютный путь на dataset и создаёт аннатацию в своей директории  
    
    """
    
    path_f = os.path.dirname(__file__)
    f = open("annotation.csv", "w")
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    for i in os.listdir(dataset):
        fold = os.path.join(dataset, i)
        for otz_num in os.listdir(fold):
            absolute = os.path.join(fold, otz_num)
            relative = get_rel(absolute, path_f)
            writer.writerow([absolute, relative, i])


if __name__ == "__main__":
    main("C:\Proganiy\Git PP\dataset")

