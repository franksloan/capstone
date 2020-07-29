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


def prettyRedshiftProps(props):
    pd.set_option('display.max_colwidth', -1)
    keysToShow = ["ClusterIdentifier", "NodeType", "ClusterStatus", "MasterUsername", "DBName", "Endpoint", "NumberOfNodes", 'VpcId']
    x = [(k, v) for k,v in props.items() if k in keysToShow]
    return pd.DataFrame(data=x, columns=["Key", "Value"])

"""
    Prints out the redshift cluster status and the ARN attached to it
    """
def main():
    redshift = boto3.client('redshift',
                       region_name="us-west-2",
                       aws_access_key_id=KEY,
                       aws_secret_access_key=SECRET
                       )
    myClusterProps = redshift.describe_clusters(ClusterIdentifier=CLUSTER_IDENTIFIER)['Clusters'][0]
    print(prettyRedshiftProps(myClusterProps))

if __name__ == "__main__":
    main()
