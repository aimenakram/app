import streamlit as st
import pandas as pd
import seaborn as sns

# Load the Iris dataset
iris = sns.load_dataset('iris')

# Streamlit app
def main():
    st.title("Simple Data Visualization App")

    # Sidebar selection
    st.sidebar.title("Select Features")
    x_axis = st.sidebar.selectbox("X-axis", iris.columns[:-1])
    y_axis = st.sidebar.selectbox("Y-axis", iris.columns[:-1])

    # Scatter plot
    st.subheader("Scatter Plot")
    sns.scatterplot(data=iris, x=x_axis, y=y_axis, hue='species')
    st.pyplot()

    # Data table
    st.subheader("Data Table")
    st.write(iris)

if __name__ == "__main__":
    main()
