import streamlit as st
import pandas as pd

# ==============================================================================
# 1. CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="Anime Recommender",
    page_icon="🎬",
    layout="wide"
)

# Titre Principal
st.title("🎬 Moteur de Recommandation d'Animés")
st.markdown("Ce site utilise un algorithme d'analyse de données pour détecter les pépites.")

# ==============================================================================
# 2. LÉGENDE (Guide des couleurs)
# ==============================================================================
with st.expander("ℹ️ **Guide des Couleurs (Légende)**", expanded=True):
    col_leg1, col_leg2, col_leg3 = st.columns(3)
    
    with col_leg1:
        st.markdown("### 🏆 :green[PÉPITE]")
        st.markdown("L'animé est **terminé** et validé. C'est une valeur sûre.")
    
    with col_leg2:
        st.markdown("### 🔥 :blue[PROMETTEUR]")
        st.markdown("L'animé est **en cours**, mais la qualité actuelle est excellente (> 8/10).")
        
    with col_leg3:
        st.markdown("### ❌ :red[REJETÉ / RISQUÉ]")
        st.markdown("L'animé ne remplit pas les critères (trop irrégulier, note faible ou fin ratée).")

st.divider()

# ==============================================================================
# 3. CHARGEMENT DES DONNÉES (Sécurisé - VERSION 3)
# ==============================================================================
try:
    # MODIFICATION IMPORTANTE ICI : On charge le fichier V3 !
    df = pd.read_csv('animes_data_v3.csv')
except FileNotFoundError:
    st.error("⚠️ Fichier de données 'animes_data_v3.csv' introuvable.")
    st.info("💡 Solution : Retourne sur ton Notebook et lance la cellule de génération V3.")
    st.stop()

# ==============================================================================
# 4. BARRE LATÉRALE (FILTRES)
# ==============================================================================
st.sidebar.header("Filtres")

# Filtre par statut
if 'Status' in df.columns:
    options_statut = df['Status'].unique()
    choix_statut = st.sidebar.multiselect(
        "Statut de l'animé", 
        options=options_statut,
        default=options_statut
    )
    # Application du filtre
    df_affiche = df[df['Status'].isin(choix_statut)]
else:
    df_affiche = df

# ==============================================================================
# 5. AFFICHAGE DES CARTES (GRID)
# ==============================================================================
cols = st.columns(3) 

for index, row in df_affiche.iterrows():
    col = cols[index % 3]
    
    with col:
        # 1. Style selon le verdict
        css_class = row.get('CSS_Class', 'status-rejected')
        
        if css_class == 'status-pepite':
            couleur_titre = "green"
            icone = "🏆"
        elif css_class == 'status-hyped':
            couleur_titre = "blue"
            icone = "🔥"
        else:
            couleur_titre = "red"
            icone = "❌"

        # 2. Explication (ne plantera plus car le fichier v3 contient la colonne)
        explication = row.get('Explication_Verdict', "Pas d'explication disponible.")

        # 3. Carte Visuelle
        with st.container():
            st.markdown(f"### {icone} :{couleur_titre}[{row['Anime']}]")
            st.caption(f"Note : **{row['Note_Globale']}/10** | {row['Nb_Episodes']} éps | {row['Status']}")
            
            # Affichage du message
            if css_class == 'status-rejected':
                st.error(f"**Verdict :** {explication}")
            else:
                st.success(f"**Verdict :** {explication}")
            
            # Score
            if 'Score_Prometteur' in row:
                st.metric("Score de Fiabilité", row['Score_Prometteur'])
            
            st.divider()