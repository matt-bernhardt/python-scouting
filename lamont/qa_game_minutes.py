# This is a QA script to make sure that games are being recorded with an accurate number of minutes played
from database import Database
from log import Log


def getMinutes(game, team, duration):
    log.message(str(game) + " " + str(team) + " " + str(duration))

    minutes = 0

    sql = ("SELECT SUM(TimeOff - TimeOn) "
           "FROM tbl_gameminutes "
           "WHERE GameID = %s "
           "AND TeamID = %s")
    rs = database.query(sql, (game, team))

    if (rs.with_rows):
        records = rs.fetchall()

    for index, item in enumerate(records):
        log.message(str(item[0]))
        if(item[0] is None):
            log.message("Skipping empty game")
        else:
            minutes = item[0]

    # decrease minutes for ejections
    sql = ("SELECT TimeOff , Duration "
           "FROM tbl_gameminutes m "
           "INNER JOIN tbl_games g on m.GameID = g.ID "
           "WHERE GameID = %s "
           "AND TeamID = %s "
           "AND Ejected = 1")
    # log.message(sql)
    rs = database.query(sql, (game, team))

    if (rs.with_rows):
        records = rs.fetchall()

    for index, item in enumerate(records):
        minutes += item[1] - item[0]

    return minutes


def reviewTeamGames(team, year):
    # This gets the list of all official games for a given team since a given year
    log.message('Reviewing team ' + str(team) + ' since ' + str(year))

    sql = ("SELECT g.ID AS GameID, MatchTime, HTeamID, HScore, ATeamID, AScore, Duration, MatchTypeID "
           "FROM tbl_games g "
           "INNER JOIN lkp_matchtypes t ON g.MatchTypeID = t.ID "
           "WHERE (HTeamID = %s OR ATeamID = %s) "
           "AND t.Official = 1 "
           "AND YEAR(MatchTime) >= %s "
           "AND MatchTime < NOW() "
           "ORDER BY g.MatchTime")
    # log.message(sql)
    rs = database.query(sql, (team, team, year, ))

    if (rs.with_rows):
        records = rs.fetchall()

    # For each game in the list, generate the number of minutes actually played
    for index, item in enumerate(records):
        recordedMinutes = getMinutes(item[0], team, item[6])  # Sum of recorded time played, compensated for ejections
        expectedMinutes = item[6] * 11  # Recorded duration * 11 players
        log.message(str(item[0]) + " " + str(recordedMinutes) + " " + str(expectedMinutes))
        delta = expectedMinutes - recordedMinutes
        output.message(str(team) + ',' + str(item[0]) + ',' + str(item[1]) + ',' + str(item[2]) + ',' + str(item[3]) + ',' + str(item[4]) + ',' + str(item[5]) + ',' + str(expectedMinutes) + ',' + str(item[7]) + ',' + str(recordedMinutes) + ',' + str(delta))


if __name__ == "__main__":

    # Initialize
    startYear = 2013
    teamlist = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 42, 43, 44, 45, 174, 175, 340, 341, 427, 463, 479, 506, 547]

    log = Log('../logs/qa_game_minutes.log')
    database = Database()
    database.connect()
    log.message('Initialization complete')

    # Output
    output = Log('../output/qa_game_minutes.csv')
    # Output header
    output.message('Team,GameID,MatchTime,Home,HScore,Away,AScore,Duration,MatchType,Sum Minutes,Delta')
    # Output body
    [reviewTeamGames(team, startYear) for team in teamlist]

    # Shut down
    output.end()
    database.disconnect()
    log.end()

print('Finished!')
