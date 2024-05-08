# header = ['Age','Dwell_Time_0', 'Dwell_Time_1', 'Dwell_Time_2', 'Dwell_Time_3', 'Dwell_Time_4', 'Dwell_Time_5',
#                   'Dwell_Time_6', 'Dwell_Time_7', 'Dwell_Time_8', 'Dwell_Time_9', 'Dwell_Time_0N', 'Dwell_Time_1N',
#                   'Dwell_Time_2N', 'Dwell_Time_3N', 'Dwell_Time_4N', 'Dwell_Time_5N', 'Dwell_Time_6N', 'Dwell_Time_7N',
#                   'Dwell_Time_8N', 'Dwell_Time_9N', 'Flight_Time_0_0NN', 'Flight_Time_0_1NN', 'Flight_Time_0_2NN',
#                   'Flight_Time_0_3NN', 'Flight_Time_0_4NN', 'Flight_Time_0_5NN', 'Flight_Time_0_6NN',
#                   'Flight_Time_0_7NN', 'Flight_Time_0_8NN', 'Flight_Time_0_9NN', 'Flight_Time_1_0NN',
#                   'Flight_Time_1_1NN', 'Flight_Time_1_2NN', 'Flight_Time_1_3NN', 'Flight_Time_1_4NN',
#                   'Flight_Time_1_5NN', 'Flight_Time_1_6NN', 'Flight_Time_1_7NN', 'Flight_Time_1_8NN',
#                   'Flight_Time_1_9NN', 'Flight_Time_2_0NN', 'Flight_Time_2_1NN', 'Flight_Time_2_2NN',
#                   'Flight_Time_2_3NN', 'Flight_Time_2_4NN', 'Flight_Time_2_5NN', 'Flight_Time_2_6NN',
#                   'Flight_Time_2_7NN', 'Flight_Time_2_8NN', 'Flight_Time_2_9NN', 'Flight_Time_3_0NN',
#                   'Flight_Time_3_1NN', 'Flight_Time_3_2NN', 'Flight_Time_3_3NN', 'Flight_Time_3_4NN',
#                   'Flight_Time_3_5NN', 'Flight_Time_3_6NN', 'Flight_Time_3_7NN', 'Flight_Time_3_8NN',
#                   'Flight_Time_3_9NN', 'Flight_Time_4_0NN', 'Flight_Time_4_1NN', 'Flight_Time_4_2NN',
#                   'Flight_Time_4_3NN', 'Flight_Time_4_4NN', 'Flight_Time_4_5NN', 'Flight_Time_4_6NN',
#                   'Flight_Time_4_7NN', 'Flight_Time_4_8NN', 'Flight_Time_4_9NN', 'Flight_Time_5_0NN',
#                   'Flight_Time_5_1NN', 'Flight_Time_5_2NN', 'Flight_Time_5_3NN', 'Flight_Time_5_4NN',
#                   'Flight_Time_5_5NN', 'Flight_Time_5_6NN', 'Flight_Time_5_7NN', 'Flight_Time_5_8NN',
#                   'Flight_Time_5_9NN', 'Flight_Time_6_0NN', 'Flight_Time_6_1NN', 'Flight_Time_6_2NN',
#                   'Flight_Time_6_3NN', 'Flight_Time_6_4NN', 'Flight_Time_6_5NN', 'Flight_Time_6_6NN',
#                   'Flight_Time_6_7NN', 'Flight_Time_6_8NN', 'Flight_Time_6_9NN', 'Flight_Time_7_0NN',
#                   'Flight_Time_7_1NN', 'Flight_Time_7_2NN', 'Flight_Time_7_3NN', 'Flight_Time_7_4NN',
#                   'Flight_Time_7_5NN', 'Flight_Time_7_6NN', 'Flight_Time_7_7NN', 'Flight_Time_7_8NN',
#                   'Flight_Time_7_9NN', 'Flight_Time_8_0NN', 'Flight_Time_8_1NN', 'Flight_Time_8_2NN',
#                   'Flight_Time_8_3NN', 'Flight_Time_8_4NN', 'Flight_Time_8_5NN', 'Flight_Time_8_6NN',
#                   'Flight_Time_8_7NN', 'Flight_Time_8_8NN', 'Flight_Time_8_9NN', 'Flight_Time_9_0NN',
#                   'Flight_Time_9_1NN', 'Flight_Time_9_2NN', 'Flight_Time_9_3NN', 'Flight_Time_9_4NN',
#                   'Flight_Time_9_5NN', 'Flight_Time_9_6NN', 'Flight_Time_9_7NN', 'Flight_Time_9_8NN',
#                   'Flight_Time_9_9NN', 'Flight_Time_0_0RR', 'Flight_Time_0_1RR', 'Flight_Time_0_2RR',
#                   'Flight_Time_0_3RR', 'Flight_Time_0_4RR', 'Flight_Time_0_5RR', 'Flight_Time_0_6RR',
#                   'Flight_Time_0_7RR', 'Flight_Time_0_8RR', 'Flight_Time_0_9RR', 'Flight_Time_1_0RR',
#                   'Flight_Time_1_1RR', 'Flight_Time_1_2RR', 'Flight_Time_1_3RR', 'Flight_Time_1_4RR',
#                   'Flight_Time_1_5RR', 'Flight_Time_1_6RR', 'Flight_Time_1_7RR', 'Flight_Time_1_8RR',
#                   'Flight_Time_1_9RR', 'Flight_Time_2_0RR', 'Flight_Time_2_1RR', 'Flight_Time_2_2RR',
#                   'Flight_Time_2_3RR', 'Flight_Time_2_4RR', 'Flight_Time_2_5RR', 'Flight_Time_2_6RR',
#                   'Flight_Time_2_7RR', 'Flight_Time_2_8RR', 'Flight_Time_2_9RR', 'Flight_Time_3_0RR',
#                   'Flight_Time_3_1RR', 'Flight_Time_3_2RR', 'Flight_Time_3_3RR', 'Flight_Time_3_4RR',
#                   'Flight_Time_3_5RR', 'Flight_Time_3_6RR', 'Flight_Time_3_7RR', 'Flight_Time_3_8RR',
#                   'Flight_Time_3_9RR', 'Flight_Time_4_0RR', 'Flight_Time_4_1RR', 'Flight_Time_4_2RR',
#                   'Flight_Time_4_3RR', 'Flight_Time_4_4RR', 'Flight_Time_4_5RR', 'Flight_Time_4_6RR',
#                   'Flight_Time_4_7RR', 'Flight_Time_4_8RR', 'Flight_Time_4_9RR', 'Flight_Time_5_0RR',
#                   'Flight_Time_5_1RR', 'Flight_Time_5_2RR', 'Flight_Time_5_3RR', 'Flight_Time_5_4RR',
#                   'Flight_Time_5_5RR', 'Flight_Time_5_6RR', 'Flight_Time_5_7RR', 'Flight_Time_5_8RR',
#                   'Flight_Time_5_9RR', 'Flight_Time_6_0RR', 'Flight_Time_6_1RR', 'Flight_Time_6_2RR',
#                   'Flight_Time_6_3RR', 'Flight_Time_6_4RR', 'Flight_Time_6_5RR', 'Flight_Time_6_6RR',
#                   'Flight_Time_6_7RR', 'Flight_Time_6_8RR', 'Flight_Time_6_9RR', 'Flight_Time_7_0RR',
#                   'Flight_Time_7_1RR', 'Flight_Time_7_2RR', 'Flight_Time_7_3RR', 'Flight_Time_7_4RR',
#                   'Flight_Time_7_5RR', 'Flight_Time_7_6RR', 'Flight_Time_7_7RR', 'Flight_Time_7_8RR',
#                   'Flight_Time_7_9RR', 'Flight_Time_8_0RR', 'Flight_Time_8_1RR', 'Flight_Time_8_2RR',
#                   'Flight_Time_8_3RR', 'Flight_Time_8_4RR', 'Flight_Time_8_5RR', 'Flight_Time_8_6RR',
#                   'Flight_Time_8_7RR', 'Flight_Time_8_8RR', 'Flight_Time_8_9RR', 'Flight_Time_9_0RR',
#                   'Flight_Time_9_1RR', 'Flight_Time_9_2RR', 'Flight_Time_9_3RR', 'Flight_Time_9_4RR',
#                   'Flight_Time_9_5RR', 'Flight_Time_9_6RR', 'Flight_Time_9_7RR', 'Flight_Time_9_8RR',
#                   'Flight_Time_9_9RR' ]

