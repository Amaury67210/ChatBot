import numpy as np
import pandas as pd
import re
import nltk
from sklearn.datasets import load_files
import pickle
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')
from nltk.corpus import stopwords
from datasets import load_dataset
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Ici, on utilise un modele Bag of Words : K-means et Dendrogramme de Clustering Hierarchique

tfidfconverter = TfidfVectorizer(max_features=1500, min_df=500, max_df=0.7, stop_words=stopwords.words('french'))
# max_features = nombre maximal de features (mots uniques dans les textes)    
# min_df = nombre minimal de textes qui contiennent cette feature    
# max_df = pourcentage de documents maximal qui contiennent cette feature    
# stopwords = les mots qui sont tellement communs dans une langue qu'ils ne donnent aucune information

classifier = RandomForestClassifier(n_estimators=1000, random_state=0)

# Signification des labels :    
# autre = 0    
# impression = 1

def init_data():
    dataset = load_dataset('piaf')
    dfLabel0 = pd.DataFrame(data = dataset['train']['question'], columns = ['texte'])
    dfLabel0['texte'] = 'Bonjour ' + dfLabel0['texte']
    dfLabel0['label'] = 0

    datasetImpression = pd.read_csv('./input/datalabelimpression/dataImpression.csv')
    #datasetImpression = pd.read_csv('/Users/amorce/Documents/Sciences_des_données/GIT3/projet-sdia-sdsc-chatbot-industriel/input/datalabelimpression/dataImpression.csv')

    datasetImpressionAvecExemplaires = pd.read_csv('./input/datalabelimpression/dataImpressionAvecExemplaires.csv')
    #datasetImpressionAvecExemplaires = pd.read_csv('/Users/amorce/Documents/Sciences_des_données/GIT3/projet-sdia-sdsc-chatbot-industriel/input/datalabelimpression/dataImpressionAvecExemplaires.csv')
    
    #CSVs generes automatiquement avec l'expression reguliere suivante :    
    #/(Bonjour, |Bonsoir, )?(je (veux|souhaite) )?(impression|imprime|imprimer|print) [a-zA-Z0-9]{1,10} ((qui (contient|a))|a)? [0-9]{1,4} (pages|p) (en [0-9]{1,2} (exemplaires|copies|fois))?/
    datasetImpression['label'] = 1
    datasetImpressionAvecExemplaires['label'] = 1
    dfLabel1 = pd.concat([datasetImpression, datasetImpressionAvecExemplaires])

    df = pd.DataFrame()
    df['texte'] = ["Bonjour, je veux imprimer doc1 qui contient 1800 pages", 
                "Bonjour, imprime moi doc2 qui contient 4500 pages",
                "quelle heure est il ?",
                "Impression doc3 4500 pages",
                "tirage mon document doc4 a 1800 pages",
                "tirimprimer mondoc"]
    df['label'] = [1, 1, 0, 1, 1, 0]

    df = pd.concat([df, dfLabel0, dfLabel1])
    df = df.sample(frac=1).reset_index(drop=True)

    return df

def create_train_model():
    df = init_data()

    X, y = df['texte'], df['label']

    textes = []
    stemmer = WordNetLemmatizer()
    for i in range(0, len(X)):
        texte = re.sub(r'\W', ' ', str(X[i])) #On enleve les caracteres speciaux
        texte = re.sub(r'\s+[a-zA-Z]\s+', ' ', texte) #On enleve les mots a 1 caractere (en milieu du texte)
        texte = re.sub(r'\^[a-zA-Z]\s+', ' ', texte) #On enleve les mots a 1 caractere (en debut du texte)
        texte = re.sub(r'\s+', ' ', texte, flags=re.I) #On enleve les espaces qui se suivent
        texte = texte.lower() #On met tous les caracteres en minuscule
        texte = texte.split()
        texte = [stemmer.lemmatize(mot) for mot in texte] #lemmatization : reduire le mot a sa forme canonique
        texte = ' '.join(texte)
        
        textes.append(texte)

    X = tfidfconverter.fit_transform(textes).toarray()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    classifier.fit(X_train, y_train) 

def predict_text(texte):
    return classifier.predict(tfidfconverter.transform([texte]).toarray())