import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("mxmh_survey_results.csv")

df.drop(['Timestamp', 'Permissions'], axis=1, inplace=True)
#df.rename(columns = {'Video ':'Date'}, inplace=True)
df.dropna(subset=['Age', 'Primary streaming service', 'While working', 'Instrumentalist', 'Composer', 'Foreign languages', 'Music effects'], inplace=True)

df['BPM'] = df['BPM'].fillna(df['BPM'].median())

age_upper_limit = df['Age'].mean() + 3 * df['Age'].std()
BPM_upper_limit = df['BPM'].mean() + 3 * df['BPM'].std()
BPM_lower_limit = df['BPM'].mean() - 3 * df['BPM'].std()
perday_upper_limit = df['Hours per day'].mean() + 3 * df['Hours per day'].std()
perday_lower_limit = df['Hours per day'].mean() - 3 * df['Hours per day'].std()

new_df = df.loc[(df["Age"] < age_upper_limit) & (df["BPM"] < BPM_upper_limit) & (df["BPM"] > BPM_lower_limit) & (df["Hours per day"] < perday_upper_limit)]

st.title("THE MUSIC PRESCRIPTION")

st.text("""Gospel music resonates most with individuals experiencing insomnia,
particularly among older age groups, and has shown to improve their condition significantly.

Lofi music is predominantly favored by individuals dealing with OCD, Anxiety, and Depression,
primarily in their mid-20s. Evidence suggests its positive impact on alleviating these
conditions among participants.

Video game music exhibits adverse effects on various mental health conditions and is
advised to be avoided. Typically preferred by individuals in their early 20s, its association
with worsening mental health is notable.

R&B, Jazz, K-pop, Country, EDM, Hip hop, Folk, Metal, and Latin genres either have a neutral
effect or show potential in improving mental well-being without adverse consequences.

Rock music might exacerbate conditions like Insomnia and Depression, outweighing any potential
benefits for individuals dealing with these issues.

Classical music might not be beneficial for individuals with OCD, Anxiety, and Depression, showing
potential to worsen their condition. However, it indicates a more promising effect for Insomnia, with
higher chances of improvement.

Listening to Lofi and Gospel music for 4-6 hours has shown promise in improving the aforementioned
conditions. Conversely, even a 2-hour exposure to Video game music and pop seems to negatively
impact some participants' mental health.""")

graph_choice = st.selectbox('Select a graph', ['Primary streaming service', 'Does music make an impact on your Mental Health?', 'Favorite Genre', 'Influence of favorite genre on mental health', 'Dependency of Genre and various factors on Mental Health'])

if graph_choice =='Primary streaming service':
    st.subheader("Primary streaming service")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x=new_df['Primary streaming service'], palette='Spectral')
    plt.xticks(rotation=45)
    st.pyplot(fig)

elif graph_choice == 'Does music make an impact on your Mental Health?':
    st.subheader("Does music make an impact on your Mental Health?")
    effects = new_df['Music effects'].value_counts()
    explode = (0, 0.2, 0)
    fig, ax = plt.subplots()
    effects.plot(kind='pie', ylabel='', ax=ax, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
    plt.title("Does music make an impact on your Mental Health?")
    st.pyplot(fig)

elif graph_choice == 'Favorite Genre':
    st.subheader("Favorite Genre")
    y = new_df['Fav genre'].value_counts()
    fig, ax = plt.subplots(figsize=(10, 6))
    y.plot(kind='bar', ax=ax,color='g')
    plt.xticks(rotation=60)
    st.pyplot(fig)

elif graph_choice == 'Influence of favorite genre on mental health':
    st.subheader("Influence of favorite genre on mental health")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=new_df['Fav genre'], y=new_df['Insomnia'], ci=None, ax=ax, marker='*', markerfacecolor='r',markersize=10,linewidth=5)
    plt.xticks(rotation=60)
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=new_df['Fav genre'], y=new_df['OCD'], ci=None, ax=ax, marker='*', markerfacecolor='r',markersize=10,linewidth=5)
    plt.xticks(rotation=60)
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=new_df['Fav genre'], y=new_df['Depression'], ci=None, ax=ax, marker='*', markerfacecolor='r',markersize=10,linewidth=5)
    plt.xticks(rotation=60)
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x=new_df['Fav genre'], y=new_df['Anxiety'], ci=None, ax=ax, marker='*', markerfacecolor='r',markersize=10,linewidth=5)
    plt.xticks(rotation=60)
    st.pyplot(fig)

elif graph_choice == 'Dependency of Genre and various factors on Mental Health':

    st.subheader("Dependency of Genre and various factors on Mental Health")
    figure1, ax1 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=new_df['Fav genre'], y=new_df['Age'], hue=new_df['Music effects'], palette="rainbow")
    plt.tight_layout()
    st.pyplot(figure1)

    # Barplot 2
    figure2, ax2 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=new_df['Fav genre'], y=new_df['Hours per day'], hue=new_df['Music effects'], palette="rainbow")
    plt.tight_layout()
    st.pyplot(figure2)

    # Barplot 3
    figure3, ax3 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=new_df['Fav genre'], y=new_df['Insomnia'], hue=new_df['Music effects'], palette="rainbow")
    plt.tight_layout()
    st.pyplot(figure3)

    # Barplot 4
    figure4, ax4 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=new_df['Fav genre'], y=new_df['OCD'], hue=new_df['Music effects'], palette="rainbow")
    plt.tight_layout()
    st.pyplot(figure4)

    # Barplot 5
    figure5, ax5 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=new_df['Fav genre'], y=new_df['Depression'], hue=new_df['Music effects'], palette="rainbow")
    plt.tight_layout()
    st.pyplot(figure5)

    # Barplot 6
    figure6, ax6 = plt.subplots(figsize=(8, 5))
    sns.barplot(x=new_df['Fav genre'], y=new_df['Anxiety'], hue=new_df['Music effects'], palette="rainbow")
    plt.tight_layout()
    st.pyplot(figure6)
