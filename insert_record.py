import sqlite3


def main():
    name = input('name > ')
    age = int(input('age > '))

    print('レコードを追加する！')

    # DBへ接続する
    conn = sqlite3.connect('sample.db')

    # SQLを組み立てる
    sql = f'INSERT INTO members (name, age) VALUES (?, ?)'

    # SQLを実行する
    conn.execute(sql, (name, age))
    conn.commit()

    # DBとの接続を閉じる
    conn.close()


if __name__ == '__main__':
    main()
