import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.title(" Iris Prediction App")
st.markdown("""
# *This app predicts the Iris Flower Type*
""")
st.sidebar.header('User Input Parameters')

def userInputFeatures():
    sepal_length = st.sidebar.slider('Sepal length', 4.2,7.7,5.2)
    sepal_width = st.sidebar.slider('Sepal width', 2.0,4.4,3.4)
    petal_length = st.sidebar.slider('Petal_length', 1.0,6.9,1.5)
    petal_width = st.sidebar.slider('Petal_width', 0.1,2.5,0.3)
    data = {
        'sepal_length':sepal_length,
        'sepal_width':sepal_width,
        'petal_length':petal_length,
        'petal_width':petal_width
    }
    features = pd.DataFrame(data,index=[0])
    return features

df = userInputFeatures()

st.subheader('> User Input Parameters')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target

clf = RandomForestClassifier()
clf.fit(X,Y)
prediction = clf.predict(df)
prediction_prob = clf.predict_proba(df)

st.subheader("""
> Class labels and their corresponding index
""")
st.write(iris.target_names)

st.subheader('> Prediction')
st.write(iris.target_names[prediction])
# st.write(prediction)
st.subheader('> Prediction Probability')
st.write(prediction_prob)

st.write(""""
# See you in the next project :smiley:
""")
