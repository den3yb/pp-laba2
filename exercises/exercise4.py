import os
from typing import Optional


def get(dataset: str, rait: str, count: int) -> Optional[str]:
    
    """
    Файл принимает абсолютный путь на dataset и значения рейтинга который нужно отоброзить и порядок в каталоге,
    и возвращает его абсолютный путь
    
    """

    for fold in os.listdir(dataset):
        if fold == rait:
            absolute = os.path.join(dataset, fold)
            all_rait = os.listdir(absolute)
            return os.path.join(absolute, all_rait[count])
    return None


if __name__ == "__main__":
    print(get("C:\Proganiy\Git PP\dataset", "4", 3))
