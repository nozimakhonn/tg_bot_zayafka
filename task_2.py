import asyncpg
import asyncio


async def create_table():
    conn = await asyncpg.connect(host ="localhost",
                                 dbname = "asyncio",
                                 user = "asyncio",
                                 password = "0906132004",
                                 port = "5432")
    await conn.execute('''CREATE TABLE IF NOT EXISTS user_data (
                                 id INTEGER PRIMARY KEY,
                                 tg_id BIGINT,
                                 username VARCHAR,
                                 fullname VARCHAR,
                                 input_name VARCHAR,
                                 input_phone VARCHAR,
                                 input_age INT)''')
    return conn


async def save_user(user_id, username, fullname, name, phone, age):
    conn = await create_table()
    conn.execute('''SELECT username FROM user_data''')
    result = conn.fetch()

    await conn.execute('''INSERT INTO user_data (tg_id, username, fullname, input_name, input_phone, input_age)
                      VALUES (%, %, %, %, %, %)''', user_id, username, fullname, name, phone, age
    )
    print(f"Total users: {len(set(result))}")

    await conn.commit()