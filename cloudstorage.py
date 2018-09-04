from google.cloud import storage
import os

#Variables definition
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'
MyProject='bigquery-public-data'
MyBucket='gcs-public-data--met'
blob_name='10871/0.jpg'
MyFolder='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Images/'
client = storage.Client(project=MyProject)
bucket = client.get_bucket(MyBucket)

def download_all_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        download_blob(bucket.name, blob.name, MyFolder+blob.name.replace('/', '_'))

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)


if __name__=='__main__':

    download_all_blobs(bucket.name)



