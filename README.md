# AI-project
Utilizzo
Eseguire il modulo Main.py
Selezionare uno dei quattro Data Sets mostrati e digitare il numero corrispondente a quello scelto.

1) Blood Transfusion
2) Iris
3) Haberman
4) Mammographic Masses

# Esecuzione
Il programma darà in ordine i seguenti output: 
-Visita per livelli dell'albero di decisione creato sull'intero dataset selezionato.

-Visualizzazione grafica dell`albero di decisione tramite libreria grafica GraphViz

-Inizio dei test con fiveFoldCrossValidation: Si scompone il dataset in 5 sottoinsiemi di dimensione n/5, selezionato 1/5 del dataset per il testing si crea l'albero decisionale sui rimanenti 4/5 del dataset. In ordine andiamo a 'spostare' il testing ed il training set ed eseguiamo in totale 5 test di classificazioni. Calcolata la media delle classificazione corrette riportiamo i risultati. Questo processo viene inizialmente eseguito senza valori mancanti nel dataset.

-Si riportano i risultati del fiveFoldCrossValidation sia per entropia che per errore di classificazione

-Si mostra su un grafico il confronto tra le misure d'impurità

# Esempio di output del file Main.py
Selezionare il dataset che si vuole testare:
1) Blood Transfusion
2) Iris
3) Haberman
4) Mammographic Masses
Digitare il numero qui --->1
***************************************************************************
Visita per livelli albero di decisione sul dataset per intero:
Monetary 6000.0
Time 0
Time 82.0
0
Frequency 0
1
Frequency 0
0
Recency 0
1
Recency 0
0
0
1
1
***************************************************************************
Visita per livelli albero di decisione sul dataset per intero:
Recency 6.0
Monetary 1000.0
Time 79.0
Time 16.0
Time 49.0
Monetary 250.0
0
Frequency 1.0
Frequency 2.0
Frequency 14.0
Frequency 10.0
Frequency 0
Frequency 17.0
0
0
0
0
1
1
0
0
0
0
0
0
##########################################################################
Entropia
Risultati Five Fold Cross Validation:
Validation set numero 1 74.50980392156863 % classificate correttamente, ovvero 76 classificazioni corrette su 102
Validation set numero 2 76.47058823529412 % classificate correttamente, ovvero 78 classificazioni corrette su 102
Validation set numero 3 74.50980392156863 % classificate correttamente, ovvero 76 classificazioni corrette su 102
Validation set numero 4 77.45098039215686 % classificate correttamente, ovvero 79 classificazioni corrette su 102
Validation set numero 5 68.62745098039215 % classificate correttamente, ovvero 70 classificazioni corrette su 102
74.31372549019608 % classificate correttamente in media, ovvero 379 classificazioni corrette su 510
##########################################################################
Classification Error
Risultati Five Fold Cross Validation:
Validation set numero 1 70.58823529411765 % classificate correttamente, ovvero 72 classificazioni corrette su 102
Validation set numero 2 71.56862745098039 % classificate correttamente, ovvero 73 classificazioni corrette su 102
Validation set numero 3 67.6470588235294 % classificate correttamente, ovvero 69 classificazioni corrette su 102
Validation set numero 4 74.50980392156863 % classificate correttamente, ovvero 76 classificazioni corrette su 102
Validation set numero 5 70.58823529411765 % classificate correttamente, ovvero 72 classificazioni corrette su 102
70.98039215686273 % classificate correttamente in media, ovvero 362 classificazioni corrette su 510


# Librerie utilizzate
random
matplotlib.pyplot 
graphviz 
math
Attenzione: solitamente sugli IDE più comuni sono quasi tutte presenti tranne per graphviz.(https://graphviz.gitlab.io/download/)

# Riferimenti
Tutti i datasets forniti in questo progetto sono stati presi da UCI Machine Learning. L'implementazione di DecisionTreeLearning.py è stata ripresa e riadattata dalla seguente repository pubblica (https://github.com/aimacode/aima-python/blob/master/learning.py), facendo riferimento a Russell & Norvig 18.3.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

# License
Giovanni Cellai, 2019
