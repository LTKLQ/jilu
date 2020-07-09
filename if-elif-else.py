num = int(input('please enter a number: '))
    #提醒用户输入一个数
if num % 2 == 0:
    print( '%d可以被2整除' % (num))
    # 数字可以被2整除
    
    if num % 5 == 0:
        print( '%d 可以同时被2和5整除' % (num))
        #可以同时被2和5整除
    elif num % 7 == 0:
        print( '%d 可以同时被2和7整除，但是不可以被5整除' % (num))

    elif num % 9 == 0:
        print( '%d 可以同时被2和9整除，但是不可以被5和7整除' % (num))   
    else:
        print( '%d不可以被5,7,9整除' % (num))
        #不可以被5,7整除
elif num % 3 == 0:
    print('%d可以被3整除，但是不可以被2整除' % (num))

    if num % 5 == 0:
        print( '%d 可以同时被3和5整除' % (num))
        #可以同时被3和5整除
    elif num % 7 == 0:
        print( '%d 可以同时被2和7整除，但是不可以被5整除' % (num))

    elif num % 9 == 0:
        print( '%d 可以同时被3和9整除，但是不可以被5和7整除' % (num))   
    else:
        print( '%d不可以被5,7,9整除，只可以被3整除' % (num))
else:
    print( '%d不可以被2,3整除' % (num))