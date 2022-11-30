import search
from yzuCourseBot import CourseBot
import os
import configparser

if __name__ == '__main__':
    configFilename = 'accounts.ini'
    if not os.path.isfile(configFilename):
        with open(configFilename, 'a') as f:
            f.writelines(["[Default]\n", "Account= your account\n", "Password= your password"])
            print('input your username and password in accounts.ini')
            exit()
    # get account info fomr ini config file
    config = configparser.ConfigParser()
    config.read(configFilename)
    Account = config['Default']['Account']
    Password = config['Default']['Password']

    # the courses you want to select, format: '`deptId`,`courseId``classId`'
    coursesList = [
        '311,EEA378B',
        # '304,CS310A',
        # '901,LS239A', 
    ]

    # Time Parameter, sleep n seconds
    delay = 1
    
    depts = set([i.split(',')[0] for i in coursesList])
    
    myBot = CourseBot(Account, Password)
    myBot.login()
    myBot.getCourseDB(depts)
    myBot.selectCourses(coursesList, delay)
