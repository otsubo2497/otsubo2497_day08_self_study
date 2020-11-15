import sqlite3


def main():
    print('membersテーブルをつくるぞ！')

    # DBに接続する
    conn = sqlite3.connect('sample.db')

    # 実行したいSQL文を用意する
    sql = """
    CREATE TABLE "members" (
    "name"	TEXT,
    "age"	INTEGER);    
    """

    # SQL文を実行する
    conn.execute(sql)
    conn.commit()

    # 接続を閉じる
    conn.close()


if __name__ == '__main__':
    main()
