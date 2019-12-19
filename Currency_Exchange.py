print('**********欢迎使用货币转换服务系统**********')
service_menu = {'1':'人名币转换美元',
                '2':'美元转换人名币','3':'人民币转换欧元',
                '0':'结束程序'} #字典变量存储操作信息
for k,v in service_menu.items():
    print(k,'.',v)
Your_Choice = input('请您选择需要的服务:')
while Your_Choice!='0':

    if Your_Choice == '1':
        print('~~~~~~~~~~~~~~~~~~~~')
        print('欢迎使用人名币转换美元服务')
        your_money = int(input('请输入您需要转换的人民币金额：'))
        print('您需要转换的人名币为：{}元'.format(your_money))
        RMB_to_US = your_money/6.72
        print('兑换成美元为：{:0.2f}$'.format(RMB_to_US))
    elif Your_Choice == '2':
        your_money = int(input('请输入您需要转换的美元金额：'))
        print('您需要转换的美元为：{}$'.format(your_money))
        US_to_RMB = your_money*6.72
        print('兑换成人名币为：{:0.2f}元'.format(US_to_RMB))
    elif Your_Choice == '3':
        your_money = int(input('请输入您需要转换的人民币金额：'))
        print('您需要转换的人民币为：{}元'.format(your_money))
        RMB_to_EUR = your_money*0.13
        print('兑换成欧元为：{:0.2f}欧元'.format(US_to_RMB))
    else:
        print('操作错误,请选择正确的操作指令.')
        Your_Choice = input('请您选择需要的服务:')
        continue
    print('====================')
    print('**********欢迎使用货币转换服务系统**********')
    for k, v in service_menu.items():
        print(k, '.', v)
    Your_Choice = input('请您选择需要的服务:')
print('感谢您的使用,祝您生活愉快,再见！')