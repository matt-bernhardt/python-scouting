import database
import log

if __name__ == "__main__":
  #Initialize
  log.start('test.log')
  database.connect()
  log.message('Database opened')

  # Get list of teams
  sql = ("SELECT teamname FROM tbl_teams ORDER BY teamname ASC")
  rs = database.query(sql)
  for (teamname) in rs:
  	log.message(teamname[0])

  # Shut down
  database.disconnect()
  log.message('Database closed')
  log.end()

  print('Finished!')