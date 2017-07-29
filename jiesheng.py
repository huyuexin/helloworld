def jiecheng(num):
    if num==1:
        jieguo=1

    else:
        jieguo=num*jiecheng(num-1)
    return jieguo

use_input=eval(input("input some num qiu jiecheng"))
use_input_jiecheng=jiecheng(use_input)
print(use_input_jiecheng)


