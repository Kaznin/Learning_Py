number_of_phone_1 = '8-999-777-1111'
clear_number_of_phone_1 = number_of_phone_1.replace('-', '')
print(clear_number_of_phone_1.isdigit())

number_of_phone_2 = '+7 999 333 2222'
clear1_number_of_phone_2 = number_of_phone_2.replace('+', '')
clear2_number_of_phone_2 = clear1_number_of_phone_2.replace(' ', '')
print(clear2_number_of_phone_2.isdigit())

number_of_phone_3 = '+7 999-555-11-11'
clear1_number_of_phone_3 = number_of_phone_2.replace('+', '')
clear2_number_of_phone_3 = clear1_number_of_phone_3.replace(' ', '')
clear3_number_of_phone_3 = clear2_number_of_phone_3.replace('-', '')
print(clear3_number_of_phone_3.isdigit())