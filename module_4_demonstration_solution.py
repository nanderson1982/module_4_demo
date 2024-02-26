"""
Description: This program will provide salary increases of 20% to all 
executives at PiXELL-River Financial.  Prior to implementing this change, 
the program will see how many executives will end up with salaries greater than 
the high-salary mark.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
Usage: 
"""

import logging

data = []
new_data = []

HIGH_SALARY = 120000
RECOMMENDED_INCREASE = 0.20


#LECTURE SECTION 1
logging.basicConfig(level = logging.DEBUG, filename = 'app.log', filemode = 'w', 
                    format = '%(asctime)s - %(levelname)s - %(message)s')

try:
      file = open('module_4_data.txt')
      data = file.readlines()


except FileNotFoundError as e:
      # print("File does not exist", e)
      logging.exception("File does not exist.")
finally:
      if file is not None:
            file.close()
            #print("File Closed")
            logging.info("File Closed")


#LECTURE SECTION 2
try:
      if len(data) == 0:
            raise Exception("No data exists.")
      else:
            for record in data:
                  items = record.split(',')
                  title = items[0]
                  name = items[1]
                  salary = float(items[2])
                  
                  #LECTURE SECTION 3
                  if salary > HIGH_SALARY:
                        logging.warning(f"{name}'s salary {salary}, is currently above the recommended maximum of {HIGH_SALARY}.")
                  if salary * (1 + RECOMMENDED_INCREASE) > HIGH_SALARY:
                        logging.warning(f"{name}'s salary {salary}, will be above the recommended maximum {HIGH_SALARY}, with the planned {RECOMMENDED_INCREASE} increase.")
                  #REQUIREMENT:  NOTE RECORDS THAT EXCEED OR WILL EXCEED HIGH_SALARY AMOUNT
                  salary *= (1 + RECOMMENDED_INCREASE)
                  new_data.append([title,name,salary])
except Exception as e:
      #print(e)
      logging.exception("Exception processing data.")


#LECTURE SECTION 4
try:
      file = open('updated_salaries.txt', 'w')
      for record in new_data:
            row = ""
            for index, item in enumerate(record):
                  row += str(item)
                  if index < len(record) - 1:
                        row += (",")
            row += '\n'
            file.write(row)
except:
      # print("Exception writing data.")
      logging.exception("Exception writing data.")
finally:
      file.write("END OF FILE.")
      file.close()

#LECTURE SECTION 5
print("End of Program")
logging.debug('Debug level message.')
logging.info('Info level message.')
logging.warning('Warning level message.')
logging.error('Error level message.')
logging.critical('Critical level message.')