header = ['Dwell_Time_1N', 'Dwell_Time_3N', 'Flight_Time_0_0NN', 'Flight_Time_0_1NN', 'Flight_Time_0_2NN', 'Flight_Time_0_3NN', 'Flight_Time_0_4NN', 'Flight_Time_0_5NN', 'Flight_Time_0_6NN', 'Flight_Time_0_7NN', 'Flight_Time_0_8NN', 'Flight_Time_0_9NN', 'Flight_Time_1_1NN', 'Flight_Time_1_2NN', 'Flight_Time_1_5NN', 'Flight_Time_1_6NN', 'Flight_Time_2_1NN', 'Flight_Time_2_4NN', 'Flight_Time_2_5NN', 'Flight_Time_2_6NN', 'Flight_Time_2_8NN', 'Flight_Time_3_2NN', 'Flight_Time_3_4NN', 'Flight_Time_3_5NN', 'Flight_Time_3_6NN', 'Flight_Time_3_7NN', 'Flight_Time_3_8NN', 'Flight_Time_3_9NN', 'Flight_Time_4_0NN', 'Flight_Time_4_1NN', 'Flight_Time_4_3NN', 'Flight_Time_4_5NN', 'Flight_Time_4_7NN', 'Flight_Time_5_1NN', 'Flight_Time_5_2NN', 'Flight_Time_5_3NN', 'Flight_Time_5_6NN', 'Flight_Time_5_8NN', 'Flight_Time_5_9NN', 'Flight_Time_6_0NN', 'Flight_Time_6_2NN', 'Flight_Time_6_9NN', 'Flight_Time_7_0NN', 'Flight_Time_7_2NN', 'Flight_Time_7_3NN', 'Flight_Time_7_4NN', 'Flight_Time_7_8NN', 'Flight_Time_7_9NN', 'Flight_Time_8_0NN', 'Flight_Time_8_1NN', 'Flight_Time_8_2NN', 'Flight_Time_8_3NN', 'Flight_Time_8_6NN', 'Flight_Time_8_8NN', 'Flight_Time_8_9NN', 'Flight_Time_9_1NN', 'Flight_Time_9_2NN', 'Flight_Time_9_3NN', 'Flight_Time_9_6NN', 'Flight_Time_9_9NN', 'Flight_Time_0_0RR', 'Flight_Time_0_1RR', 'Flight_Time_0_3RR', 'Flight_Time_0_4RR', 'Flight_Time_0_5RR', 'Flight_Time_0_8RR', 'Flight_Time_0_9RR', 'Flight_Time_1_2RR', 'Flight_Time_1_3RR', 'Flight_Time_1_5RR', 'Flight_Time_1_7RR', 'Flight_Time_1_8RR', 'Flight_Time_1_9RR', 'Flight_Time_2_0RR', 'Flight_Time_2_1RR', 'Flight_Time_2_2RR', 'Flight_Time_2_3RR', 'Flight_Time_2_7RR', 'Flight_Time_3_0RR', 'Flight_Time_3_3RR', 'Flight_Time_3_5RR', 'Flight_Time_4_0RR', 'Flight_Time_4_6RR', 'Flight_Time_4_8RR', 'Flight_Time_5_0RR', 'Flight_Time_5_1RR', 'Flight_Time_5_2RR', 'Flight_Time_5_6RR', 'Flight_Time_5_9RR', 'Flight_Time_6_0RR', 'Flight_Time_6_1RR', 'Flight_Time_6_2RR', 'Flight_Time_6_3RR', 'Flight_Time_6_4RR', 'Flight_Time_6_5RR', 'Flight_Time_6_7RR', 'Flight_Time_7_2RR', 'Flight_Time_8_0RR', 'Flight_Time_8_2RR', 'Flight_Time_8_3RR', 'Flight_Time_8_6RR', 'Flight_Time_8_7RR', 'Flight_Time_8_8RR', 'Flight_Time_8_9RR', 'Flight_Time_9_1RR', 'Flight_Time_9_2RR', 'Flight_Time_9_4RR', 'Flight_Time_9_5RR', 'Flight_Time_9_6RR', 'Flight_Time_9_8RR']

