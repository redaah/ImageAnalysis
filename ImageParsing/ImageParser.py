# Imports the Google Cloud client library
from google.cloud import bigquery
import os
#import cloudstorage
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='/Users/rafa/Documents/Thesis/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'

#My Variables
MyProject='bigquery-public-data'
MyDataset='the_met'
MyTable='images'
MyBucket='gcs-public-data--met'
MyFolder='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Images/'

#References
client = bigquery.Client(project=MyProject)
dataset_ref = client.dataset(MyDataset)
table_ref = dataset_ref.table(MyTable)


table = client.get_table(table_ref)  # API Request

# Use the start index to load an arbitrary portion of the table
rows = client.list_rows(table, start_index=10, max_results=1)

for row in rows:
    FileName=(row.gcs_url.replace('gs://', '').replace(MyBucket+'/', ''))     # prints row data
    print(FileName)
    #cloudstorage.ImageDownload(FileName,MyFolder)

