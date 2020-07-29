from airflow import settings
from airflow.models import Connection
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

"""
    Create a connection to a service
    """
class AddConnectionOperator(BaseOperator):
    ui_color = '#358140'

    @apply_defaults
    def __init__(self,
                 conn_id='',
                 conn_type='',
                 host='',
                 login='',
                 password='',
                 port='',
                 *args, **kwargs):

        super(AddConnectionOperator, self).__init__(*args, **kwargs)
        self.conn_id=conn_id,
        self.conn_type=conn_type,
        self.host=host,
        self.login=login,
        self.password=password,
        self.port=port


    def execute(self, context):
        conn = Connection(
            conn_id=self.conn_id,
            conn_type=self.conn_type,
            host=self.host,
            login=self.login,
            password=self.password,
            port=self.port
        ) #create a connection object
        session = settings.Session() # get the session
        session.add(conn)
        session.commit()

        self.log.info("Creating an airflow connection with id '{}'".format(self.conn_id))
