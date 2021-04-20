"""
Created on Tue Apr 20 09:04:10 2021
"""

import pandas as pd
import matplotlib.pyplot as plt

diagrama_data = pd.read_excel('diagrama_peso_posicao.xlsx')
diagrama_data.drop(diagrama_data.iloc[:,-3:], axis = 1, inplace = True)
diagrama_data.drop(index = 0, inplace = True)

colunas = ['n','desc','W','x','W.x','x_cg','cma']
diagrama_data.columns = colunas



#%% Diagrama: Peso x Posição do CG
data_xW = diagrama_data[['W', 'x_cg']].dropna()
data_xW = data_xW.reindex(index = [5,7,9,11,13,21,19,17,15,5])

fig_dia = plt.figure(figsize=(7,5))

plt.plot(data_xW['x_cg'], data_xW['W'], '-o')
plt.grid()
plt.xlabel("x (m)")
plt.ylabel("Peso (N)")
plt.title("Diagrama: Peso $\\times$ Posição do CG")

for i in range(0, len(data_xW)):
    x_cg = data_xW.iloc[i,:].values[1]
    W_cg = data_xW.iloc[i,:].values[0]
    text = data_xW.index[i]
    plt.text(x_cg + 0.001, W_cg,  text, fontsize = 12)

plt.tight_layout()
plt.show()

