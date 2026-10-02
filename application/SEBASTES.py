import os
import subprocess
import datetime

#  define the path to the error logs - MUST USE '\\' as path separator
ERRORLOGPATH = '..\\logs\\'

#  check for the error log directory, create if needed
if not (os.path.exists(ERRORLOGPATH)):
    #  directory doesn't exist - create it
    os.mkdir(ERRORLOGPATH)

#  generate a file name for the log file
logFileName = datetime.datetime.utcnow().strftime('D%m%d%YT%H%M%S')
logFileName = ERRORLOGPATH + 'SEBASTES_Errors-' + logFileName + '.txt'
output_f = open(logFileName, 'w')

#  set the startupinfo struct to hide the console window on Windows
startupinfo = None

#  start SEBASTES and pipe the console output to our errors file
p = subprocess.Popen('pythonw .\\MainWindow.pyw', stdout=output_f, stderr=output_f,
                     startupinfo=startupinfo)


