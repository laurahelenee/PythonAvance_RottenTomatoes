import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.figure_factory as ff

#import de la base de données issue de PySpark
best_movies_at_home = pd.read_csv("best_movies_at_home_final.csv",sep=';',on_bad_lines='skip')


#création de 5 onglets différents dans le streamlit
tabs = st.tabs(["Présentation", "Sommaire", "Etude préliminaire", "Etude des reviews", "Recommandation de films"])
tab_plots0 = tabs[0]
tab_plots = tabs[3]
tab_plots1 = tabs[2]
tab_plots3 = tabs[4]
tab_plots10 = tabs[1]


#premier onglet : réalisation d'une présentation générale du travail + de la base de données
with tab_plots0:
    
    st.progress(20) #barre de progression implémentée au fur et à mesure des pages
    
    
    st.title('Etude des meilleurs films à regarder chez soi en Janvier 2023, selon le site Rotten Tomatoes')
    #import d'une image lié au site Rotten Tomatoes
    st.image("https://www.rottentomatoes.com/assets/pizza-pie/head-assets/images/RT_TwitterCard_2018.jpg")

    #rédaction de la présentation générale
    st.markdown(
    """
    Le site **Rotten Tomatoes** (www.rottentomatoes.com) est un site américain dédié à **la critique de films provenant du monde entier**. Il permet, à chaque instant et dès la sortie du film, de retrouver l'ensemble des informations  sur le film en question ainsi que des indicateurs permettant à l'utilisateur d'en jauger la qualité, de façon relativement objective. Au delà de cet aspect plutôt technique, ce site publie également des articles sur différents aspects de l'univers cinématographique, basé sur ces données.
    
    """)
    st.markdown(
    """
Dans le cadre de ce projet, nous avons donc récupéré les données provenant d'un de ces articles, détaillant **150 films que l'auteur conseillait de regarder à la maison, en janvier 2023.** Au délà de la récupération des données disponibles sur la première page du site internet, nous avons également récupéré, à l'aide de Python, des informations propres à chaque film, trouvable en cliquant sur chacune des icônes de la page principale.
    
    """)
    
    st.markdown(
    """
Une fois cette étape réalisée, nous avons donc récupéré une base de données contenant l'ensemble des films de l'article choisi. Dans un second temps, nous avons donc ensuite procédé à une création de différentes variables à l'aide du language de programmation PysPark, avec comme objectif d'avoir une base de données **plus complète et correctement définie.** La dataframe finale est alors représentée ci-dessous, accompagné d'un dictionnaire expliquant les différentes variables de la base de données. 
    \n
    """)
    #affichage de la base de données
    st.dataframe(best_movies_at_home)
    
    
    #définition du dictionnaire des variables
    st.header(" \n Dictionnaire des variables \n")
        
    st.markdown(
        """
- **titles** : Titre des films
- **audience scores** : Pourcentage des utilisateurs ayant accordé une note positive au film parmi l'ensemble des gens l'ayant noté
- **audience state** : Classification des films selon le score du public (si plus de 60% des utilisateurs ont accordé une note de 3,5/5 au film en question, le film est jugé "Upright", sinon il est jugé "Spilled")
- **tomatometer** : Pourcentage des critiques professionnels ayant accordé une note positive au film parmi l'ensemble des spécialistes l'ayant noté.
- **tomatometer state** : Classification des films selon le tomatometer (si plus de 60% des critiques d'un film sont positives, le film est jugé "Fresh tandis que si c'est inférieur, il est jugé "Rotten"). Cependant, un film peut également être jugé "Certified fresh" sous certaines conditions (tomatometer supérieur à 75%, au moins 5 critiques par des "Top critics" etc...)
- **critics consensus** : Résumé de l'ensemble des critiques réalisés par les critiques professionnels.
- **Trigger Warning** : Classement du film selon la partie de la population à qui il s'adresse (PG-13...)
- **Language** : Langue principale parlée dans le film
- **Director** : Directeur(s) du film
- **Producer** : Producteur(s) du film
- **Box-office (in M$)** : Nombre d'argents qu'à rapporté le film lors de son passage au cinéma
- **Distributor** : Distributeur du film (Netflix...)
- **Release year** : Année de sortie du film
- **Full length** : Durée du film en minutes
- **Genre n°1** : Premier genre cinématographique du film
- **Genre n°2** : Second genre cinématographique du film
- **Genre n°3** : Troisième genre cinématographique du film
- **Release date (in date)** : Date de sortie du film
- **Current date** : Date à laquelle a été réalisé le WebScrapping
- **Number of days since the release** : Nombre de jours écoulés entre la date de sortie du film et le jour durant lequel le WebScrapping a été réalisé
    
        """)


    
