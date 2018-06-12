import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'Zdw2948031.',
    'db': 'python',
    'charset': 'utf8mb4',
}
conn = pymysql.connect(**config)
cur = conn.cursor()


class Sql:

    @classmethod
    def insert_dytt(cls, name, link):
        try:
            sql = "INSERT INTO dytt (movie_name,down_link) VALUES (%s, %s)"
            values = (name, link)
            cur.execute(sql, values)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
            raise e

    @classmethod
    def insert_dangdang(cls, title, author, link):
        sql = "insert into dangdang('title','author','link') values (%(title)s,%(author)s,%(link)s)"
        values = {
            'title': title,
            'author': author,
            'link': link,
        }
        cur.execute(sql, values)
        conn.commit()
