import datetime as dt, time

try:
    f = open(r'C:\Code\Payroll-Schedule.csv')

except:
    print 'File cannot be opened...'
    exit()

line = f.readlines()
for lines in line:
    words = lines.split(',')
    todayDate = dt.datetime.now()
    frmtTodayDate = dt.datetime.now().strftime("%d-%b")
    
    frmtCurrentMonth = dt.datetime.now().strftime("%b")
    
    try:
    
        # Create variable for 6 day notice
        sixDay = dt.timedelta(days=6)
        sixDayWarning = todayDate + sixDay
        frmtSixDayWarning = sixDayWarning.strftime("%d-%b") #match formating to file    
        
        

        # Create variable for 3 day notice
        fourDay = dt.timedelta(days=4)
        fourDayWarning = todayDate + fourDay
        frmtFourDayWarning = fourDayWarning.strftime("%d-%b") #match formating to file

        # Create variables for 1 day notice
        zeroDay = dt.timedelta(days=0)
        zeroDayWarning = todayDate + zeroDay
        frmtZeroDayWarning = zeroDayWarning.strftime("%d-%b") #match formating to file
    
    except:
    
        print 'Problem with variable definition section.....'
        exit()
    
    # Only process records in current month
    #if words[1] < frmtTodayDate:
    #    print words[1]
    # dateDueMonth = words[1]
    # dateDueMonth = dateDueMonth[-3:]
    # if dateDueMonth != frmtCurrentMonth:
    #    print words[1]
    #    continue

    
    
    if words[1] == frmtSixDayWarning.lstrip("0"): #formatting adds leading zero
        print "Timesheet due!! For Pay Period =>", words[2]
        print "Today's Date                   =>", frmtTodayDate
        print "TimeSheets Due By              =>", words[1], "Only 6 days remaining!"
        print '\n'
        print "Please Approve Timesheet Today!!!" 
    elif words[1] == frmtFourDayWarning.lstrip("0"): #formatting adds leading zero
        print "Timesheet due!! For Pay Period =>", words[2]
        print "Today's Date                   =>", frmtTodayDate
        print "TimeSheets Due By              =>", words[1], "Only 4 days remaining!"
        print '\n'
        print "Please Approve Timesheet Today!!!"
    elif words[1] == frmtZeroDayWarning.lstrip("0"):
        print "Today's Date      =>", frmtTodayDate
        print "TimeSheets Due By =>", words[1], "No days remaining, Approve Timesheet!"
        print '\n'
        print "Please Approve Timesheet Today!!!"
    else:
        x = None
        continue

#if x == None:
#    print "Today's Date                   =>", frmtTodayDate
#    print "No Timesheet due!! For the current pay period =>"
time.sleep(5)
print "Program Exiting ..."
f.close()

k=input("Please Enter 1 to exit: ")
if k == '1':
	sys.exit()
