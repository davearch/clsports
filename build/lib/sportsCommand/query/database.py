# sportsCommand
#
from sportsCommand.query.query import query
from sportsCommand.nfl.league import league
from sportsCommand.nfl.team import team
import sys
import sqlite3

class sportsCommandDB():
    __version__ = 2
    _TABLE_sportsCommandDB = "CREATE TABLE sportsCommandDB(version INTEGER);"

    _TABLE_leagues         = "CREATE TABLE leagues(" \
                             "name TEXT NOT NULL UNIQUE, " \
                             "enabled INTEGER NOT NULL DEFAULT 1," \
                             "league_id TEXT NOT NULL UNIQUE, " \
                             ");" \
                             "CREATE INDEX leagues_name on leagues(name);"

    _TABLE_teams           = "CREATE TABLE teams(" \
                             "name TEXT NOT NULL, " \
                             "team_id TEXT NOT NULL, " \
                             "enabled INTEGER NOT NULL DEFAULT 1" \
                             ");"

    _TABLE_players         = "CREATE TABLE players(" \
                             "name_first TEXT NOT NULL, " \
                             "name_last TEXT NOT NULL, " \
                             "position TEXT NOT NULL, " \
                             "jersey_number INTEGER NOT NULL DEFAULT 1" \
                             "status INTEGER NOT NULL DEFAULT 1" \
                             "enabled INTEGER NOT NULL DEFAULT 1" \
                             "playerteam TEXT NOT NULL, " \
                             "FOREIGN KEY(playerteam) REFERENCES teams(tead_id)" \
                             ");"

    def __init__(self):
        filename = '/tmp/sc.db'
        try:
            self._db = sqlite3.connect(
                filename, check_same_thread=False,
                detect_types=sqlite3.PARSE_DECLTYPES)
            self._dbFilename = filename
        except sqlite3.OperationalError, e:
            raise
        cur = self._db.cursor()
        cur.execute("PRAGMA foreign_keys = ON;")
        try:
            cur.execute("SELECT version FROM fail2banDb LIMIT 1")
        except sqlite3.OperationalError:
            self.createDB()
        else:
            version = cur.fetchone()[0]
        finally:
            cur.close()



    def createDB(self, cur):
        cur.executescript(sportsCommandDB._TABLE_sportsCommandDB)
        cur.execute("INSERT INTO sportsCommandDB(version) VALUES(?)",
                    (sportsCommand.__version__, ))
        cur.executescript(sportsCommandDB._TABLE_leagues)
        cur.executescript(sportsCommandDB._TABLE_teams)
        cur.executescript(sportsCommandDB._TABLE_players)
        cur.executescript("SELECT version from sportsCommandDB LIMIT 1")
        return cur.fetchone()[0]

    def filename(self):
        return self._dbFilename

    def addLeague(self, cur, league):
        cur.execute(
            "INSERT or REPLACE INTO leagues(name, league_id, enabled) VALUES(?, ?, 1)",
            (league.name, league.league_id,))

    def delLeague(self, cur, league):
        cur.execute(
            "UPDATE leagues set enabled=0 WHERE name = ?", (league.name, ))

    def delAllLeagues(self, cur):
        cur.execute("UPDATE leagues set enabled=0")

    def getLeagueNames(self, cur):
        cur.execute("SELECT name from leagues")
        return set(row[0] for row in cur.fetchmany())

    def addTeam(self, cur, team):
        cur.execute(
            "INSERT OR REPLACE INTO leagues(name, team_id) VALUES(?, ?)",
            (team.name, team.team_id))

    def delTeam(self, cur, team):
        cur.execute(
            "UPDATE teams set enabled=0 WHERE name = ?", (team.name, ))

    def getTeamNames(self, cur):
        cur.execute("SELECT name from teams")
        return set(row[0] for row in cur.fetchmany())

    def addPlayer(self, cur, player):
        cur.execute(
            "INSERT OR REPLACE INTO players(name_first, name_last, position," \
            "jersey_number, status, enabled, playerteam) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (player.name_first, player.name_last, player.position,
             player.jersey_number, player.status, player.enabled, player.playerteam))

    def delPlayer(self, cur, player):
        cur.execute(
            "UPDATE players set enabled=0 WHERE name = ?", (player.name, ))

    def getPlayerNames(self, cur):
        cur.execute("SELECT name from players")
        return set(row[0] for row in cur.fetchmany())
