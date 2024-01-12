from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action

import requests
import json
from bs4 import BeautifulSoup
from pyvi import ViTokenizer, ViPosTagger
# import mysql.connector


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="admin",
#   database="laptop_store"
# )

# cursor = mydb.cursor()

class ActionAskKnowledgeBaseSanPham(Action):

    def name(self):
        return "action_best_product"

    def run(self, dispatcher,tracker,domain):
        # text = tracker.latest_message['text']
        # text_input = text.lower()
        # mysql_select_query = ''' SELECT * from product'''
        # cursor.execute(mysql_select_query)
        # record = cursor.fetchall()
        # for result in record:
            # san_pham = result[0].lower()
        dispatcher.utter_message("Nội dung bạn muốn bot trả lời test ----------------")
        # if not check:
            # dispatcher.utter_message("Dạ cửa hàng em chưa có sản phẩm như anh chi cần ạ")
        return