flags = [False, False, False, False, False ,False, False, False, False, False, False,  True,
 False,  True, False, False, False, False, False, False,  True,  True,  True,  True,
  True,  True,  True,  True,  True,  True, False,  True,  True, False, False,  True,
  True, False, False, False, False,  True, False, False,  True,  True,  True, False,
  True, False, False, False,  True ,False,  True,  True,  True,  True,  True,  True,
  True,  True, False,  True, False,  True, False,  True, False, False, False,  True,
  True,  True, False, False,  True, False,  True,  True,  True, False,  True, False,
 False, False, False, False ,False,  True,  True, False,  True,  True,  True, False,
 False, False,  True,  True,  True,  True,  True  ,True, False, False,  True, False,
  True,  True, False,  True,  True,  True, False, False,  True, False, False,  True,
  True,  True, False,  True,  True,  True, False, False,  True,  True, False, False,
  True,  True, False,  True, False,  True,  True,  True,  True,  True,  True,  True,
 False, False, False,  True, False, False,  True, False, False,  True, False,  True,
 False, False, False, False,  True, False, False, False, False, False,  True, False,
  True, False,  True,  True,  True, False ,False, False,  True, False, False,  True,
  True,  True,  True,  True,  True,  True, False,  True, False, False, False, False,
  True, False, False, False, False, False, False, False,  True, False,  True,  True,
 False, False,  True,  True,  True,  True, False,  True,  True, False,  True,  True,
  True, False,  True, False]
