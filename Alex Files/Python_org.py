import sqlite3,time

while True:
    databaseOne = sqlite3.connect("main")
    cursorOne = databaseOne.cursor()
    cursorOne.execute('''CREATE TABLE IF NOT EXISTS databaseTableTwo(devmac,strongest_signal,type,first_time,last_time)''')#Creating the table in the second database
    cursorOne.execute('DELETE FROM databaseTableTwo')
    cursorOne.execute('''attach 'Kismet-20200226-17-20-47-1.kismet' as other;''')#attach temporally the kismet database
    cursorOne.execute('''INSERT INTO databaseTableTwo SELECT devmac,strongest_signal,type,first_time,last_time FROM other.devices WHERE NOT Type = "Wi-Fi AP" AND Strongest_signal >=-60 ;''')
   #adding the filtered infomation to the main database
   
    x = cursorOne.execute('''SELECT * FROM databaseTableTwo; ''')
    databaseOne.commit()#save the changes, it 
    for y in x:
            if y[1] >= -60:
              print(y);
    print("endprocess","\n")#print just so we can follow what is doing
    
    databaseOne.close()
    time.sleep(60)
