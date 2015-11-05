# This is a QA script to reconcile final game scores with records of individual goals

from database import Database
from log import Log


def getGoals(game, team):
    goals = {}
    goals['team'] = 0
    goals['opponent'] = 0
    goals['error'] = 0

    sql = ("SELECT ID, TeamID, Event "
           "FROM tbl_gameevents "
           "WHERE GameID = %s "
           "AND Event IN (1,6)")
    # log.message(sql)
    rs = database.query(sql, (game, ))

    if (rs.with_rows):
        records = rs.fetchall()

    for index, item in enumerate(records):
        log.message(str(item[0]) + ": " + str(item[1]) + "_" + str(team) + " and " + str(item[2]))
        if (item[1] == team and item[2] == 1):
            goals['team'] += 1
        elif (item[1] == team and item[2] == 6):
            goals['opponent'] += 1
        elif (item[1] != team and item[2] == 1):
            goals['opponent'] += 1
        elif (item[1] != team and item[2] == 6):
            goals['team'] += 1
        else:
            goals['error'] += 1

    return goals


def reviewTeamGames(team, year):
    # This gets the list of all official games for a given team since a given year
    log.message('Reviewing team ' + str(team) + ' since ' + str(year))

    sql = ("SELECT g.ID AS GameID, g.MatchTime, MatchType, IF(HTeamID = %s, HScore, AScore) AS GoalsExpected, if(HTeamID = %s, ATeamID, HTeamID) AS Opponent, if(HTeamID = %s, AScore, HScore) AS OppGoalsExpected "
           "FROM tbl_games g "
           "INNER JOIN lkp_matchtypes t ON g.MatchTypeID = t.ID "
           "WHERE (HTeamID = %s OR ATeamID = %s) "
           "AND t.Official = 1 "
           "AND YEAR(MatchTime) >= %s "
           "AND MatchTime < NOW() "
           "ORDER BY g.MatchTime")
    # log.message(sql)
    rs = database.query(sql, (team, team, team, team, team, year, ))

    if (rs.with_rows):
        records = rs.fetchall()

    # For each game in the list, generate the number of minutes actually played
    for index, item in enumerate(records):
        # Get goal records from tbl_gameevents, for this game, by this team
        goalsRecorded = getGoals(item[0], team)
        log.message("Game " + str(item[0]) + " by team " + str(team) + ": " + str(goalsRecorded) + " errors")
        output.message(str(team) + ',' + str(item[0]) + ',' + str(item[1]) + ',' + str(item[2]) + ',' + str(item[3]) + ',' + str(goalsRecorded['team']) + ', ,' + str(item[4]) + ',' + str(item[5]) + ',' + str(goalsRecorded['opponent']))


if __name__ == "__main__":

    # Initialize
    startYear = 2013
    teamlist = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 42, 43, 44, 45, 174, 175, 340, 341, 427, 463, 479, 506, 547]

    log = Log('../logs/qa_game_goals.log')
    database = Database()
    database.connect()
    log.message('Initialization complete')

    # Output
    output = Log('../output/qa_game_goals.csv')
    # Output header
    output.message('Team,GameID,MatchTime,MatchType,Expected,Recorded,Delta,Opponent,Expected,Recorded,Delta')
    # Output body
    [reviewTeamGames(team, startYear) for team in teamlist]

    # Shut down
    output.end()
    database.disconnect()
    log.end()

print ('Finished!')
