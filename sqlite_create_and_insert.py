import sqlite3
connection= sqlite3.connect('sqlite_ci.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE if not Exists Website
               (Post text, Autor text, Views real)''')

post_text = 'this is a raw  post'
post_author = 'alixapordev'
post_views = 6900


INSERT_QUERY = f"INSERT INTO Website VALUES ('{post_text}','{post_author}','{post_views}')"
cursor.execute(INSERT_QUERY)

# check the data in website using select statement
for row in cursor.execute('SELECT * FROM Website'):
    print(row)
    
# Save (commit) the changes
connection.commit()
# close connection
connection.close() 