import os

def next(dataset:str,rait:str,count:int) ->str:
    for fold in os.listdir(dataset):
        if fold == rait:
            absolute = os.path.join(dataset,fold)
            all_rait = os.listdir(absolute)
            print (os.path.join(absolute, all_rait[count]))
    




if __name__ == '__main__':
    print(next("C:\Proganiy\Git PP\dataset","1",0))