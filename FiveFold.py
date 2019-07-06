import random
import DataSet
import matplotlib.pyplot as plt
import DecisionTreeLearning

#creo il validation set per il 5 fold cross validation
def testing(fileDataset, number):
    length = int(len(fileDataset.examples) / 5)
    k = number * length
    validation = []
    i = 0
    while i < length:
        validation.append(fileDataset.examples[i + k])
        i = i + 1
    return DataSet.DataSet(validation, fileDataset.inputs, fileDataset.attributes, fileDataset.target,
                           fileDataset.attrnames, fileDataset.values)

#creo il training set per il 5 fold cross validation
def training(fileDataset, number):
    totalLength = len(fileDataset.examples)
    length = int(len(fileDataset.examples) / 5)
    k = number * length
    training = []
    i = 0
    while i < k:
        training.append(fileDataset.examples[i])
        i = i + 1
    j = k + length
    while j < totalLength:
        training.append(fileDataset.examples[j])
        j = j + 1
    return DataSet.DataSet(training, fileDataset.inputs, fileDataset.attributes, fileDataset.target,
                           fileDataset.attrnames, fileDataset.values)

#ritorna la media di una lista
def avg(list):
    length = len(list)
    count = 0
    for i in list:
        count = count + i
    return count / length


def fiveFoldCrossValidation(fileDataset, ce):
    print ('Risultati Five Fold Cross Validation:')
    i = 0
    percents = []
    corrects = []
    random.shuffle(fileDataset.examples)
    while i < 5:
        train = training(fileDataset, i)
        val = testing(fileDataset, i)
        tree = DecisionTreeLearning.DecisionTreeLearner(train, ce)
        correctV = 0
        for example in val.examples:
            if tree.__call__(example) == example[len(example) - 1]:
                correctV = correctV + 1
        percent = (correctV * 100) / len(val.examples)
        print ('Validation set numero', i + 1, percent, '% classificate correttamente, ovvero', correctV, \
            'classificazioni corrette su', len(val.examples))
        i = i + 1
        percents.append(percent)
        corrects.append(correctV)
    print (avg(percents), '% classificate correttamente in media, ovvero', sum(corrects),
        'classificazioni corrette su', len(val.examples) * 5)
    return avg(percents)

def test(fileDataset):
    print('##########################################################################')
    print('Entropia')
    entropy=fiveFoldCrossValidation(fileDataset,0)
    print('##########################################################################')
    print('Classification Error')
    clerror=fiveFoldCrossValidation(fileDataset,1)
    ind = [0,1]  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(0, entropy, width, color='#d62728')
    p2 = plt.bar(1, clerror, width)

    plt.ylabel('Percentuali Classificazioni Corrette')
    plt.title('Confronto')
    plt.xticks(ind, ('Entropia', 'Errore Di Classificazione'))
    plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
    plt.legend((p1[0],p2[0]), ('Entropia', 'Errore Di Classificazione'))

    plt.show()

