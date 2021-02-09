import sqlite3

def main():
    db = sqlite3.connect("information.db")
    db.row_factory=sqlite3.Row
    db.execute("create table if not exists Admin(Name text, age int)")
    db.execute("insert into Admin(Name,age)values(?,?)", ("Youssef", 23))
    db.execute("insert into Admin(Name,age)values(?,?)", ("Yassir", 4))
    db.execute("insert into Admin(Name,age)values(?,?)", ("moad", 8))
    db.execute("insert into Admin(Name,age)values(?,?)", ("etman", 3))
    db.commit()
    #db.execute("delete from Admin where name='moad'")
    db.execute("UPDATE Admin set age=4 where name='etman'")
    cursor = db.execute("select * from Admin")
    for row in cursor:
        print("Name:{}; Age:{}".format(row["Name"], row["age"]))
if __name__ == "__main__":
    main()
