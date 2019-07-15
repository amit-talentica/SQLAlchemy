import sqlalchemy as db
import pandas as pd
engine=db.\
create_engine('mysql+mysqlconnector://root:akm@localhost:3306/myflaskapp')

connection=engine.connect()
results=engine.execute('select*from quotes')
#first_result=results.fetchone()
many_result=results.fetchmany(2)
#print(many_result)
#print(type(many_result))
all_results=results.fetchall()
#print(all_results)
#print(many_result)
#print(first_result)
#print(type(first_result))

#Visualization_Of_Data

query=('select*from quotes')
post_df=pd.read_sql_query(query,engine)
print(type(post_df))
print(post_df.columns)
#print (post_df.head)

