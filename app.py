import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
import altair

import os
import requests
import matplotlib.pyplot as plt






st.set_page_config(layout='wide')

  

output_path = 'output/df_final.xlsx'
df_final=pd.read_excel(output_path)



   



df_final['high'] = pd.to_numeric(df_final['high'])
df_final['low'] = pd.to_numeric(df_final['low'])
df_final['previous close'] = pd.to_numeric(df_final['previous close'])


df_final['diff_pct'] = (df_final['high'] - df_final['low']) / df_final['low'] * 100
df_final['diff_pct1'] = (df_final['high'] - df_final['previous close']) / df_final['previous close'] * 100
df_final['diff_pct2'] = (df_final['low'] - df_final['previous close']) / df_final['previous close'] * 100


# df_final['color'] = np.where(df_final['diff_pct'] < 5, 'green', 'red')
# df_final['color1'] = np.where(df_final['diff_pct1'] < 5, 'yellow', 'green')
# df_final['color2'] = np.where(df_final['diff_pct2'] <-5, 'red', 'green')

# Plot a bar chart of the differences with the appropriate colors
fig, ax = plt.subplots()
fig1,ax1=plt.subplots()
fig2,ax2=plt.subplots()
df_final.plot(kind='bar', x='symbol', y='diff_pct', ax=ax )  #color=df_final['color'] , ax=ax)
df_final.plot(kind='bar', x='symbol', y='diff_pct1', ax=ax1) #color=df_final['color1'], ax=ax1)
df_final.plot(kind='bar', x='symbol', y='diff_pct2', ax=ax2 ) #color=df_final['color2'], ax=ax2)
ax.set_title('Difference between High and Low')
ax.set_xlabel('symbol')
ax.set_ylabel('Difference (as %)')
ax1.set_title("Difference between High and Previous day's close")
ax1.set_xlabel('symbol')
ax1.set_ylabel('Difference (as %)')
ax2.set_title("Difference between low and Previous day's close")
ax2.set_xlabel('symbol')
ax2.set_ylabel('Difference (as %)')
#options = list(df_final['symbol'])

st.title('Stock Analysis')
tab1, tab2, tab3 = st.tabs(["Difference between high and low price of stocks", "Difference between high and previous day's close", "Difference between low and previous day's close"])
# Display the chart in Streamlit

with tab1:
    options = list(df_final['symbol'])
    col1, col2 = st.columns([5,3],gap="medium")

    with col1:
       st.header("Difference between high and low price of a stock")
       st.pyplot(fig,use_container_width=True)
    with col2:
       st.header("View explanation of the analysis")
       with st.expander("Click to See explanation"):
         st.write("If the one day high and low are relatively close together, it could indicate that the share is experiencing less volatility or trading in a narrow range.Cutoff is 5%.")
       stock_selected = st.selectbox("Select a stock:", options,key='tab1')
       stock_data = df_final[df_final['symbol'] == stock_selected]
       st.write(f"Selected Stock: {stock_selected}")
       st.write(f"Percentage change: {stock_data['diff_pct'].values[0]:.2f}%")

       if stock_data['diff_pct'].values[0] > 5 :
           st.write("This stock is volatile. Keep a check!")
       else:
           st.write("This stock is not volatile.") 
with tab2:
    options = list(df_final['symbol'])
    col3, col4 = st.columns([5,3],gap="medium")
    with col3:
       st.header("Difference between high and previous day's close")
       st.pyplot(fig1,use_container_width=True)
    with col4:
       st.header("View explanation of the analysis")
       with st.expander("Click to See explanation"):
         st.write("If the one day high is much higher than the previous day's close, it could indicate that there is positive news or investor sentiment towards the company, which is driving up the price.")
       stock_selected1 = st.selectbox("Select a stock:", options,key='tab2')
       stock_data1 = df_final[df_final['symbol'] == stock_selected1]
       st.write(f"Selected Stock: {stock_selected1}")
       st.write(f"Percentage change: {stock_data1['diff_pct1'].values[0]:.2f}%")
       if stock_data1['diff_pct1'].values[0] < 5:
           st.write("No positive news as such")
       else:
           st.write("There could be a positive news.") 
with tab3:
    options = list(df_final['symbol'])
    col5, col6 = st.columns([5,3],gap="medium")
    with col5:
       st.header("Difference between low and previous day's close")
       st.pyplot(fig2,use_container_width=True)
    with col6:
       st.header("View explanation of the analysis")
       with st.expander("Click to See explanation"):
         st.write("If the one day low is much lower than the previous day's close, it could indicate that there is negative news or investor sentiment towards the company, which is driving down the price.  Cutoff is -5%.")
       stock_selected2 = st.selectbox("Select a stock:", options,key='tab3')
       stock_data2 = df_final[df_final['symbol'] == stock_selected2]
       st.write(f"Selected Stock: {stock_selected2}")
       st.write(f"Percentage change: {stock_data2['diff_pct2'].values[0]:.2f}%")
       if stock_data2['diff_pct2'].values[0] < -5 :
           st.write("Alarming")
       else:
           st.write("Not alarming") 
