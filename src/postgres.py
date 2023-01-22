import psycopg2

from constants import DATABASE, DATABASE_USER, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT

connection = psycopg2.connect(
    database = DATABASE,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD,
    host = DATABASE_HOST,
    port = DATABASE_PORT
)
