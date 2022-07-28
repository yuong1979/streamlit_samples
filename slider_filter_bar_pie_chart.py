# requirements for firestore
# pip install firebase_admin

from argparse import _StoreFalseAction
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image



db = firestore.Client.from_service_account_json("serviceAccountKey.json")

st.set_page_config(page_title='Survey Results')
st.header('Survey Results 2021')
st.subheader('Was the tutorial helpful?')

# ### --- LOAD DATAFRAME
surveylist = []
docs = db.collection('Survey').get()
for doc in docs:
    surveylist.append(doc.to_dict())

#turning the data into a dataframe
df = pd.DataFrame(surveylist)

#aggregate the data by department
df_participants = df.groupby(['Department'])['Age'].count()

#convert to datafram from series
df_participants = pd.DataFrame({'Department':df_participants.index, 'Count':df_participants.values})

# --- STREAMLIT SELECTION
department = df['Department'].unique().tolist()
ages = df['Age'].unique().tolist()

age_selection = st.slider('Age:',
                        min_value= min(ages),
                        max_value= max(ages),
                        value=(min(ages),max(ages)))


department_selection = st.multiselect('Department:',
                                    department,
                                    default=department)

# --- FILTER DATAFRAME BASED ON SELECTION
mask = (df['Age'].between(*age_selection)) & (df['Department'].isin(department_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Available Results: {number_of_result}*')

# --- GROUP DATAFRAME AFTER SELECTION
df_grouped = df[mask].groupby(by=['Rating']).count()[['Age']]
df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped = df_grouped.reset_index()

# --- PLOT BAR CHART
bar_chart = px.bar(df_grouped,
                   x='Rating',
                   y='Votes',
                   text='Votes',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# --- DISPLAY IMAGE & DATAFRAME
col1, col2 = st.columns(2)
image = Image.open('images/survey.jpg')

col1.image(image,
        caption='Designed by slidesgo / Freepik',
        use_column_width=True)
col2.dataframe(df[mask])

# --- PLOT PIE CHART
pie_chart = px.pie(df_participants,
                title='Total No. of Participants',
                values='Count',
                names='Department')

st.plotly_chart(pie_chart)



# based on tutorial by https://youtu.be/7zeAIEPJaoQ?list=PL7QI8ORyVSCaejt2LICRQtOTwmPiwKO2n






## data simulation

# db.collection('Survey').add({"Department":"Logistic", "Age": 23, "Rating": "4 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 56, "Rating": "2 Star"})
# db.collection('Survey').add({"Department":"Logistic", "Age": 40, "Rating": "4 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 40, "Rating": "4 Star"})
# db.collection('Survey').add({"Department":"Finance", "Age": 25, "Rating": "5 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 40, "Rating": "1 Star"})
# db.collection('Survey').add({"Department":"Finance", "Age": 35, "Rating": "2 Star"})
# db.collection('Survey').add({"Department":"Finance", "Age": 45, "Rating": "2 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 60, "Rating": "2 Star"})
# db.collection('Survey').add({"Department":"Logistic", "Age": 26, "Rating": "5 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 46, "Rating": "1 Star"})
# db.collection('Survey').add({"Department":"Finance", "Age": 47, "Rating": "2 Star"})
# db.collection('Survey').add({"Department":"Sales", "Age": 33, "Rating": "3 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 36, "Rating": "4 Star"})
# db.collection('Survey').add({"Department":"Purchasing", "Age": 40, "Rating": "5 Star"})
# db.collection('Survey').add({"Department":"Sales", "Age": 35, "Rating": "1 Star"})
# db.collection('Survey').add({"Department":"Logistic", "Age": 27, "Rating": "2 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 21, "Rating": "3 Star"})
# db.collection('Survey').add({"Department":"Sales", "Age": 18, "Rating": "4 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 47, "Rating": "5 Star"})
# db.collection('Survey').add({"Department":"Finance", "Age": 56, "Rating": "5 Star"})
# db.collection('Survey').add({"Department":"Sales", "Age": 28, "Rating": "5 Star"})
# db.collection('Survey').add({"Department":"Purchasing", "Age": 27, "Rating": "4 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 23, "Rating": "3 Star"})
# db.collection('Survey').add({"Department":"Finance", "Age": 28, "Rating": "2 Star"})
# db.collection('Survey').add({"Department":"Purchasing", "Age": 51, "Rating": "1 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 52, "Rating": "1 Star"})
# db.collection('Survey').add({"Department":"Sales", "Age": 32, "Rating": "1 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 45, "Rating": "2 Star"})
# db.collection('Survey').add({"Department":"Sales", "Age": 47, "Rating": "1 Star"})
# db.collection('Survey').add({"Department":"Logistic", "Age": 42, "Rating": "5 Star"})
# db.collection('Survey').add({"Department":"Finance", "Age": 41, "Rating": "1 Star"})
# db.collection('Survey').add({"Department":"Marketing", "Age": 43, "Rating": "4 Star"})
# db.collection('Survey').add({"Department":"Logistic", "Age": 44, "Rating": "5 Star"})
# db.collection('Survey').add({"Department":"Sales", "Age": 34, "Rating": "1 Star"})













