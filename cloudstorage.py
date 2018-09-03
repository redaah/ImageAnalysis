from google.cloud import storage
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'
MyProject='bigquery-public-data'
MyBucket='gcs-public-data--met'
blob_name='10871/0.jpg'
MyFolder='C:/Users/Rafael/PycharmProjects/ImageAnalysis/Images/'
#delimiter=''
client = storage.Client(project=MyProject)
bucket = client.get_bucket(MyBucket)

def ImageDownload(blob_name, folder):
    # https://console.cloud.google.com/storage/browser/[bucket-id]/
    blob=bucket.blob(blob_name)
    blob.download_to_filename(folder+blob_name.replace('/', '_'))


if __name__=='__main__':
    #ImageDownload('437814/1.jpg','C:/Users/Rafael/PycharmProjects/ImageAnalysis/Images/')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/Rafael/PycharmProjects/ImageAnalysis/Authentication/MyPython-b4f57d70838f.json'
    prefix='437814/object.json'
    blobs = bucket.list_blobs(prefix=prefix)
    print('Blobs:')
    for blob in blobs:
        print(blob.name)
        blob.download_to_filename(MyFolder + blob.name.replace('/', '_'))