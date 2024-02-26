import streamlit as st
import pandas as pd

st.markdown("# Kart Stats 🏎️")
st.sidebar.markdown("# Kart Stats 🏎️")

st.write(' # Mariokart *Stats Website*')

df_kart = pd.read_csv('data/kart_stats.csv')

# Visualization 1
selected_columns = ['Body', 'Weight', 'Acceleration', 'On-Road traction', 'Off-Road Traction', 'Mini-Turbo']
st.dataframe(df_kart[selected_columns]
              .style.highlight_max(color='lightgreen', axis=0, subset=['Weight', 'Acceleration', 'On-Road traction', 'Off-Road Traction', 'Mini-Turbo'])
              .highlight_min(color='red', axis=0, subset=['Weight', 'Acceleration', 'On-Road traction', 'Off-Road Traction', 'Mini-Turbo']))

# Visualization 2 (Line Chart)
st.line_chart(df_kart[['Acceleration', 'Ground Speed']])

# Visualization 3 (Bar Chart)
selected_bar_columns = ['Body', 'On-Road traction', 'Off-Road Traction']
st.bar_chart(df_kart[selected_bar_columns].set_index('Body'))

# Dynamic Bar Chart for Individual Karts
chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])

df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]
df_single_kart = df_single_kart.drop(columns=['Body'])

df_unp_kart = df_single_kart.unstack().rename_axis(['category', 'row number']).reset_index().drop(columns='row number').rename({0: 'strength'}, axis=1)

st.bar_chart(df_unp_kart, x='category', y='strength')