#nouvel onglet : rédaction d'un sommaire
with tab_plots10:
    st.progress(40)

    
    st.header("Sommaire")
        
    st.markdown(
"""
- **"Analyse descriptive des films"** : Réalisation d'une analyse descriptive pour déterminer les caractéristiques des films de cette base de données.
- **"Etude des reviews"** : A l'aide d'un processus de text-mining, réalisation d'une étude du consensus critique associé à chaque film
- **"Recommandation de films"** : Réalisation d'un processus permettant de recommander un film de cette base de données, selon les caractéristiques souhaitées.
"""
)
    
             
#réalisation du troisième onglet : réalisation d'une analyse descriptive
with tab_plots1:
    st.progress(60)
    
    #import des librairies nécessaires à la réalisation de ces graphiques
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    st.title('Analyse descriptive des films')
    
    #réalisation d'un pie chart pour les états du tomatometer
    col31,colT38 = st.columns([1,12])
    with colT38:
        st.markdown(" **Répartition des états selon le score Tomatometer** \n")
    pie_tomato = px.pie(best_movies_at_home, values=best_movies_at_home['tomatometer state'].value_counts().to_list(), names=best_movies_at_home['tomatometer state'].unique().tolist(), 
             color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(pie_tomato, use_container_width=True)
    
    #réalisation d'un pie chart pour les états des scores du public
    col31,colT37 = st.columns([1,12])
    with colT37:
        st.markdown(" **Répartition des états selon le score du public** \n")
    pie_audience = px.pie(best_movies_at_home, values=best_movies_at_home['audience state'].value_counts().to_list(), names=best_movies_at_home['audience state'].unique().tolist(), 
             color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(pie_audience, use_container_width=True)
    
    st.markdown(
        """
        On remarque alors que les critiques provenant des utilisateurs du site internet et des critiques professionnels sont **globalement assez similaires** vis-à-vis des films de la base de données : 85% des films reçoivent un avis globalement positif tandis que 15% en reçoivent un plutôt négatif
        """)
    
    #réalisation d'un pie chart pour les langues des différents films
    col31,colT36 = st.columns([1,12])
    with colT36:
        st.markdown(" **Répartition des langues parlées** \n")
    pie_language = px.pie(best_movies_at_home, values=best_movies_at_home['Language'].value_counts().to_list(), names=best_movies_at_home['Language'].unique().tolist(), 
             color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(pie_language)
    
    #réalisation d'un pie chart pour les genres des différents films

    col31,colT35 = st.columns([1,12])
    with colT35:
        st.markdown(" **Répartition des genres** \n")
    pie_genre_1 = px.pie(best_movies_at_home, values=best_movies_at_home['Genre n°1'].value_counts().to_list(), names=best_movies_at_home['Genre n°1'].unique().tolist(), 
             color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(pie_genre_1)
    
    st.markdown(
        """
Les films de ce classement sont majoritairement destinés à **un public anglophone**, avec 9 films sur 10 où la langue majoritaire est l'anglais. Cela peut démontrer d'un manque de développement à l'international de ce site internet.
Les genres des films sont cependant **beaucoup plus diversifiés avec une répartition presque équipondérante entre des genres très différents** tels que les films d'horreur, les films comiques, les thrillers ou les films familiaux
        """)
    st.header('Etude des caractéristiques des films')
    st.subheader('Statistiques descriptives sur la notation des films ')

    col1, col2 = st.columns(2) #on créée 2 colonnes pour stocker nos métriques

    #moyenne des tomatometer et audience scores arrondis au centième près
    tomatomean = round(best_movies_at_home['tomatometer'].mean(),2) 
    audiencemean = round(best_movies_at_home['audience scores'].mean(),2)
    col1.metric("Average tomatometer score",tomatomean)
    col2.metric("Average audience score",audiencemean)

    #minimum des scores d'audience et tomato 
    tomatomin = round(best_movies_at_home['tomatometer'].min(),0)
    audiencemin = round(best_movies_at_home['audience scores'].min(),0)
    col1.metric("Minimum tomatometer score",tomatomin)
    col2.metric("Minimum audience score",audiencemin)

    #maximum des scores d'audience et tomato
    tomatomax = best_movies_at_home['tomatometer'].max()
    audiencemax = best_movies_at_home['audience scores'].max()
    col1.metric("Maximum tomatometer score",tomatomax)
    col2.metric("Maximum audience score",audiencemax)    


    #réalisation d'une étude du box office : calcul de la moyenne, écart type, minimum et maximum
    st.subheader("Etude du Box-Office")
        
    kpi1, kpi2 = st.columns(2) #permet de mettre la moyenne et l'écart type côte à côte
    mean_box_office = round(best_movies_at_home['Box-office (in M$) '].mean(),0) #définition de la moyenne
    #représentation de la moyenne des recettes
    kpi1.metric(
        label="Moyenne des recettes au box-office",
        value= "$" + str(mean_box_office) + "M")
    
    std_box_office = round(best_movies_at_home['Box-office (in M$) '].std(),0) #définition de l'écart type
    #représentatin de l'écart type des recettes
    kpi2.metric(
        label="Ecart type des recettes au box-office",
        value= "$" + str(std_box_office) + "M")

    kpi3, kpi4 = st.columns(2) #permet de mettre le minimum et le maximum côte à côte
    min_box_office = round(best_movies_at_home['Box-office (in M$) '].min(),0)
    max_box_office = round(best_movies_at_home['Box-office (in M$) '].max())

    #définition des films avec la recette minimale et la recette maximale pour les ajouter à côté de la valeur minimale et maximale
    max_box_office_film = best_movies_at_home[best_movies_at_home['Box-office (in M$) ']==max_box_office]['titles'].values[0]
    min_box_office_film = best_movies_at_home[best_movies_at_home['Box-office (in M$) ']==min_box_office]['titles'].values[0]

    kpi3.metric(    
        label="Minimum des recettes au box-office : " + str(min_box_office_film),
        value= "$" + str(min_box_office) + "M") #ajout de la valeur minimale de recettes + du film pour lequel c'est le cas

    kpi4.metric(    
        label="Maximum des recettes au box-office : " + str(max_box_office_film),
        value= "$" + str(max_box_office) + "M") #ajout de la valeur maximale de recettes + du film pour lequel c'est le cas
    
    st.markdown(
        """
           \n
        Les recettes moyennes des films de la base de données se situent ainsi autour de **100M de dollars**, ce qui nous démontre que **les films sélectionnés sont avant tout des films ayant eu un certain succès populaire**. Cependant, ce résultat peut être considéré comme **biaisé**. En effet, **l'écart type est assez important, démontrant d'une forte hétérogénéité** entre les recettes des différents films. Si on observe le film ayant rapporté le plus de recettes (Avengers : ENDGAME) à un niveau de recettes de 858M de dollars, on peut penser que **la moyenne observée a été tiré vers le haut par les "super-productions" (Marvel...) dont les recettes sont toujours majoritairement plus élevées que l'ensemble des films.** Cela expliquerait alors la forte hétérogénéité observée dans la base de données.
        """)
    
    #réalisation d'une étude de la moyenne, écart type, minimum et maximum de la durée des films
 
    st.subheader("Etude de la durée des films")
        
    kpi6, kpi7 = st.columns(2)
    mean_box_office = round(best_movies_at_home['Full length in minutes'].mean(),0)
    kpi6.metric(
        label="Durée moyenne des films",
        value= str(mean_box_office) + " minutes")


    std_box_office = round(best_movies_at_home['Full length in minutes'].std(),0)
    kpi7.metric(
        label="Ecart type de la durée des films",
        value= str(std_box_office) + " minutes")
    
    kpi10, kpi11 = st.columns(2)
    min_duree = round(best_movies_at_home['Full length in minutes'].min(),0)
    max_duree = round(best_movies_at_home['Full length in minutes'].max())

    max_duree_film = best_movies_at_home[best_movies_at_home['Full length in minutes']==max_duree]['titles'].values[0]
    min_duree_film = best_movies_at_home[best_movies_at_home['Full length in minutes']==min_duree]['titles'].values[0]

    kpi10.metric(    
        label="Film le plus court : " + str(min_duree_film),
        value=  str(min_duree) + " minutes")

    kpi11.metric(    
        label="Film le plus long : " + str(max_duree_film),
        value=  str(max_duree) + " minutes")
    
    
    st.markdown(
        """
La durée moyenne des films de cette article est donc** d'environ 1h50**. Le faible écart type (21 minutes) nous indique que **la durée des films est plutôt homogène autour de cette médiane**, malgré quelques exceptions comme Avengers : ENDGAME, film ayant une durée de plus de 3h. 
        """)
        
    #réalisation de la moyenne, écart type ainsi que minimum et maximum de l'ancienneté des différents films
    st.subheader("Ancienneté des films proposés")
    
    st.markdown("A l'aide de la variable \"Number of days since the release\" construire au préalable, il est possible de réaliser une étude de l'ancienneté des films proposés dans cette article")
    
    kpi12, kpi13 = st.columns(2)
    mean_jour = round(best_movies_at_home['Number of days since the release'].mean(),0)
    kpi12.metric(
        label="Ancienneté moyenne des films",
        value= str(mean_jour) + " jours")


    std_jour = round(best_movies_at_home['Number of days since the release'].std(),0)
    kpi13.metric(
        label="Ecart type de l'ancienneté des films",
        value= str(std_jour) + " jours")
    
    kpi14, kpi15 = st.columns(2)
    min_jour = round(best_movies_at_home['Number of days since the release'].min(),0)
    max_jour = round(best_movies_at_home['Number of days since the release'].max())

    max_jour_film = best_movies_at_home[best_movies_at_home['Number of days since the release']==max_jour]['titles'].values[0]
    min_jour_film = best_movies_at_home[best_movies_at_home['Number of days since the release']==min_jour]['titles'].values[0]

    kpi14.metric(    
        label="Film le plus récent : " + str(min_jour_film),
        value= str(min_jour) + " jours")

    kpi15.metric(    
        label="Film le plus ancien : " + str(max_jour_film),
        value= str(max_jour) + " jours")
    
    st.markdown(
        """
        L'ancienneté moyenne des films de la base de données est donc **d'environ 2 ans** : malgré une rédaction récente, les films recommandés ne sont pas nécessairement récents. De plus, comme on l'observe avec **cet important écart-type**, on remarque que la base de données contient des films à la fois anciens et récents, **de façon hétérogène**.
        """)

    st.header('Distribution des variables numériques')
    #distribution des scores tomatometer
    histo_tomatometer = px.histogram(best_movies_at_home, x='tomatometer', title="Distribution des scores par Rotten Tomatoes")
    st.plotly_chart(histo_tomatometer)

    #distribution des scores d'audience
    histo_audience = px.histogram(best_movies_at_home, x='audience scores', title="Distribution des scores d'audience")
    st.plotly_chart(histo_audience)

    st.markdown('''
    
 Les films de ce classement sont principalement bien notés par Rotten Tomatoes et l'audience, bien que les scores accordés par le site soient
 plus élevés que ceux accordés par l'audience. En effet, on tend à voir une concentration des scores en fin de distribution pour les scores accordés
 par Rotten Tomatoes, contrairement aux scores accordés par l'audience qui sont un peu mieux répartis. 
    
    ''')

    #distribution des chiffres du box office
    histo_box_office = px.histogram(best_movies_at_home, x='Box-office (in M$) ', title="Distribution du Box-Office")
    st.plotly_chart(histo_box_office)
    st.markdown('''
 La plupart des films situés dans ce classement ont des chiffres en termes de Box-Office inférieurs à $200M. Il existe néanmoins des films qui connaissent un plus grand succès, 
 mais représentent une part infime du classement des films.     
    ''')

    st.header('Etude des corrélations entre les variables numériques')
    
    df_col = best_movies_at_home[['audience scores', 'tomatometer', 'Box-office (in M$) ', 'Full length in minutes', 
                              'Number of days since the release']]
    fig, ax = plt.subplots()

    sns.heatmap(df_col.corr(), ax=ax, annot=True)

    st.write(fig)

    st.markdown('''
    Sur la matrice des corrélations, on voit que les variables sont très peu corrélées entre elles : les variables les plus corrélées sont le box-office et la durée en minutes du film. 
    \n En effet, on voit des coefficients de corrélation avoisinant les 0 pour la plupart des corrélations prises deux à deux. 
    ''')

    st.subheader('Etude visuelle des relations entre variables')

    #scatter plot avec le box office en fonction du nombre de jours après le lancement du film
    fig = px.scatter(best_movies_at_home, x="Number of days since the release", y="Box-office (in M$) ", hover_name="titles",size_max=60, title="Evolution du box-office basé sur l'ancienneté du film :")
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    st.markdown('''
    On remarque que l'ancienneté du film n'a pas d'impact sur les chiffres du box-office d'un film. Les films ayant fait un gros chiffre au box office ne sont pas forcément ceux qui sont 
    les plus anciens.  
    ''')

    #scatter plot avec le box office en fonction des scores d'audience
    fig1 = px.scatter(best_movies_at_home, x="audience scores", y="Box-office (in M$) ", hover_name="titles", title="Evolution du box-office basé sur le score de l'audience :")
    st.plotly_chart(fig1, theme="streamlit", use_container_width=True) 
    st.markdown('''
    A travers ce graphique, on voit que ceux qui font le meilleur score en termes d'audience ne sont pas forcément ceux qui ont fait le plus gros chiffre en termes de box-office. 
    De plus, il n'y a pas de relation flagrante entre les deux variables. 
    ''')

    #scatter plot avec le box office en fonction de la durée du film
    fig2 = px.scatter(best_movies_at_home, x="Full length in minutes", y="Box-office (in M$) ", hover_name="titles", title="Evolution du box-office basé sur la longueur du film en minutes :")
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)
    st.markdown('''
    Etant donné que nous avons beaucoup de films récents dans notre classement, nous voyons une concentration des points sur le côté inférieur gauche du graphique. On ne voit cependant
    pas de lien entre la durée du film en minutes et le box-office. 
    ''')

    #scatter plot avec les scores en fonction du tomatometer
    fig_link_audience_tomato = px.scatter(best_movies_at_home, x="tomatometer", y="audience scores", color="Language", hover_name="titles",size_max=60, title="Relation entre le tomatometer et le score d'audience :")
    st.plotly_chart(fig_link_audience_tomato, theme="streamlit", use_container_width=True)
    st.markdown('''
    La forte concentration des observations sur le coin droit supérieur du graphique témoigne des scores élevés des films, à la fois au niveau du tomatometer et au niveau des scores d'audience.
    Cependant, la répartition des points sur le graphique ne semble pas montrer de relation marquante entre les deux variables, du fait que l'avis entre Rotten Tomatoes et l'audience peut diverger. 
    ''')

    #scatter plot avec les minutes en fonction de l'ancienneté du film
    fig_link_length_days = px.scatter(best_movies_at_home, x="Number of days since the release", y="Full length in minutes", hover_name="titles",size_max=60, title="Relation entre la durée et l'ancienneté du film :")
    st.plotly_chart(fig_link_length_days, theme="streamlit", use_container_width=True)
    st.markdown('''
    Notre classement comporte beaucoup de films récents. A priori, l'ancienneté du film ne semble pas impacter la durée du film, étant donné qu'on ne voit pas de relation entre les deux
    variables à travers notre plot. 
    ''')

    

#nouvel onglet : réalisation d'une étude des consensus critiques déterminés pour chacun des films 
with tab_plots:
    st.progress(80)

    st.header('Etude des reviews')
    
    st.markdown('Basé sur les critiques déposés par les spécialistes, un avis général vis-à-vis du film est rédigé pour chacun des films, donnant une idée de **l\'avis majoritaire concernant le ce film.**')
    
    st.markdown('Cependant, étant donné qu\'il s\'agit de phrases, **il n\'est pas possible de réaliser les mêmes études que précedemment** (graphique de répartition, étude des corrélations). Néanmoins, ces commentaires contiennent **des informations pertinentes concernant les spécificités des films** que l\'on ne retrouve pas dans les autres variables. Ainsi, il est nécessaire de **les analyser d\'une façon différente**')
    
    st.markdown('Pour cela, on a privilégié **la réalisation d\'un nuage de mots ("WordCloud") : cela va nous permettre d\'afficher les mots les plus courants** parmi les avis de l\'ensemble des films de cette base de données. On peut ainsi réaliser la réprésentation suivante sur l\'ensemble de la base de données :')
                
    #changement du nom des colonnes pour favoriser le code
    best_movies_at_home = best_movies_at_home.rename(columns={"critics consensus": "critics_consensus"})
    best_movies_at_home = best_movies_at_home.rename(columns={"tomatometer state": "tomatometer_state"})

    #récupération dans une variable text de l'ensemble des consensus critiques des films de la base de données
    text = ""
    for comment in best_movies_at_home.critics_consensus : 
        text += comment
    
    #réalisation d'un wordcloud > import des librairies
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    
    #définition des caractéristiques du wordcloud (couleur, nb de mots à disposer au maximum, police...)
    wc = WordCloud(background_color="white", max_words=1000, max_font_size=50, random_state=42)
    
    #affichage du wordcloud
    fig, ax = plt.subplots(figsize = (12, 8))
    wc.generate(text)          
    ax.imshow(wc)   
    st.pyplot(fig)
    
    st.markdown('Ainsi, **les mots ayant la police la plus grande sont ceux qui reviennent le plus dans les avis généraux**. On peut ainsi indiquer que les mots les plus courants de ces commentaires concernent l\'histoire ("story"), la performance ("performance") ainsi que le casting du film ("cast"). Cependant, une analyse sur la base de données entière est assez limité : **il peut donc être intéressant de réaliser différents nuages de mots sur plusieurs sous-parties du dataframe et d\'en comparer les résultats.** ')

    st.markdown('On a alors trouvé pertinent de **comparer les différents états des scores attribués par l\'audience : **"certified fresh"**, **"fresh"**, **"rotten".** On pourra ainsi trouver les points communs entre les films de ces différentes catégories pour pouvoir déterminer les caractéristiques communes des différentes catégories.')

    st.markdown('On représente alors les trois différents graphiques (de gauche à droite \"rotten\", \"fresh\" et \"certified fresh\" : ')

    #Filtration de la base de données uniquement sur les films classés "rotten"
    best_movies_at_home_rotten = best_movies_at_home[(best_movies_at_home.tomatometer_state == "Rotten")]
                
    #une fois cela fait, on réalise une étude similaire à la précédente, à la différence que celle-ci sera réalisé uniquement sur les films rotten.
    text_rotten = ""
    for comment_rotten in best_movies_at_home_rotten.critics_consensus : 
        text_rotten += comment_rotten
    
    wc_rotten = WordCloud(background_color="white", max_words=1000, max_font_size=50, random_state=42)
    
    fig_rotten, ax_rotten = plt.subplots(figsize = (10, 8))
    wc_rotten.generate(text_rotten)          
    ax_rotten.imshow(wc_rotten)
    
    #Nuage de mots similaire pour les films classifiés "Fresh"
    best_movies_at_home_fresh = best_movies_at_home[(best_movies_at_home.tomatometer_state == "Fresh")]
                
    text_fresh = ""
    for comment_fresh in best_movies_at_home_fresh.critics_consensus : 
        text_fresh += comment_fresh
    
    wc_fresh = WordCloud(background_color="white", max_words=1000, max_font_size=50, random_state=42)
    
    fig_fresh, ax_fresh = plt.subplots(figsize = (10, 8))
    wc_fresh.generate(text_fresh)          
    ax_fresh.imshow(wc_fresh) 
                
    #Nuage de mots similaire pour les films classifiés "Certified fresh"
    best_movies_at_home_certified_fresh = best_movies_at_home[(best_movies_at_home.tomatometer_state == "Certified fresh")]
                
    text_certified_fresh = ""
    for comment_certified_fresh in best_movies_at_home_certified_fresh.critics_consensus : 
        text_certified_fresh += comment_certified_fresh
    
    wc_certified_fresh = WordCloud(background_color="white", max_words=1000, max_font_size=50, random_state=42)
    
    fig_certified_fresh, ax_certified_fresh = plt.subplots(figsize = (10, 8))
    wc_certified_fresh.generate(text_certified_fresh)          
    ax_certified_fresh.imshow(wc_certified_fresh) 

    data_container = st.container()

    #affichage des trois graphiques rotten, fresh et certified fresh côte à côte dans l'application
    with data_container:
        plot1, plot2, plot3 = st.columns(3)
        with plot1:
            st.pyplot(fig_rotten)
        with plot2:
            st.pyplot(fig_fresh)
        with plot3:
            st.pyplot(fig_certified_fresh)

    
    st.markdown(
    """
    Ainsi, si on souhaite interpréter ces résultats, on peut déterminer les aspects importants pour chacun des états. Par exemple, pour les critiques des films classés \"certified fresh\" tout à droite, on peut penser que les raisons pour lesquelles ces films ont été apprécié par la critique sont liés à **l'histoire (story), à la direction (director) ou à l'écriture du scénario (writer)**. On déduit cela car ce sont les mots qui apparaissent en plus gros dans le wordcloud, impliquant qu'ils ont été les plus fréquents dans les critiques des films de cette catégorie.
    """)
    
#ouverture d'un nouvel onglet : réalisation d'un système de recommandation de films
with tab_plots3:
    st.progress(100)

    st.title("Qu'est-ce qu'on regarde ce soir ?")
    st.markdown('''
    Envie de ne pas perdre de temps sur le choix d'un film, tout en ayant un genre ou une durée en tête ? 
    \n Nous vous proposons un outil qui vous renverra des recommandations de films, basées sur vos envies. 
    \n L'outil comporte un volet 'Trigger Warning', à utiliser lorsque vous êtes notamment en compagnie de public sensible. 
    
    ''')

    language = best_movies_at_home['Language'].unique().tolist() #on récupère les valeurs uniques des langues
    language_choice = st.multiselect('Select the language',language) #possibilité de sélectionner plusieurs langues avec 'multiselect' parmi les différentes valeurs uniques 

    #le principe appliqué à language sera aussi appliqué aux variables suivantes : trigger warning, distributor, length et genre n°1

    tw = best_movies_at_home['Trigger Warning'].unique().tolist() 
    tw_choice = st.multiselect('Select the trigger warning',tw)

    distrib = best_movies_at_home['Distributor'].unique().tolist()
    distrib_choice = st.multiselect('Select the distributor',distrib)

    full_length = best_movies_at_home['Full length in minutes'].unique().tolist()
    length_choice = st.multiselect('Select the length',full_length)

    genre = best_movies_at_home['Genre n°1'].unique().tolist()
    genre_choice = st.multiselect('Select the genre', genre)

    #on renvoie le dataframe filtré sur le streamlit, où chaque filtre représente le choix fait par l'utilisateur. 
    st.dataframe(best_movies_at_home.loc[(best_movies_at_home['Language'].isin(language_choice)) | (best_movies_at_home['Trigger Warning'].isin(tw_choice)) | (best_movies_at_home['Distributor'].isin(distrib_choice)) | (best_movies_at_home['Full length in minutes'].isin(length_choice)) | (best_movies_at_home['Genre n°1'].isin(genre_choice))])

