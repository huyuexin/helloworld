#FileNotFoundError找不到文件错误
def count_words(filename):
    try:
        with open(filename) as fileobject:
            contents = fileobject.read()
    except FileNotFoundError:
        msg='sorry th file  '+filename+" dose no exist"
        print(msg)
    else:
        words=contents.split()
        num_words=len(words)
        print(filename +" has words is " + str(num_words))
filename = 'alice.txt'
count_words(filename)
filename1 = 'pi_digits.txt'
count_words(filename1)