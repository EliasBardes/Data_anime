# 🎬 Anime Recommendation Engine

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Pandas](https://img.shields.io/badge/Data-Analysis-green)

Une application Data-Driven pour identifier les **"Pépites"** (Hidden Gems) dans un catalogue d'animés en utilisant un algorithme de scoring pondéré.

## 📊 Le Problème
Se fier uniquement à la note moyenne d'un animé est trompeur. Une série peut avoir une bonne moyenne mais une fin catastrophique, ou être très irrégulière.
**Objectif :** Construire un outil d'aide à la décision pour recommander des œuvres fiables.

## 💡 La Solution Technique
Le projet se divise en deux parties :

1.  **Le Backend Analytique (Jupyter Notebook)** :
    * Nettoyage des données brutes.
    * **Feature Engineering :** Création d'un *Score de Fiabilité* qui prend en compte la note du pire épisode (risque) et l'écart-type (régularité).
    * Génération d'un verdict explicable (Pourquoi cet animé est-il rejeté ?).

2.  **Le Frontend (Streamlit)** :
    * Dashboard interactif pour explorer le catalogue.
    * Affichage des "Cartes Animés" avec code couleur (Pépite / Prometteur / Risqué).
    * Explicabilité du verdict en temps réel.

## 🛠️ Installation & Lancement

1.  **Cloner le projet :**
    ```bash
    git clone [https://github.com/ton-pseudo/anime-recommender.git](https://github.com/ton-pseudo/anime-recommender.git)
    cd anime-recommender
    ```

2.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Générer les données (ETL) :**
    Ouvrez et exécutez le notebook `Analyse_Editoriale_Animes.ipynb` pour créer le fichier `animes_data_v3.csv`.

4.  **Lancer l'application Web :**
    ```bash
    streamlit run app.py
    ```

## 🧮 L'Algorithme de Scoring
Le score est calculé selon la formule suivante :
> `Score = (0.6 * Moyenne) + (0.3 * Min) - (0.1 * Ecart)`

Cette approche favorise la **régularité** et la **sûreté** éditoriale plutôt que les pics de "hype".

---
*Projet réalisé dans le cadre d'un Bachelor Data & AI.*