headerInitial = []
index = 0
for head in header:
    if flags[index]:
        headerInitial.append(head)
    index += 1
# for i in headerInitial:
print(headerInitial)



# c1 = 1
# c0 = 0
# for i in Data:
#     if i==0:
#         c0 += 1
#     elif i==1:
#         c1 += 1
#
# print(f"Ta 0 einai : {c0}")
# print(f"Ta 1 einai : {c1}")
# print(f"Sunolo {c0+c1-1}")
# print(Data.count(False))
# print(Data.count(True))

import csv
import pandas as pd
import os

filename = "C:/kl_csv/Classification/features_new_age.csv"
file_to_csv = "C:/kl_csv/Classification/features_new_new_age.csv"


# filename = "C:/kl_csv/Classification/features_new_age.csv"
# file_to_csv = "C:/kl_csv/test/features_new_new_age.csv"
def is_csv_empty(file_path):
    return os.stat(file_path).st_size == 0
header = ['Age', 'Dwell_Time_1N', 'Dwell_Time_3N', 'Flight_Time_0_0NN', 'Flight_Time_0_1NN', 'Flight_Time_0_2NN', 'Flight_Time_0_3NN', 'Flight_Time_0_4NN', 'Flight_Time_0_5NN', 'Flight_Time_0_6NN', 'Flight_Time_0_7NN', 'Flight_Time_0_8NN', 'Flight_Time_0_9NN', 'Flight_Time_1_1NN', 'Flight_Time_1_2NN', 'Flight_Time_1_5NN', 'Flight_Time_1_6NN', 'Flight_Time_2_1NN', 'Flight_Time_2_4NN', 'Flight_Time_2_5NN', 'Flight_Time_2_6NN', 'Flight_Time_2_8NN', 'Flight_Time_3_2NN', 'Flight_Time_3_4NN', 'Flight_Time_3_5NN', 'Flight_Time_3_6NN', 'Flight_Time_3_7NN', 'Flight_Time_3_8NN', 'Flight_Time_3_9NN', 'Flight_Time_4_0NN', 'Flight_Time_4_1NN', 'Flight_Time_4_3NN', 'Flight_Time_4_5NN', 'Flight_Time_4_7NN', 'Flight_Time_5_1NN', 'Flight_Time_5_2NN', 'Flight_Time_5_3NN', 'Flight_Time_5_6NN', 'Flight_Time_5_8NN', 'Flight_Time_5_9NN', 'Flight_Time_6_0NN', 'Flight_Time_6_2NN', 'Flight_Time_6_9NN', 'Flight_Time_7_0NN', 'Flight_Time_7_2NN', 'Flight_Time_7_3NN', 'Flight_Time_7_4NN', 'Flight_Time_7_8NN', 'Flight_Time_7_9NN', 'Flight_Time_8_0NN', 'Flight_Time_8_1NN', 'Flight_Time_8_2NN', 'Flight_Time_8_3NN', 'Flight_Time_8_6NN', 'Flight_Time_8_8NN', 'Flight_Time_8_9NN', 'Flight_Time_9_1NN', 'Flight_Time_9_2NN', 'Flight_Time_9_3NN', 'Flight_Time_9_6NN', 'Flight_Time_9_9NN', 'Flight_Time_0_0RR', 'Flight_Time_0_1RR', 'Flight_Time_0_3RR', 'Flight_Time_0_4RR', 'Flight_Time_0_5RR', 'Flight_Time_0_8RR', 'Flight_Time_0_9RR', 'Flight_Time_1_2RR', 'Flight_Time_1_3RR', 'Flight_Time_1_5RR', 'Flight_Time_1_7RR', 'Flight_Time_1_8RR', 'Flight_Time_1_9RR', 'Flight_Time_2_0RR', 'Flight_Time_2_1RR', 'Flight_Time_2_2RR', 'Flight_Time_2_3RR', 'Flight_Time_2_7RR', 'Flight_Time_3_0RR', 'Flight_Time_3_3RR', 'Flight_Time_3_5RR', 'Flight_Time_4_0RR', 'Flight_Time_4_6RR', 'Flight_Time_4_8RR', 'Flight_Time_5_0RR', 'Flight_Time_5_1RR', 'Flight_Time_5_2RR', 'Flight_Time_5_6RR', 'Flight_Time_5_9RR', 'Flight_Time_6_0RR', 'Flight_Time_6_1RR', 'Flight_Time_6_2RR', 'Flight_Time_6_3RR', 'Flight_Time_6_4RR', 'Flight_Time_6_5RR', 'Flight_Time_6_7RR', 'Flight_Time_7_2RR', 'Flight_Time_8_0RR', 'Flight_Time_8_2RR', 'Flight_Time_8_3RR', 'Flight_Time_8_6RR', 'Flight_Time_8_7RR', 'Flight_Time_8_8RR', 'Flight_Time_8_9RR', 'Flight_Time_9_1RR', 'Flight_Time_9_2RR', 'Flight_Time_9_4RR', 'Flight_Time_9_5RR', 'Flight_Time_9_6RR', 'Flight_Time_9_8RR']

