import psycopg2


def create_table():
    conn = psycopg2.connect(host = "localhost",
                            dbname = "postgres",
                            user = "postgres",
                            password = "0906132004",
                            port = "5432")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_data (
                                    id SERIAL PRIMARY KEY,
                                    tg_id BIGINT,
                                    username VARCHAR,
                                    fullname VARCHAR,
                                    input_name VARCHAR,
                                    input_phone VARCHAR,
                                    input_age INT)''')
    conn.commit()
    return conn, cursor

def save_user(user_id, username, fullname, name, phone, age):
    conn, cursor = create_table()
    cursor.execute('''SELECT username FROM user_data''')
    result = cursor.fetchall()
    cursor.execute('''INSERT INTO user_data (tg_id, username, fullname, input_name, input_phone, input_age)
                        VALUES (%s, %s, %s, %s, %s, %s)''', [user_id, username, fullname, name, phone, age])
    print(f"Total users: {len(set(result))}")
    conn.commit()