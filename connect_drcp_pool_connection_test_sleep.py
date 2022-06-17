import cx_Oracle
import sys
import time

# This connection test app_user connectivity
# This test uses connection pooling rather than normal dedicated connection
#con = cx_Oracle.connect('vmp_core_stage01_app/D0wnl0adm0v135_FAKE@localhost:11521/orac81r2')

#This connect test system connectivity Rac group81
#con = cx_Oracle.connect('system/C81r4CP4sFAKE@localhost:11521/orac81r2')

#This connection test testdba12 the scan db with pooled connection
#con = cx_Oracle.connect('marlon_test/test123@localhost:1521/xe')

#con = cx_Oracle.connect('marlon_test/test123@localhost:1521/xe',pool=MarloTest)

try:
    pool = cx_Oracle.SessionPool(user='marlon_test',password='test123',dsn='localhost',min=2,max=4,increment=2)
    con1 = pool.acquire()
    print con1.version

except cx_Oracle.DatabaseError, exc:
    error, = exc.args
    print >> sys.stderr, "Oracle-Error-Code:", error.code
    print >> sys.stderr, "Oracle-Error-Message:", error.message

cur = con1.cursor()
#cur.execute('select count(synonym_name) from user_synonyms')
cur.execute('select * from hr_test')
#cur.execute('select host_name from gv$instance where instance_number=userenv(\'instance\')')
for result in cur:
	print result
    
time.sleep(5)


try:
    pool = cx_Oracle.SessionPool(user='marlon_test',password='test123',dsn='localhost',min=2,max=4,increment=2)
    con2 = pool.acquire()
    print con2.version

except cx_Oracle.DatabaseError, exc:
    error, = exc.args
    print >> sys.stderr, "Oracle-Error-Code:", error.code
    print >> sys.stderr, "Oracle-Error-Message:", error.message

    
cur2 = con2.cursor()
#cur.execute('select count(synonym_name) from user_synonyms')
cur2.execute('select * from hr_test')
#cur.execute('select host_name from gv$instance where instance_number=userenv(\'instance\')')
for result in cur2:
	print result
    
time.sleep(5)
    
    
try:
    pool = cx_Oracle.SessionPool(user='marlon_test',password='test123',dsn='localhost',min=2,max=4,increment=2)
    con3 = pool.acquire()
    print con3.version

except cx_Oracle.DatabaseError, exc:
    error, = exc.args
    print >> sys.stderr, "Oracle-Error-Code:", error.code
    print >> sys.stderr, "Oracle-Error-Message:", error.message

    
cur3 = con3.cursor()
#cur.execute('select count(synonym_name) from user_synonyms')
cur3.execute('select * from hr_test')
#cur.execute('select host_name from gv$instance where instance_number=userenv(\'instance\')')
for result in cur3:
	print result
    
time.sleep(5)


try:
    pool = cx_Oracle.SessionPool(user='marlon_test',password='test123',dsn='localhost',min=2,max=4,increment=2)
    con4 = pool.acquire()
    print con4.version

except cx_Oracle.DatabaseError, exc:
    error, = exc.args
    print >> sys.stderr, "Oracle-Error-Code:", error.code
    print >> sys.stderr, "Oracle-Error-Message:", error.message

    
cur4 = con4.cursor()
#cur.execute('select count(synonym_name) from user_synonyms')
cur4.execute('select * from hr_test')
#cur.execute('select host_name from gv$instance where instance_number=userenv(\'instance\')')
for result in cur4:
	print result
    
time.sleep(5)

try:
    pool = cx_Oracle.SessionPool(user='marlon_test',password='test123',dsn='localhost',min=2,max=4,increment=2)
    con5 = pool.acquire()
    print con5.version

except cx_Oracle.DatabaseError, exc:
    error, = exc.args
    print >> sys.stderr, "Oracle-Error-Code:", error.code
    print >> sys.stderr, "Oracle-Error-Message:", error.message

    
cur5 = con5.cursor()
#cur.execute('select count(synonym_name) from user_synonyms')
cur5.execute('select * from hr_test')
#cur.execute('select host_name from gv$instance where instance_number=userenv(\'instance\')')
for result in cur5:
	print result
    
time.sleep(5)

cur.close()
cur2.close()
cur3.close()
cur4.close()
cur5.close()


con1.close()
con2.close()
con3.close()
con4.close()
con5.close()



