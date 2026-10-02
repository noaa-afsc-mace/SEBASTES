# coding=utf-8

#     National Oceanic and Atmospheric Administration (NOAA)
#     Alaskan Fisheries Science Center (AFSC)
#     Resource Assessment and Conservation Engineering (RACE)
#     Midwater Assessment and Conservation Engineering (MACE)

#  THIS SOFTWARE AND ITS DOCUMENTATION ARE CONSIDERED TO BE IN THE PUBLIC DOMAIN
#  AND THUS ARE AVAILABLE FOR UNRESTRICTED PUBLIC USE. THEY ARE FURNISHED "AS
#  IS."  THE AUTHORS, THE UNITED STATES GOVERNMENT, ITS INSTRUMENTALITIES,
#  OFFICERS, EMPLOYEES, AND AGENTS MAKE NO WARRANTY, EXPRESS OR IMPLIED,
#  AS TO THE USEFULNESS OF THE SOFTWARE AND DOCUMENTATION FOR ANY PURPOSE.
#  THEY ASSUME NO RESPONSIBILITY (1) FOR THE USE OF THE SOFTWARE AND
#  DOCUMENTATION; OR (2) TO PROVIDE TECHNICAL SUPPORT TO USERS.

"""
.. module:: dbConnection

    :synopsis: dbConnection provides a more Pythonic interface
               for QSqlQuery and wraps in some other code that
               was common to many of MACE's applications.


| Developed by:  Rick Towler   <rick.towler@noaa.gov>
|                Kresimir Williams   <kresimir.williams@noaa.gov>
| National Oceanic and Atmospheric Administration (NOAA)
| National Marine Fisheries Service (NMFS)
| Alaska Fisheries Science Center (AFSC)
| Midwater Assesment and Conservation Engineering Group (MACE)
|
| Author:
|       Rick Towler   <rick.towler@noaa.gov>
| Maintained by:
|       Rick Towler   <rick.towler@noaa.gov>
"""
import logging
from PySide6 import QtSql


class SQLError(Exception):

    def __init__(self, query):

        self.QSqlQuery = query
        self.error = self.__stripErrorChars(query.lastError().text())
        self.SqlText = str(query.lastQuery())

    def __str__(self):

        return repr(' ::: '.join([self.error, self.SqlText]))

    def __stripErrorChars(self, rawMsg):
        '''
        stripErrorChars is a simple method to extract the readable text from
        error messages returned by QSqlQuery.
        '''
        msg = []
        for s in rawMsg:
            if (s != "\x00"):
                msg.append(s)
            else:
                break

        return ''.join(msg)


class DBError(Exception):

    def __init__(self, db):

        self.db = db
        self.error = self.__stripErrorChars(db.lastError().text())

    def __str__(self):

        return repr(' ::: '.join([ str(self.db.databaseName()), self.error]))

    def __stripErrorChars(self, rawMsg):
        '''
        stripErrorChars is a simple method to extract the readable text from
        error messages returned by QSqlQuery.
        '''
        msg = []
        for s in rawMsg:
            if (s != '\x00'):
                msg.append(s)
            else:
                break

        return ''.join(msg)


