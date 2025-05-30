import seaborn as sns
import pandas as pd

titanic_df = sns.load_dataset('titanic')
titanic_df.to_csv('data/titanic.csv', index=False)

