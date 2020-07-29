import boto3
import configparser
import json

# CONFIG
config = configparser.ConfigParser()
config.read('aws.cfg')
config.read('redshift.cfg')

KEY                = config.get('AWS','KEY')
SECRET             = config.get('AWS','SECRET')

CLUSTER_TYPE       = config.get("REDSHIFT","CLUSTER_TYPE")
NUM_NODES          = config.get("REDSHIFT","NUM_NODES")
NODE_TYPE          = config.get("REDSHIFT","NODE_TYPE")
CLUSTER_IDENTIFIER = config.get("REDSHIFT","CLUSTER_IDENTIFIER")

DB_NAME            = config.get("DATABASE","NAME")
DB_USER            = config.get("DATABASE","USER")
DB_PASSWORD        = config.get("DATABASE","PASSWORD")



"""
    Create an AWS Redshift cluster using details
    configured in dwh.cfg

    INPUTS:
    * redshift - a connection to AWS Redshift
    * roleArn - the ARN to create the cluster for
    """
def create_redshift_cluster(redshift):
    try:
        print("Creating redshift cluster")
        return redshift.create_cluster(
            #HW
            ClusterType=CLUSTER_TYPE,
            NodeType=NODE_TYPE,
            NumberOfNodes=int(NUM_NODES),

            #Identifiers & Credentials
            DBName=DB_NAME,
            ClusterIdentifier=CLUSTER_IDENTIFIER,
            MasterUsername=DB_USER,
            MasterUserPassword=DB_PASSWORD
        )
    except Exception as e:
        print(e)

"""
    Create Redshift cluster
    """
def main():

    redshift = boto3.client('redshift',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                       )

    cluster = create_redshift_cluster(redshift)
    print("Finished creating cluster")


if __name__ == "__main__":
    main()
