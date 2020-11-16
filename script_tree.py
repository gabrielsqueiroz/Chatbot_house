import pandas as pd
import numpy as np
from sklearn import tree


dados = pd.read_excel('BASE_FINAL.xlsx')

y_train = dados['ABAIXO_ACIMA']
x_train = dados.drop(['ABAIXO_ACIMA'], axis=1).values
decision_tree = tree.DecisionTreeClassifier(max_depth = 20)
decision_tree.fit(x_train, y_train)


with open("arvore.dot", 'w') as f:
    f = tree.export_graphviz(decision_tree,
                             out_file = f,
                             max_depth = 20,
                             impurity = True,
                             feature_names = list(dados.drop(['ABAIXO_ACIMA'], axis=1)),
                             class_names = ['False', 'True'],
                             rounded = True,
                             filled = True)  