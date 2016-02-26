import psycopg2
import sys
from secrets import *

def connect(db_name):
    try:
        conn = psycopg2.connect(database=db_name, user=DATABASE_USERNAME, host='localhost', password=DATABASE_PASSWORD)
    except psycopg2.DatabaseError, e:
        print 'Error %s' % e
        sys.exit(1)

    return conn

def get_most_openings(conn):
    cur = conn.cursor()
    s = "SELECT agency, SUM(number_of_positions) AS total_pos FROM jobs GROUP BY agency ORDER BY total_pos DESC LIMIT 1;" 
    cur.execute(s)
    return cur.fetchone()

def get_lowest_paying_department(conn):
    cur = conn.cursor()
    s = "SELECT agency, salary_range_from FROM jobs WHERE salary_range_from IN (SELECT MIN(salary_range_from) FROM jobs);"
    cur.execute(s)
    return cur.fetchone()

def get_highest_paying_department(conn):
    cur = conn.cursor()
    s = "SELECT agency, salary_range_ro FROM jobs WHERE salary_range_ro IN (SELECT MAX(salary_range_ro) FROM jobs);"
    cur.execute(s)
    return cur.fetchone()

def get_hardest_job(conn):
    cur = conn.cursor()
    s = "SELECT number_of_positions, posting_date, business_title, level FROM jobs WHERE level IN ('M3', 'M4', 'M5') AND to_timestamp(posting_date, 'MM/DD/YYYY HH24:MI:SS') < '12/30/2013 00:00:00' ORDER BY to_timestamp(posting_date, 'MM/DD/YYYY HH24:MI:SS') ASC;"
    cur.execute(s)
    return cur.fetchone()


if __name__=='__main__':
    db_name = 'nycdata'
    conn = connect(db_name)

    ##############################
    # Who has the most openings? #
    ##############################
    most_opening_agency = get_most_openings(conn)[0]
    most_opening_number = get_most_openings(conn)[1]
    print "The agency with most openings is " + most_opening_agency + " and with number of openings " + str(most_opening_number)

    ######################################################
    # Which departments have the lowest paying position? #
    ######################################################
    lowest_paying_agency = get_lowest_paying_department(conn)[0]
    lowest_paying_amount = get_lowest_paying_department(conn)[1]
    print "The department with lowest paying position is " + lowest_paying_agency + " and with amount of " + str(lowest_paying_amount) + " dollars"

    #######################################################
    # Which departments have the highest paying position? #
    #######################################################
    highest_paying_agency = get_highest_paying_department(conn)[0]
    highest_paying_amount = get_highest_paying_department(conn)[1]
    print "The department with highest paying position is " + highest_paying_agency + " and with amount of " + str(highest_paying_amount) + " dollars"


    ################################
    # Which job is hardest to fill #
    ################################
    hardest_job = get_hardest_job(conn)[2]
    print "The hardest job to fill is " + hardest_job + " posted on " + get_hardest_job(conn)[1]


    conn.close() 


