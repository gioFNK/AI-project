import DataSet
import DecisionTreeLearning
import FiveFold

#permetto all'utente di selezionare il dataset da usare
index = input('Selezionare il dataset che si vuole testare:\n'
              '1) Blood Transfusion\n'
              '2) Iris\n'
              '3) Haberman\n'
              '4) Mammographic Masses\n'
              'Digitare il numero qui --->')

if index == "1":
    filesource = 'BloodTransfusion.txt'
    fileAttr = ['Recency', 'Frequency', 'Monetary', 'Time', 'Donate']
    posClassification = 4
    fileClass = ['0', '1']

elif index == "2":
    filesource = 'Iris.txt'
    fileAttr = ['Sepal-length', 'Sepal-width', 'Petal-length', 'Petal-width', 'Class']
    posClassification = 4
    fileClass = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

elif index == "3":
    filesource = 'Haberman.txt'
    fileAttr = ['Age', 'Patient year of operation', 'Number of positive axillary nodes detected', ' Survival status']
    posClassification = 3
    fileClass = ['1', '2']

elif index == "4":
    filesource = 'MammographicMasses.txt'
    fileAttr = ['BI-RADS', 'Age', 'Shape', 'Margin', 'Density', ' Severity']
    posClassification = 5
    fileClass = ['0', '1']

#chiamo il metodo che fa il parsing del file .txt del dataset scelto
fileDataset = DataSet.setDataSet(filesource, fileAttr, posClassification, fileClass)


#creazione dell albero di decisione con dataset completo
#entropia
ce=1
tree = DecisionTreeLearning.DecisionTreeLearner(fileDataset, ce)
#visita per livelli dell albero con dataset completo e visualizzazione grafica
tree.GraphViz(ce)
#Classification error
ce=0
tree = DecisionTreeLearning.DecisionTreeLearner(fileDataset, ce)
#visita per livelli dell albero con dataset completo e visualizzazione grafica
tree.GraphViz(ce)
FiveFold.test(fileDataset)