# Projet 02: Librairies scientifiques et graphiques et POO

- [Projet 02: Librairies scientifiques et graphiques et POO](#projet-02-librairies-scientifiques-et-graphiques-et-poo)
  - [Directives particulières](#directives-particulières)
  - [Introduction](#introduction)
  - [Objectifs](#objectifs)
  - [Partie 1: Analyse de Pokédex](#partie-1-analyse-de-pokédex)
    - [Préparation du dataset 🧹](#préparation-du-dataset-)
      - [1.0 Chargement des données](#10-chargement-des-données)
      - [1.1 Suppression des colonnes non pertinentes](#11-suppression-des-colonnes-non-pertinentes)
      - [1.2 Renommage des colonnes restantes](#12-renommage-des-colonnes-restantes)
      - [1.3. Nettoyage des données](#13-nettoyage-des-données)
      - [1.4 Correction des types de données](#14-correction-des-types-de-données)
    - [Visualisation de données 📈](#visualisation-de-données-)
      - [Quelques méthodes utiles pour les prochaines étapes](#quelques-méthodes-utiles-pour-les-prochaines-étapes)
      - [1.5 Le Spectre des Types](#15-le-spectre-des-types)
      - [1.6 La Course aux Légendes](#16-la-course-aux-légendes)
      - [1.7 L'Ascension Générationnelle](#17-lascension-générationnelle)
      - [1.8 Le Radar des Éléments](#18-le-radar-des-éléments)
    - [Filtrage, tri et agrégation](#filtrage-tri-et-agrégation)
      - [1.9 Le Panthéon des Spécialistes](#19-le-panthéon-des-spécialistes)
      - [1.10 Les Liens Invisibles](#110-les-liens-invisibles)
    - [Modélisation et prévision](#modélisation-et-prévision)
      - [1.11 L'Oracle des Légendes](#111-loracle-des-légendes)
        - [1.11.1 split\_data(df)](#1111-split_datadf)
        - [1.11.2 normalize\_data(x\_train, x\_test)](#1112-normalize_datax_train-x_test)
        - [1.11.3 train\_model(x\_train, y\_train)](#1113-train_modelx_train-y_train)
        - [1.11.4 evaluate\_model(model, x\_test, y\_test)](#1114-evaluate_modelmodel-x_test-y_test)
        - [1.11.5 predict\_legendary(df)](#1115-predict_legendarydf)
  - [Partie 2: L'Arène des Pokémons](#partie-2-larène-des-pokémons)
  - [Annexe: Guide et normes de codage](#annexe-guide-et-normes-de-codage)

<!-- :alarm_clock: [Date de remise le Dimanche 22 novembre 23h59](https://www.timeanddate.com/countdown/generic?iso=20201122T235959&p0=165&msg=Remise+TP5&font=cursive) -->

## Directives particulières
* Le fichier requirements.txt contient les librairies à installer pour faire le laboratoire;
* Il est suggéré de respecter le [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
* Dans chaque programme, vous pouvez ajouter d’autres fonctions à celles décrites dans l’énoncé pour améliorer la lisibilité.

## Introduction
<p align="justify"> Bienvenue dans ce projet sur le monde fascinant des Pokémon ! Ce travail pratique se compose de deux grandes parties. Dans la première partie, nous plongerons dans une analyse détaillée de Pokédex en utilisant des techniques de visualisation de données, de filtrage et d'agrégation avec un dataset approuvé par le Professeur Chen. Dans la seconde partie, nous allons créer notre propre bataille de Pokémon en utilisant plusieurs concepts de la programmation orientée objet. Alors, êtes-vous prêts à devenir le meilleur dresseur ? </p>

![Pythonmon](/assets/pythonmon.webp)

<p align="left"> <i>Crédits: <a href="https://openai.com/blog/dall-e/">DALLE 3</a></i></p>

## Objectifs
- Se familiariser avec des techniques de visualisation de données
- Appliquer des méthodes de filtrage, de tri et d'agrégation sur des ensembles de données
- Comprendre et appliquer les concepts de la programmation orientée objet

## Partie 1: Analyse de Pokédex
Dans cette première étape de notre aventure, nous allons explorer les données disponibles dans un Pokédex. Un Pokédex, pour ceux qui ne sont pas familiers avec le terme, est un appareil électronique de poche que les dresseurs de Pokémon portent avec eux pour garder des informations sur toutes les différentes espèces de Pokémon. Pour cette analyse, nous utiliserons un dataset publiquement disponible sur [Kaggle](https://www.kaggle.com/datasets/rounakbanik/pokemon). Ce dataset a été légèrement modifié pour les besoins de ce projet. Il contient divers attributs sur chaque Pokémon, tels que leur type, leur génération, et bien sûr, leurs statistiques de combat. Nous allons employer différentes techniques de visualisation et d'analyse de données pour obtenir des insights intéressants sur ces créatures fascinantes.

### Préparation du dataset 🧹

#### 1.0 Chargement des données
Pour démarrer ce projet, la première étape consiste à charger le dataset dans ce que nous appellerons notre "Pokédex". Vous utiliserez la librairie Pandas pour lire le fichier CSV qui contient toutes les données des Pokémon. Votre tâche est de compléter la fonction create_pokedex() qui doit retourner un DataFrame Pandas contenant toutes les données. Après avoir créé votre Pokédex, jetez un premier coup d'œil aux données en affichant les 5 premières lignes du DataFrame.

#### 1.1 Suppression des colonnes non pertinentes
Après avoir chargé votre dataset dans le Pokédex, la prochaine étape est de filtrer les colonnes qui nous intéressent vraiment. Pour cela, vous allez compléter la fonction filter_columns() pour ne garder que les colonnes suivantes: **name**, **type1**, **type2**, **attack**, **defense**, **sp_attack**, **sp_defense**, **hp**, **speed**, **generation** et **is_legendary**. 

![Q1.1](/assets/Q1.1.png)

#### 1.2 Renommage des colonnes restantes

Une fois que vous avez les colonnes nécessaires, il serait agréable de renommer ces colonnes pour qu'elles soient plus lisibles. Le nouveau dataframe devrait avoir les colonnes suivantes: **Name**, **Primary Type**, **Secondary Type**, **Attack**, **Defense**, **Special** **Attack**, **Special** **Defense**, **HP**, **Speed**, **Generation** et **Legendary**.

![Q1.2](/assets/Q1.2.png)


#### 1.3. Nettoyage des données
Après avoir supprimé et renommé les colonnes, le prochain pas est de nettoyer les données pour éliminer toute irrégularité qui pourrait affecter nos analyses. Plus spécifiquement, votre tâche consiste à faire les choses suivantes :

- Supprimer les lignes en double
- Supprimez toutes les lignes avec des valeurs NA dans les colonnes, à l'exception de la colonne "**Secondary Type**" où les valeurs NA sont acceptables (il est possible qu'un Pokémon n'ait qu'un seul type).
- Après des suppressions de lignes, les index de votre DataFrame peuvent être en désordre. Réinitialisez-les pour avoir une séquence ordonnée.

![Q1.3](/assets/Q1.3.png)

#### 1.4 Correction des types de données
Maintenant que votre ensemble de données est propre, il est temps de s'assurer que chaque colonne a le bon type de données. Pour ce faire, votre mission est de convertir les colonnes suivantes en type de données int :

- Generation
- HP
- Speed

![Q1.4](/assets/Q1.4.png)

### Visualisation de données 📈

#### Quelques méthodes utiles pour les prochaines étapes

Les DataFrame et Series Pandas ont plusieurs méthodes utiles pour effectuer des calculs statistiques et des opérations de filtrage. Voici quelques-unes des méthodes que vous pourriez trouver utiles pour les prochaines étapes:
- [mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html): Calcule la moyenne des valeurs d'une colonne
- [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html): Regroupe les lignes d'un DataFrame selon les valeurs d'une colonne
- [sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html): Trie les lignes d'un DataFrame selon les valeurs d'une colonne
- [value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html): Compte le nombre d'occurrences de chaque valeur dans une colonne
- [unique](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html): Retourne les valeurs uniques d'une colonne

#### 1.5 Le Spectre des Types

Une fois votre DataFrame impeccablement nettoyé et typé, vous êtes prêt à passer à quelque chose d'un peu plus visuel : un graphique à secteurs (plus communément appelé "pie chart" en anglais 🥧) ! Vous allez utiliser la librairie Plotly pour créer ce graphique. Il représentera la distribution des types primaires parmi tous les Pokémon de votre ensemble de données. Il nous donnera une idée claire de la diversité des types primaires dans l'univers Pokémon. Utilisez la fonction [px.pie](https://plotly.com/python/pie-charts/).

![Q1.5](/assets/Q1.5.png)

Quelques conseils:
- Ajustez les dimensions de graphique à 800x600 pour une meilleure visualisation.

#### 1.6 La Course aux Légendes
Vous êtes maintenant prêts à vous plonger dans le monde fascinant des Pokémon Légendaires. Pour cela, vous allez créer un histogramme en utilisant la bibliothèque Seaborn. Cet histogramme va révéler le nombre de Pokémon Légendaires en fonction de leur génération. Utilisez la fonction [sns.barplot](https://seaborn.pydata.org/generated/seaborn.barplot.html).

![Q1.6](/assets/Q1.6.png)

#### 1.7 L'Ascension Générationnelle
Le prochain défi vous mènera à une comparaison multi-dimensionnelle des statistiques moyennes des Pokémon à travers les différentes générations. Vous utiliserez Plotly pour créer un graphique en lignes superposées, une pour chaque statistique (**Attack**, **Defense**, **HP**, **Special** **Attack**, **Special** **Defense** et **Speed**). Chaque ligne représentera la moyenne de la statistique pour chaque génération. Utilisez une instance de la classe [go.Figure](https://plotly.com/python/creating-and-updating-figures/) pour créer votre graphique où vous ajouterez chacune des lignes. Cette visualisation vous aidera à comprendre comment les statistiques moyennes des Pokémon ont évolué au fil des générations.

![Q1.7](/assets/Q1.7.png)

Quelques conseils:
<!-- parler de scatter -->
- Chaque ligne du graphique peut être représentée par un [scatter plot](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html).
- L'attribut **mode** de la classe Scatter peut être utilisé pour définir le type de ligne (lignes, lignes + marqueurs, marqueurs).

#### 1.8 Le Radar des Éléments

Vous êtes sur le point d'entrer dans la bataille des éléments, où chaque type de Pokémon dévoile ses forces et ses faiblesses en matière d'Attaque, de Défense et de HP. Vous utiliserez Plotly pour créer une série de graphiques radars qui captureront ces aspects clés. Chaque graphique radar représentera la performance de tous les types de Pokémon pour une statistique donnée. Vous devez aligner horizontalement les trois graphiques radars pour faciliter la comparaison entre les types de Pokémon. La fonction [make_subplots](https://plotly.com/python/subplots/) peut être utilisée pour créer des sous-graphiques. Utilisez la fonction [go.Scatterpolar](https://plotly.com/python/polar-chart/) pour créer les différents graphiques radars et les ajouter à votre figure. Cette visualisation vous aidera à comprendre les forces et les faiblesses de chaque type de Pokémon.

![Q1.8](/assets/Q1.8.png)

Quelques conseils:

- Redimensionnez votre figure à 1400x600 pour une meilleure visualisation.

### Filtrage, tri et agrégation 

#### 1.9 Le Panthéon des Spécialistes

Dans ce segment, nous allons couronner l'élite des Pokémon en fonction de leurs statistiques clés : Attaque, Défense, HP et Vitesse. Utilisez Pandas pour filtrer les 5 meilleurs Pokémon pour chaque statistique. Ce seront les Pokémon que vous voudrez avoir dans votre équipe si vous cherchez à maximiser une statistique particulière ! 

![Q1.9](/assets/Q1.9.png)

Quelques conseils:

- La méthode [nlargest](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nlargest.html) vous sera grandement utile pour cette tâche.
- Pour une meilleure présentation, utilisez la fonction [display(...)](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html) pour afficher les DataFrames au lieu de `print()`.

#### 1.10 Les Liens Invisibles

Dans cette section, nous allons plonger dans les relations intrinsèques entre les différentes statistiques des Pokémon. Une matrice de corrélation vous permettra de mesurer à quel point les statistiques sont interdépendantes. Cela donne une idée de la relation entre, par exemple, la vitesse et l'attaque d'un Pokémon : sont-ils généralement proportionnels ou indépendants?

Utilisez la bibliothèque Seaborn pour générer la matrice de corrélation des statistiques suivantes: **Attack**, **Defense**, **HP**, **Special** **Attack**, **Special** **Defense**, **HP** et **Speed**. Utilisez la fonction [sns.heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html) pour créer la matrice de corrélation.

![Q1.10](/assets/Q1.10.png)

Quelques conseils:

- Utilisez la palette de couleurs `crest` pour avoir le même rendu que l'image ci-dessus.

### Modélisation et prévision 

#### 1.11 L'Oracle des Légendes

Dans cette section, vous allez déployer vos compétences en machine learning pour résoudre une question éternelle : peut-on prédire si un Pokémon est légendaire en fonction de ses statistiques ? Vous utiliserez le classificateur [k-NN (k-Nearest Neighbors)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) de la librairie Scikit-Learn pour cette mission. Le processus est décomposé en plusieurs étapes clés.

##### 1.11.1 split_data(df)

La première étape dans tout pipeline d'apprentissage automatique est la division du jeu de données en ensembles d'entraînement et de test. Cette fonction déjà donnée divise le DataFrame en deux ensembles : un ensemble d'entraînement et un ensemble de test.

##### 1.11.2 normalize_data(x_train, x_test)

La mise à l'échelle des données est cruciale lors de l'utilisation de modèles qui sont sensibles à la magnitude des entrées. Cette fonction normalise les caractéristiques d'entraînement et de test. Pour ce faire, vous utiliserez la classe [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) de Scikit-Learn. L'objectif est de centrer les données autour de 0 et de les mettre à l'échelle pour avoir une variance unitaire. Les méthodes [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.fit_transform) et [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.transform) de la classe StandardScaler vous seront utiles respectivement pour l'ensemble d'entraînement et l'ensemble de test. Cette fonction retournera les ensembles d'entraînement et de test normalisés.

##### 1.11.3 train_model(x_train, y_train)

Après la préparation des données, il est temps d'entraîner le modèle. Cette fonction prend les caractéristiques et les labels d'entraînement et renvoie un modèle entraîné. Pour ce faire, vous utiliserez la classe [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) de Scikit-Learn. Vous pouvez utiliser les paramètres par défaut (n_neighbors=5). La méthode [fit](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.fit) de la classe KNeighborsClassifier vous permettra d'entraîner le modèle qui sera retourné par la fonction.

##### 1.11.4 evaluate_model(model, x_test, y_test)

Une fois le modèle formé, l'étape suivante est de le tester sur les données que le modèle n'a jamais vues. Cette fonction évalue les performances du modèle sur l'ensemble de test. Pour ce faire, vous utiliserez la méthode [predict](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict) de la classe KNeighborsClassifier pour prédire les labels de l'ensemble de test et la fonction [accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) de pour calculer la précision du modèle, qui sera retournée par la fonction.

##### 1.11.5 predict_legendary(df)

Cette fonction agit comme coordinateur, orchestrant l'exécution de toutes les fonctions ci-dessus. Elle est également responsable de l'impression de la précision du modèle. Voici les étapes à suivre pour compléter cette fonction :
- Divisez le DataFrame en ensembles d'entraînement et de test en appelant la fonction `split_data(df)`.
- Normalisez les ensembles d'entraînement et de test en appelant la fonction `normalize_data(x_train, x_test)`.
- Utilisez les ensembles d'entraînement normalisés pour entraîner le modèle en appelant la fonction `train_model(x_train, y_train)`.
- Utilisez le modèle entraîné pour évaluer les performances sur l'ensemble de test en appelant la fonction `evaluate_model(model, x_test, y_test)`.
- Affichez le nombre de données d'entraînement et de test.
- Affichez la précision du modèle.

**Afficahge attendu:**
![Q1.11](/assets/Q1.11.png)

**Insight** : La précision du modèle vous donne un aperçu de la fiabilité des prédictions. Plus la précision est élevée, plus vous pouvez être sûr que le modèle prédit correctement la légendarité d'un Pokémon en fonction de ses statistiques.


## Partie 2: L'Arène des Pokémons

Dans cette deuxième section du TP, nous changeons de cap et plongeons dans le monde passionant de la programmation orientée objet. Vous aurez la tâche de créer une simulation de combat entre Pokémon, tour par tour, en utilisant la puissante de la POO. Vous allez créer plusieurs classes, notamment une classe abstraite `Pokemon` pour représenter un Pokémon avec toutes ses caractéristiques, d'autres classes abstraites pour représenter les différents types de Pokémon, et enfin des classes concrètes pour représenter les Pokémon eux-mêmes. Vous allez également créer une classe `PokemonBattle` pour orchestrer les duels.

Ce segment a donc pour but de vous familiariser avec les concepts de base de la POO en Python en mettant l'accent sur l'encapsulation, l'héritage, et le polymorphisme.

Préparez-vous à entrer dans l'arène! 🏟️


## Annexe: Guide et normes de codage
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. Vous avertis aussi si vous ne respectez pas certaines de normes de PEP8.
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)
