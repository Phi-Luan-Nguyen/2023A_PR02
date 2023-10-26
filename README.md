# Projet 02: Librairies scientifiques et graphiques et POO

- [Projet 02: Librairies scientifiques et graphiques et POO](#projet-02-librairies-scientifiques-et-graphiques-et-poo)
  - [Directives particulières](#directives-particulières)
  - [Introduction](#introduction)
  - [Objectifs](#objectifs)
  - [Partie 1: Analyse d'un Pokédex](#partie-1-analyse-dun-pokédex)
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
    - [Vue d'ensemble](#vue-densemble)
    - [2.1 Création de la classe abstraite `Pokemon`](#21-création-de-la-classe-abstraite-pokemon)
      - [2.1.1 Abstraction](#211-abstraction)
      - [2.1.2 Constructeur](#212-constructeur)
      - [2.1.3 Les propriétés en lecture (getters)](#213-les-propriétés-en-lecture-getters)
      - [2.1.4 Les propriétés en écriture (setters)](#214-les-propriétés-en-écriture-setters)
      - [2.1.5 Méthodes abstraites](#215-méthodes-abstraites)
      - [2.1.6 Méthodes concrètes](#216-méthodes-concrètes)
      - [2.1.7 Méthodes magiques](#217-méthodes-magiques)
    - [2.2 Création des classes abstraites `PokemonType`](#22-création-des-classes-abstraites-pokemontype)
      - [2.2.1 Héritage et Abstraction](#221-héritage-et-abstraction)
      - [2.2.2 Constructeur](#222-constructeur)
      - [2.2.3 Implémentation de `get_attack_multiplier`](#223-implémentation-de-get_attack_multiplier)
    - [2.3 Le Triptyque: Squirtle, Charmander et Bulbasaur](#23-le-triptyque-squirtle-charmander-et-bulbasaur)
      - [2.3.1 Héritage](#231-héritage)
      - [2.3.2 Constructeur](#232-constructeur)
      - [2.3.3 Implémentation de `evolve`](#233-implémentation-de-evolve)
      - [2.3.4 Implémentation de `get_signature_sound` 🎶](#234-implémentation-de-get_signature_sound-)
    - [2.4 Complétion de la classe `PokemonArena`](#24-complétion-de-la-classe-pokemonarena)
    - [2.5 Création du script principal](#25-création-du-script-principal)
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

## Partie 1: Analyse d'un Pokédex
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

La première étape dans tout pipeline d'apprentissage automatique est la division du jeu de données en ensembles d'entraînement et de tests. Cette fonction déjà donnée divise le DataFrame en deux ensembles : un ensemble d'entraînement et un ensemble de tests.

##### 1.11.2 normalize_data(x_train, x_test)

La mise à l'échelle des données est cruciale lors de l'utilisation de modèles qui sont sensibles à la magnitude des entrées. Cette fonction normalise les caractéristiques d'entraînement et de tests. Pour ce faire, vous utiliserez la classe [StandardScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) de Scikit-Learn. L'objectif est de centrer les données autour de 0 et de les mettre à l'échelle pour avoir une variance unitaire. Les méthodes [fit_transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.fit_transform) et [transform](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler.transform) de la classe StandardScaler vous seront utiles respectivement pour l'ensemble d'entraînement et l'ensemble de tests. Cette fonction retournera les ensembles d'entraînement et de tests normalisés.

##### 1.11.3 train_model(x_train, y_train)

Après la préparation des données, il est temps d'entraîner le modèle. Cette fonction prend les caractéristiques et les labels d'entraînement et renvoie un modèle entraîné. Pour ce faire, vous utiliserez la classe [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) de Scikit-Learn. Vous pouvez utiliser les paramètres par défaut (n_neighbors=5). La méthode [fit](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.fit) de la classe KNeighborsClassifier vous permettra d'entraîner le modèle qui sera retourné par la fonction.

##### 1.11.4 evaluate_model(model, x_test, y_test)

Une fois le modèle formé, l'étape suivante est de le tester sur les données que le modèle n'a jamais vues. Cette fonction évalue les performances du modèle sur l'ensemble de tests. Pour ce faire, vous utiliserez la méthode [predict](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier.predict) de la classe KNeighborsClassifier pour prédire les labels de l'ensemble de tests et la fonction [accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) de pour calculer la précision du modèle, qui sera retournée par la fonction.

##### 1.11.5 predict_legendary(df)

Cette fonction agit comme coordinateur, orchestrant l'exécution de toutes les fonctions ci-dessus. Elle est également responsable de l'impression de la précision du modèle. Voici les étapes à suivre pour compléter cette fonction :
- Divisez le DataFrame en ensembles d'entraînement et de tests en appelant la fonction `split_data(df)`.
- Normalisez les ensembles d'entraînement et de tests en appelant la fonction `normalize_data(x_train, x_test)`.
- Utilisez les ensembles d'entraînement normalisés pour entraîner le modèle en appelant la fonction `train_model(x_train, y_train)`.
- Utilisez le modèle entraîné pour évaluer les performances sur l'ensemble de tests en appelant la fonction `evaluate_model(model, x_test, y_test)`.
- Affichez le nombre de données d'entraînement et de tests.
- Affichez la précision du modèle.

**Afficahge attendu:**
![Q1.11](/assets/Q1.11.png)

**Insight** : La précision du modèle vous donne un aperçu de la fiabilité des prédictions. Plus la précision est élevée, plus vous pouvez être sûr que le modèle prédit correctement la légendarité d'un Pokémon en fonction de ses statistiques.


## Partie 2: L'Arène des Pokémons

Dans cette deuxième section du TP, nous changeons de cap et plongeons dans le monde passionant de la programmation orientée objet. Vous aurez la tâche de créer une simulation de combat tour par tour entre Pokémon, en utilisant la puissante de la POO.

Ce segment a donc pour but de vous familiariser avec les concepts de base de la POO en Python en mettant l'accent sur l'encapsulation, l'héritage, et le polymorphisme.

Préparez-vous à entrer dans l'arène! 🏟️

### Vue d'ensemble

Tout d'abord, vous développerez une classe abstraite `Pokemon` pour les caractéristiques communes à tous les Pokémon. Ensuite, vous développerez des sous-classes abstraites `PokemonType` pour trois différents types de Pokémon. Ces classes seront des enfants de la classe `Pokemon` et définiront des caractéristiques communes des Pokémon de ce type. Puis, vous développerez une sous-classe concrète représentant un Pokémon spécifique pour chaque type.

Par la suite, vous compléterez deux fonctions de la classe `PokemonArena` utilisant le polymorphisme des pokémons pour simuler un combat entre deux Pokémon.

Finalement, vous écrirez un simple script principal pour tester le fonctionnement de votre code précédemment écrit.

### 2.1 Création de la classe abstraite `Pokemon`

Cette classe est la pierre angulaire de notre simulation. Elle représente les caractéristiques communes à tous les Pokémon. Vous devez compléter la classe `Pokemon` en suivant les directives suivantes:

#### 2.1.1 Abstraction

Pour commencer, vous devez rendre la classe `Pokemon` abstraite afin qu'elle ne puisse pas être instanciée directement.

Conseil: Allez voir la documentation de la librairie [abc](https://docs.python.org/3/library/abc.html).

#### 2.1.2 Constructeur

La méthode `__init__` est le constructeur de la classe. Elle est appelée lorsqu'une instance de la classe est créée. Vous devez compléter le constructeur de la classe `Pokemon`.

- Le constructeur doit prendre les paramètres suivants:
  - `name`: le nom du Pokémon
  - `attack`: l'attaque du Pokémon
  - `defense`: la défense du Pokémon
  - `type`: le type du Pokémon

Lors de cette initialisation, vous devez garder en mémoire les paramètres dans des attributs privés utilisant la convention du double underscore (ex: `name` devient `__name`). Vous devez également initialiser les attributs suivants:

- `__health`: la santé du Pokémon. Elle doit être initialisée à la valeur maximale de santé (voir la constante `MAX_HEALTH` dans le fichier `constants.py`).
- `__state`: l'état du Pokémon. Elle doit être initialisée à `NORMAL`.
- `__state_counter`: le compteur d'état du Pokémon. Il sera utilisé pour compter le nombre de tours restants d'un état induit (ex: empoisonné). Il doit être initialisé à 0.
- `__evolved`: un booléen indiquant si le Pokémon a évolué. Il doit être initialisé à `False`.

#### 2.1.3 Les propriétés en lecture (getters)

Les propriétés en lecture permettent d'accéder aux attributs privés d'un objet. Les getters sont souvent utilisés pour obtenir les valeurs des attributs sans les exposer directement. Vous devez utiliser le décorateur [@property](https://docs.python.org/3/library/functions.html#property) pour la définition de chaque getter.

Voici la liste des getters à implémenter:

- `name`: retourne le nom du Pokémon (string)
- `attack`: retourne l'attaque du Pokémon (int)
- `defense`: retourne la défense du Pokémon (int)
- `type`: retourne le type du Pokémon (PokemonType)
- `health`: retourne la santé du Pokémon (int)
- `state`: retourne l'état du Pokémon (PokemonState)
- `state_counter`: retourne le compteur d'état du Pokémon (int)
- `evolved`: retourne un booléen indiquant si le Pokémon a évolué (bool)

#### 2.1.4 Les propriétés en écriture (setters)

Les propriétés en écriture permettent de modifier les attributs privés d'un objet et de valider les valeurs données avant leur modification. Vous devez utiliser le décorateur [@attributename.setter](https://docs.python.org/3/library/functions.html#property) pour la définition de chaque setter. Vous devez également valider les valeurs données avant de les assigner aux attributs privés de l'objet.

Voici la liste des setters à implémenter:

- `name`: prend un nom en paramètre et assigne le nom à l'attribut `__name` seulement si le nom n'est pas une chaîne vide.
- `attack`: prend une attaque en paramètre et assigne l'attaque à l'attribut `__attack` seulement si l'attaque est supérieure ou égale à 0.
- `defense`: prend une défense en paramètre et assigne la défense à l'attribut `__defense` seulement si la défense est supérieure ou égale à 0.
- `state`: prend un état en paramètre et assigne l'état à l'attribut `__state` seulement si l'état est un membre de l'énumération `PokemonState`.
- `state_counter`: prend un compteur d'état en paramètre et assigne le compteur d'état à l'attribut `__state_counter` seulement si la valeur est supérieure ou égale à 0.

#### 2.1.5 Méthodes abstraites

Les méthodes abstraites sont des méthodes qui ne sont pas implémentées dans la classe abstraite, mais qui doivent être obligatoirement être implémentées dans les sous-classes. Vous devez utiliser le décorateur [@abstractmethod](https://docs.python.org/3/library/abc.html#abc.abstractmethod) pour la définition de chaque méthode abstraite.

Voici la liste des méthodes abstraites à implémenter:

- a) `get_attack_multiplier`: prend un type de Pokémon en paramètre et retourne le multiplicateur d'attaque (double) du Pokémon en fonction du type du Pokémon attaqué (passé en paramètre). Cette méthode sera implémentée dans les sous-classes de `Pokemon`.
- b) `generate_random_induced_state`: retourne un tuple contenant un état induit aléatoirement (PokemonState) et le nombre de tours restants de l'état induit (int). Cette méthode sert à générer un état induit aléatoire lorsqu'un Pokémon attaque un autre Pokémon et sera implémentée dans les sous-classes de `Pokemon`.
- c) `get_signature_sound`: retourne le son de signature du Pokémon (string). Cette méthode sera implémentée dans les sous-classes de `PokemonType`.
- d) `evolve`: cette méthode ne reçoit aucun paramètre et ne retourne rien. Elle permet d'évoluer le Pokémon. Cette méthode sera implémentée dans les sous-classes de `PokemonType`.

#### 2.1.6 Méthodes concrètes

Les méthodes concrètes sont des méthodes qui sont implémentées dans la classe abstraite et qui peuvent être utilisées directement par les sous-classes. Vous devez implémenter les méthodes suivantes:

- a) `decrement_state_counter`: cette fonction ne reçoit aucun paramètre et ne retourne rien. Elle décrémente le compteur d'état du Pokémon de 1. Si le compteur d'état est déjà à 0, la fonction ne fait rien.
- b) `is_knocked_out`: cette fonction ne reçoit aucun paramètre et retourne un booléen indiquant si le Pokémon est KO (True) ou non (False). Un Pokémon est KO si sa santé est à 0.
- c) `heal`: cette fonction ne reçoit aucun paramètre et ne retourne rien. Elle remet la santé du Pokémon à la valeur maximale de santé (voir la constante `MAX_HEALTH` dans le fichier `constants.py`).

#### 2.1.7 Méthodes magiques

Les méthodes magiques sont des méthodes spéciales ayant des noms spécifiques (ex: `__init__`, `__str__`, `__repr__`, etc.) qui permettent de modifier le comportement de l'objet. 

Nous allons les utiliser pour surcharger des opérateurs spécifiques ("+" et "-") ou lorsqu'on tente d'interpréter l'objet comme une chaîne de caractères (via `str(...)`, `print(...)`, etc.).

**a) def __str\__(self):**
Cette méthode spéciale est appelée lorsqu'on tente d'interpréter l'objet comme une chaîne de caractères (ex: `str(pokemon)` ou `print(pokemon)`). Elle retourne une chaîne de caractères représentant le Pokémon. 
 
La chaîne de caractères doit être de la forme suivante: 
 `<name> est de type <type>. Il a <attack> points d'attaque et <defense> points de défense.`. 

**b) def __add\__(self, health: int):**
Cette méthode spéciale est appelée lorsqu'on tente d'ajouter un nombre à un Pokémon (ex: `pokemon + 10`). Elle ne retourne rien. Elle doit ajouter la valeur passée en paramètre à la santé du Pokémon. Si la valeur passée en paramètre est négative, la fonction ne fait rien. La santé du Pokémon ne peut pas dépasser la valeur maximale de santé (voir la constante `MAX_HEALTH` dans le fichier `constants.py`).

**c) def __sub\__(self, damage: int):**
Cette méthode spéciale est appelée lorsqu'on tente de soustraire un nombre à un Pokémon (ex: `pokemon - 10`). Elle ne retourne rien. Elle doit soustraire la valeur passée en paramètre à la santé du Pokémon. Si la valeur passée en paramètre est négative, la fonction ne fait rien. La santé du Pokémon ne peut pas être négative.

### 2.2 Création des classes abstraites `PokemonType`

Les classes abstraites `PokemonTypeWater`, `PokemonTypeFire` et `PokemonTypeGrass` représentent les caractéristiques communes à tous les Pokémon de leur type.

#### 2.2.1 Héritage et Abstraction

Pour commencer, vous devez faire hériter les trois classes de la classe abstraite `Pokemon`. Vous devez également rendre les trois classes abstraites afin qu'elles ne puissent pas être instanciées directement. 

#### 2.2.2 Constructeur

Le constructeur des trois classes doit prendre les paramètres suivants:

- `name`: le nom du Pokémon
- `attack`: l'attaque du Pokémon
- `defense`: la défense du Pokémon

Vous devez absolument utiliser le constructeur de la classe parent pour garder en mémoire les différents paramètres. Chaque sous-classe devra donc donner le type qui lui correspond dans cet appel.

Conseil: Voir la documentation de la librairie [super](https://docs.python.org/3/library/functions.html#super).

#### 2.2.3 Implémentation de `get_attack_multiplier`

Dans l'univers de Pokémon, la notion de type est très importante pour prédire l'issue d'un combat. Chaque type de Pokémon a des forces et des faiblesses contre d'autres types de Pokémon. Par exemple, un Pokémon de type **FEU** aura un avantage contre un Pokémon de type **PLANTE**. On peut dire que, contrairement au langage Python, le monde des Pokémon est fortement typé (sans mauvais jeu de mot 😉).

Vous devez donc implémenter la méthode abstraite `get_attack_multiplier` dans les trois classes. Cette méthode retourne le multiplicateur d'attaque (double) du Pokémon en fonction du type du Pokémon attaqué (passé en paramètre).

Voici les multiplicateurs d'attaque pour chaque type de Pokémon:

- **Pour les pokémons de type FIRE**:
  - GRASS: 1.25
  - WATER: 0.75
  - Autre: 1.0

- **Pour les pokémons de type WATER**:
  - FIRE: 1.25
  - GRASS: 0.75
  - Autre: 1.0

- **Pour les pokémons de type GRASS**:
  - WATER: 1.25
  - FIRE: 0.75
  - Autre: 1.0


### 2.3 Le Triptyque: Squirtle, Charmander et Bulbasaur

Les trois classes `Squirtle`, `Charmander` et `Bulbasaur` représentent les trois Pokémon de départ les plus emblématiques de cet univers. Chacun de ces Pokémon incarne un élément fondamental - Eau, Feu, et Plante - et possède la capacité fascinante d'évoluer, de gagner en puissance, et d'exprimer leur individualité à travers un son unique.

#### 2.3.1 Héritage

Les trois classes doivent hériter de la classe abstraite correspondant à leur type de Pokémon (`PokemonWaterType`, `PokemonFireType` et `PokemonGrassType`). Cet héritage permet une implémentation cohérente et propre des comportements spécifiques à chaque type.

#### 2.3.2 Constructeur

Le constructeur des trois classes ne prend aucun paramètre. Vous devez  utiliser le constructeur de la classe parent en lui donnant les caractéristiques spécifiques du Pokémon en question. Chaque constructeur ne doit donc pas dépasser une ligne de code.

Voici les caractéristiques de base de chaque Pokémon:

- **Squirtle**:
  - Nom: Squirtle
  - Attaque: 48
  - Défense: 65

- **Charmander**:
  - Nom: Charmander
  - Attaque: 52
  - Défense: 43

- **Bulbasaur**:
  - Nom: Bulbasaur
  - Attaque: 49
  - Défense: 49

#### 2.3.3 Implémentation de `evolve`

Ce qui rend ces Pokémon particulièrement captivants, c'est leur capacité à évoluer et à monter en puissance. La méthode `evolve` assure cette transformation en modifiant les attributs d'attaque et de défense ainsi que le nom du Pokémon, reflétant ainsi son nouvel état évolutif. Elle ne prend aucun paramètre et ne retourne rien.

Voici les caractéristiques de chaque Pokémon après son évolution:

- **Squirtle**:
  - Nom: Wartortle
  - Attaque: 63
  - Défense: 80

- **Charmander**:
  - Nom: Charmeleon
  - Attaque: 64
  - Défense: 58

- **Bulbasaur**:
  - Nom: Ivysaur
  - Attaque: 62
  - Défense: 63

#### 2.3.4 Implémentation de `get_signature_sound` 🎶

Chaque Pokémon exprime sa singularité à travers un son distinct. La méthode `get_signature_sound` nous gratifie de ces sonorités emblématiques. Elle ne prend aucun paramètre et retourne le son de signature du Pokémon (string).

Voici les sons de signature de chaque Pokémon:

- **Squirtle**: "Squirtle-squirtle"
- **Charmander**: "Char-char"
- **Bulbasaur**: "Bulba-bulba"

### 2.4 Complétion de la classe `PokemonArena`

La construction de l'arène de combat est presque achevée. La dernière brique à poser est l'implémentation de la méthode `attack` de la classe `PokemonArena`. Cette méthode prend deux paramètres: un Pokémon attaquant et un Pokémon défenseur. Elle calcule les dégâts infligés par l'attaquant au défenseur en fonction du multiplicateur de dégâts de l'attaquant et soustrait les dégâts aux points de vie du défenseur. La méthode doit retourner les dégâts infligés. 

**Important**: Il est nécessaire d'utiliser la méthode `get_attack_multiplier` de la classe `Pokemon` pour calculer le multiplicateur de dégâts de l'attaquant et d'utiliser la surcharge de l'opérateur "-" pour soustraire les dégâts aux points de vie du défenseur.

### 2.5 Création du script principal

Vous êtes maintenant prêt à entrer dans l'arène et à vivre l'expérience ultime de la vie de dresseur/dresseuse de Pokémon! Dans ce script principal, nous allons tester tous les aspects de la dynamique entre les Pokémon, de leur tout premier combat jusqu'à leur forme évoluée.

Il est donc temps de vous diriger vers le fichier [main.py](part2/main.py) et suivre les instructions TODO pour compléter votre aventure. Le combat final vous attend! ⭐️

## Annexe: Guide et normes de codage
- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. Vous avertis aussi si vous ne respectez pas certaines de normes de PEP8.
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)
