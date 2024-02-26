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
data = []
new_data = []

HIGH_SALARY = 120000
RECOMMENDED_INCREASE = 0.20

 
#LECTURE SECTION 1
# Initialize File to None (null) outside of try so that it is accessible in try and finally blocks.

file = None

try:
      file = open('module_4_data.txt')
      data = file.readlines()  
      1/0

except FileNotFoundError as e:
      print("File does not exist", e)
except Exception as e:
      print("General exception", e)

finally:
      if file is not None:
            file.close()
            print("File closed.")

#LECTURE SECTION 2
try:
      if len(data)  == 0:
            raise Exception("No data exists.")
      for record in data:
            items = record.split(',')
            title = items[0]
            name = items[1]
            salary = float(items[2])
            
            #LECTURE SECTION 3
            #REQUIREMENT:  NOTE RECORDS THAT EXCEED OR WILL EXCEED HIGH_SALARY AMOUNT
            salary *= (1 - RECOMMENDED_INCREASE)
            new_data.append([title,name,salary])

except Exception as e:
      print(e)



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
      print("Exception writing data.")

finally:
      file.write("END OF FILE.")
      file.close()

#LECTURE SECTION 5
print("End of Program")

