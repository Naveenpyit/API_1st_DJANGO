from rest_framework.decorators import api_view,authentication_classes
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from decouple import config  # type: ignore
import psycopg2


def db_connetion():
    return psycopg2.connect(
        dbname=config('DB_NAME'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        host=config('DB_HOST'),
        port=config('DB_PORT')
    )
    
class api_methods():
    @staticmethod
    def get_view(query):
        try:
            conn=db_connetion()
            cursor=conn.cursor()
            # query="Select * from ph_business"
            cursor.execute(query)
            col_name=[desc[0] for desc in cursor.description]
            rows=cursor.fetchall()
            cursor.close()
            conn.close()
            res=[dict(zip(col_name,row))for row in rows]
            return res
        except Exception as e:
            return {"Error":str(e)}
