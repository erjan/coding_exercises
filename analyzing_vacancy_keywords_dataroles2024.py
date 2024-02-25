
from collections import Counter


def analyze_vacancy_keywords(filename):

    vacancy_dataset = open(filename, 'r')

    vacancy_dataset =  vacancy_dataset.read()

    vacancy_dataset = vacancy_dataset.split('\n')


    for i in range(len(vacancy_dataset)):
        vacancy_dataset[i] = vacancy_dataset[i].lower()

    vacancy_dataset = dict(Counter(vacancy_dataset))


    vacancy_dataset = sorted(vacancy_dataset.items(),key = lambda x: -x[1])

    v = filename.split('.txt')[0]
    print('ANALYZING FOR vacancy in: ' + v)
    print()
    
    for x in vacancy_dataset:
        print(x)
    print()


analyze_vacancy_keywords('data_eng.txt')

analyze_vacancy_keywords('python_backend_engineer.txt')

analyze_vacancy_keywords('mlops.txt')
