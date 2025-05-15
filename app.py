import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st



st.checkbox('Option 1')
st.title("Data Visualization web application")

st.header("Part 1: Data Exploration")
st.write("In this section, we will explore the Altair cars dataset.")
st.markdown("*Further resources [here](https://altair-viz.github.io/gallery/selection_histogram.html)*")

slider = st.slider("Slider title", 0, 100, 50)
if slider > 60:
    st.header("Surprise")
check = st.checkbox("Checkbox title", ["Add a constant", "Add beta 1", "Add beta 2"])
radio = st.radio("Radio title", ["Yes", "No"])
txt = st.text_input("Type here")
txt_area = st.text_area("Type here")
button = st.button("Button name")


df = px.data.iris()

st.dataframe(df)
st.text('Iris dataset')


radio = st.radio("Radio title", ["Iris", "CO2", 'maps'])


if radio == 'Iris':
    #Scatter Plot
    fig = px.scatter(df, x='sepal_width',
                     y='sepal_length',
                     color='species',
                     size='petal_length',
                     hover_data=['petal_width'],
                     marginal_x='box')


    st.title("Iris Plotly")
    st.plotly_chart(fig)

    #Violin PLot
    fig = px.violin(df
                    , y="sepal_width"
                    , color="species"
                    , box=True
                    , points='all')
    st.plotly_chart(fig)


elif radio == 'CO2':
    #Matplotlib
    df = pd.read_csv('data/CO2_per_capita.csv', sep=";")
    df_france = df[df['Country Name'] == 'France']
    df_thailande = df[df['Country Name'] == 'Thailand']

    plt.figure()
    plt.subplot(1, 2, 1)
    sns.lineplot(x='Year', y= 'CO2 Per Capita (metric tons)', data=df_france, color='orange')
    plt.subplot(1, 2, 2)
    sns.lineplot(x='Year', y= 'CO2 Per Capita (metric tons)', data=df_thailande)
    st.pyplot(plt)
    
    # TODO: Transform your data so that you can easily plot it


    
    start_year, end_year = st.slider('choose years',  min_value=1970, max_value=2011,value=(2000, 2011))
    n = st.selectbox("Select number of country to diplay", [3,5,10,20,30], index=2)

    mask = (df['Year'] >= start_year) & (df['Year'] <= end_year)

    df_filtered = df[mask]

    df_filtered_sum = df_filtered.groupby('Country Name')['CO2 Per Capita (metric tons)'].sum()

    df_filtered_sum = df_filtered_sum.reset_index()

    df_filtered_sum

    df_sorted = df_filtered_sum.sort_values(by='CO2 Per Capita (metric tons)', ascending=False)

    df_top = df_sorted.head(n)


    plt.figure()

    sns.barplot(x= df_top['Country Name'] ,y = df_top['CO2 Per Capita (metric tons)'])
    plt.xticks(rotation=90)
    st.pyplot(plt)


elif radio == 'maps':
    co2 = pd.read_csv('data/CO2_per_capita.csv', sep=";")

    co2 = co2.dropna().sort_values('Year')

    # TODO: Visualize your data on a World map
    fig = px.scatter_geo(co2, locations="Country Code",
                        # color="continent", # which column to use to set the color of markers
                        hover_name="Country Name", # column added to hover information
                        size="CO2 Per Capita (metric tons)", # size of markers
                        animation_frame='Year')
    st.plotly_chart(fig)
    
    


