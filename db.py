import sqlite3
from sqlite3 import Error

database = "oceny.db"
sql_create_zmiany_table = """ CREATE TABLE IF NOT EXISTS zmiany (
                                        id text PRIMARY KEY,
                                        opis text,
                                        data text
                                    ); """

sql_create_oceny_table = """ CREATE TABLE IF NOT EXISTS oceny (
                                        id text PRIMARY KEY,
                                        przedmiot text,
                                        wykladowca text,
                                        forma_zaliczenia text,
                                        rodz_zajec text,
                                        ocena1 text,
                                        data1 text,
                                        ocena2 text,
                                        data2 text

                                    ); """

sql_create_oceny_nowe_table = """ CREATE TABLE IF NOT EXISTS oceny_nowe (
                                        id text PRIMARY KEY,
                                        przedmiot text,
                                        wykladowca text,
                                        forma_zaliczenia text,
                                        rodz_zajec text,
                                        ocena1 text,
                                        data1 text,
                                        ocena2 text,
                                        data2 text

                                    ); """
 
 
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print("Błąd przy połączeniu z bazą:")
        print(e)
    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print("Błąd przy tworzeniu tabel:")
        print(e)

#insert or ignore
def insert_oceny(conn, table,row):
    sql = "INSERT OR IGNORE INTO "+table+" VALUES(?,?,?,?,?,?,?,?,?)"
    try:
        cur = conn.cursor()
        cur.execute(sql, row)
        #print("ins= "+str(cur.rowcount))
        #return cur.lastrowid
    except sqlite3.Error as e:
        print("Database error: %s" % e)
    except Exception as e:
        print("Exception in _query: %s" % e)


def query(conn,query):
    cur = conn.cursor()
    cur.execute(query)

def select_oceny(conn,table):
    cur = conn.cursor()#print("TABLE: "+table)
    cur.execute("SELECT * FROM "+table)
 
    rows = cur.fetchall()
    return rows

def select_diff(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM oceny_nowe EXCEPT select * FROM oceny")
 
    rows = cur.fetchall()
    return rows

def oceny_copy(conn):
    cur = conn.cursor()
    query(conn,"DELETE FROM oceny;")
    cur.execute("INSERT INTO oceny SELECT * FROM oceny_nowe WHERE 1")


 
def prepareTablesAndConnection():
    global database
    global sql_create_oceny_table, sql_create_oceny_nowe_table, sql_create_zmiany_table

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        pass
        # create projects table
        create_table(conn, sql_create_oceny_table)
        create_table(conn, sql_create_oceny_nowe_table)
        create_table(conn, sql_create_zmiany_table)
    else:
        print("Error! cannot create the database connection.")

    return conn

if __name__ == '__main__':
    db()



"""
def update_oceny(conn, row):
    r=()
    r = row[1:] + (row[0],)
    print(r)
    sql = ''' UPDATE oceny_nowe
              SET 
                  przedmiot = ? ,
                  wykladowca = ? ,
                  forma_zaliczenia = ? ,
                  rodz_zajec = ? ,
                  ocena1 = ? ,
                  data1 = ? ,
                  ocena2 = ? ,
                  data2 = ? 
              WHERE id = ?'''

    cur = conn.cursor()
    cur.execute(sql, r)
    print("modif= "+str(cur.rowcount))
"""