import sqlite3
conn=sqlite3.connect('test.db')
conn.execute('''CREATE TABLE users(
	username       TEXT    PRIMARY KEY NOT NULL,
	password       TEXT    NOT NULL,
	access        TEXT    NOT NULL);''')
conn.execute("INSERT INTO users (username,password,access) VALUES ('cust1','Lazada_567','/api/shop');")
conn.execute("INSERT INTO users (username,password,access) VALUES ('cust2','RestlessSou7','/api/shop/stats')")
conn.execute("INSERT INTO users (username,password,access) VALUES ('cust3','Plinking@13','/api/merchant')")
conn.execute("INSERT INTO users (username,password,access) VALUES ('cust4','Hebrew_357','/api/merchant/products')")
conn.execute("INSERT INTO users (username,password,access) VALUES ('cust5','JackJack!!2','/api')")
conn.execute("INSERT INTO users (username,password,access) VALUES ('cust6','BingoWinner*123','/api/product')")
conn.execute("INSERT INTO users (username,password,access) VALUES ('cust7','WallopKirk_96','/api/product/stats')")
conn.commit()
conn.close()
