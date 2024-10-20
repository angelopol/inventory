import sqlite3

def GetConnection():
    connection = sqlite3.connect("inventory.db")
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='inventory';")
    TableExists = cursor.fetchone()
    if not TableExists:
        cursor.execute("CREATE TABLE inventory (id INTEGER PRIMARY KEY, name TEXT, ubication TEXT, code TEXT, supplier TEXT, photo TEXT, created_at DATETIME)")

    cursor.close()
    return connection

def GetItems():
    cursor = GetConnection().cursor()
    cursor.execute("SELECT * FROM inventory ORDER BY created_at")
    items = cursor.fetchall()
    cursor.close()
    return items

def GetItemsByName(name):
    cursor = GetConnection().cursor()
    cursor.execute("SELECT * FROM inventory WHERE name LIKE '%' || ? || '%' ORDER BY created_at", (name,))
    items = cursor.fetchall()
    cursor.close()
    return items

def GetItemsByCode(code):
    cursor = GetConnection().cursor()
    cursor.execute("SELECT * FROM inventory WHERE code LIKE '%' || ? || '%' ORDER BY created_at", (code,))
    items = cursor.fetchall()
    cursor.close()
    return items

def GetItemsBySupplier(supplier):
    cursor = GetConnection().cursor()
    cursor.execute("SELECT * FROM inventory WHERE supplier LIKE '%' || ? || '%' ORDER BY created_at", (supplier,))
    items = cursor.fetchall()
    cursor.close()
    return items

def GetItemsByUbication(ubication):
    cursor = GetConnection().cursor()
    cursor.execute("SELECT * FROM inventory WHERE ubication LIKE '%' || ? || '%' ORDER BY created_at", (ubication,))
    items = cursor.fetchall()
    cursor.close()
    return items

def StoreItem(name, ubication, code, supplier, photo = ""):
    connection = GetConnection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO inventory (name, ubication, created_at, code, supplier, photo) VALUES (?, ?, datetime('now'), ?, ?, ?)", (name, ubication, code, supplier, photo))
    connection.commit()
    cursor.close()

def DeleteItem(id):
    connection = GetConnection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM inventory WHERE id = ?", (id,))
    connection.commit()
    cursor.close()

def UpdateItem(id, name, ubication, code, supplier, photo = ""):
    connection = GetConnection()
    cursor = connection.cursor()
    cursor.execute("UPDATE inventory SET name = ?, ubication = ?, code = ?, supplier = ?, photo = ? WHERE id = ?", (name, ubication, code, supplier, photo, id))
    connection.commit()
    cursor.close()