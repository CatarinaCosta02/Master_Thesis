import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Dados: 3 tentativas por índice
runs = {
    'L2': [131.1493, 120.0852, 120.9731],
    'Cosine': [142.6558, 76.6456, 46.4067],
    'HNSW': [13.2484, 0.9880, 2.6464],
    'LSH': [25.4655, 11.9200, 8.9121]
}

# Calcular médias
means = {idx: np.mean(vals) for idx, vals in runs.items()}

# Preparar DataFrame
df = pd.DataFrame(runs)

# Parâmetros de plot
indices = list(df.columns)
x = np.arange(len(indices))
width = 0.2

fig, ax = plt.subplots(figsize=(10,5))

colors = [ '#4B8BBE', "#7ab5f5", '#1F3A93']  # cores das 3 runs
mean_color = '#A9A9A9' # cor da média

# Barras das runs
for i in range(3):
    ax.bar(x - 1.5*width + i*width, df.iloc[i], width, label=f'Run {i+1}', color=colors[i])

# Barra da média (deslocada à direita)
ax.bar(x + 1.5*width, [means[idx] for idx in indices], width, label='Mean', color=mean_color)

# Configurações
ax.set_xticks(x)
ax.set_xticklabels(indices, fontsize=11)
ax.set_ylabel('Search Time (ms)', fontsize=12)
ax.set_title('FAISS Index Search Time', fontsize=14, fontweight='bold')
ax.legend(frameon=False)
ax.grid(axis='y', linestyle='--', alpha=0.4)

# Adicionar valores nas barras
for i in range(3):
    for j, val in enumerate(df.iloc[i]):
        ax.text(j - 1.5*width + i*width, val + 2, f'{val:.1f}', ha='center', va='bottom', fontsize=9)

for j, val in enumerate([means[idx] for idx in indices]):
    ax.text(j + 1.5*width, val + 2, f'{val:.1f}', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()


# -------------------------------
# GRÁFICO 2: BOXPLOT
# -------------------------------

plt.figure(figsize=(10,5))
plt.boxplot(runs.values(), labels=runs.keys(), patch_artist=True,
            boxprops=dict(facecolor='#4B8BBE', color='#4B8BBE'),
            medianprops=dict(color='black'),
            whiskerprops=dict(color='#4B8BBE'),
            capprops=dict(color='#4B8BBE'))
plt.ylabel('Search Time (ms)')
plt.title('FAISS Index Search Times Distribution ', fontsize=14, fontweight='bold')
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.show()