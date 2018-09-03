# Imports the Google Cloud client library
from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/Users/rafa/Documents/Thesis/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'

#My Variables
MyProject='bigquery-public-data'
MyDataset='the_met'
MyTable='images'

#References
client = bigquery.Client(project=MyProject)
dataset_ref = client.dataset(MyDataset)
table_ref = dataset_ref.table(MyTable)


table = client.get_table(table_ref)  # API Request


# Use the start index to load an arbitrary portion of the table
rows = client.list_rows(table, start_index=10, max_results=1)

# Print row data in tabular format
format_string = '{!s:<16} ' * len(rows.schema)
field_names = [field.name for field in rows.schema]
#print(format_string.format(*field_names))  # prints column headers
for row in rows:
    print(row.gcs_url)     # prints row data


