from google.cloud import storage
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'
MyProject='bigquery-public-data'
prefix='10871/'
delimiter=''

client = storage.Client(project=MyProject)
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('gcs-public-data--met')
# Then do other things...
blobs = bucket.list_blobs(prefix=prefix, delimiter=delimiter)

for blob in blobs:
    print(blob.name)

i=1