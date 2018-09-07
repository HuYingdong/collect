import MySQLdb
default_db = {'host': 'localhost', 'user': 'root', 'db': 'test_db'}
connection = MySQLdb.connect(**default_db)


class Mysql:

    @staticmethod
    def select(table=None, values=[], cond={}, cursor=None):
        if not table:
            return {}
        table = '`' + table + '`'
        key = list(map(lambda x: '`' + x + '`', values)) if values else []
        con = list(map(lambda x: ('`' + x + '`', x), list(cond))) if cond else []
        if key and con:
            sql = 'SELECT ' + ','.join(key) + ' FROM %s' % table + ' WHERE ' + ' and '.join(
                ['{}=%({})s'.format(i[0], i[1]) for i in con]) + ';'
        elif key:
            sql = 'SELECT ' + ','.join(key) + ' FROM %s' % table + ';'
        elif con:
            sql = 'SELECT *' + ' FROM %s' % table + ' WHERE ' + ' and '.join(
                ['{}=%({})s'.format(i[0], i[1]) for i in con]) + ';'
        else:
            sql = 'SELECT *' + ' FROM %s' % table + ';'
        if cursor:
            counts = cursor.execute(sql, cond) if con else cursor.execute(sql)
        else:
            with connection.cursor() as cursor:
                counts = cursor.execute(sql, cond) if con else cursor.execute(sql)
        if counts == 0:
            return {}
        key = list(map(lambda x: x[0], cursor.description))
        result = list(dict(zip(key, value)) for value in cursor.fetchall())
        return result

    @staticmethod
    def insert(table=None, values=None, cursor=None):
        if not table or not values:
            return {}
        table = '`' + table + '`'
        if isinstance(values, dict):
            key = list(map(lambda x: '`' + x + '`', list(values)))
            sql = 'INSERT INTO %s (' % table + ','.join(key) + ') VALUES (' + ','.join(
                ['%({})s'.format(i) for i in list(values)]) + ');'

        elif isinstance(values, list):
            key = list(map(lambda x: '`' + x + '`', list(values[0])))
            sql = 'INSERT INTO %s (' % table + ','.join(key) + ') VALUES (' + ','.join(
                ['%({})s'.format(i) for i in list(values[0])]) + ');'
        else:
            return {}
        if cursor:
            result = cursor.execute(sql, values) if isinstance(values, dict) else cursor.executemany(sql, values)
        else:
            with connection.cursor() as cursor:
                result = cursor.execute(sql, values) if isinstance(values, dict) else cursor.executemany(sql, values)
        return {'insert_counts': result}

    @staticmethod
    def update(table=None, values=None, cond=None, cursor=None):
        if not table or not values or not cond:
            return {}
        table = '`' + table + '`'
        key = list(map(lambda x: ('`' + x + '`', x), list(values)))
        con = list(map(lambda x: ('`' + x + '`', x), list(cond)))
        sql = 'UPDATE %s SET ' % table + ','.join(['{}=%({})s'.format(i[0], i[1]) for i in key]) + \
              ' WHERE' + ' and '.join(['{}=%({})s'.format(i[0], i[1]) for i in con]) + ';'
        if cursor:
            result = cursor.execute(sql, dict(values, **cond))
        else:
            with connection as cursor:
                result = cursor.execute(sql, dict(values, **cond))
        return {'update_counts': result}

    @staticmethod
    def delete(table=None, cond=None, cursor=None):
        if not table or not cond:
            return {}
        table = '`' + table + '`'
        con = list(map(lambda x: ('`' + x + '`', x), list(cond)))
        sql = 'DELETE FROM %s WHERE (' % table + ' and '.join(
            ['{}=%({})s'.format(i[0], i[1]) for i in con]) + ');'
        if cursor:
            result = cursor.execute(sql, cond)
        else:
            with connection as cursor:
                result = cursor.execute(sql, cond)
        return {'delete_counts': result}
