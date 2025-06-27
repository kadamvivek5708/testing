import streamlit as st
import pandas as pd
import numpy as np

st.title('Fill Null Values')
filee = st.file_uploader('Choose a file')

if filee is not None:
  file = pd.read_csv(filee)
  st.dataframe(file)
   
  option = st.selectbox(
       'Fill with',
       ('Mean', 'Min', 'Max'))

  if(st.button('Generate')):
      if(option == 'Mean'):
        file['Column1'].fillna((file['Column1'].mean()), inplace=True)
        file['Column2'].fillna((file['Column2'].mean()), inplace=True)
        file['Column3'].fillna((file['Column3'].mean()), inplace=True)

      if(option == 'Min'):
        file['Column1'].fillna((file['Column1'].min()), inplace=True)
        file['Column2'].fillna((file['Column2'].min()), inplace=True)
        file['Column3'].fillna((file['Column3'].min()), inplace=True)

      if(option == 'Max'):
        file['Column1'].fillna((file['Column1'].max()), inplace=True)
        file['Column2'].fillna((file['Column2'].max()), inplace=True)
        file['Column3'].fillna((file['Column3'].max()), inplace=True)


      st.dataframe(file)
