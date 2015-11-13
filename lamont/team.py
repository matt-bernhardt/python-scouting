from database import Database


class Team():

    def __init__(self):
        self.data = []
        self.db = Database()
        self.db.connect()

    def load(self, tid):
        sql = ('SELECT * '
               'FROM tbl_teams t '
               'WHERE t.ID = %s')
        print('Query defined')

        rs = self.db.query(sql, (tid, ))
        print('Query executed')

        if (rs.with_rows):
            records = rs.fetchall()
        print('Data retrieved')

        for index, item in enumerate(records):
            print(str(index))
            print(str(type(item)))
            for key, value in enumerate(item):
                print(str(value))
            # self.data.index = self.data.item[index]

        return self.data
