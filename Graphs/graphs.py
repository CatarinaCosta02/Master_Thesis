import matplotlib.pyplot as plt
import numpy as np

# Classes / doenças
classes = ['2724', '4019', 'E785', 'Z87891', 'E039', 'Z794']

# Métricas por modelo
metrics_rf = {'Precision': [0.70,0.74,0.60,0.53,0.71,0.50],
              'Recall':    [0.79,0.63,0.56,0.31,0.96,0.58],
              'F1-score':  [0.74,0.68,0.58,0.39,0.82,0.54]}

metrics_svm = {'Precision': [0.65,0.46,0.69,0.48,0.71,0.52],
               'Recall':    [0.68,0.56,0.43,0.24,0.99,0.65],
               'F1-score':  [0.66,0.51,0.53,0.32,0.83,0.58]}

metrics_xgb = {'Precision': [0.68,0.77,0.62,0.61,0.72,0.51],
               'Recall':    [0.82,0.62,0.57,0.25,0.98,0.67],
               'F1-score':  [0.74,0.69,0.59,0.35,0.83,0.58]}

# Configurações
bar_width = 0.25
x = np.arange(len(classes))

# Paleta em tons de azul e cinza
colors = {
    'Random Forest': '#4B8BBE',  # azul médio (Python blue)
    'SVM': '#A9A9A9',            # cinza médio
    'XGBoost': '#1F3A93'         # azul escuro
}

# Criar gráfico separado para cada métrica
for metric in ['Precision', 'Recall', 'F1-score']:
    plt.figure(figsize=(10,5))
    
    plt.bar(x - bar_width, metrics_rf[metric], width=bar_width, label='Random Forest', color=colors['Random Forest'])
    plt.bar(x, metrics_svm[metric], width=bar_width, label='SVM', color=colors['SVM'])
    plt.bar(x + bar_width, metrics_xgb[metric], width=bar_width, label='XGBoost', color=colors['XGBoost'])
    
    plt.xticks(x, classes)
    plt.ylim(0, 1)
    plt.xlabel('IDC_Code Disease')
    plt.ylabel(metric)
    plt.title(f'Model comparison in {metric}')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()