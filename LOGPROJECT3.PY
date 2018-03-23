# /usr/bin/env python3 LOGPROJECT3.py

#  LOG PROJECT

"""
Query questions:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?
"""

import psycopg2


def connect():
    return psycopg2.connect("dbname=news")


DBNAME = "news"


def runQuery(query):
    """runQuery takes a string as a parameter. It runs the query and returns
    the result as a list of tuples"""
    try:
        db = connect()
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows
    except BaseException:
        print("Unable to connect to the database")

# query 1
# What are the most popular three articles of all time?


def query1():
    """Return the most popular 3 articles """

    query = """select articles.title, count(*) as views from articles join
    log on articles.slug =
    substring(log.path,10) where path != '/'group by substring(log.path, 10)
    ,articles.title
    order by views desc limit 3;"""
    popular_articles = runQuery(query)
    # Display header and results for Query 1
    print('--- Top Three Articles by Page View ---')
    for i in popular_articles:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")
    print(" ")  # Display line break for legibility

# query 2
# Who are the most popular article authors of all time?


def query2():
    """Return the most popular 3 authors """

    query = """select authors.name, count(log.path)
    as views from authors left join articles on authors.id =
    articles.author left join log on log.path like concat('%', articles.slug)
    group by authors.name order by views desc;"""
    popular_authors = runQuery(query)
    # Display header and results for Query 2
    print('--- Top Three Authors by Page View ---')
    for i in popular_authors:
        print('"' + i[0] + '" -- ' + str(i[1]) + " views")
    print(" ")  # Display line break for legibility

# query 3
# On which days did more than 1% of requests lead to errors?


def query3():
    """Return the days that the errors were more than 1% """

    query = """select * from rate_val where val > 1;"""
    errors_per_day = runQuery(query)
    # Display header and results for Query 3
    print('--- days that the errors were more than 1% ---')
    for i in errors_per_day:
        print('"' + i[0] + '" -- ' + str(i[1]) + " percentage ")
    print(" ")  # Display line break for legibility


if __name__ == '__main__':
    print(" ")
    print("**** Results ****")
    print(" ")
    query1()
    query2()
    query3()
