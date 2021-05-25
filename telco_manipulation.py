from env import host, username, password
from pydataset import data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from env import host, username, password
def get_db_url(username,password,host,db_name):
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'

churn_db = pd.read_sql('''SELECT * FROM customers 
                          JOIN internet_service_types USING(internet_service_type_id)
                          JOIN contract_types USING(contract_type_id)
                          JOIN payment_types USING (payment_type_id);''',
                        churn_url)