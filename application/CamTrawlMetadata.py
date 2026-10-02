"""
CamTrawlMetadata provides an interface for interacting with the sqlite metadata database
created by the CamTrawlAcquisition application. The idea is that applications that use the
metadata database use this class to extract data from the database instead of querying it
directly.

This class also provides a method to create metadata files to convert pre-metadata database
deployments to ones with a sqlite metadata database.
"""

import os
import datetime
import csv
import base64
from PySide6 import QtCore
from PySide6 import QtSql


class CamTrawlMetadata(QtCore.QObject):

    def __init__(self):
        '''
        Set newFormat to create a sensorData data structure that is ultimately
        '''
        super(CamTrawlMetadata, self).__init__(None)

        self.deploymentPath = ''
        self.dbFilename = ''
        self.imageExtension = ''
        self.clear()
        self.dbConnectionName = None


    def clear(self):

        self.startImage = -1
        self.endImage = 0
        self.cameras = {}
        self.imageData = {}
        self.marks = {}
        self.sensorData = {}
        self.nDroppedImages = 0
        self.droppedData = {}
        self.deploymentData = {}
        self.asyncData = {}
        self.imageNumbers = []


    def open(self, deploymentPath, dbConnectionName='CTMetadata'):
        """
        open opens up the CamTrawlMetadata SQLite database file and updates the
        database so it conforms to the latest format.

        You must provide full path to the deployment.
        """

        self.deploymentPath = str(deploymentPath)
        dbFile = os.path.normpath(self.deploymentPath + os.sep + 'logs' + os.sep + 'CamTrawlMetadata.db3')
        self.dbConnectionName = dbConnectionName

        if (os.path.isfile(dbFile)):
            db = QtSql.QSqlDatabase.addDatabase("QSQLITE", dbConnectionName)
            db.setDatabaseName(dbFile)
            if not db.open():
                raise dbError('Error opening SQLite database file ' + dbFile +'.')

            #  store the database filename
            self.dbFilename = dbFile

            #  Here we update/add in any new metadata elements that might be lacking from files created
            #  using an older format.

            #  if marks table doesn't exist, create it
            if (not 'marks' in db.tables()):
                query = QtSql.QSqlQuery("CREATE TABLE marks (frame_number INTEGER, mark_description TEXT)", db)
                query.exec_()

            #  if deployment_data table doesn't exist, create it
            if (not 'deployment_data' in db.tables()):
                query = QtSql.QSqlQuery("CREATE TABLE deployment_data (deployment_parameter TEXT NOT NULL," +
                        "parameter_value TEXT NOT NULL, PRIMARY KEY(deployment_parameter ))", db)
                query.exec_()
                #  and insert initial default parameters
                query = QtSql.QSqlQuery("INSERT INTO deployment_data (deployment_parameter,parameter_value) " +
                        "VALUES ('hours_offset_to_utc','0')", db)
                query.exec_()

            #  if async_data table doesn't exist, create it
            if (not 'async_data' in db.tables()):
                query = QtSql.QSqlQuery("CREATE TABLE async_data (time TEXT NOT NULL," +
                        "sensor_id TEXT NOT NULL, header TEXT NOT NULL, data TEXT," +
                        "PRIMARY KEY(time,sensor_id,header))", db)
                query.exec_()

            #   if the cameras table doesn't contain the "orientation" column, add it
            hasColumn = False
            query = QtSql.QSqlQuery("PRAGMA table_info(cameras);", db)
            while query.next():
                if (query.value(1).lower() == 'rotation'):
                    hasColumn = True
                    break
            if (not hasColumn):
                #  we don't have it, add the column
                query = QtSql.QSqlQuery("ALTER TABLE cameras ADD COLUMN rotation TEXT DEFAULT 'NONE'", db)
                query.exec_()

            #  if the cameras table doesn't contain the "display_exposure" column, add it
            hasColumn = False
            query = QtSql.QSqlQuery("PRAGMA table_info(cameras);", db)
            while query.next():
                if (query.value(1).lower() == 'display_exposure'):
                    hasColumn = True
                    break
            if (not hasColumn):
                #  we don't have it, add the column
                query = QtSql.QSqlQuery("ALTER TABLE cameras ADD COLUMN display_exposure INTEGER DEFAULT 1", db)
                query.exec_()

            #  if the images table doesn't contain the "exposure_us" column, add it
            hasColumn = False
            query = QtSql.QSqlQuery("PRAGMA table_info(images);", db)
            while query.next():
                if (query.value(1).lower() == 'exposure_us'):
                    hasColumn = True
                    break
            if (not hasColumn):
                #  we don't have it, add the column
                query = QtSql.QSqlQuery("ALTER TABLE images ADD COLUMN exposure_us INTEGER", db)
                query.exec_()

            #  if the images table doesn't contain the "discarded" column, add it
            hasColumn = False
            query = QtSql.QSqlQuery("PRAGMA table_info(images);", db)
            while query.next():
                if (query.value(1).lower() == 'discarded'):
                    hasColumn = True
                    break
            if (not hasColumn):
                #  we don't have it, add the column
                query = QtSql.QSqlQuery("ALTER TABLE images ADD COLUMN discarded INTEGER", db)
                query.exec_()

            #  if the images table doesn't contain the "md5_checksum" column, add it
            hasColumn = False
            query = QtSql.QSqlQuery("PRAGMA table_info(images);", db)
            while query.next():
                if (query.value(1).lower() == 'md5_checksum'):
                    hasColumn = True
                    break
            if (not hasColumn):
                #  we don't have it, add the column
                query = QtSql.QSqlQuery("ALTER TABLE images ADD COLUMN md5_checksum TEXT", db)
                query.exec_()

            #  if the images table doesn't contain the "gain" column, add it
            hasColumn = False
            query = QtSql.QSqlQuery("PRAGMA table_info(images);", db)
            while query.next():
                if (query.value(1).lower() == 'gain'):
                    hasColumn = True
                    break
            if (not hasColumn):
                #  we don't have it, add the column
                query = QtSql.QSqlQuery("ALTER TABLE images ADD COLUMN gain FLOAT", db)
                query.exec_()

            #  if the images table doesn't contain the "still_image" column, add it
            hasColumn = False
            query = QtSql.QSqlQuery("PRAGMA table_info(images);", db)
            while query.next():
                if (query.value(1).lower() == 'still_image'):
                    hasColumn = True
                    break
            if (not hasColumn):
                #  we don't have it, add the column
                query = QtSql.QSqlQuery("ALTER TABLE images ADD COLUMN still_image INTEGER DEFAULT 1", db)
                query.exec_()

            #  if the images table doesn't contain the "video_frame" column, add it
            hasColumn = False
            query = QtSql.QSqlQuery("PRAGMA table_info(images);", db)
            while query.next():
                if (query.value(1).lower() == 'video_frame'):
                    hasColumn = True
                    break
            if (not hasColumn):
                #  we don't have it, add the column
                query = QtSql.QSqlQuery("ALTER TABLE images ADD COLUMN video_frame INTEGER DEFAULT 0", db)
                query.exec_()

            #  lastly, we determine the image file type
            query = QtSql.QSqlQuery("SELECT parameter_value FROM deployment_data WHERE deployment_parameter=" +
                    "'image_file_type'", db)
            query.exec_()
            if query.first():
                #  image type in metadata - use it
                if query.value(0).lower()[0] != '.':
                    self.imageExtension = "." + query.value(0).lower()
                else:
                    self.imageExtension = query.value(0).lower()
            else:
                #  image type not in deployment_data table, determine type and update that in the deployment_data table
                imageTypes = ['.jpg', '.jpeg', '.tif', '.tiff', '.avi']
                queryStr = "SELECT camera, name FROM images WHERE (discarded IS NULL or discarded=0) and still_image=1;"
                query = QtSql.QSqlQuery(queryStr, db)
                if query.first():
                    camera = query.value(0)
                    filename = query.value(1)
                    imagePath = os.path.normpath(self.deploymentPath + os.sep + 'images' + os.sep + camera +
                            os.sep + filename)
                    for type in imageTypes:
                        if (os.path.isfile(imagePath + type)):
                            self.imageExtension = type
                            break
                    #  insert the image type into the deployment_data table
                    query = QtSql.QSqlQuery("INSERT INTO deployment_data (deployment_parameter,parameter_value) " +
                        "VALUES ('image_file_type','" + self.imageExtension[1:] + "')", db)
                    query.exec_()

                else:
                    #  no images in images table
                    self.imageExtension = ''

        else:
            #  couldn't open the metadata database file
            raise dbError('SQLite file ' + dbFile +' does not exist.')


    def close(self):

        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        #  close the database
        if (db) and (db.isOpen()):
            db.close()
        del db

        if (self.dbConnectionName):
            QtSql.QSqlDatabase.removeDatabase(self.dbConnectionName)
            self.dbConnectionName = None

        #  and clear out
        self.clear()

        self.deploymentPath = ''
        self.dbFilename = ''
        self.imageExtension = ''


    def convertToDatabase(self, deploymentPath, cameras, labels):
        """
        convertToDatabase creates the CamTrawl metadata database for older deployments that
        stored this data in flat files. It also has limited ability to create a database
        simply from image files as long as those files are arranged and named properly.
        """

        self.close()

        self.deploymentPath = str(deploymentPath)
        dbDir = os.path.normpath(self.deploymentPath + os.sep + 'logs')
        dbFile = os.path.normpath(dbDir + os.sep + 'CamTrawlMetadata.db3')

        nCameras = len(cameras)
        images = [[]] * nCameras
        maxImages = [0] * nCameras

        #  check if the logs directory exists and create if not - this is for non-CamTrawl datasets
        if (not os.path.isdir(dbDir)):
            os.makedirs(dbDir)

        #  create the database file
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE", "metadb");
        db.setDatabaseName(dbFile);
        if (db.open()):
            dbQuery = QtSql.QSqlQuery(db)
            dbQuery.exec_("CREATE TABLE cameras (camera TEXT NOT NULL, mac_address TEXT, model TEXT, label TEXT, " +
                    "orientation INTEGER DEFAULT 0, PRIMARY KEY(camera))")
            dbQuery.exec_("CREATE TABLE images (number INTEGER NOT NULL, camera TEXT NOT NULL, time TEXT, name TEXT, " +
                    "exposure_us INTEGER, discarded INTEGER, PRIMARY KEY(number,camera))")
            dbQuery.exec_("CREATE TABLE dropped (number INTEGER NOT NULL, camera TEXT NOT_NULL, time TEXT, " +
                    "PRIMARY KEY(number,camera))")
            dbQuery.exec_("CREATE TABLE sensor_data (number INTEGER, sensor_id TEXT, header TEXT, data TEXT)")
            dbQuery.exec_("CREATE TABLE deployment_data (deployment_parameter TEXT NOT NULL," +
                    "parameter_value TEXT NOT NULL, PRIMARY KEY(deployment_parameter ))")
        else:
            errText = str(dbQuery.lastError().text())
            error = dbError('Unable to create new metadata database ' + dbFile + ':::' + errText)
            raise error

        #  and insert initial default parameters into deployment_data
        dbQuery.exec_("INSERT INTO deployment_data (deployment_parameter,parameter_value) " +
                "VALUES ('hours_offset_to_utc','0'")

        #  start a transaction - this improves performance of bulk inserts significantly since SQLite
        #  doesn't wrap *every* insert in a transaction (which is the default if no transaction has
        #  been initiated explicitly.) THIS IS HUGE - like 300x faster!
        ok = dbQuery.exec_("BEGIN TRANSACTION")
        if (not ok):
            errText = str(dbQuery.lastError().text())
            error = dbError('Unable to start transaction:::' + errText)
            raise error

        for i in range(nCameras):
            #  create an entry for this camera in the cameras table
            camParts = cameras[i].split('_')
            model = camParts[0]
            if (len(camParts) > 1):
                serial = camParts[1]
            else:
                serial = '00-00-00-00-00-00'
            ok = dbQuery.exec_("INSERT INTO cameras VALUES ('" + cameras[i] + "','" + serial + "','" + model +
                    "','" + labels[i] + "',0)")
            if (not ok):
                errText = str(dbQuery.lastError().text())
                error = dbError('Unable to insert data into metadata database:::' + errText)
                raise error

            #  get the image list for this camera
            imagePath = os.path.normpath(self.deploymentPath + os.sep + 'images' + os.sep + cameras[i])
            images[i] = self.getImageList(imagePath)
            maxImages[i] = max(images[i].keys())

        #  figure out max number of images for all cameras
        maxImages = max(maxImages)

        #  work through the images, inserting them into the images table
        for j in range(1, maxImages+1):
            for i in range(nCameras):
                try:
                    #  try to extract this image number from this camera
                    #  If a camera was using a trigger divider it may not always have an image.
                    thisImage = images[i][j]

                    #  remove the extension - bone headed and needs to be fixed but I never included
                    #  the extension in the new metadata database
                    thisImage = thisImage[0:-4]

                    #  create the time string
                    parts = thisImage.split('_')
                    dateTime = parts[1].split('-')
                    ymd = dateTime[0][1:]
                    ymd = ymd[0:4] + '-' + ymd[4:6] + '-' + ymd[6:8]
                    hms = dateTime[1][1:]
                    hms = hms[0:2] + ':' + hms[2:4] + ':' + hms[4:]
                    dateTime = ymd + " " + hms

                    #  insert this image into the images table
                    ok = dbQuery.exec_("INSERT INTO images VALUES (" + str(j) + ",'" + cameras[i] + "','" + dateTime +
                            "','" + thisImage + "',-1,NULL)")
                    if (not ok):
                        errText = str(dbQuery.lastError().text())
                        error = dbError('Unable to insert data into metadata database:::' + errText)
                        raise error

                except:
                    #  this camera didn't have this image number - just move along
                    pass

        #  insert the sensor data
        attitudeFile = os.path.normpath(self.deploymentPath + os.sep + 'logs' + os.sep + 'attitude.log')
        if (os.path.isfile(attitudeFile)):
            f = open(attitudeFile, 'rt')
            try:
                #  create a CSV reader
                reader = csv.reader(f)
                #  skip the header
                reader.next()

                #  insert this row into the sensor_data table
                for row in reader:
                    sentence = '$OHPR,' + row[2] + ',' + row[3] + ',' + row[4] + ',' + '-999.0,' + row[5] + ',0,0,0*00'
                    ok = dbQuery.exec_("INSERT INTO sensor_data VALUES (" + row[1] + ",'CTControl','$OHPR','" + sentence + "')")
            finally:
                f.close()

        #  end the transaction
        ok = dbQuery.exec_("END TRANSACTION")
        if (not ok):
            errText = str(dbQuery.lastError().text())
            error = dbError('Unable to end transaction:::' + errText)
            raise error

        #  close the database
        db.close()

        #  now open up our new database
        self.open(self.deploymentPath)

        #  and query it
        self.query()


    def query(self, startTime=None, endTime=None, returnDiscards=False):
        """
        query is the main method for extracting data from the metadata database. Calling
        this method populates the following properties based on the provided start and end
        times. If no start or end times are provided the entire database is read.

        These properties are updated when query is executed:
            startImage = contains the starting image number based on the provided start time

            endImage  = contains the ending image number based on the provided end time

            cameras = a dict keyed by camera name containing the cameras table data

            imageData = a dict keyed by camera name and image number containing the image table data

            marks = a dict keyed by frame number containing mark descriptions

            sensorData = a dict keyed by sensor id, sensor header, and image number containing
                         the sensor data string for that senor/header/image. It also has keys
                         for 'time' and 'utc_time' keyed by image number that contain the system
                         time the image and sensor data were recorded as well as the "UTC"
                         time which is the acquired time offset by the value of the
                         "hours_offset_to_utc" parameter from the deployment_data table. The
                         times are datetime objects. The hours_offset_to_utc parameter is
                         0 by default and not set by the CamTrawl acquisition software. If you
                         want to use it, you must set it manually.

            asyncData = a dict keyed by sensor id and sensor header containing asyncronous sensor
                        data. Async sensor data is primarily comprised of operational parameters
                        such as camera and system temperatures, system voltage, sensor status, etc.
            nDroppedImages = contains the number of dropped images
            droppedData = a dict keyed by camera name and image number which contains the trigger
                        time of the image that was dropped
            deploymentData = a dict keyed by deployment_parameter which contains the parameter's
                        data value.

        """

        #  get a reference to our database connection - this is the correct way to
        #  use QSqlDatabase. One should not store this reference as a class property
        #  since it prevents QSqlDatabase from being correctly cleaned up when the
        #  application quits. Instead, use the "database" method to get a local
        #  reference that will be destroyed when the method goes out of scope.
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        #  clear out existing data
        self.clear()

        #  determine the start and end times
        if startTime:
            startTimeStr = startTime.strftime("%Y-%m-%d %H:%M:%S")
        else:
            startTimeStr = "1900-01-01 01:00:00"
        if endTime:
            endTimeStr = endTime.strftime("%Y-%m-%d %H:%M:%S")
        else:
            endTimeStr = "2999-01-01 01:00:00"

        #  define the date range constraint clause
        timeClause = "time between datetime('" + startTimeStr + "') and datetime('" + endTimeStr + "')"

        #  define the discard clause - used to exclude discarded images metadata
        discardClause = "(discarded IS NULL or discarded=0) AND "

        #try:

        #  determine the number of dropped images
        query = QtSql.QSqlQuery("SELECT DISTINCT number FROM dropped;", db)
        self.nDroppedImages = 0
        if query.first():
            self.nDroppedImages = query.value(0)

        #  get the camera information
        query = QtSql.QSqlQuery("SELECT * from cameras;", db)
        self.nCameras = 0
        while query.next():
            #  convert orientation to integer

            #none, cw90, cw180, cw270, fliplr, flipud
            rot = str(query.value(4)).lower()
            if rot == 'none':
                orientation = 0
            elif rot == 'cw90':
                orientation = 90
            elif rot == 'cw180':
                orientation = 180
            elif rot == 'cw270':
                orientation = 270
            elif rot == 'fliplr':
                orientation = -1
            elif rot == 'flipud':
                orientation = -2
            else:
                orientation = 0
            self.cameras[query.value(0)] = {"mac_address":query.value(1),
                                            "model":str(query.value(2)),
                                            "label":str(query.value(3)),
                                            "orientation":orientation}
            self.nCameras = self.nCameras + 1
        if (self.nCameras == 0):
            #  must be an older database format - try a different way...
            query = QtSql.QSqlQuery("SELECT DISTINCT camera FROM images;", db)
            self.nCameras = 0
            while query.next():
                self.cameras[query.value(0)] = {"mac_address":'', "model":'', "label":'', "orientation":0}
            self.nCameras = self.nCameras + 1

        #  read in deployment data - deployment data is a catch all for various parameters
        query = QtSql.QSqlQuery("SELECT deployment_parameter, parameter_value from deployment_data;", db)
        self.deploymentData = {}
        while query.next():
            self.deploymentData[query.value(0)] = query.value(1)

        #  try to convert the utc offset to a float
        try:
            timeOffset = float(self.deploymentData['hours_offset_to_utc'])
        except:
            timeOffset = 0

        #  get the dropped image data
        self.droppedData = {}
        query = QtSql.QSqlQuery("SELECT DISTINCT camera FROM dropped;", db)
        while query.next():
            self.droppedData[query.value(0)] = {}
        query = QtSql.QSqlQuery("SELECT number, camera, time from dropped;", db)

        #  and store the dropped data
        while query.next():
            #  create datetime objects to represent times and adjust for time offset
            recordedTime = datetime.datetime.strptime(query.value(2),
                    "%Y-%m-%d %H:%M:%S.%f")
            utcTime = recordedTime + datetime.timedelta(hours=timeOffset)
            self.droppedData[query.value(1)][query.value(0)] = utcTime

        #  load the image data
        for camera in self.cameras:
            self.imageData[camera] = {}

            if (returnDiscards):
                queryStr = ("SELECT number, time, name FROM images WHERE camera='" +
                                    camera + "' AND still_image=1 AND " + timeClause +
                                    ' ORDER BY number ASC;')
            else:
                queryStr = ("SELECT number, time, name FROM images WHERE camera='" +
                                    camera + "' AND still_image=1 AND " + discardClause +
                                    timeClause + ' ORDER BY number ASC;')
            query = QtSql.QSqlQuery(queryStr, db)

            while query.next():
                #  set the start image number
                if (self.startImage == -1):
                    self.startImage = query.value(0)

                #  create datetime objects to represent times and adjust for time offset
                recordedTime = datetime.datetime.strptime(query.value(1),"%Y-%m-%d %H:%M:%S.%f")
                utcTime = recordedTime + datetime.timedelta(hours=timeOffset)

                #  populate the imageData dict
                self.imageData[camera][query.value(0)] = [recordedTime, utcTime, query.value(2)]
                #  keep assigning endImage - it will ultimately contain the end image number
                self.endImage = query.value(0)

        #  now build an index of image numbers
        start_set = set(self.imageData[camera].keys())
        for otherCam in self.cameras:
            if otherCam == camera:
                continue
            start_set.intersection(self.imageData[otherCam].keys())
        self.imageNumbers = sorted(start_set)


        #  load the sensor data

        #  build a dictionary using sensor IDs and headers as keys
        self.sensorData = {}
        self.sensorData['time'] = {}
        self.sensorData['utc_time'] = {}
        query = QtSql.QSqlQuery("SELECT DISTINCT sensor_id FROM sensor_data", db)
        while query.next():
            sensorId = query.value(0)
            self.sensorData[sensorId] = {}
            queryStr = ("SELECT DISTINCT header FROM sensor_data WHERE sensor_id = '" + sensorId + "'")
            query2 = QtSql.QSqlQuery(queryStr, db)
            while query2.next():
                sensorHeader = query2.value(0)
                self.sensorData[sensorId][sensorHeader] = {}

        #  then fill it...
        queryStr = ("SELECT DISTINCT im.number, im.time, sd.sensor_id, sd.header, sd.data " +
                "FROM images im, sensor_data sd WHERE im.number = sd.number AND im.number >= " +
                str(self.startImage) + " AND im.number <= " + str(self.endImage))
        query = QtSql.QSqlQuery(queryStr, db)
        while query.next():
            sensorId = query.value(2)
            sensorHeader = query.value(3)

            #  create datetime objects to represent times and adjust for time offset
            recordedTime = datetime.datetime.strptime(query.value(1),"%Y-%m-%d %H:%M:%S.%f")
            utcTime = recordedTime + datetime.timedelta(hours=timeOffset)

            try:
                #  assign the data value to the sensorData dictionary
                self.sensorData[sensorId][sensorHeader][query.value(0)] = query.value(4)
                self.sensorData['time'][query.value(0)] = recordedTime
                self.sensorData['utc_time'][query.value(0)] = utcTime
            except KeyError:
                #  there is an issue with parsing the keys (bad key) so we have to skip this data value
                pass
            except:
                self.sensorData[sensorId][sensorHeader][query.value(0)] = ''
                self.sensorData['time'][query.value(0)] = recordedTime
                self.sensorData['utc_time'][query.value(0)] = utcTime

        #  load the async data

        #  build a dictionary using sensor IDs as keys
        query = QtSql.QSqlQuery("SELECT DISTINCT sensor_id FROM async_data", db)
        while query.next():
            sensorID = query.value(0)
            self.asyncData[sensorID] = {}
            queryStr = ("SELECT DISTINCT header FROM async_data WHERE sensor_id = '" + sensorID + "'")
            query2 = QtSql.QSqlQuery(queryStr, db)
            while query2.next():
                sensorHeader = query2.value(0)
                self.asyncData[sensorID][sensorHeader] = {'time':[], 'utc_time':[], 'data':[]}

        #  then fill it...
        queryStr = ("SELECT time, sensor_id, header, data FROM async_data WHERE " +
                   timeClause + " ORDER BY time")
        query = QtSql.QSqlQuery(queryStr, db)
        while query.next():
            sensorID = query.value(1)
            sensorHeader = query.value(2)

            #  create datetime objects to represent times and adjust for time offset
            recordedTime = datetime.datetime.strptime(query.value(0),"%Y-%m-%d %H:%M:%S.%f")
            utcTime = recordedTime + datetime.timedelta(hours=timeOffset)

            try:
                #  assign the data values to the asyncData dictionary
                self.asyncData[sensorID][sensorHeader]['time'].append(recordedTime)
                self.asyncData[sensorID][sensorHeader]['utc_time'].append(utcTime)
                self.asyncData[sensorID][sensorHeader]['data'].append(query.value(3))
            except KeyError:
                #  there is an issue with parsing the keys (bad key) so we have to skip this data value
                pass
            except:
                #  There was an issue converting the data value to string - insert an empty string
                self.asyncData[sensorID][sensorHeader]['time'].append(recordedTime)
                self.asyncData[sensorID][sensorHeader]['utc_time'].append(utcTime)
                self.asyncData[sensorID][sensorHeader]['data'].append('')

        # load mark data
        queryStr = ("SELECT frame_number, mark_description FROM marks WHERE frame_number >= " +
                str(self.startImage) + " AND frame_number <= " + str(self.endImage))
        query = QtSql.QSqlQuery(queryStr, db)
        while query.next():
            self.marks.update({query.value(0):query.value(1)})

        #except:
        #    raise dbError('Error querying SQLite database')


    def setDiscarded(self, startFrame, endFrame, unset=False):
        """
        setDiscarded sets (or optionally unsets) a range of images as "discarded" given the start
        and end frame of the range. The bounds are inclusive. This method only changes the
        value of the "discarded" field of the affected frames in the images table. It does not
        actually delete the data files.

        This is the first step in trimming a deployment. The next step would be calling
        deleteDiscardedImages to actually delete the image files that have been marked as
        discarded.
        """
        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        if (unset):
            QtSql.QSqlQuery("UPDATE images SET discarded=NULL WHERE number>=" + str(startFrame) +
                    " AND number<=" + str(endFrame) + ";",  db)
        else:
            QtSql.QSqlQuery("UPDATE images SET discarded=1 WHERE number>=" + str(startFrame) +
                    " AND number<=" + str(endFrame) + ";",  db)


    def deleteDiscardedImages(self):

        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        # query all of the images marked as discarded
        queryStr = "SELECT camera, name FROM images WHERE discarded=1 ORDER BY camera"
        query = QtSql.QSqlQuery(queryStr, db)
        while query.next():
            #  attempt to delete these images
            camera = query.value(0)
            filename = query.value(1) + self.imageExtension
            fullPath = os.path.normpath(self.deploymentPath + os.sep + 'images' +
                    os.sep + camera + os.sep + filename)
            os.remove(fullPath)


    def createMark(self, frame, description):
        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        # clear out any current mark for this frame
        self.removeMark(frame)
        # insert mark
        QtSql.QSqlQuery("insert into marks (frame_number, mark_description) VALUES(" + str(frame) +
                ",'" + description+"')",  db)
        self.marks.update({frame:description})


    def removeMark(self, frame):
        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        # clear out any current mark for this frame
        if frame in self.marks:
            QtSql.QSqlQuery("delete from marks where frame_number=" + str(frame), db)
            del(self.marks[frame])


    def getAllMarks(self):
        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        # return a dict containing all marks in the deployment.
        marks = {}
        query = QtSql.QSqlQuery("select frame_number, mark_description from marks ORDER BY frame_number ASC", db)
        while query.next():
            marks[query.value(0)] = query.value(1)

        return marks


    def findNextMark(self, frame):
        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        # find the next mark
        query = QtSql.QSqlQuery("select frame_number,  mark_description from marks where frame_number>" +
                str(frame) + " ORDER BY frame_number ASC", db)
        if query.first():
            return query.value(0),query.value(1)
        else:
            return None, None


    def findPreviousMark(self, frame):
        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        # find the previous mark
        query = QtSql.QSqlQuery("select frame_number, mark_description from marks where frame_number<" +
                str(frame) + " ORDER BY frame_number DESC", db)
        if query.first():
            return query.value(0),query.value(1)
        else:
            return None, None


    def setImageAdjustments(self, camera, adjustments):
        """
        setImageAdjustments inserts/updates the image adjustment properties for
        the specified camera in the deployment_data table.

        camera is the camera name these adjustments are associated with and
        adjustments is a string containing the binary pickled adjustments data
        structure.

        Since we need a unique way to identify settings for individual cameras we
        are using the MAC address (which is the serial number for USB3 cameras) to
        link the adjustments to a camera. This of course breaks down when no MAC
        address is available. Since modern CamTrawl systems always have this property
        I am not providing a workaround.
        """
        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        #  construct the deployment_parameter string
        parameter = self.cameras[camera]["mac_address"] + '_adjustments'

        #  encode the data so it can be stored as a string
        adjustments = base64.b64encode(adjustments).decode("utf-8")

        #  check if it exists
        query = QtSql.QSqlQuery("SELECT parameter_value FROM deployment_data WHERE deployment_parameter='" +
                parameter + "'", db)
        query.exec_()
        if query.first():
            #  parameter exists, update it
            query = QtSql.QSqlQuery("UPDATE deployment_data SET parameter_value='" + adjustments +
                    "' WHERE deployment_parameter='" + parameter + "'", db)
            query.exec_()
        else:
            #  parameter doesn't exist, insert it
            query = QtSql.QSqlQuery("INSERT INTO deployment_data (deployment_parameter,parameter_value) " +
                    "VALUES ('" + parameter + "','" + adjustments + "')", db)
            query.exec_()


    def getImageAdjustments(self, camera):
        """
        getImageAdjustments retrieves the image adjustment properties for
        the specified camera in the deployment_data table.
        """
        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        #  construct the deployment_parameter string
        parameter = self.cameras[camera]["mac_address"] + '_adjustments'

        #  check if it exists
        query = QtSql.QSqlQuery("SELECT parameter_value FROM deployment_data WHERE deployment_parameter='" +
                parameter + "'", db)
        query.exec_()
        if query.first():
            #  parameter exists - extract and decode
            adjustments = query.value(0)
            adjustments = base64.b64decode(adjustments)
        else:
            #  parameter doesn't exist
            adjustments = None

        return adjustments


    def exportMetadataToCSV(self, outputNameBase):
        """
        exportMetadataToCSV exports select metadata tables to csv files. Currently it exports
        the cameras and images tables and the $OHPR (attitude) data from the sensors table.
        outputNameBase must be the full path to the output directory file including the file
        name header. For example "c:\output\my_deployment-" which will result in files named
        c:\output\my_deployment-cameras.csv, c:\output\my_deployment-images.csv, etc.

        Moving forward, we should store the sensor .csv headers in the deployment_data folder
        so we can export all sensor data with a header that describes the columns of data.
        """

        #  get a reference to our database connection
        if (not self.dbConnectionName):
            return
        db = QtSql.QSqlDatabase.database(self.dbConnectionName)

        #  export the camera table
        outputFile = outputNameBase + 'cameras.csv'
        exportFile = QtCore.QFile(outputFile)
        ok = exportFile.open(QtCore.QIODevice.ReadWrite)
        if (not ok):
            raise IOError("Unable to open export file " + outputFile)
        stream = QtCore.QTextStream(exportFile)
        header = ['camera', 'serial number', 'model', 'label', 'orientation']
        for i in range(len(header) - 1):
            stream  << header[i] << ","
        stream << header[i+1] << "\r\n"

        query = QtSql.QSqlQuery("SELECT camera, mac_address, model, label, orientation FROM cameras", db)
        while query.next():
            stream  << query.value(0) << "," << query.value(1) << "," \
                    << query.value(2) << "," << query.value(3) << "," \
                    << query.value(4) <<"\r\n"
        exportFile.close()

        #  export the images table
        outputFile = outputNameBase + 'images.csv'
        exportFile = QtCore.QFile(outputFile)
        ok = exportFile.open(QtCore.QIODevice.ReadWrite)
        if (not ok):
            raise IOError("Unable to open export file " + outputFile)
        stream = QtCore.QTextStream(exportFile)
        header = ['frame number', 'camera', 'time-recorded', 'time-utc', 'image name', 'exposure (us)', 'discarded']
        for i in range(len(header) - 1):
            stream  << header[i] << ","
        stream << header[i+1] << "\r\n"

        #  try to convert the utc offset to a float
        try:
            timeOffset = float(self.deploymentData['hours_offset_to_utc'])
        except:
            timeOffset = 0

        query = QtSql.QSqlQuery("SELECT number, camera, time, name, exposure_us, discarded FROM images", db)
        while query.next():
            #  convert the recorded time to a datetime and compute the UTC time
            recordedTime = datetime.datetime.strptime(query.value(2),"%Y-%m-%d %H:%M:%S.%f")
            utcTime = recordedTime + datetime.timedelta(hours=timeOffset)
            stream  << query.value(0) << "," << query.value(1) << "," \
                    << recordedTime.strftime("%Y-%m-%d %H:%M:%S.%f") << "," \
                    << utcTime.strftime("%Y-%m-%d %H:%M:%S.%f") << "," \
                    << query.value(3) << "," << query.value(4) << "," \
                    << query.value(5) <<"\r\n"
        exportFile.close()

        #  export the sensor data - for now we are only exporting the OHPR (attitude) data.
        outputFile = outputNameBase + 'OHPR.csv'
        exportFile = QtCore.QFile(outputFile)
        ok = exportFile.open(QtCore.QIODevice.ReadWrite)
        if (not ok):
            raise IOError("Unable to open export file " + outputFile)
        stream = QtCore.QTextStream(exportFile)

        header = ['frame', 'time-recorded', 'time-utc', 'heading (deg)', 'pitch (deg)', 'roll (deg)',
                'internal temperature (c)', 'depth (m)', 'Xi', 'Yi', 'Zi']
        for i in range(len(header) - 1):
            stream  << header[i] << ","
        stream << header[i+1] << "\r\n"

        query = QtSql.QSqlQuery("SELECT number, data FROM sensor_data WHERE header='$OHPR'", db)
        while query.next():
            #  need to get the time from the images table
            timeQuery = QtSql.QSqlQuery("SELECT time FROM images WHERE number=" +
                    str(query.value(0)), db)
            if timeQuery.first():
                #  convert the recorded time to a datetime and compute the UTC time
                recordedTime = datetime.datetime.strptime(timeQuery.value(0),"%Y-%m-%d %H:%M:%S.%f")
                utcTime = recordedTime + datetime.timedelta(hours=timeOffset)

                stream << query.value(0) << "," << recordedTime.strftime("%Y-%m-%d %H:%M:%S.%f") << "," \
                       << utcTime.strftime("%Y-%m-%d %H:%M:%S.%f") << "," \
                       << query.value(1)[6:] << "\r\n"
        exportFile.close()
        
