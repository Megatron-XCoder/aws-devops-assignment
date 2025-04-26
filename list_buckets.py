import boto3

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    print("Your S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")

def count_objects_in_bucket(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print(f"Total objects in {bucket_name}: {len(response['Contents'])}")
    else:
        print(f"No objects found in {bucket_name}.")

if __name__ == "__main__":
    list_s3_buckets()

    bucket_name = input("Enter the S3 bucket name to count objects: ")
    count_objects_in_bucket(bucket_name)

