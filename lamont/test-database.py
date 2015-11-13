from database import Database

print('Starting...')

print('Creating database...')
database = Database()
print(str(type(database)))
print(str(type(database.cnx)))
print(str(type(database.cursor)))

print('')

print('Connecting...')
database.connect()
print(str(type(database.cnx)))
print(str(type(database.cursor)))

print('')

sql = ('SELECT count(ID) FROM tbl_players p WHERE FirstName = %s')
params = ('Brian', )
rs = database.query(sql, params)
for value in rs:
    print(str(value[0]) + ' players named ' + str(params[0]) + ' in database')

print('Database queried')

print(str(database.warnings))

print('Database warnings retrieved')

database.disconnect()

print('Database closed')

print('Finished!')
