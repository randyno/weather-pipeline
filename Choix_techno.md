
## Serveur de données :
Nous avions deux possibilités :
- MySQL (déjà utilise avant)
- DuckDB (suite a une recommandation pour ce cas d'usage)

| Caractéristique | MySQL | DuckDB |
| Type | Serveur (Lourd) | Fichier (Léger)|
| Installation | Nouveau service Docker | Juste une library Python |
| Vitesse (Calculs) | Standard | Très rapide (Vectorisé) |
| Lecture CSV | Import manuel requis | Lecture directe native |
| Usage idéal | Application Web | Pipeline de données / dbt |