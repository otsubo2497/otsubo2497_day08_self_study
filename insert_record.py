import sqlite3


def main():
    print('レコードを追加する！')

    # DBへ接続する
    conn = sqlite3.connect('sample.db')

    # SQLを組み立てる
    # TODO:実はセキュリティ的にアウトな書き方をしているので、後で修正！
    sql = 'INSERT INTO members (name, age) VALUES ("Ken", 19);'

    # SQLを実行する
    conn.execute(sql)
    conn.commit()

    # DBとの接続を閉じる
    conn.close()


if __name__ == '__main__':
    main()
