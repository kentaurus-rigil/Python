import sqlite3

conn = sqlite3.connect('assign164.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        col_docx TEXT, \
        col_jpg TEXT, \
        col_mpg TEXT,\
        col_pdf TEXT,\
        col_png TEXT,\
        col_txt TEXT\
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('assign164.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_docx) VALUES (?)", \
                ('information.docx',))
    cur.execute("INSERT INTO tbl_files(col_jpg) VALUES (?)", \
                ('myPhoto.jpg',))
    cur.execute("INSERT INTO tbl_files(col_mpg) VALUES (?)", \
                ('myMovie.mpg',))
    cur.execute("INSERT INTO tbl_files(col_pdf) VALUES (?)", \
                ('data.pdf',))
    cur.execute("INSERT INTO tbl_files(col_png) VALUES (?)", \
                ('myImage.png',))
    cur.execute("INSERT INTO tbl_files(col_txt) VALUES (?)", \
                ('Hello.txt',))
    cur.execute("INSERT INTO tbl_files(col_txt) VALUES (?)", \
                ('World.txt',))
    conn.commit()
conn.close()

conn = sqlite3.connect('assign164.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txt FROM tbl_files WHERE col_txt LIKE '%.txt'")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File Name: {}".format(item[0])
        print(msg)


