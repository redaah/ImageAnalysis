# Imports the Google Cloud client library
from google.cloud import bigquery
import os

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/Rafael/Desktop/Temp/bigquerytest-2e2156128650.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/Users/rafa/Documents/Thesis/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'

#My Variables
MyProject='bigquery-public-data'
MyDataset='the_met'
MyTable='images'

#References
client = bigquery.Client(project=MyProject)
dataset_ref = client.dataset(MyDataset)
table_ref = dataset_ref.table(MyTable)


table = client.get_table(table_ref)  # API Request

# View table properties
print(table.schema)
print(table.description)
print(table.num_rows)
