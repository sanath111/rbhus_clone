import MySQLdb
import MySQLdb.cursors
import time
import sys
import socket
import os
import tempfile
import debug
import constants

hostname = socket.gethostname()
tempDir = tempfile.gettempdir()

db_params = constants.db_params

# dbHostname = "localhost"
# dbPort = "3306"
# dbDatabase = "test"
# username = "root"
# password="password"


class db:
  def __init__(self):
    self.__conn = None

  def __del__(self):
    self.disconnect()

  def disconnect(self):
    try:
      self.__conn.close()
    except:
      debug.debug(str(sys.exc_info()))
    debug.debug("Db connection closed" +"\n")


  
  # def _connDb(self,hostname,port,dbname,user,password):
  #   try:
  #     conn = MySQLdb.connect(host = hostname,port=port,db = dbname,user=user,password=password)
  #     conn.autocommit(1)
  #   except:
  #     raise
  #   return(conn)
    
  def _connRbhus(self):
    while 1:
      try:
        # con = self._connDb(hostname=dbHostname,port=int(dbPort),dbname=dbDatabase,user=username,password=password)
        conn = MySQLdb.connect(**db_params)
        conn.autocommit(1)
        debug.debug("Db connected")
        return conn
      except:
        debug.error("Db not connected : "+ str(sys.exc_info()))
      time.sleep(1)


  def execute(self, query, dictionary=False):
    while 1:
      try:
        self.__conn = self._connRbhus()
        if dictionary:
          cur = self.__conn.cursor(MySQLdb.cursors.DictCursor)
        else:
          cur = self.__conn.cursor()
        debug.info(query)
        cur.execute(query)
        if dictionary:
          try:
            rows = cur.fetchall()
          except:
            debug.info("Fetching failed: " + str(sys.exc_info()))
          cur.close()
          self.disconnect()
          if rows:
            return rows
          else:
            return 0
        else:
          cur.close()
          self.disconnect()
          return 1
      except:
        debug.info("Failed query : " + str(query) + " : " + str(sys.exc_info()))
        if str(sys.exc_info()).find("Can't connect to MySQL") >= 0:
          time.sleep(1)
          try:
            cur.close()
          except:
            pass
          self.disconnect()
          self.__conn = self._connRbhus()
          continue
        if str(sys.exc_info()).find("Duplicate entry") >= 0:
          try:
            cur.close()
          except:
            pass
          self.disconnect()
          return str(sys.exc_info())
        if str(sys.exc_info()).find("foreign key constraint fails") >= 0:
          try:
            cur.close()
          except:
            pass
          self.disconnect()
          return str(sys.exc_info())
        else:
          try:
            cur.close()
          except:
            pass
          self.disconnect()
          raise