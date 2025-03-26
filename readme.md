
# Rapport TD ATDN 1 Bouizegarene Hachimi




### EXO 1 :

![Exo 1 PNG](https://raw.githubusercontent.com/HachimiBouizegarene/ATDN2-TD1/refs/heads/master/assets/IMG_0206.jpg)
### Exo 2 :
#### 2.1, 2.2 Resultats : 
```
- Moyenne du rendement : 7.378418687218944
- Médiane du rendement : 7.349138167259971
- Mode du rendement : 3.000276469608442
- Écart-type du rendement : 2.569990985326707
- Variance du rendement : 6.6048536646605385
- Étendue du rendement : 8.995742859645505

```

#### 2.3 :

**histogrammes :**

![Exo 2 Histogramme](https://github.com/HachimiBouizegarene/ATDN2-TD1/blob/master/assets/exo-2-2.1_2.3-histogramme.png?raw=true)

**boxplots :**

![Exo 2 boxplots](https://github.com/HachimiBouizegarene/ATDN2-TD1/blob/master/assets/exo-2-2.1_2.3-box.png?raw=true)

#### 2.4 :
**Matrice de corrélation :**

![Exo 2 boxplots](https://github.com/HachimiBouizegarene/ATDN2-TD1/blob/master/assets/exo-2-2.1_2.4.png?raw=true)

### EXO3 :
**Resultats :**
```
F : 1.3560517305539426
P-value : 0.2581509831874908
```
**Interpretation :**\
p-value est trop élevée. Cela suggère que le type de sol n'affecte pas le rendement de manière significative. 

Cela valide l'Hypothèse H0 : Le type de sol n'influence pas le rendement.

### EXO4 :
J'ai divisé les données en 80 % pour l'entraînement et 20 % pour le test. Après avoir essayé une régression linéaire et une régression polynomiale de degré 2, j'obtiens ces résultats :
```
MAE Regression lineaire : 2.0946431257300704
MSE, Regression lineaire : 6.054354910757684
RMSE, Regression lineaire : 2.4605598774989574
MAE Regression polynomiale : 2.2071139666509576
MSE Regression polynomiale : 6.464510519678741
RMSE Regression polynomiale : 2.542540170710925
```
Les résultats sont médiocres, puisque si l'on utilise une méthode naïve consistant à dire que la prédiction est égale à la moyenne des données d'entraînement (y_train), on obtient de meilleurs résultats. Cela rend donc le modèle inutile. Je m'attendais à ces résultats, puisque les données ne sont pas suffisamment corrélées, comme on l'a vu dans l'exercice précédent.