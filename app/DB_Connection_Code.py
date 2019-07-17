import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
def getDbConnection():
    #Get Database connection
    try:
        connection = mysql.connector.connect(host='localhost', database='cricketTeam', user='root', password='admin')
        return connection
    except mysql.connector.Error as error :
        print("Failed to connect to database {}".format(error))
def closeDbConnection(connection):
    #Close Database connection
    try:
        connection.close()
    except mysql.connector.Error as error :
        print("Failed to close database connection {}".format(error))

def readDbVersion():
    try:
        connection = getDbConnection()
        db_Info = connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version is ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Your connected to - ", record)
        closeDbConnection(connection)
    except mysql.connector.Error as error :
        print("Failed to read database version {}".format(error))
        
def ReadCricketMatch(Match_id):
    #Read data from Hospital table
    try:
        #Call getDbConnection method to get connection. 
    #This method already provided in question 1
    
        connection = getDbConnection()
        cursor = connection.cursor()
        sql_select_query = """select * from mytable"""
        #sql_select_query = """select * from Hospital where Hospital_Id = %s"""
        cursor.execute(sql_select_query)
        #cursor.execute(sql_select_query, (Match_id, ))
        records = cursor.fetchall()
        print("Printing Hospital record")
        # print (records)
        for row in records:
            print("**************Player Information ********************")
            print("PlayerId : ", row[0])
            print("Team : ",row[1])
            print("Name", row[2])
            print("matches", row[3])
            print("InningsPlayed", row[4])
            print("RunsScored", row[5])
            print("HighestScore", row[6])
            print("BattingAVG", row[7])
            print("4s", row[8])
            print("6s", row[9])
            print("IsBowler\n", row[10]) 
            # print("Match Name: = ", row[1])
            # print("Match Score:  = ", row[2], "\n")
        #Close db connection
        closeDbConnection(connection)
    except mysql.connector.Error as error :
        print("Failed to read MatchInfo table {}".format(error))

print("Start of a Python cricket Database Programming Exercise\n")
readDbVersion()
ReadCricketMatch(1)
print("End of a Python cricket Database Programming Exercise\n\n")