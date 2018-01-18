import MySQLdb

class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    #! Открытие соединения
    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db
            )
            self._connection.set_character_set('utf8')

    #! Закрытие соединения
    def disconnect(self):
        if self._connection:
            self._connection.close()
class Team1:
    def __init__(self, db_connection, team_name, rating, sport, number_of_players ):
        self.db_connection = db_connection.connection
        self.team_name = team_name
        self.rating = rating
        self.sport = sport
        self.number_of_players = number_of_players

    def save(self):
        c = self.db_connection.cursor()
        c.execute("insert into app_team (team_name, rating, sport, number_of_players) values(%s, %s, %s, %s);",
                  (self.team_name, self.rating, self.sport, self.number_of_players))
        self.db_connection.commit()
        c.execute("SELECT * FROM app_team;")
        c.close()
class User_11:
    def __init__(self, db_connection, first_name, last_name, phone, email, birthday, passport):
        self.db_connection = db_connection.connection
        self.first_name  = first_name
        self.last_name  = last_name
        self.phone = phone
        self.email = email
        self.birthday = birthday
        self.passport = passport

    def save(self):
        c = self.db_connection.cursor()
        c.execute("insert into app_user_1 (first_name , last_name, phone, email, birthday, passport) values(%s, %s, %s, %s, %s, %s);",
                  ( self.first_name, self.last_name, self.phone, self.email, self.birthday, self.passport))
        self.db_connection.commit()
        c.close()
# class Bet1:
#     def __init__(self, db_connection,  user, team, date, amount):
#         self.db_connection = db_connection.connection
#         self.user  = user
#         self.team  = team
#         self.date  = date
#         self.amount = amount
#
#
#     def save(self):
#         c = self.db_connection.cursor()
#         c.execute("insert into app_bet ( user, team, date, amount) values( %s,%s, %s, %s);",
#                   (  self.user,self.team, self.date, self.amount))
#         self.db_connection.commit()
#         c.close()



conn = Connection("dbuser", "123", "db")

with conn:
     app_team = Team1(conn, 'локомотив', 2, 'хоккей', '13')
     app_team.save()
     app_user_1 = User_11(conn, 'Алина','Ипатова', 34678655, 'alina@mail.ru','1999-03-06',456677766)
     app_user_1.save()
    # app_bet=Bet1(conn,app_user_1,app_team,'2017-10-11',1300)
    # app_bet.save()



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# from app.models import User_1, Team, Bet
# from datetime import datetime
# x=User_1.objects.get(pk=2)
# y = Team.objects.get(pk=2)
#
# b=Bet.objects.create(user=x,team=y,date='2017-11-11',amount=4000)
# b.save()
#
#
# y = Team.objects.all()
#
# yz=y.filter(team_name="спартак")
#
# print([r.rating for r in yz])
