import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import LabelEncoder

#chargement des donnees
data = pd.read_csv('rendement_mais.csv')

#moyenne, median; mode
moyenne = data['RENDEMENT_T_HA'].mean()
mediane = data['RENDEMENT_T_HA'].median()
mode = data['RENDEMENT_T_HA'].mode()[0]

print(f"Moyenne du rendement : {moyenne}")
print(f"Médiane du rendement : {mediane}")
print(f"Mode du rendement : {mode}")

#ecart-type, variance, etendu
ecart_type = data['RENDEMENT_T_HA'].std()
variance = data['RENDEMENT_T_HA'].var()
etendue = data['RENDEMENT_T_HA'].max() - data['RENDEMENT_T_HA'].min()

print(f"Écart-type du rendement : {ecart_type}")
print(f"Variance du rendement : {variance}")
print(f"Étendue du rendement : {etendue}")

#LEs Histogrammes
fig, axes = plt.subplots(1, 3, figsize=(15, 7))
sns.histplot(data['RENDEMENT_T_HA'], kde=True, ax=axes[0]).set_title("Histogramme du rendement")
sns.histplot(data['PRECIPITATIONS_MM'], kde=True, ax=axes[1]).set_title("Histogramme des precipitations")
sns.histplot(data['TEMPERATURE_C'], kde=True, ax=axes[2]).set_title("Histogramme de la temperature")
plt.tight_layout()

#Les Boxplots
fig, axes = plt.subplots(1, 3, figsize=(15, 7))
sns.boxplot(x=data['RENDEMENT_T_HA'], ax=axes[0]).set_title("Boxplot du rendement")
sns.boxplot(x=data['PRECIPITATIONS_MM'], ax=axes[1]).set_title("Boxplot des precipitations")
sns.boxplot(x=data['TEMPERATURE_C'], ax=axes[2]).set_title("Boxplot de la temperature")
plt.tight_layout()

# plt.show()

#Selection toutes sauf type_sol qui est un string


#matrice de corelation
encoder = LabelEncoder()
data["TYPE_SOL"] = encoder.fit_transform(data['TYPE_SOL'])
corr_matrix = data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True)
plt.title("Matrice de Correlation")
plt.show()