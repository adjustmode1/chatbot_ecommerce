# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from __future__ import unicode_literals

# from rasa_core_sdk import Action
# from rasa_core_sdk.events import SlotSet
# from rasa_core_sdk.events import UserUtteranceReverted
# from rasa_core_sdk.events import AllSlotsReset
# from rasa_core_sdk.events import Restarted

# import requests
# import json
# from bs4 import BeautifulSoup
# from pyvi import ViTokenizer, ViPosTagger
# import mysql.connector


# # mydb = mysql.connector.connect(
# #   host="localhost",
# #   user="root",
# #   password="admin",
# #   database="laptop_store"
# # )

# # cursor = mydb.cursor()

# def name_cap(text):
#     tarr = text.split()
#     for idx in range(len(tarr)):
#         tarr[idx] = tarr[idx].capitalize()
#     return ' '.join(tarr)

# class ActionAskKnowledgeBaseSanPham(Action):

#     def name(self):
#         return "action_best_product"

#     def run(self, dispatcher,tracker,domain):
#         # text = tracker.latest_message['text']
#         # text_input = text.lower()
#         # mysql_select_query = ''' SELECT * from product'''
#         # cursor.execute(mysql_select_query)
#         # record = cursor.fetchall()
#         # for result in record:
#             # san_pham = result[0].lower()
#         dispatcher.utter_message("Nội dung bạn muốn bot trả lời test ----------------")
#         # if not check:
#             # dispatcher.utter_message("Dạ cửa hàng em chưa có sản phẩm như anh chi cần ạ")
#         return

# class action_save_cust_info(Action):
#     def name(self):
#         return 'action_save_cust_info'

#     def run(self, dispatcher, tracker, domain):
#         user_id = (tracker.current_state())["sender_id"]
#         print(user_id)
#         cust_name = next(tracker.get_latest_entity_values("cust_name"), None)
#         cust_sex = next(tracker.get_latest_entity_values("cust_sex"), None)
#         bot_position = "SHB"

#         if (cust_sex is  None):
#             cust_sex = "Quý khách"

#         if (cust_sex == "anh") | (cust_sex == "chị"):
#            bot_position = "em"
#         elif (cust_sex == "cô") | (cust_sex == "chú"):
#             bot_position = "cháu"
#         else:
#             cust_sex = "Quý khách"
#             bot_position = "SHB"

#         if not cust_name:
#             #dispatcher.utter_template("utter_greet_name",tracker)
#             return []

#         print (name_cap(cust_name))
#         return [SlotSet('cust_name', " "+name_cap(cust_name)),SlotSet('cust_sex', name_cap(cust_sex)),SlotSet('bot_position', name_cap(bot_position))]

# class action_save_mobile_no(Action):
#     def name(self):
#         return 'action_save_mobile_no'

#     def run(self, dispatcher, tracker, domain):
#         user_id = (tracker.current_state())["sender_id"]
#         print(user_id)
#         mobile_no = next(tracker.get_latest_entity_values("inp_number"), None)

#         if not mobile_no:
#             return  [UserUtteranceReverted()]

#         mobile_no = mobile_no.replace(" ","")
#         #print (cust_name)
#         return [SlotSet('mobile_no', mobile_no)]



# class action_reset_slot(Action):

#     def name(self):
#         return "action_reset_slot"

#     def run(self, dispatcher, tracker, domain):
#         return [SlotSet("transfer_nick", None),SlotSet("transfer_amount", None),SlotSet("transfer_amount_unit", None)]