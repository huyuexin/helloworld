# 整个文件读取
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# 相对目录下  /
file_path = 'text_files/派.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
# 逐行读取
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
#with外读取 逐行读取
file_path='pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()

print(pi_string)

print(len(pi_string))
#打印前面几位  用于长数据
print(pi_string[:10]+'...')
change_pi=pi_string
#更换数据 替换replace
print(change_pi.replace('3','0'))