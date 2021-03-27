import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()
        
    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows
    
    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)", (part, customer, retailer,price))
        self.conn.commit()
        
    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id = ?", (id,))
        elf.conn.commit()
    
    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?, retailer = ?, price = ? WHERE id = ?",(part, customer, retailer, price, id))
        self.cur.commit()
        
    #destructor
    def __del__(self):
        self.conn.close()
        
db = Database('store.db')

#populating the db
#db.insert("4GB DDRA Ram","John Doe", "Microcenter", "160")
#db.insert("Asus Mobo","Mike Henry", "Microcenter", "360")
#db.insert("500w PSU","Harrison Wekesa", "Newegg", "80")
#db.insert("2GB DDR4 Ram","Jimmy Gait", "Newegg", "70")
#db.insert("24 inch Samsung Monitor","Nathan Rutto", "Best buy", "180")
#db.insert("NVIDIA RTX 2080","Ali Kaba", "Newegg", "679")
#db.insert("600w Corsair PSU","Alfred Mutua", "Newegg", "130")