Pour cette fonctionnalite, nous allons entrainer plusieurs models afin de predire la temperature des 24 prochaines heures. 
- Modele 1 : Regression lineaire (scikit-learn)
- Modele 2 : RandomForestRegressor (scikit-learn)
- Model 3 : xgboost
- Model 4 : Prophet (Meta) -- Utile dans les predictions sur l'economie et les series temporelles meteo

Modèle|Type|Force|Pourquoi l'employer dans ce projet ?
Régression Linéaire|Linéaire|Simplicité absolue|"Sert de ""Baseline"". Si tes autres modèles ne font pas mieux| c'est qu'ils ""overfittent""."
K-Nearest Neighbors (KNN)|Non-paramétrique|Logique de voisinage|"Prédit la température en regardant les moments passés qui ""ressemblaient"" à aujourd'hui."
Random Forest Regressor|Ensemble (Baggage)|Robustesse|"Gère très bien les relations complexes entre vent| humidité et nuages sans réglage complexe."
XGBoost ou LightGBM|Boosting|Performance pure|C'est le standard de l'industrie. Très rapide à entraîner sur 1 200 lignes.