# header = ["Gender", 'Dwell_Time_0', 'Dwell_Time_1', 'Dwell_Time_2', 'Dwell_Time_3', 'Dwell_Time_4', 'Dwell_Time_5',
#                   'Dwell_Time_6', 'Dwell_Time_7', 'Dwell_Time_8', 'Dwell_Time_9', 'Dwell_Time_0N', 'Dwell_Time_1N',
#                   'Dwell_Time_2N', 'Dwell_Time_3N', 'Dwell_Time_4N', 'Dwell_Time_5N', 'Dwell_Time_6N', 'Dwell_Time_7N',
#                   'Dwell_Time_8N', 'Dwell_Time_9N', 'Flight_Time_0_0NN', 'Flight_Time_0_1NN', 'Flight_Time_0_2NN',
#                   'Flight_Time_0_3NN', 'Flight_Time_0_4NN', 'Flight_Time_0_5NN', 'Flight_Time_0_6NN',
#                   'Flight_Time_0_7NN', 'Flight_Time_0_8NN', 'Flight_Time_0_9NN', 'Flight_Time_1_0NN',
#                   'Flight_Time_1_1NN', 'Flight_Time_1_2NN', 'Flight_Time_1_3NN', 'Flight_Time_1_4NN',
#                   'Flight_Time_1_5NN', 'Flight_Time_1_6NN', 'Flight_Time_1_7NN', 'Flight_Time_1_8NN',
#                   'Flight_Time_1_9NN', 'Flight_Time_2_0NN', 'Flight_Time_2_1NN', 'Flight_Time_2_2NN',
#                   'Flight_Time_2_3NN', 'Flight_Time_2_4NN', 'Flight_Time_2_5NN', 'Flight_Time_2_6NN',
#                   'Flight_Time_2_7NN', 'Flight_Time_2_8NN', 'Flight_Time_2_9NN', 'Flight_Time_3_0NN',
#                   'Flight_Time_3_1NN', 'Flight_Time_3_2NN', 'Flight_Time_3_3NN', 'Flight_Time_3_4NN',
#                   'Flight_Time_3_5NN', 'Flight_Time_3_6NN', 'Flight_Time_3_7NN', 'Flight_Time_3_8NN',
#                   'Flight_Time_3_9NN', 'Flight_Time_4_0NN', 'Flight_Time_4_1NN', 'Flight_Time_4_2NN',
#                   'Flight_Time_4_3NN', 'Flight_Time_4_4NN', 'Flight_Time_4_5NN', 'Flight_Time_4_6NN',
#                   'Flight_Time_4_7NN', 'Flight_Time_4_8NN', 'Flight_Time_4_9NN', 'Flight_Time_5_0NN',
#                   'Flight_Time_5_1NN', 'Flight_Time_5_2NN', 'Flight_Time_5_3NN', 'Flight_Time_5_4NN',
#                   'Flight_Time_5_5NN', 'Flight_Time_5_6NN', 'Flight_Time_5_7NN', 'Flight_Time_5_8NN',
#                   'Flight_Time_5_9NN', 'Flight_Time_6_0NN', 'Flight_Time_6_1NN', 'Flight_Time_6_2NN',
#                   'Flight_Time_6_3NN', 'Flight_Time_6_4NN', 'Flight_Time_6_5NN', 'Flight_Time_6_6NN',
#                   'Flight_Time_6_7NN', 'Flight_Time_6_8NN', 'Flight_Time_6_9NN', 'Flight_Time_7_0NN',
#                   'Flight_Time_7_1NN', 'Flight_Time_7_2NN', 'Flight_Time_7_3NN', 'Flight_Time_7_4NN',
#                   'Flight_Time_7_5NN', 'Flight_Time_7_6NN', 'Flight_Time_7_7NN', 'Flight_Time_7_8NN',
#                   'Flight_Time_7_9NN', 'Flight_Time_8_0NN', 'Flight_Time_8_1NN', 'Flight_Time_8_2NN',
#                   'Flight_Time_8_3NN', 'Flight_Time_8_4NN', 'Flight_Time_8_5NN', 'Flight_Time_8_6NN',
#                   'Flight_Time_8_7NN', 'Flight_Time_8_8NN', 'Flight_Time_8_9NN', 'Flight_Time_9_0NN',
#                   'Flight_Time_9_1NN', 'Flight_Time_9_2NN', 'Flight_Time_9_3NN', 'Flight_Time_9_4NN',
#                   'Flight_Time_9_5NN', 'Flight_Time_9_6NN', 'Flight_Time_9_7NN', 'Flight_Time_9_8NN',
#                   'Flight_Time_9_9NN', 'Flight_Time_0_0RN', 'Flight_Time_0_1RN', 'Flight_Time_0_2RN',
#                   'Flight_Time_0_3RN', 'Flight_Time_0_4RN', 'Flight_Time_0_5RN', 'Flight_Time_0_6RN',
#                   'Flight_Time_0_7RN', 'Flight_Time_0_8RN', 'Flight_Time_0_9RN', 'Flight_Time_1_0RN',
#                   'Flight_Time_1_1RN', 'Flight_Time_1_2RN', 'Flight_Time_1_3RN', 'Flight_Time_1_4RN',
#                   'Flight_Time_1_5RN', 'Flight_Time_1_6RN', 'Flight_Time_1_7RN', 'Flight_Time_1_8RN',
#                   'Flight_Time_1_9RN', 'Flight_Time_2_0RN', 'Flight_Time_2_1RN', 'Flight_Time_2_2RN',
#                   'Flight_Time_2_3RN', 'Flight_Time_2_4RN', 'Flight_Time_2_5RN', 'Flight_Time_2_6RN',
#                   'Flight_Time_2_7RN', 'Flight_Time_2_8RN', 'Flight_Time_2_9RN', 'Flight_Time_3_0RN',
#                   'Flight_Time_3_1RN', 'Flight_Time_3_2RN', 'Flight_Time_3_3RN', 'Flight_Time_3_4RN',
#                   'Flight_Time_3_5RN', 'Flight_Time_3_6RN', 'Flight_Time_3_7RN', 'Flight_Time_3_8RN',
#                   'Flight_Time_3_9RN', 'Flight_Time_4_0RN', 'Flight_Time_4_1RN', 'Flight_Time_4_2RN',
#                   'Flight_Time_4_3RN', 'Flight_Time_4_4RN', 'Flight_Time_4_5RN', 'Flight_Time_4_6RN',
#                   'Flight_Time_4_7RN', 'Flight_Time_4_8RN', 'Flight_Time_4_9RN', 'Flight_Time_5_0RN',
#                   'Flight_Time_5_1RN', 'Flight_Time_5_2RN', 'Flight_Time_5_3RN', 'Flight_Time_5_4RN',
#                   'Flight_Time_5_5RN', 'Flight_Time_5_6RN', 'Flight_Time_5_7RN', 'Flight_Time_5_8RN',
#                   'Flight_Time_5_9RN', 'Flight_Time_6_0RN', 'Flight_Time_6_1RN', 'Flight_Time_6_2RN',
#                   'Flight_Time_6_3RN', 'Flight_Time_6_4RN', 'Flight_Time_6_5RN', 'Flight_Time_6_6RN',
#                   'Flight_Time_6_7RN', 'Flight_Time_6_8RN', 'Flight_Time_6_9RN', 'Flight_Time_7_0RN',
#                   'Flight_Time_7_1RN', 'Flight_Time_7_2RN', 'Flight_Time_7_3RN', 'Flight_Time_7_4RN',
#                   'Flight_Time_7_5RN', 'Flight_Time_7_6RN', 'Flight_Time_7_7RN', 'Flight_Time_7_8RN',
#                   'Flight_Time_7_9RN', 'Flight_Time_8_0RN', 'Flight_Time_8_1RN', 'Flight_Time_8_2RN',
#                   'Flight_Time_8_3RN', 'Flight_Time_8_4RN', 'Flight_Time_8_5RN', 'Flight_Time_8_6RN',
#                   'Flight_Time_8_7RN', 'Flight_Time_8_8RN', 'Flight_Time_8_9RN', 'Flight_Time_9_0RN',
#                   'Flight_Time_9_1RN', 'Flight_Time_9_2RN', 'Flight_Time_9_3RN', 'Flight_Time_9_4RN',
#                   'Flight_Time_9_5RN', 'Flight_Time_9_6RN', 'Flight_Time_9_7RN', 'Flight_Time_9_8RN',
#                   'Flight_Time_9_9RN', 'Flight_Time_0_0RR', 'Flight_Time_0_1RR', 'Flight_Time_0_2RR',
#                   'Flight_Time_0_3RR', 'Flight_Time_0_4RR', 'Flight_Time_0_5RR', 'Flight_Time_0_6RR',
#                   'Flight_Time_0_7RR', 'Flight_Time_0_8RR', 'Flight_Time_0_9RR', 'Flight_Time_1_0RR',
#                   'Flight_Time_1_1RR', 'Flight_Time_1_2RR', 'Flight_Time_1_3RR', 'Flight_Time_1_4RR',
#                   'Flight_Time_1_5RR', 'Flight_Time_1_6RR', 'Flight_Time_1_7RR', 'Flight_Time_1_8RR',
#                   'Flight_Time_1_9RR', 'Flight_Time_2_0RR', 'Flight_Time_2_1RR', 'Flight_Time_2_2RR',
#                   'Flight_Time_2_3RR', 'Flight_Time_2_4RR', 'Flight_Time_2_5RR', 'Flight_Time_2_6RR',
#                   'Flight_Time_2_7RR', 'Flight_Time_2_8RR', 'Flight_Time_2_9RR', 'Flight_Time_3_0RR',
#                   'Flight_Time_3_1RR', 'Flight_Time_3_2RR', 'Flight_Time_3_3RR', 'Flight_Time_3_4RR',
#                   'Flight_Time_3_5RR', 'Flight_Time_3_6RR', 'Flight_Time_3_7RR', 'Flight_Time_3_8RR',
#                   'Flight_Time_3_9RR', 'Flight_Time_4_0RR', 'Flight_Time_4_1RR', 'Flight_Time_4_2RR',
#                   'Flight_Time_4_3RR', 'Flight_Time_4_4RR', 'Flight_Time_4_5RR', 'Flight_Time_4_6RR',
#                   'Flight_Time_4_7RR', 'Flight_Time_4_8RR', 'Flight_Time_4_9RR', 'Flight_Time_5_0RR',
#                   'Flight_Time_5_1RR', 'Flight_Time_5_2RR', 'Flight_Time_5_3RR', 'Flight_Time_5_4RR',
#                   'Flight_Time_5_5RR', 'Flight_Time_5_6RR', 'Flight_Time_5_7RR', 'Flight_Time_5_8RR',
#                   'Flight_Time_5_9RR', 'Flight_Time_6_0RR', 'Flight_Time_6_1RR', 'Flight_Time_6_2RR',
#                   'Flight_Time_6_3RR', 'Flight_Time_6_4RR', 'Flight_Time_6_5RR', 'Flight_Time_6_6RR',
#                   'Flight_Time_6_7RR', 'Flight_Time_6_8RR', 'Flight_Time_6_9RR', 'Flight_Time_7_0RR',
#                   'Flight_Time_7_1RR', 'Flight_Time_7_2RR', 'Flight_Time_7_3RR', 'Flight_Time_7_4RR',
#                   'Flight_Time_7_5RR', 'Flight_Time_7_6RR', 'Flight_Time_7_7RR', 'Flight_Time_7_8RR',
#                   'Flight_Time_7_9RR', 'Flight_Time_8_0RR', 'Flight_Time_8_1RR', 'Flight_Time_8_2RR',
#                   'Flight_Time_8_3RR', 'Flight_Time_8_4RR', 'Flight_Time_8_5RR', 'Flight_Time_8_6RR',
#                   'Flight_Time_8_7RR', 'Flight_Time_8_8RR', 'Flight_Time_8_9RR', 'Flight_Time_9_0RR',
#                   'Flight_Time_9_1RR', 'Flight_Time_9_2RR', 'Flight_Time_9_3RR', 'Flight_Time_9_4RR',
#                   'Flight_Time_9_5RR', 'Flight_Time_9_6RR', 'Flight_Time_9_7RR', 'Flight_Time_9_8RR',
#                   'Flight_Time_9_9RR']
with open(filename, 'r') as file:
    reader = csv.reader(file)
    c = 0
    # for flag in flags:
    #     if flag:
    for row in reader:
        print(f"row {len(row)}")
        print(f"flags {len(flags)}")
        print(f"header {len(header)}")
        c_feature = 0
        c_mpinak_mesa = 0
        data = []

        if c == 0:
            c += 1
        else:
            index = 0
            data.append(row[0])
            for flag in flags:
                if flag:
                    data.append(row[index])
                index += 1
                # if c_feature < 21 or c_feature > 120:
                # if c_feature < 21 or (c_feature > 120 and c_feature < 221) or c_feature > 320:
                c_feature += 1

            print(len(data))
            # print(f"einai sunolika {c_mpinak_mesa}")
            with open(file_to_csv, 'a', newline="") as filee:
                csvwriter = csv.writer(filee)
                empty = is_csv_empty(file_to_csv)
                if empty:
                    csvwriter.writerow(header)
                    csvwriter.writerow(data)
                else:
                    csvwriter.writerow(data)
        # # print(data)
        # dh = pd.DataFrame(header)
          # dh.to_csv(file_to_csv, index=False)
        # df = pd.DataFrame(data)
        # df.to_csv(file_to_csv, index=False)
        c+=1
    # print(header)
    # print("--")
