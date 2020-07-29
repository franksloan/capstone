import pandas as pd
import boto3
import configparser

# CONFIG
config = configparser.ConfigParser()
config.read('aws.cfg')
config.read('redshift.cfg')

KEY                = config.get('AWS','KEY')
SECRET             = config.get('AWS','SECRET')
CLUSTER_IDENTIFIER = config.get("REDSHIFT","CLUSTER_IDENTIFIER")

"""
    Delete to Redshift cluster.
    """
def main():
    redshift = boto3.client('redshift',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                       )
    redshift.delete_cluster( ClusterIdentifier=CLUSTER_IDENTIFIER,  SkipFinalClusterSnapshot=True)

if __name__ == "__main__":
    main()
