import pymysql


def connect_database(host, username, password, database, sqls):

    conn = pymysql.connect(host = host,
                           user = username,
                           password = password,
                           database = database);

    cur = conn.cursor();
    try:
        for sql in sqls:
            cur.execute(sql);
    except:
        print("sql执行失败")

    cur.close();
    conn.close();
