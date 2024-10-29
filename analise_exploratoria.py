import pandas as pd

base_original = pd.read_csv('pasta_excel/processed.csv', sep='|')

base_original.describe()


base_original.info()