#        #  export the asynch sensor data
#        outputFile = outputNameBase + 'asynch.csv'
#        exportFile = QtCore.QFile(outputFile)
#        ok = exportFile.open(QtCore.QIODevice.ReadWrite)
#        if (not ok):
#            raise IOError("Unable to open export file " + outputFile)
#        stream = QtCore.QTextStream(exportFile)
#
#        header = ['time-recorded', 'time-utc', 'sensor_id','header','data']
#        for i in range(len(header) - 1):
#            stream  << header[i] << ","
#        stream << header[i+1] << "\r\n"
#
#        query = QtSql.QSqlQuery("SELECT time,sensor_id,header,data FROM async_data", db)
#        while query.next():
#
#            #  convert the recorded time to a datetime and compute the UTC time
#            recordedTime = datetime.datetime.strptime(query.value(0),"%Y-%m-%d %H:%M:%S.%f")
#            utcTime = recordedTime + datetime.timedelta(hours=timeOffset)
#
#            stream << recordedTime.strftime("%Y-%m-%d %H:%M:%S.%f") << "," \
#                   << utcTime.strftime("%Y-%m-%d %H:%M:%S.%f") << "," \
#                   << query.value(1) << "," \
#                   << query.value(2) << "," \
#                   << query.value(3) << "\r\n"
#        exportFile.close()


    def getImageList(self, path, renameImages=True):
        '''
        getImageList is used by convertToDatabase to generate a dictionary of
        image file names. It will by default attempt to fix simple numbering
        issues seen on early CamTrawl deployments including renaming the files.
        '''

        imageTypes = ['jpg', 'tif', 'tiff', 'jpeg']
        imageDict = {}

        #  get a sorted list of the files in the image directory
        images = os.listdir(path)
        images.sort()
        nImages = len(images)

        #  loop through the images, checking if the numbering is consistent
        for i in range(nImages-1):

            #  parse the extension and see what we have
            if ((images[i][-3:].lower() not in imageTypes) or
                (images[i+1][-3:].lower() not in imageTypes)):
                    #  this isn't a file we care about
                    continue
            try:
                #  try to extract the image number from this and the next file
                thisNumber = int(images[i].split('_')[0])
                nextNumber = int(images[i+1].split('_')[0])
                imageDict[thisNumber] = images[i]
            except:
                #  this image name must be mangled or it is not a camtrawl image
                continue

            #  check if we're in simple order
            if (thisNumber == nextNumber - 1):
                #  image is in order - nothing to do
                rename = -1
            elif (thisNumber == nextNumber):
                #  image number is repeated
                rename = thisNumber + 1
            else:
                #  some other issue
                rename = -1
                print('ACK!---------------Unknown image numbering issue:')
                print('     ' + images[i])
                print('bad->' + images[i+1])
                if (i < nImages-2):
                    print('     ' + images[i+2])

            if (rename > -1):
                #  we're renaming this file
                oldName = images[i+1]
                nameParts = images[i+1].split('_')
                nameParts[0] = '%05i' % rename
                newName = '_'.join(nameParts)
                images[i+1] = newName
                if (renameImages):
                    os.rename(path + os.sep + oldName, path + os.sep + newName)

        return imageDict


class dbError(Exception):
    def __init__(self, msg, parent=None):
        self.errText = msg
        self.parent = parent

    def __str__(self):
        return repr(self.errText)
