import sqlite3

def create_table():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS finances (id INTEGER PRIMARY KEY, type TEXT,amount REAL,
    category TEXT)''')
    conn.commit()
    conn.close()

def enter_income():
    sum = float(input('Enter the income amount:'))
    category = input('Enter the income category:')
    add_record('income', sum, category)
    print('Income recorded successfully!')

def enter_expense():
    sum = float(input('Enter the expense amount:'))
    category = input('Enter the expense category:')
    add_record('expenses', sum, category)
    print('Expense recorded successfully!')

def get_balance():
    return view_balance()

def get_all_incomes():
    return generate_report('income')

def get_all_expenses():
    return generate_report('expenses')

def delete_record():
    record_id = int(input('Enter the ID of the record you want to delete:'))
    delete_record_by_id(record_id)
    print('Record deleted successfully!')

def update_record():
    record_id = int(input('Enter the ID of the record you want to update:'))
    new_type = input('Enter the new type (income/expenses): ')
    new_amount = float(input('Enter the new amount:'))
    new_category = input('Enter the new category:')
    update_record_by_id(record_id, new_type, new_amount, new_category)
    print('Record updated successfully!')

def add_record(type, amount, category):
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO finances(type, amount, category) VALUES (?, ?, ?)', (type, amount, category))
    conn.commit()
    conn.close()

def view_balance():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(CASE WHEN type="income" THEN amuont ELSE -amount END) FROM finances')
    balance = cursor.fetchone()[0]
    conn.close()
    return balance if balance else 0

def generete_report(type):
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM finances WHERE type= ?', (type,))
    records = cursor.fetchall()
    conn.close()
    return records

def delete_record_by_id(record_id):
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM finances WHERE id = ?', (record_id,))
    conn.commit()
    conn.close()

def update_record_by_id(record_id, new_type, new_amount, new_category):
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE finances SET type = ?, amount = ?, category = ? WHERE id = ?', (new_type,
    new_category, record_id))
    conn.commit()
    conn.close()

def print_menu():
    print("\n===== Personal Finances Management =====")
    print('1. Enter Income')
    print('2. Enter Expenses')
    print('3. Get Balance')
    print('4. Get All Incomes')
    print('5. Get All Expenses')
    print('6. Delete Income/Expense')
    print('7. Update Income/Expense')
    print('8. Exit')

create_table()
while True:
    if choice == '1':
        enter_income()
    elif choice =='2':
        enter_expense()
    elif choice =='3':
        print('Balance:', get_balance())
    elif choice =='4':
        print('All Incomes:', get_all_incomes())
    elif choice =='5':
        print('All Expenses:', get_all_expenses())
    elif choice =='6':
        delete_record()
    elif choice =='7':
        update_record()
    elif choice =='8':
        print('Exiting the application.')
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 8.')