import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def Main():
    my_csv =  Path(__file__).parents[1] / 'NASCAR/dataframe.csv'
    df = pd.read_csv(my_csv)
    names = df['Winner_Manufacturer'].value_counts().index
    values = df['Winner_Manufacturer'].value_counts()

    sns.set_theme(style="whitegrid")
    fig = sns.barplot(data=df, x=names, y=values, palette='Blues_d', saturation = 2)
    fig.set_ylabel('Points')
    plt.xticks(rotation=45)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

st.header('Vencedores da Nascar de 1952-2021')
Main()