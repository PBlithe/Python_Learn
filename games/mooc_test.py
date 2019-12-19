import datetime
import random
import sys


def guide_page(guide_word):
    starts = '********************'
    print('{0}{1}{0}'.format(starts,guide_word))


#判断指定的值是否为数字
def all_num(n):
    return n.isdigit()


'''判定指定序列中的数值是否相等以及记录数字区间起始位置的值是否大于记录数字区间终止位置的值
设置列表类型的参数用于接收指定的序列'''
def num_legal(ls):
    if ls[0] == ls[1]:
        print('您输入区间数字相同!!请重新启动程序')
        sys.exit()
    elif ls[0] > ls[1]:
        print('您输入的数字区间大小有误!!请重新启动程序')
        sys.exit()
    else:
        return 1


#根据参数值，产生一个位于参数值区间以内的随机数
def set_final_num(num1,num2):
    l =[num1,num2]
    if list(filter(all_num,l)) == l:
        if num_legal(l) == 1:
            print('所产生的随机数字区间为:',l)
            num1 = int(num1)
            num2 = int(num2)
            return random.randint(num1,num2)

    else:
        print('您所输入的为非数字字符,请重新启动!')
        sys.exit()


#判定所输入的数值是否在指定的区间
def check_num_legal(num):
    if int(i)>num or int(j) < num:
        return True
    return False


#玩家每一次猜测数字和本次猜测次数两项信息写入日志文件
def write_record(times,value):
    with open('record.txt','a+',encoding='utf-8') as f:
        date = datetime.datetime.now()
        f.write(date.strftime('%Y-%m-%d %H:%M:%S.%f'))
        f.write(':')
        f.write('第{}次您猜测的数字为:{}\n'.format(times,value))


#依据所产生的随机数字(rand1)，提示玩家输入猜测数字并进行比对直到猜测到正确数字
def main(rand1):
    temp = rand1
    count = 0
    while True:
        guess_num = int(input('请继续输入您猜测的数字:'))
        if check_num_legal(guess_num):
            print('对不起您输入的数字未在指定区间')
            continue
        count += 1
        write_record(count,guess_num)
        if guess_num == rand1:
            print('**********************')
            print('恭喜您！只用了{}次就赢得了游戏'.format(count))
            break;
        elif guess_num<rand1:
            print('**********************')
            print('Lower than the answer')
        else :
            print('**********************')
            print('Higher than the answer')


if __name__ == '__main__':
    guide_word = '欢迎进入数字猜猜猜小游戏'
    guide_page(guide_word)
    i = input('数字区间起始值:')
    j = input('数字区间起始值:')
    rand_num = set_final_num(i,j)
    main(rand_num)