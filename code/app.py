# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 19:17:31 2023

@author: akshaypjadhav
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import re
import os



cwd = re.sub(r'\\','/',str(os.getcwd()))
cwd = cwd[:cwd.rfind('/')+1]
cwd = cwd +'data/'
print (cwd)
# Load data

file = "Industry.xlsx"

data = pd.read_excel(cwd + file )

# Streamlit app title
st.title("Task Automation Analysis - CGI")

# Dropdown for variable selection
selected_var5 = st.selectbox("Select an Industry", data['var5'].unique())
filtered_data = data[data['var5'] == selected_var5]

# Define a custom color mapping function with gradients
def custom_color_mapping(v1, v2, v3):
    if v1 > 4.7849 and v2 > 5.8651 and v3 > 4.7255:
        return 'rgb(170, 0, 0)'
    elif v1 > 4.7849 and v2 > 5.8651 and v3 < 2.9132:
        return 'rgb(0, 0, 255)'
    elif v1 > 4.7849 and v2 > 5.8651 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(170, 0, 0)'
    elif v1 > 4.7849 and v2 < 2.8727 and v3 > 4.7255:
        return 'rgb(255, 180, 180)'
    elif v1 > 4.7849 and v2 < 2.8727 and v3 < 2.9132:
        return 'rgb(0, 0, 255)'
    elif v1 > 4.7849 and v2 < 2.8727 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(0, 0, 255)'
    elif v1 > 4.7849 and 2.8727 < v2 < 5.8651 and v3 > 4.7255:
        return 'rgb(255, 0, 0)'
    elif v1 > 4.7849 and 2.8727 < v2 < 5.8651 and v3 < 2.9132:
        return 'rgb(0, 0, 255)'
    elif v1 > 4.7849 and 2.8727 < v2 < 5.8651 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(255, 0, 0)'
    elif v1 <= 2.3333 and v2 > 5.8651 and v3 > 4.7255:
        return 'rgb(255, 180, 180)'
    elif v1 <= 2.3333 and v2 > 5.8651 and v3 < 2.9132:
        return 'rgb(0, 0, 255)'
    elif v1 <= 2.3333 and v2 > 5.8651 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(0, 0, 255)'
    elif v1 <= 2.3333 and v2 < 2.8727 and v3 > 4.7255:
        return 'rgb(0, 170, 0)'
    elif v1 <= 2.3333 and v2 < 2.8727 and v3 < 2.9132:
        return 'rgb(0, 170, 0)'
    elif v1 <= 2.3333 and v2 < 2.8727 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(0, 170, 0)'
    elif v1 <= 2.3333 and 2.8727 < v2 < 5.8651 and v3 > 4.7255:
        return 'rgb(180, 255, 180)'
    elif v1 <= 2.3333 and 2.8727 < v2 < 5.8651 and v3 < 2.9132:
        return 'rgb(0, 255, 0)'
    elif v1 <= 2.3333 and 2.8727 < v2 < 5.8651 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(180, 255, 180)'
    elif 2.333 < v1 < 4.7849 and v2 > 5.8651 and v3 > 4.7255:
        return 'rgb(255, 0, 0)'
    elif 2.333 < v1 < 4.7849 and v2 > 5.8651 and v3 < 2.9132:
        return 'rgb(0, 0, 255)'
    elif 2.333 < v1 < 4.7849 and v2 > 5.8651 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(255, 0, 0)'
    elif 2.333 < v1 < 4.7849 and v2 < 2.8727 and v3 > 4.7255:
        return 'rgb(0, 170, 0)'
    elif 2.333 < v1 < 4.7849 and v2 < 2.8727 and v3 < 2.9132:
        return 'rgb(0, 170, 0)'
    elif 2.333 < v1 < 4.7849 and v2 < 2.8727 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(0, 170, 0)'
    elif 2.333 < v1 < 4.7849 and 2.8727 < v2 < 5.8651 and v3 > 4.7255:
        return 'rgb(0, 255, 0)'
    elif 2.333 < v1 < 4.7849 and 2.8727 < v2 < 5.8651 and v3 < 2.9132:
        return 'rgb(0, 0, 170)'
    elif 2.333 < v1 < 4.7849 and 2.8727 < v2 < 5.8651 and 2.9132 <= v3 <= 4.7255:
        return 'rgb(0, 0, 255)'
    else:
        return 'gray'

# Apply the color mapping function to each data point
var1 = data['var1']
var2 = data['var2']
var3 = data['var3']

colors = [custom_color_mapping(v1, v2, v3) for v1, v2, v3 in zip(var1, var2, var3)]
# Create a 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=filtered_data['var1'],
    y=filtered_data['var2'],
    z=filtered_data['var3'],
    text=[f'Creative Difficulty = {x} <br>Context Variability = {y} <br>Accuracy = {z} <br>Task = {v4}'
          for x, y, z, v4 in zip(filtered_data['var1'], filtered_data['var2'], filtered_data['var3'], filtered_data['var4'])],
    mode='markers',
    hoverinfo='text',
    marker=dict(
        size=2,
        color=colors,
        opacity=0.8
    ),
    showlegend=False
)])

# Customize plot layout
fig.update_layout(scene=dict(
    xaxis_title='Creative Difficulty',
    yaxis_title='Context variability',
    zaxis_title='Accuracy',
    xaxis_range=[0, 10],
    yaxis_range=[0, 10],
    zaxis_range=[0, 10],
    aspectmode='cube',
))


# Display the plot using Streamlit
st.plotly_chart(fig)


# Run Streamlit app
if __name__ == "__main__":
    st.write("Open this link in your browser: [Task Automation Analysis - CGI](http://localhost:8501/)")
    st.write("Copy and paste the link in your browser to view the app.")
