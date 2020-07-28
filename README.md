# capstone
Capstone project for Udacity data engineering

## Running the project

Please enter the `KEY` and `SECRET` for your AWS account in `aws.cfg`

To create a Redshift cluster:
```
python launch_redshift.py
```
Check the status:
```
python check_redshift_status.py
```

Delete the Redshift cluster:
```
python tear_down_redshift.py
```
