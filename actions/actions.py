from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# from rasa_core_sdk import Action
from rasa_sdk.interfaces import Action

# import requests
# import json
# from bs4 import BeautifulSoup
# from pyvi import ViTokenizer, ViPosTagger
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="laptop_store"
)

cursor = mydb.cursor()

class ActionAskKnowledgeBaseSanPham(Action):

    def name(self):
        return "action_best_product"

    def run(self, dispatcher,tracker,domain):
        mysql_select_query = ''' SELECT * from san_pham'''
        cursor.execute(mysql_select_query)
        record = cursor.fetchone()
        # for result in record:
            # san_pham = result[0].lower()
        if record:
            dispatcher.utter_message("http://127.0.0.1:3000/products/" + record[0])
        else:
            dispatcher.utter_message("Dạ cửa hàng em chưa có sản phẩm như anh chi cần ạ")
        return []
    

class ActionGreet(Action):
    def name(self):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_greet")
        return []