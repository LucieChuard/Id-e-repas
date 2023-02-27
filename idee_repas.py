import sqlite3
import pymysql
import random



# database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="root", database="recettes")

cursor = connection.cursor()
# some other statements  with the help of cursor

def fct(i,cursor):

    i=i
    while i>1:
        y=random.randint(1,2) 
        
    
        if y==1:
            cursor.execute (f"SELECT plat FROM liste_recettes WHERE type = 'Plat seul'")
            plat=random.choice(cursor.fetchall())
       
            i-=1
            
        
        else :
    
            cursor.execute(f"SELECT plat FROM liste_recettes WHERE type = 'accompagnement'" )
            a=random.choice(cursor.fetchall())
    
            cursor.execute(f"SELECT plat FROM liste_recettes WHERE type = 'viande'" )
            b=random.choice(cursor.fetchall())
            plat=a+b
       
            i-=1
             

        return(plat)


connection.close()