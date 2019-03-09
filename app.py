# # string operations
# course = 'python for beginners'
#
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.find('f'))
# print('f' in course)
# print(course[:4])
# custom_message = f'You are Enrolled in {course}'
# print(custom_message)
# # copying a complete string
#
# new_message = custom_message[:]
# print(f'Copied String: {new_message}')
#
# prices = [10, 20, 30]
# total_price = 0
# for price in prices:
#     total_price += price
# print(total_price)


numbers = [2, 2, 2, 8]

for x in numbers:
    out = ''
    for y in range(x):
        out += 'x'
    print(out)
