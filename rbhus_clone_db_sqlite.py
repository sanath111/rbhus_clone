import os
import sys
import sqlite3
import time
import debug
import constants

projDir = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])
sys.path.append(projDir)

db_file = os.path.join(constants.database_folder, "rbhus_clone.db")


class db:
    def __init__(self):
        self.__conn = None

    def __del__(self):
        self.disconnect()

    def disconnect(self):
        try:
            if self.__conn:
                self.__conn.close()
                debug.info("Db connection closed\n")
        except:
            debug.info("Error during disconnect: " + str(sys.exc_info()))

    def _connect(self):
        """
        Connect to the SQLite database.
        If the database file doesn't exist, it will be created automatically.
        """
        while True:
            try:
                conn = sqlite3.connect(db_file)
                conn.row_factory = sqlite3.Row  # Ensures rows can be accessed as dictionaries
                debug.info("Db connected")
                return conn
            except:
                debug.info("Db not connected: " + str(sys.exc_info()))
                time.sleep(1)

    def execute(self, query, dictionary=False):
        """
        Execute an SQL query on the database.

        Parameters:
            query (str): The SQL query to execute.
            dictionary (bool): If True, fetch results as dictionaries.

        Returns:
            int: 1 for successful non-SELECT commands (e.g., INSERT, UPDATE).
            list[dict] or list[tuple]: Query results for SELECT commands.
            0: If SELECT returns no results.
        """
        while True:
            try:
                # Ensure connection is established
                self.__conn = self._connect()
                if dictionary:
                    self.__conn.row_factory = sqlite3.Row  # Enable dictionary-like results
                else:
                    self.__conn.row_factory = None  # Use default row format (tuple)

                cur = self.__conn.cursor()
                debug.info(query)
                cur.execute(query)

                if query.strip().upper().startswith("SELECT"):
                    rows = cur.fetchall()
                    cur.close()
                    self.disconnect()
                    if rows:
                        if dictionary:
                            return [dict(row) for row in rows]  # Convert rows to dictionaries
                        else:
                            return rows
                    else:
                        return 0  # No results
                else:
                    # Commit changes for non-SELECT queries
                    self.__conn.commit()
                    cur.close()
                    self.disconnect()
                    return 1
            except sqlite3.Error as e:
                debug.info(f"Failed query: {query} : {e}")
                if "UNIQUE constraint failed" in str(sys.exc_info()):
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

