# #if there is similar numbers in the list return true otherwise return false

# def problem1():
#     list_nums = [1 , 2 , 3 , 4 , 5 , 6 , 9 , 20 , 10 , 30, 40 , 0 , 8]
#     num2 = int()
#     for i in range(len(list_nums)):
#         num1 = list_nums[i]
#         num2 = num2 + 1
#         # print(num1)
    
#         for j in range( num2 , len(list_nums)):
#             if num1 == list_nums[j]:
#                 return True
#             if num1 != list_nums[j]:
                
#                 continue
#             else:
#                 return False
#             # print(list_nums[j])
              
# print(problem1())

#-----------------------------------------------------------------------------------------------------------------------------------------------

# if 2 strings have the same chracters despite the arrangment of charaacters is diffrent return true otherwise return false

# def problem2():
    
#     num3 = int()
#     print("enter 2 strings")
#     string1 = input()
#     string2 = input()

#     for i in range(len(string1)):
#         # print(string1[i])
#         num1 = string1[i]
    
#         for j in range(len(string2)):
#             # print(string2[j])
#             if string2[j] == num1:
#                 num3 = num3 + 1
#                 break
#             # if string2[j] < num1:
#             #     continue
            
#     if num3 >= len(string1):
#         return True
#     if num3 != len(string1):
#         return False
#     if len(string1) != len(string2):
#         return False
# print(problem2())
         
#-----------------------------------------------------------------------------------------------------------------------------------------------
# # return the sum of two values in a list which equel the target

# def problem3():
#     nums_list = [1 , 4 , 6 , 4]
#     target = 10
#     num1 = int()
#     num2 = int()
#     num_rotations = int()
    
#     for i in range(len(nums_list)):
#         num_rotations = num_rotations + 1
#         # print(nums_list[i])
#         num2 = nums_list[i]
        
#         for j in range(num_rotations , len(nums_list)):
#             print(nums_list[j])
#             if num2 + nums_list[j] == target:
#                 return num2 , nums_list[j]
#             # if num2 > nums_list[j]:
#             #     return num2
#             # else:
#             #     return nums_list[j]
            
        
    
    
# print(problem3())
 
#-----------------------------------------------------------------------------------------------------------------------------------------------    
        
# import os   
# string="bbc"
# string2="bba"





# for i in range(len(string)):

    
#     for j in range(len(string2)):
#         if string[i] == string[j]:
#             os.system('cls')
#             print("true")
#         if string[i] != string[j]:
#             os.system('cls')
#             print("false")

    

# def maximum(a , b):
#     if a > b:
#         return a
#     else : 
#         return b
    

# print(maximum(100 , 1000))
    






# def multiplication():
#     result = 1
#     list_num = [1 , 2 , 3, 4 ,6]
    
#     for i in range(len(list_num)):
#         result = result * list_num[i]
        
#     return result
    
# print(multiplication())
        


# def number_check_app(list_1):
#    num = int()
#    points = int()
#    num3 = int()
#    company_num = list_1[0 : 3]
#    company_name = str() 

#    for i in list_1:
#       num = num + 1
      
#    if num == 11:
#       points = points + 1
   
#    if list_1.isdigit() == True:
#       points = points + 1
   
#    if company_num == "010" or "011" or "015" or "012":
#       points = points + 1
#       if company_num == "010":
#          company_name = "vodafone"
#       if company_num == "011":
#          company_name == "etisalat"
#       if company_num == "012":
#          company_name == "orange"
#       if company_num == "015":
#          company_name == "we"
   
#    if points == 3:
#       print("this number is valid")
#       return company_name
#    else:
#       print("this number is invalid")
      
  
# print("enter your phone numebr")
# phone_number = input()  
# print(number_check_app(phone_number))

# import os
# from time import sleep


# list1 = []
# list2 = []
# list3 = []
# list4 = []
# num1 = float()
# num2 = float()
# num3 = float()
# num4 = float()
# num5 = float()
# num6 = float()
# num7 = float()


# print("enter number of courses")
# num_of_subjects = int(input())
# os.system('cls')

# for x in range(num_of_subjects):
#     print("enter your courses names")
#     subject1 = input()
#     list4.append(subject1)


# for i in range(num_of_subjects):
#     print("enter credit hours of the couerses")
#     num1 = int(input())
#     list1.append(num1)
#     # os.system('cls')

# print("your credit hours : ",list1)

# for j in range(num_of_subjects):
#     print("enter your grades for every course")
#     num2 = float(input())
#     list2.append(num2)
#     # os.system('cls')
    
# print("your grades for every credit hour = " , list2)

# #---------------------------------------------------------------------------------------

# for k in range(len(list1)):
#     num3 = list1[k]
#     num4 = list2[k]
#     num5 = num3 * num4
#     list3.append(num5)
    
# for l in range(len(list1)):
#     num6 = num6 + list3[l]
    
# for m in range(len(list1)):
#     num7 = num7 + list1[m]
    
# final_result = num6 / num7
# os.system('cls')

# print("courses : " , list4)
# print("your credit hours : ",list1)
# print("your grades for every credit hour = " , list2)
# print ("your gpa = ",final_result)
    

# print("fuck")
# number = str()
# number = input()
# num = number[0:3:1]
# if len(num) == 11 and num.isdigit():
#     print ('invalid number')
  
# else:

#     if num == "010":
#         print('VODAFON')

#     elif num == "011":
#         print('ETISALAT')

   
    
        


from student import car

car1 = car()

car1.color = "blue"
car1.make  = "china"
car1.model_num = 93648
car1.moving()

print(car1)


    


