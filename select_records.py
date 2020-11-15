import sqlite3


def main():
    print('全レコードを取得する！')

    # DBに接続
    conn = sqlite3.connect('sample.db')

    # SQLを組み立てる
    sql = 'SELECT name, age FROM members;'

    # SQLを実行する
    results = conn.execute(sql).fetchall()

    print(results)

    conn.close()

    # ミニ課題: 次のような形式で出力してね
    # Bobさん 25歳
    # Kenさん 19歳
    # ...

    for result in results:
        name = result[0]
        age = result[1]
        print(f'{name}さん {age}歳')

    # 参考
    for (name, age) in results:
        print(f'{name}さん {age}歳')

    for result in results:
        name, age = result
        print(f'{name}さん {age}歳')

    for result in results:
        name, age = result[0], result[1]
        print(f'{name}さん {age}歳')

if __name__ == '__main__':
    main()
