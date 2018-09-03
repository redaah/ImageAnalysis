from google.cloud import storage
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'
MyProject='bigquery-public-data'
MyBucket='gcs-public-data--met'
#blob_name='10871/0.jpg'
#delimiter=''

def ImageDownload(blob_name, folder):
    client = storage.Client(project=MyProject)
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    bucket = client.get_bucket(MyBucket)

    blob=bucket.blob(blob_name)
    blob.download_to_filename(folder+blob_name.replace('/', '_'))


if __name__=='__main__':
    ImageDownload('10871/0.jpg','C:/Users/Rafael/PycharmProjects/ImageAnalysis/Images/')