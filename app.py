from basic import file

fee = input('请输入费用:')
members = input('请输入成员,用逗号隔开:')
file.save_record(members.split(','),fee)
print(file.read_file('resources/record.txt'))
