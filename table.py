import pandas as pd

file= 'Resources/cities.csv'

cities_df=pd.read_csv(file)
cities_df.to_html('data.html')
