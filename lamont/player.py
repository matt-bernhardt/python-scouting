from database import Database


class Player():

    def __init__(self):
        self.data = {}
        self.db = Database()
        self.db.connect()

    def loadID(self, tid):
        # This looks up a player record by ID
        sql = ('SELECT ID, FirstName, LastName '
               'FROM tbl_players p '
               'WHERE p.ID = %s')
        rs = self.db.query(sql, (tid, ))

        if (rs.with_rows):
            records = rs.fetchall()

        for index, item in enumerate(records):
            self.data["ID"] = item[0]
            self.data["First"] = item[1]
            self.data["Last"] = item[2]

        return self

    def lookup(self, needle):
        # This takes a dictionary 'needle' and uses it to look up player information
        print("Looking up...")
        for item in needle:
            print(str(item))
        output = {}
        print("\n")
        return output

    def lookupName(self, name):
        sql = ('SELECT ID, FirstName, LastName '
               'FROM tbl_players p '
               'WHERE TRIM(CONCAT(FirstName," ",LastName)) LIKE %s '
               'ORDER BY LastName ASC, FirstName')
        rs = self.db.query(sql, (name, ))

        if (rs.with_rows):
            records = rs.fetchall()

        for index, item in enumerate(records):
            self.data.index = self.data.item[index]

        return self

    def dumpToTerminal(self):
        print("Dumping...")
        for item in self.data:
            print(str(item) + ": " + str(self.data[item]))
        print("...Done\n")
