import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the glue dataset
glue_data = sns.load_dataset('glue')

# Extract the necessary columns
glue_data = glue_data[['Year', 'Score', 'Model', 'Encoder']]

# Define the encoders and their respective colors
encoder_palette = {'Transformer': 'green', 'LSTM': 'orange'}

# Create the catplots
g = sns.catplot(
    data=glue_data,
    x='Year', y='Score',
    hue='Encoder',
    col='Model',
    kind='violin',
    palette=encoder_palette,
    height=4, aspect=0.7
)

# Adjust the layout and display the plot
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('Score Dependency on Year by Model and Encoder')
plt.show()