# # #
# # #
# # # print(len(header))
# # # print(len(data))
# # # from pandas import read_csv
# # # # ANOVA feature selection for numeric input and categorical output
# # # from sklearn.datasets import make_classification
# # # from sklearn.feature_selection import SelectKBest
# # # from sklearn.feature_selection import f_classif
# # # # generate dataset
# # # X, y = make_classification(n_samples=370, n_features=421, n_informative=2)
# # # # define feature selection
# # # fs = SelectKBest(score_func=f_classif, k=2)
# # # # apply feature selection
# # # X_selected = fs.fit_transform(X, y)
# # # print(X_selected.shape)
# # #
# #
# #
# # import pandas as pd
# # import csv
# # # filename="C:/kl_csv/test/features_age.csv"
# # # # load the dataset as a pandas DataFrame
# # # data = read_csv(filename, header=None)
# # # # retrieve numpy array
# # # dataset = data.values
# # #
# # # # split into input (X) and output (y) variables
# # # X = dataset[:, :-1]
# # # y = dataset[:,-1]
# #
# # from sklearn.datasets import make_classification
# # from sklearn.model_selection import train_test_split
# # from sklearn.feature_selection import RFECV
# # from sklearn.ensemble import RandomForestClassifier
# # import matplotlib.pyplot as plt
# #
# # # Generate synthetic dataset (replace with your own data)
# # X, y = make_classification(n_samples=370, n_features=421, n_classes=2, random_state=1)
# #
# # # Split dataset into training and testing sets
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# #
# # # Initialize a Random Forest classifier
# # rf_classifier = RandomForestClassifier(n_estimators=100, random_state=1)
# #
# # # Initialize RFECV with Random Forest classifier and 5-fold cross-validation
# # rfecv = RFECV(estimator=rf_classifier, step=1, cv=5, scoring='accuracy')
# #
# # # Fit RFECV to training data
# # rfecv.fit(X_train, y_train)
# #
# # # Plot number of features vs. cross-validation scores
# # plt.figure()
# # plt.xlabel("Number of features selected")
# # plt.ylabel("Cross validation score (accuracy)")
# # plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
# # plt.show()
# #
# # # Get selected features
# # selected_features = rfecv.support_
# #
# # # Print selected features
# # print("Selected Features:")
# # for i, feature in enumerate(selected_features):
# #     if feature:
# #         print(f"Feature {i+1}: Selected")
# #     else:
# #         print(f"Feature {i+1}: Not Selected")
#
#
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.feature_selection import SelectFromModel
#
# # Generate synthetic dataset (replace with your own data)
# X, y = make_classification(n_samples=370, n_features=321, n_classes=2, random_state=42)
#
# # Split dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Initialize Random Forest classifier
# rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
#
# # Fit Random Forest classifier to training data
# rf_classifier.fit(X_train, y_train)
#
# # Initialize feature selector using Random Forest classifier
# feature_selector = SelectFromModel(rf_classifier)
#
# # Fit feature selector to training data
# feature_selector.fit(X_train, y_train)
#
# # Transform training and testing data to select features
# X_train_selected = feature_selector.transform(X_train)
# X_test_selected = feature_selector.transform(X_test)
#
# # Print selected feature indices
# selected_feature_indices = feature_selector.get_support(indices=True)
# print("Selected Feature Indices:", selected_feature_indices)
#
# # Train Random Forest classifier on selected features
# rf_classifier_selected = RandomForestClassifier(n_estimators=100, random_state=42)
# rf_classifier_selected.fit(X_train_selected, y_train)
#
# # Evaluate model performance on test data
# accuracy = rf_classifier_selected.score(X_test_selected, y_test)
# print("Accuracy on Test Data with Selected Features:", accuracy)
