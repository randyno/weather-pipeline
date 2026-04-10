
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

==> `DuckDB` car simple a installer, rapide, lit les fichiers `.csv`

## Outil de visualisation 
Contraintes : 
* Je ne maitrise pas les langages de developpement Web (JS, HTML, CSS)
* Je ne maitrise pas non plus Django


Technologie | Langage principal | Courbe d'apprentissage | Effort de design
Streamlit | Python | Facile | Faible (automatique)
Evidence | SQL / Markdown | Très Facile | Très faible (élégant)
Superset | No-Code (Interface) | Moyenne (config Docker) | Personnalisable