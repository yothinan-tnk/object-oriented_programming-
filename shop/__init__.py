import database

mycursor = database.mydb.cursor()

# ---------------------------------- #
def selectdb(table):
    sql = f"SELECT * FROM {table}"
    mycursor.execute(sql)
    show = mycursor.fetchall()
    return show

# ---------------------------------- #
def deletedb(table, id_name, id):
    sql = f"DELETE FROM {table} WHERE {id_name} = %s"
    val = (id,)
    mycursor.execute(sql, val)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False

# ---------------------------------- #
def editdb(table, column, id_name, id, val): 
    sql = f"UPDATE {table} SET {column} = %s WHERE {id_name} = %s"
    val_sql = (val, id)
    mycursor.execute(sql, val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False

# ---------------------------------- #
def insert_product(name, price, stock):
    sql = "INSERT INTO product VALUES (%s, %s, %s, %s)"
    val_sql = (None, name, price, stock) 
    mycursor.execute(sql, val_sql)
    database.mydb.commit()
    if mycursor.rowcount > 0:
        return True
    else:
        return False

# ตัวอย่างการใช้งานฟังก์ชัน insert_product
print(insert_product("test", 595, 5555))
