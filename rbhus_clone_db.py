import MySQLdb
import MySQLdb.cursors
import time
import sys
import socket
import os
import tempfile
import debug

hostname = socket.gethostname()
tempDir = tempfile.gettempdir()

dbHostname = "localhost"
dbPort = "3306"
dbDatabase = "test"
# dbLogDatabase = "rbhusPipeLog"

# try:
#   dbHostname = os.environ['rbhusPipe_dbHostname']
# except:
#   pass
# try:
#   dbPort = os.environ['rbhusPipe_dbPort']
# except:
#   pass
# try:
#   dbDatabase = os.environ['rbhusPipe_dbDatabase']
# except:
#   pass
# try:
#   dbLogDatabase = os.environ['rbhusPipe_dbLogDatabase']
# except:
#   pass
username = "nobody"
try:
  if(sys.platform.find("win") >= 0):
    username = os.environ['USERNAME']
  if(sys.platform.find("linux") >= 0):
    username = os.environ['USER']
except:
  pass


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


  
  def _connDb(self,hostname,port,dbname,user="root"):
    try:
      conn = MySQLdb.connect(host = hostname,port=port,db = dbname,user=user)
      conn.autocommit(1)
    except:
      raise
    return(conn)
    
  def _connRbhus(self):
    while(1):
      try:
        con = self._connDb(hostname=dbHostname,port=int(dbPort),dbname=dbDatabase,user=username)
        debug.debug("Db connected")
        return(con)
      except:
        debug.error("Db not connected : "+ str(sys.exc_info()))
      time.sleep(1)


  def execute(self,query,dictionary=False):
    while(1):
      try:
        self.__conn = self._connRbhus()
        if(dictionary):
          cur = self.__conn.cursor(MySQLdb.cursors.DictCursor)
        else:
          cur = self.__conn.cursor()
        debug.debug(query)
        cur.execute(query)
        if(dictionary):
          try:
            rows = cur.fetchall()
          except:
            debug.error("fetching failed : "+ str(sys.exc_info()))
          
          cur.close()
          self.disconnect()
          if(rows):
            return(rows)
          else:
            return(0)
        else:
          cur.close()
          self.disconnect()
          return(1)
      except:
        debug.error("Failed query : "+ str(query) +" : "+ str(sys.exc_info()))
        if(str(sys.exc_info()).find("Can't connect to MySQL") >= 0):
          time.sleep(1)
          try:
            cur.close()
          except:
            pass
          self.disconnect()
          self.__conn = self._connRbhus()
          continue
        else:
          try:
            cur.close()
          except:
            pass
          self.disconnect()
          raise