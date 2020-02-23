import webbrowser
import serial
import MySQLdb

q=0
w=1
e=2

obj=serial.Serial('COM4',9600)
#obj.open()
if (obj.isOpen()):
##    obj.read()
##    print obj.readline()
    tagid=obj.readline()
    tagid = tagid[:12]
obj.close()


db=MySQLdb.connect("localhost","root","","database1")
ptr=db.cursor()
i=1
ptr.execute("UPDATE current_customer SET tag_id='%s' "%(tagid))
db.commit()

ptr.execute("SELECT TAG_ID FROM toll_management")
dt = ptr.fetchone()
db.commit ()
print dt[0]
if tagid==dt[0]:
    print tagid, dt[0]
    i=0  
print i
if i==0: 
    
    ptr.execute("SELECT WHEELER_TYPE, BALANCE FROM toll_management WHERE TAG_ID='%s'"%(tagid))
    a = ptr.fetchall ()
    db.commit()
    wheeltyp = a[0][0]
    bal = a[0][1]
    if(int (wheeltyp)==2):
        
        if(int (bal)>=15):
            c=int (bal)-15
            ptr.execute("UPDATE toll_management SET BALANCE='%d' WHERE TAG_ID='%s'"%(int(c),tagid))
            db.commit()
            obj.open()
            obj.write('w')
            obj.close()
            ptr.execute("UPDATE current_customer SET bal_status='1' WHERE tag_id='%s'"%(tagid))
            db.commit()
            new="http://localhost/php_pgms/welcome.html"
            webbrowser.open(new)
            
            
            
        else:
            obj.open()
            obj.write('e')
            obj.close()
            ptr.execute("UPDATE current_customer SET bal_status='2' WHERE tag_id='%s'"%(tagid))
            db.commit()
            new="http://localhost/php_pgms/welcome.html"
            webbrowser.open(new)

            
    if(int (wheeltyp)==3):
        
        if(int (bal)>=20):
            c=int (bal)-20
            ptr.execute("UPDATE toll_management SET BALANCE='%d' WHERE TAG_ID='%s'"%(int (c),tagid))
            db.commit()
            obj.open()
            obj.write('w')
            obj.close()
            ptr.execute("UPDATE current_customer SET bal_status='1' WHERE tag_id='%s'"%(tagid))
            db.commit()
            new="http://localhost/php_pgms/welcome.html"
            webbrowser.open(new)

        else:
            obj.open()
            obj.write('e')
            obj.close()
            ptr.execute("UPDATE current_customer SET bal_status='2' WHERE tag_id='%s'"%(tagid))
            db.commit()
            new="http://localhost/php_pgms/welcome.html"
            webbrowser.open(new)

    if(int (wheeltyp)==4):
        
        if(int (bal)>=30):
            c=int (bal)-30
            ptr.execute("UPDATE toll management SET BALANCE='%d' WHERE TAG_ID='%s'"%(int (c),tagid))
            db.commit()
            obj.open()
            obj.write('w')
            obj.close()
            ptr.execute("UPDATE current_customer SET bal_status='1' WHERE tag_id='%s'"%(tagid))
            db.commit()
            new="http://localhost/php_pgms/welcome.html"
            webbrowser.open(new)

        else:
            obj.open()
            obj.write('e')
            obj.close()
            ptr.execute("UPDATE current_customer SET bal_status='2' WHERE tag_id='%s'"%(tagid))
            db.commit()
            new="http://localhost/php_pgms/welcome.html"
            webbrowser.open(new)

            
else:
    
    ptr.execute("UPDATE current_customer SET tag_id='%s' WHERE Slno='1' "%(i))
    db.commit()
    obj.open()
    obj.write("0")
    obj.close()
    ptr.execute("UPDATE current_customer SET bal_status='0'")
    db.commit()
    new="http://localhost/php_pgms/welcome.html"
    webbrowser.open(new)
    
    

