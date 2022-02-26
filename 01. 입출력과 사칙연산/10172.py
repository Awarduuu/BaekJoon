# String formatting
# 둘째 줄에 }가 있어서 불가능
# slash = "\\"
# print('|\_/| \n|q p|   /} \n( 0 )"""\ \n|"^"`    | \n||_/={}__|'.format(slash))

# f-string
# 둘째 줄에 }가 있어서 불가능
# slash = "\\"
# print(f'|\_/| \n|q p|   /} \n( 0 )"""\ \n|"^"`    | \n||_/={slash}__|')


# % formatting
slash = "\\"
slash_2 = "\\"
print('|\_/| \n|q p|   /} \n( 0 )"""\ \n|"^"`    | \n||_/=%s%s__|' % (slash,slash_2))