class dbQueryResults:
    '''
    The dbQueryResults class provides an iterator interface for the qSqlQuery
    object. This can be used to provide a more transparent method for iterating
    through results returned by SQL SELECT statements since the column values
    are returned in a list which can be unpacked in a for-in loop. For example:

        sql = ("SELECT device_id, device_name FROM clamsbase2.devices")
        results = self.db.dbQuery(sql)
        for dev_id, dev_name in results:
            print(dev_id)
            print(dev_name)

    Note that ALL values are returned as Python strings EXCEPT for NULL's which
    are returned as None.

    The class has the following properties:

        columns     - a list of column names as lower case python strings ordered
                      the same as the data.
        columnTypes - A list of strings describing the data type of the columns.
                      Note that this *is not* the data type of the returned data
                      as all values are returned as strings but the type of the
                      database column.
        nColumns    - An integer denoting the number of columns in the returned
                      result.
        query       - The reference to the qSQLQuery object used to generate the
                      query results.

    '''

    def __init__(self, qSqlQuery, columns, types, dateFormatString=None):

        self.query = qSqlQuery
        self.columns = columns
        self.columnTypes = types
        self.nColumns = len(self.columns)
        self.rowList = [None] * self.nColumns

        if dateFormatString:
            self.dateFormat = dateFormatString
        else:
            self.dateFormat = 'MM/dd/yyyy hh:mm:ss'


    def convert(self, i):

        if (self.query.isNull(i)):
            val = None
        #  handle DateTime conversion explicitly
        elif (self.columnTypes[i] == 'QDateTime'):
            val = self.query.value(i).toString(self.dateFormat)
        #  deal with PyQt4/PyQt5 differences in returning integer values as "floats"
        elif (self.columnTypes[i] in ['float','double']):
            if (self.query.value(i).is_integer()):
                val = str(int(self.query.value(i)))
            else:
                val = str(self.query.value(i))
        else:
                #  try a direct conversion to python string
                val = str(self.query.value(i))

        return val

    def __iter__(self):
        return self

    def __next__(self):

        if self.query.next():
            #  build a new list of items for this row
            self.rowList = [self.convert(i) for i in range(self.nColumns)]
            return self.rowList
        else:
            raise StopIteration

    def first(self):

        if self.query.first():
            #  build the list of items to return
            self.rowList = [self.convert(i) for i in range(self.nColumns)]
        else:
            #  nothing to return as the query is empty
            self.rowList = [None] * self.nColumns

        return self.rowList

    def last(self):

        if self.query.last():
            #  build the list of items to return
            self.rowList = [self.convert(i) for i in range(self.nColumns)]
        else:
            #  nothing to return as the query is empty
            self.rowList = [None] * self.nColumns

        return self.rowList


