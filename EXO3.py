import pandas as pd
from scipy import stats

data = pd.read_csv('rendement_mais.csv')

# Creation des groupes
type_sols = data['TYPE_SOL'].unique()
groupes = [data[data['TYPE_SOL'] == type_sol]['RENDEMENT_T_HA'] for type_sol in type_sols]

# le test ANOVA
f_stat, p_value = stats.f_oneway(*groupes)

# Affichage des resultas
print(f"F : {f_stat}")
print(f"P-value : {p_value}")
