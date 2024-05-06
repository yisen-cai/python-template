import sqlite3


# https://docs.python.org/3/library/sqlite3.html
def data_process():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    res = cur.execute("SELECT name FROM sqlite_master")
    if res is not None and len(res.fetchall()) == 0:
        cur.execute("CREATE TABLE movie(title, year, score)")
    cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """)
    con.commit()
    res = cur.execute("select score from movie")
    all_score = res.fetchall()
    print(all_score)

    res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
    print(res.fetchone() is None)

    # execute many lines
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    con.commit()

    for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
        print(row)

    con.close()


if __name__ == '__main__':
    data_process()