class dbConnection:
    '''
    The dbConnection class is a simple class that encapsulates much of the common
    code we've implemented for SQL interaction in CLAMS and MACEBASE.

        driver - set to the QSqlDatabase driver you wish to use for
                 the connection. See QSqlDatabase docs for details but
                 common options are:

                 QPSQL    - Postgres SQL driver
                 QMYSQL   - MySQL driver
                 QSQLITE  - SQLite version 3 or greater
                 QSQLITE2 - SQLite version 2
                 QODBC3   - ODBC driver (default)

                 For Oracle connections, use the default ODBC driver. The
                 full QOCI driver does not ship with Qt.

                 Note that when using the ODBC driver with NON-Oracle
                 databases you need to set the isOracle keyword to 'False'
    '''

    def __init__(self, source, username, password, label='db', driver='QODBC',
            isOracle=True, hostname=None, port=5432, serviceName=None, OracleHome=None,
            ODBCOptions=["SQL_ATTR_ODBC_VERSION=SQL_OV_ODBC3", "SQL_ATTR_PACKET_SIZE=127"],
            OracleODBCFetchBufferSize=33554432):
        '''
    
            source (str): The source argument differs depending on the driver you are using.

                QODBC: For non-Oracle ODBC connections, this is the ODBC Data Source Name (DSN).

                       For Oracle ODBC connections, this is the TNS Name from your tnsnames.ora
                       file that describes your connection. For Oracle connections, you can set
                       this to None, and then set the hostname, port, and serviceName arguments
                       to connect without using a tnsnames.ora file.

            username (str): Set this to the username you are using to log into your database
            password (str): Set this to the password for your user

            hostname (str): Optional. Set this to the database server hostname. This argument is
                    required if source is None.
            port (int): Set this to an integer specifying the database server port to connect to.
            serviceName (str): Optional. Required for Oracle ODBC connection if source is None.

        '''

        self.label = label
        self.lastError = ''
        self.qtDateFormatString = None
        self.loggingEnabled = False
        self.logger = None
        self.handler = None
        self.hasTransactions = False
        self.preparedQuery = None

        #  Postgres handles ForwardOnly queries differently than other drivers
        #  so we change the default behavior of dbConnection to *not* set
        #  forwardOnly when connecting to a Postgres database
        self.isPostgres = False

        #  force isOracle keyword for drivers that are obviously *not* oracle
        if (driver.lower() not in ['qodbc', 'qoci']):
            #  this is for sure not an oracle driver
            isOracle=False

            if driver.lower() == 'qpsql':
                #  Postgres doesn't handle ForwardOnly queries like other drivers
                #  so we will disable forward only by default when using the QPSQL driver.
                self.isPostgres = True

        #  create an instance of QSqlDatabase - if None is passed as the label
        #  we'll create the Qt "default" connection.
        if (label == None):
            self.db = QtSql.QSqlDatabase.addDatabase(driver)
        else:
            self.db = QtSql.QSqlDatabase.addDatabase(driver, label)

        #  configure the QSqlDatabase connection. Changes in Qt 6.9.x require Oracle ODBC
        #  connections to use a full connection string, instead of simply passing an ODBC
        #  DSN and then setting the username and password. Since this approach should be
        #  backwards compatible with previous versions of Qt, we'll switch to using it for
        #  all Oracle ODBC connections.
        #
        #    NOTE! With this approach, the source is the TNS Name, NOT the ODBC DSN name
        #
        if isOracle and driver.lower() == 'qodbc':
            connectionOptions = []

            #  For Oracle ODBC connections, we have to construct a connection string.
            #  First, extract the Oracle home name from the registry if needed
            if OracleHome is None:
                #  Try to get a list of Oracle driver installations (aka Oracle Home)
                #OracleHome = _get_oracle_homes()
                OracleHome = get_oracle_odbc_driver_name()

                if OracleHome is None:
                    raise ValueError("Unable to find an entry for the Oracle ODBC driver. " +
                            "Has this been installed?")
                            
            #  set the driver entry
            connectionOptions.append("Driver={" + OracleHome + "}")

            #  Now determine if we're using a TNS name, or hostname:port/servicename
            if source is None:
                #  TNS name not provided, try to use hostname:port/servicename
                if hostname is None or serviceName is None:
                    raise ValueError("When not providing a TNS source name, you must pass the " +
                            "hostname, port and serviceName used to connect to your database.")

                #  pass the full hostname:port/servicename as the "DB Questionnaire" entry
                connectionOptions.append("DBQ=" + hostname + ":" + port + "/" + serviceName)
            else:
                #  pass the TNS name as the "DB Questionnaire" entry
                connectionOptions.append("DBQ=" + source)

            #  add the username and password
            connectionOptions.append("UID=" + username)
            connectionOptions.append("PWD=" + password)

            #  add the fetch buffer size - don't allow a FBS smaller than 16k
            if OracleODBCFetchBufferSize > 16384:
                connectionOptions.append("FBS=" + str(OracleODBCFetchBufferSize))

            #  assemble the connection string
            connectString = ';'.join(connectionOptions) + ";"

            #  finally, set the connection string in the database object
            self.db.setDatabaseName(connectString)

            #  Now apply our ODBC options
            for option in ODBCOptions:
                self.db.setConnectOptions(option)

        else:
            #  non-Oracle connections can be configured as they have always been, using
            #  the appropriate methods to set the source, username, password, etc.
            self.db.setDatabaseName(source)
            self.db.setUserName(username)
            self.db.setPassword(password)
            if hostname:
                self.db.setHostName(hostname)
                self.db.setPort(port)

        if (isOracle):
            #  set the default Oracle date and timestamp formats
            self.NLS_DATE_FORMAT = 'MM/DD/YYYY HH24:MI:SS'
            self.NLS_TIMESTAMP_FORMAT = 'MM/DD/YYYY HH24:MI:SS.FF3'
        else:
            #  non-Oracle databases do not support this NLS business
            self.NLS_DATE_FORMAT = None
            self.NLS_TIMESTAMP_FORMAT = None
        

    def startTransaction(self):
        '''
        startTransaction starts a transaction if your driver supports transactions.
        Check the state of the hasTransactions property AFTER YOU HAVE CONNECTED TO
        YOUR DB to determine if your driver supports transactions.
        '''

        #  start a transaction
        ok = self.db.transaction()
        #  check if we had a problem
        if (not ok):
            #  ooops, there was a problem - report the error
            raise DBError(self.db)


    def commit(self):
        '''
        commit will end a transaction and commit data to your database if you have started
        a transaction and your driver supports transactions
        '''
        #  commit
        ok = self.db.commit()
        #  check if we had a problem
        if (not ok):
            #  ooops, there was a problem - report the error
            raise DBError(self.db)


    def rollback(self):
        '''
        rollback will end a transaction and undo everything you have done after starting
        the transaction.
        '''
        #  rollback
        ok = self.db.rollback()
        #  check if we had a problem
        if (not ok):
            #  ooops, there was a problem - report the error
            raise DBError(self.db)


    def setOracleDateFormat(self, formatString=None, QtFormatString=None):
        '''
        setOracleDateFormat sets the Oracle NLS_DATE_FORMAT variable for the current session.
        The NLS_DATE_FORMAT specifies the format that dates are returned from or inserted
        into the database if the TO_CHAR() or TO_DATE() functions are called without a
        format string. The default format is:

           MM/DD/YYYY HH24:MI:SS

        You should rarely need to change this. IF YOU DO CHANGE THE DATE FORMAT
        YOU REALLY SHOULD CHANGE THE QT FORMAT STRING TO MATCH. If you fail to
        do this, you will either get bogus dates or errors from date conversion
        when using the dbQueryResults class since it converts dates to strings
        automagically. The format expressions are defined here:

        http://qt-project.org/doc/qt-4.8/qdatetime.html#toString
        '''

        #  use the default format string if none provided
        if formatString:
            self.NLS_DATE_FORMAT = formatString

        if QtFormatString:
            self.qtDateFormatString = QtFormatString

        if self.db.isOpen():
            #  set the date and time formats for our connections
            sql = "alter session set NLS_DATE_FORMAT = '" + self.NLS_DATE_FORMAT + "'"
            query = self.db.exec(sql)
            error = query.lastError().isValid()
            if (error):
                #  there was a problem setting the date format - raise an error message
                err = DBError(self.db)
                self.lastError = err.error
                raise err


    def setOracleTimestampFormat(self, formatString=None):
        '''
        setOracleTimestampFormat sets the Oracle NLS_TIMESTAMP_FORMAT variable for the
        current session. The NLS_TIMESTAMP_FORMAT specifies the format that timestamps
        are returned/inserted from the database if the TO_CHAR() or TO_TIMESTAMP()
        functions are called without a format string. The default format is:

           MM/DD/YYYY HH24:MI:SS.FF3

        Since QtSql drops milliseconds from Timestamp columns, you *must* use the
        TO_CHAR() function to convert timestamps to strings on the database side
        to preserve them. You then must use the TO_TIMESTAMP() function when inserting
        these strings into the database.
        '''

        #  use the default format string if none provided
        if formatString:
            self.NLS_TIMESTAMP_FORMAT = formatString

        if self.db.isOpen():
            sql="alter session set NLS_TIMESTAMP_FORMAT='" + self.NLS_TIMESTAMP_FORMAT + "'"
            query = self.db.exec(sql)
            error = query.lastError().isValid()
            if (error):
                #  there was a problem setting the timestamp format - raise an error message
                err = DBError(self.db)
                self.lastError = err.error
                raise err


    def enableLogging(self, logfile):
        '''
        enableLogging creates a log file and logs SQL INSERT, UPDATE, DELETE
        statements to that log file. This is primarily used to log changes to
        the CLAMS database serving as a 3rd line of defense against data loss.

        logfile is the full path to the file you wish to log to.
        '''
        self.logger = logging.getLogger(self.label)
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler(logfile)
        formatter = logging.Formatter('%(asctime)s ::: %(message)s')
        self.handler.setFormatter(formatter)

        self.logger.addHandler(self.handler)
        self.loggingEnabled = True


    def disableLogging(self):
        '''
        disableLogging stops logging if it has been enabled.
        '''

        if self.logger:
            self.logger.removeHandler(self.handler)
            self.handler.close()

            self.logger = None
            self.handler = None
            self.loggingEnabled = False


    def prepare(self, sql):
        '''
        prepare creates a sql query object and prepares the provided SQL query
        for execution. It will return the prepared query object if successful
        and return None if not.

        Typically this is used with insert/update statements where you provide
        placeholders for binding values and then call dbExecPrepared with the
        data you want to insert/update. This allows for more efficient inserts
        and updates since the SQL is run through the database optimizer only
        once during preparation and this approach should be used when inserting
        or updating lots of data.
        '''

        #  define a query object
        preparedQuery = QtSql.QSqlQuery(self.db)

        #  execute the sql
        ok = preparedQuery.prepare(sql)

        #  check if we had a problem
        if (not ok):
            return None
        else:
            return preparedQuery


    def dbExecPrepared(self, preparedQuery, data):
        '''
        dbExecPrepared executes a previously prepared query using the data provided.

        The data argument must be a dicitonary keyed by the binding values used when
        preparing the query. For example, assuming the following SQL:

        sql = ("INSERT INTO ships (ship, name, description, active) " +
               "VALUES (:ship, :name, :description, :active)"
        db.prepare(sql)

        you would create a dict in this form:

        data = {":ship":[1,2,3],
                ":name":["a","b","c"],
                ":description":["x","y","z"],
                ":active":[0,0,0]}

        where the values are lists containing the data you want to insert for
        that key. The lists must be the same length and the values must be
        ordered appropriately (i.e. values that share an index comprise a
        record)

        In cases where you are obtaining data to insert on a record by record
        basis (i.e. you're querying it out of the database) you can pass a dict
        that contains scalar values (not lists) and call dbExecPrepared
        once for every record you are inserting. This is still more efficient
        than not using bound variables.

        data = {":ship":1,
                ":name":"a",
                ":description":"x",
                ":active":0}

        '''

        #  we can't do anything if there isn't a prepared query
        if (preparedQuery is None):
            return

        #  get the bind value names
        bindNames = list(data.keys())

        #  bind the data
        for name in bindNames:
            preparedQuery.bindValue(name, data[name])

        #  check if we've been a dict of lists - if we have been given lists
        #  we bind the lists and call execBatch
        if (isinstance(data[bindNames[0]], list)):
            #  we've been give lists containing many records
            ok = preparedQuery.execBatch()
        else:
            #  we were only passed one record's worth of data
            ok = preparedQuery.exec()

        #  check if we had a problem
        if (not ok):
            #  ooops, there was a problem - report the error
            raise SQLError(preparedQuery)


    def dbOpen(self):

        #  do nothing if we're already open
        if self.db.isOpen():
            return

        #  open up database connection
        self.db.open()
        if (self.db.isOpenError()) or (not self.db.isValid()):
            err = DBError(self.db)
            self.lastError = err.error
            raise err

        #  set the Date and Timestamp formats if provided
        if (self.NLS_DATE_FORMAT):
            self.setOracleDateFormat()
        if (self.NLS_TIMESTAMP_FORMAT):
            self.setOracleTimestampFormat()

        #  check if the driver supports transactions.
        self.hasTransactions = self.db.driver().hasFeature(QtSql.QSqlDriver.DriverFeature.Transactions)


    def dbClose(self):
        if (self.db.isOpen()):
            self.db.close()
            #QtSql.QSqlDatabase.removeDatabase(self.db.connectionName())
            self.lastError = ''


    def dbQuery(self, sql, asDict=False, **kwargs):
        '''
        dbQuery executes the provided SQL statement and returns either a
        dbQueryResults object that can be used to iterate through the result
        set created by the SQL OR it can return a dictionary that contains
        the full result set. It will raise an error if there is an issue
        executing the SQL.

        Set the forwardOnly keyword to True to improve performance of the
        query, especially for large result sets. This instructs the database
        driver to *not* cache the results. Since dbQueryResults cannot iterate
        backwards, there is *almost* no reason not to. The only reason would be:

            PostgreSQL: While navigating the query results in forward-only mode,
            do not execute any other SQL command on the same database connection.
            This will cause the query results to be lost.

            Calling dbQueryResults.first() multiple times for the same query will
            result in an error when forwardOnly=True. Good coding practices can
            eliminate the need of calling dbQueryResults.first() multiple times so
            this isn't an excuse for setting forwardOnly=False.

        By default, this method returns a dbQueryResults instance which you can
        use to iterate through the results. Set the asDict keyword to True to
        return a dictionary, keyed by query column names that contains the full
        results of the query. This results in the entire query data set being
        read into RAM and may cause issues with very large data sets. Use your
        brain.
        '''

        #  handle the forwardOnly keyword argument. Since, as stated above, Postgres
        #  doesn't allow for nested queries when in ForwardOnly mode, we don't enable
        #  forwardOnly mode by default for Postgres.
        if 'forwardOnly' in kwargs:
            #  forwardOnly was explicitly passed so use that value
            forwardOnly = kwargs['forwardOnly']
        else:
            #  forwardOnly was not passed, set the default based on the driver
            if self.isPostgres:
                forwardOnly = False
            else:
                forwardOnly = True

        #  create the structures required for our dbSelectResults class
        columns = []
        types = []

        #  get a QSqlQuery object
        query = self.dbExec(sql, forwardOnly=forwardOnly)

        #  get a QSqlRecord from the query
        dbRecord = query.record()

        #  if the record is not empty, get the column details
        if (not dbRecord.isEmpty()):
            for i in range(dbRecord.count()):
                columns.append(str(dbRecord.fieldName(i)).lower())
                types.append(dbRecord.field(i).metaType().name())

        if (asDict):

            #  get an instance of dbQueryREsults
            dbq = dbQueryResults(query, columns, types,
                        dateFormatString=self.qtDateFormatString)

            #  create the return dictionary with keys mapped to column names
            result = {k:[] for k in columns}

            #  populate the dict with data returned from the query
            for vals in dbq:
                for i in range(dbq.nColumns):
                    result[columns[i]].append(vals[i])

            #  return the dict
            return result

        else:

            #  return an instance of our dbSelectResults class
            return dbQueryResults(query, columns, types,
                        dateFormatString=self.qtDateFormatString)


    def dbExec(self, sql, **kwargs):
        '''
        dbExec is a simple wrapper function that checks if your sql statement executed
        successfully and raises an error if it didn't.

        This method is intended to be used for queries that do not return results. So
        it is best used for INSERT, UPDATE, DELETE statements as well as calling
        stored procedures or functions.

        it returns the qSqlQuery object used to execute the passed sql.
        '''

        #  handle the forwardOnly keyword argument. Since, as stated above, Postgres
        #  doesn't allow for nested queries when in ForwardOnly mode, we don't enable
        #  forwardOnly mode by default for Postgres.
        if 'forwardOnly' in kwargs:
            #  forwardOnly was explicitly passed so use that value
            forwardOnly = kwargs['forwardOnly']
        else:
            #  forwardOnly was not passed, set the default based on the driver
            if self.isPostgres:
                forwardOnly = False
            else:
                forwardOnly = True

        #  define a query object
        query = QtSql.QSqlQuery(self.db)

        #  set the forwardOnly property if needed
        if (forwardOnly):
            query.setForwardOnly(True)

        #  execute the sql
        ok = query.exec(sql)

        #  check if we had a problem
        if (not ok):
            #  ooops, there was a problem - report the error
            raise SQLError(query)

        #  check if we're logging DML changes to the database and log if so
        if self.loggingEnabled:
            #  changes are defined here as INSERT, UPDATE and DELETE DML statements
            if (sql.split(' ')[0].lower() in ['insert', 'update', 'delete']):
                self.logger.info(sql)

        return query


