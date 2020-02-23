import MySQLdb
db=MySQLdb.connect(host="localhost",user="root",passwd="",db="database1")
tagid=obj.readline()
ptr=db.cursor()
i=1
ptr.execute("SELECT TAG_ID FROM toll management")
for tag in ptr.fetchone():
    if(tag==tagid):    
        i=tagid
    else :
        i=0        
    
ptr.execute("UPDATE current_customer SET tag_id =%s"%(i))
}