def get_oracle_home_from_registry():

    import winreg

    # Check both the native registry and the 32-bit redirected registry
    registry_flags = [winreg.KEY_WOW64_64KEY, winreg.KEY_WOW64_32KEY]
    
    for flag in registry_flags:
        try:
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Oracle", 0, winreg.KEY_READ | flag)
            index = 0
            while True:
                try:
                    subkey_name = winreg.EnumKey(hkey, index)
                    subkey = winreg.OpenKey(hkey, subkey_name)
                    try:
                        oracle_home, _ = winreg.QueryValueEx(subkey, "ORACLE_HOME")
                        if oracle_home:
                            return oracle_home
                    except FileNotFoundError:
                        pass
                    index += 1
                except OSError:
                    break # No more subkeys
        except FileNotFoundError:
            continue

    return None


def get_oracle_odbc_driver_name():

    import winreg

    # Check both the native registry and the 32-bit redirected registry
    registry_flags = [winreg.KEY_WOW64_64KEY, winreg.KEY_WOW64_32KEY]
    
    for flag in registry_flags:
        try:
            # Open the official Windows ODBC drivers registry location
            path = r"SOFTWARE\ODBC\ODBCINST.INI\ODBC Drivers"
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path, 0, winreg.KEY_READ | flag)
                                                                                    
            
                                                              
            index = 0
            while True:
                try:
                    # Enumerate through the names of installed drivers
                    driver_name, _, _ = winreg.EnumValue(hkey, index)
                    
                    # Look for strings starting with "Oracle in " o
                    if "oracle in" in driver_name.lower() or driver_name.lower() == "oracle bdb":
                        return driver_name

                    index += 1
                except OSError:
                                                
                    break
        except FileNotFoundError:
            continue
            
    return None
