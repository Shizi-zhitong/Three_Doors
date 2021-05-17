# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 16:28
# @Author  : 狮子之瞳
# @FileName: Game_Chinese.py
# @Software: PyCharm
# @Mail    ：109991923@qq.com

'''--------------------嗨！直接右键单击-->选择"运行"就可以开始游戏啦！-------------------
   -----------如果遇到游戏问题，先参考"游戏说明.docx"，还是无法解决的话欢迎和我联系-----------
   -----------------------------------祝游戏愉快-----------------------------------'''

import time
explosion = 0
tank2 = False

# -1. 从"医院/尖叫"选择点开始 -2. 从"电梯/楼梯"选择点开始
def flash_back1():
    choice6 = input('请选择回溯点：\n -1. 从"医院/尖叫"选择点开始\n -2. 从"电梯/楼梯"选择点开始\n>')

    if '1' in choice6:
        hospital_scream()
    elif '2' in choice6:
        hospital()
    else:
        print('(也就是说，可以回到过去的时间点吧？)')
        time.sleep(1)
        print('(要回到哪个时间点呢？输入1或2就可以了吧)')
        time.sleep(1)
        flash_back1()


# -1. 从"医院/尖叫"选择点开始 -2. 从"网吧/装甲车"选择点开始
def flash_back2():
    choice4 = input('请选择回溯点：\n -1. 从"医院/尖叫"选择点开始\n -2. 从"网吧/装甲车"选择点开始\n>')

    if '1' in choice4:
        hospital_scream()
    elif '2' in choice4:
        netbar_tank()
    else:
        print('(也就是说，可以回到过去的时间点吧？)')
        time.sleep(1)
        print('(要回到哪个时间点呢？输入1或2就可以了吧)')
        time.sleep(1)
        flash_back2()


# -1. 从"医院/求助声"选择点开始 -2. 从"帮助/走开"选择点开始
def flash_back3():
    choice5 = input('请选择回溯点：\n -1. 从"医院/求助声"选择点开始\n -2. 从"帮助/走开"选择点开始\n>')

    if '1' in choice5:
        hospital_scream()
    elif '2' in choice5:
        scream()
    else:
        print('(也就是说，可以回到过去的时间点吧？)')
        time.sleep(1)
        print('(要回到哪个时间点呢？输入1或2就可以了吧)')
        time.sleep(1)
        flash_back3()


# 1. 从"医院/尖叫"选择点开始 -2. 从"敲门/推门"选择点开始
def flash_back4():
    choice4 = input('请选择回溯点：\n -1. 从"医院/尖叫"选择点开始\n -2. 从"敲门/推门"选择点开始\n>')

    if '1' in choice4:
        hospital_scream()
    elif '2' in choice4:
        knock_open()
    else:
        print('(也就是说，可以回到过去的时间点吧？)')
        time.sleep(1)
        print('(要回到哪个时间点呢？输入1或2就可以了吧)')
        flash_back4()
        time.sleep(1)


def tank_password():
    password9 = False
    i = 0
    while password9 == False and i <= 3:
        password10 = input('来试试看吧，你输入了密码：\n>')
        i += 1
        if password10 == '19285' or password10 == 'black sheep wall':
            password9 = True
            print('密码正确！自爆程序停止')
            basement1_3()
        elif password10 == 'there is no cow level':
            password9 = True
            cheating()
        else:
            print('好像不太对，再试试看吧')
    else:
        print('3分钟到了，你还是没有解出正确的密码')
        time.sleep(1.5)
        print('你决定直接下车')
        time.sleep(1)
        print('但是已经太迟了')
        time.sleep(1)
        print('达成结局 11：什么？这就是彩蛋？？'.center(80, '-'))

        flash_back2()


def cheating():
    print('这都被你发现了！？')
    time.sleep(1)
    print('看来我的游戏没有白做嘛')
    time.sleep(1)
    print('你就是为了这个来的吧？')
    input('>')
    time.sleep(1)
    print('来，给你吧：')
    time.sleep(1)
    print('达成真结局 10.1：there is no cow level'.center(80, '-'))
    time.sleep(1)
    print('达成真结局 10.2：隐藏成就达成'.center(80, '-'))
    time.sleep(1)
    print('达成真结局 10.3：白金奖杯取得'.center(80, '-'))
    time.sleep(1)
    print('达成真结局 10.4：全成就完成'.center(81, '-'))
    time.sleep(1)
    print('取得称号：硬核玩家'.center(82, '-'))
    time.sleep(1)
    print('\n感谢游玩！\n')
    time.sleep(1)
    exit(0)


def name_character():
    global name
    name = input('勇士啊，请告诉我你的名字吧：\n>')
    while bool(name) == False:
        print('你还没有告诉我你的名字呢！！！')
        name_character()


def career_choose():
    global career
    career = input(f'{name}，你心仪的职业是（请输入数字，不带标点符号）：\n>')
    if career == '1':
        career = '圣骑士'
        print('圣骑士？想不到你还挺传统的嘛！最近没什么人选圣骑士啦。不过圣骑士看起来挺能打的是不是？')
        time.sleep(2)
    elif career == '2':
        career = '巫师'
        print('巫师？唔...虽然这件事不该对玩家透漏，不过这个版本巫师被削弱得很厉害...开玩笑的')
        time.sleep(2)
    elif career == '3':
        career = '盗贼'
        print('盗贼？我就知道！我已经看穿你内心的邪恶念头啦！')
        time.sleep(1.5)
    elif career == '4':
        career = '高达驾驶员'
        print('恭喜你发现隐藏职业高达驾驶员！虽然游戏里并不保证配备高达，但是能驾驶高达毕竟是一项难能可贵的技能嘛！')
        time.sleep(2)
    else:
        print('我说了只有三个职业！你在想什么！再给你一次机会吧')
        time.sleep(1.5)
        career_choose()
    return career


def control_room_password2():
    password8 = input('你在主控室的密码面板上输入了：\n -1. power overwhelming\n -2. black sheep wall \n -3. there is no cow level')
    password8 = input('请输入数字，不带标点符号\n>')
    if password8 == '1':
        print('好像失败了....')
        time.sleep(1)
        print('(该死，星际争霸果然是个老游戏了)')
        time.sleep(1.5)
        print('再回忆一下吧...')
        time.sleep(1)
        control_room_password2()

    elif password8 == '2':
        print('密码正确！')
        time.sleep(1)
        print('(这个作弊码已经很久没用过了，充满了过去的回忆)')
        time.sleep(1.5)
        basement1_4()
    elif password8 == '3':
        print('你输入了这个无敌的作弊码')
        time.sleep(1)
        cheating()
    elif password8 == 'black sheep wall':
        print('你已经深谙此道，直接输入了作弊码')
        time.sleep(1.5)
        basement1_4()
    elif password8 == 'there is no cow level':
        print('你已经深谙此道，直接输入了终极作弊码')
        time.sleep(1.5)
        cheating()
    else:
        print('你输入了一串不知名的字符，尝试打开密码门')
        time.sleep(1.5)
        print('但是失败了！')
        time.sleep(1)
        print('再试一次吧...只要输入1、2或者3就可以了')
        time.sleep(1.5)
        control_room_password2()


def basement1_2():
    turn_off = input('要按下关闭按钮吗？\n1. 按下去吧\n2. 果然还是别按了\n>')
    time.sleep(1.5)
    if turn_off == '2':
        print('(莫名其妙的按钮按下去可能很危险，还是别去碰比较好)')
        time.sleep(1.5)
        print('这么想着，你离开了主控室')
        time.sleep(1.5)
        print('\n(接下来去哪里好呢...)')
        time.sleep(1.5)
        print('你在基地里漫无目的地游荡')
        input('>')
        time.sleep(1.5)
        print('(感觉越来越饿了...)')
        time.sleep(1.5)
        print('你的意识开始模糊，耳畔传来尖锐的耳鸣')
        time.sleep(1.5)
        print('(啊，食物的味道...)')
        input('>')
        time.sleep(1.5)
        print('你扑向了那个看起来有些熟悉的身影')
        time.sleep(1.5)
        print('达成结局 9：是我...杀了我...？'.center(80, '-'))
        time.sleep(1.5)
        print('正在回溯时间.....')
        input('>')
        time.sleep(1.5)
        print('一看你就没有看支线任务的内容吧？')
        time.sleep(1.5)
        print('待会儿记得去网吧看看吧')
        time.sleep(1.5)
        print('但是我们不需要从那么久远的地方重新开始...')
        time.sleep(1.5)
        print('你回到了"OFF"按钮前')
        basement1_2()
    elif turn_off == '1':
        print('也许按下按钮，关闭的通道会形成巨大的能量缺口，吞噬一切')
        time.sleep(1.5)
        print('但就算这样，也比这个崩坏的世界要好')
        time.sleep(1.5)
        print('你毅然决然地按下了按钮')
        input('>')
        time.sleep(1.5)
        print('身边的一切似乎开始逐渐消失了')
        time.sleep(1.5)
        print('耳边传来系统的声音：')
        time.sleep(1.5)
        print(f'"{name}，【门 1：循环的世界】任务完成"')
        input('>')
        time.sleep(1.5)
        print('达成真结局 10：时间旅行者'.center(80, '-'))
        time.sleep(1.5)
        print('感谢游玩！')
        exit(0)
    else:
        print('你在原地纠结了好一会儿...最终还是决定：')
        basement1_2()


def basement1_3():
    print('你成功解除了自爆程序')
    time.sleep(1)
    print('这时你才发现，前方不远处有一只长相抽象、好像蜥蜴、蛇与蟑螂融合体的生物"')
    time.sleep(2)
    print('它黄色的眼睛眯成了一条细缝，示威似的盯着你')
    input('>')
    time.sleep(1.5)
    print('拥有一辆装甲车的你丝毫不慌，准备直接把对面轰成碎片')
    time.sleep(1.5)
    print('这时你发现，这辆装甲车已经备有弹药了')
    input('>')
    time.sleep(1.5)
    print('(...........靠)')
    time.sleep(1)
    print('(不能就这样坐以待毙下去)，你想')
    time.sleep(1.5)
    print('稍加思索，你在控制台上输入了：')
    time.sleep(1.5)
    print('''[Capital 77777777]  04070000 005352A0 04A2CB71''')
    input('>')
    time.sleep(1)
    print('''[Player Inf HP]   04070000 00535300 A9017BFD''')
    input('>')
    time.sleep(1)
    print('''[Change EN Max]   04070000 00316740 2A0003E8''')
    input('>')
    time.sleep(1)
    print('''[Change MP Max]   04070000 003171F0 2A0003E8''')
    input('>')
    time.sleep(1)
    print('''[Check Pilot AP Max]   04070000 00228A30 B9001E69''')
    input('>')
    time.sleep(1)
    print('''[Pilot Upgrade 999]   04070000 0053528C 00009528''')
    input('>')
    time.sleep(1)
    print('你驾驶装甲车自信满满地炸死了面前的奇怪生物')
    time.sleep(1.5)
    print('(原来开金手指是这样的感觉啊)')
    input('>')
    time.sleep(1)
    print('装甲车上的导航系统显示出主控室的位置')
    time.sleep(1.5)
    print('看来主控室在地下，是一个类似防空洞之类的避难处')
    time.sleep(1.5)
    print('你下了车，往地下避难处走去')
    input('>')
    time.sleep(1)
    print('来到主控室面前，主控室的玻璃门紧闭，旁边有一个密码面板')
    time.sleep(1.5)
    print('\n(又是密码，去他妈的密码)')
    time.sleep(1)
    print('不过，你现在有了其他的想法')

    control_room_password2()


def basement1_4():
    print('你成功进入了主控室')
    time.sleep(1.5)
    print('主控室内，上百台各式各样的设备同时运转，发出"嗡嗡"的蜂鸣声')
    time.sleep(2)
    print('这里一尘不染，看起来没有遭到入侵')
    time.sleep(1.5)
    print('\n(废话...这么绕的密码提示，谁能解得开)')
    time.sleep(1.5)
    print('(也就只有像我这种...)')
    time.sleep(1.5)
    print('在无数个黑色机箱的映衬下，墙上的红色"OFF"按钮显得格外醒目')
    time.sleep(1)
    basement1_2()


def control_room_password():
    print('''以下10道单选题只有唯一解，请问10题的答案各是什么？
    Q1：第一个答案为B的問題是哪一个问题？
        (A)2　(B)3　(C)4　(D)5　(E)6

    Q2：唯一连续两个有相同答案的问题是：
        (A)2，3　(B)3，4　(C)4，5　(D)5，6　(E)6，7

    Q3：本问题的答案和哪一和问题的答案相同？
        (A)1　(B)2　(C)4　(D)7　(E)6

    Q4：答案是A的问题的个数是：
        (A)0　(B)1　(C)2　(D)3　(E)4

    Q5：本问题的答案和哪一个问题的答案相同？
        (A)10　(B)9　(C)8　(D)7　(E)6

    Q6：答案A的个数和答案什么的个数相同？
        (A)B　(B)C　 (C)D　(D)E　(E)以上皆非

    Q7：按字母順序，本问题的答案和下一个问题的答案相差几个字母？（A和B相差1）
        (A)4　(B)3　(C)2　(D)1　(E)0

    Q8：答案为母音字母的问题有几个？（母音字母：AE）
        (A)2　(B)3　(C)4　(D)5　(E)6

    Q9：答案为子音字母的个数为：（子音字母：BCD）
        (A)质数　(B)阶乘数　(C)平方数　(D)立方数　(E)5的倍数

    Q10：本问题的答案是：
        (A)A　(B)B　(C)C　(D)D　(E)E''')
    time.sleep(2)
    print('密码为10个大写字母，不带标点符号'.center(80, '-'))
    time.sleep(1.5)
    control_room_password = False
    if career == '盗贼':
        print('你想像前几次一样直接打开密码锁')
        time.sleep(1)
        print('可主控室的安全等级很高，你无法破解')
        time.sleep(1.5)
        print('没办法，只好尝试着解题了')
        time.sleep(1.5)
    while control_room_password == False:
        password6 = input('经过一番缜密的思考，你输入了：\n>')
        if password6 == 'CDEBEEDCBA' or password6 == 'black sheep wall':
            control_room_password = True
            print('密码正确！')
            time.sleep(1)
            basement1_4()
        elif password6 == 'there is no cow level':
            cheating()
        else:
            print('密码错误')
            time.sleep(1)
            print('我的答案不对吗？再好好想想吧')


def glass_door():
    password2 = False
    print('在密码面板旁边，你们看到了密码提示：')
    time.sleep(1)
    print('''一天晚上，赵先生和赵太太邀請钱先生、钱太太、孙先生、孙太太到家里吃饭，
             饭后他们一起打牌聊天。一聊之下，发现其中有一位最近中了彩券，乐不可支。

             从他们当晚的互动，已知以下內容：

                -中奖者的配偶在当晚打牌输了
                -赵先生有心脏疾病，不能剧烈运动
                -钱太太当晚和另一位太太聊得起敬，都沒有一起打牌
                -钱先生和孙太太当晚初次见面，才认识的
                -赵先生打牌贏了，赵太太却打输了
                -钱先生上周才和中奖者一起参加马拉松比赛
             请问，那位幸运的中奖者是谁？''')
    time.sleep(2)
    print('密码为3个中文字符'.center(80, '-'))
    time.sleep(1.5)
    print('\n(哪家科研机构会把密码提示贴在门边啊？？？？)')
    time.sleep(1.5)
    print('(你们活该被入侵好吧？？)\n')
    time.sleep(1.5)
    while password2 == False:
        if head == True:
            print('你突然想起了背包里的"死不瞑目的看门人头颅"')
            time.sleep(1.5)
            print('你将头颅靠近密码密码面板')
            time.sleep(1.5)
            print('"虹膜识别成功"')
            time.sleep(1)
            print('门开了')
            time.sleep(1)
            password2 = True
        elif career == '盗贼':
            print('(不过，我的职业是盗贼，应该对密码类很擅长吧？)')
            time.sleep(1.5)
            print(f'"系统提示：{name}使用主动技能"即使是中世纪的盗贼，也能开27世纪的密码锁"！')
            time.sleep(2)
            print('"系统提示：密码破解成功！"')
            time.sleep(1)
            print('\n(...等等，那个主动技能名字叫什么来着？？)\n')
            time.sleep(1.5)
            password2 = True
        else:
            print('还是思考一下吧...')
            time.sleep(1.5)
            password2 = input('几经思考，你输入了：\n>')
            time.sleep(1.5)
            if password2 == '钱太太' or password2 == 'black sheep wall':
                print('密码正确！\n门开了')
                time.sleep(1.5)
            elif password2 == 'there is no cow level':
                cheating()
            else:
                print('密码错误')
                time.sleep(1.5)


def giant_spider():
    global head
    head = False
    print('你们拔出了武器')
    time.sleep(1.5)
    if career == '圣骑士':
        print('你刚拔出圣剑，准备大战一场，耳边突然传来了系统提示：')
        time.sleep(1.5)
        print('系统提示：圣骑士从不欺凌弱小，哪怕是一只小小的蜘蛛')
        time.sleep(1.5)
        print('\n(合着职业设定就是用来干这事儿的？？？？？\n(你TM觉得这是一只小小的蜘蛛？？？))\n')
        time.sleep(2)
        print('但是无关紧要，高达驾驶员手中的武器显然非同小可，三两下就搞定了这只丑陋的生物')
        time.sleep(2)
    elif career == '巫师':
        print('（说起来，我是攻击型巫师还是辅助型巫师啊...）')
        time.sleep(1.5)
        print('但是无关紧要，高达驾驶员手中的武器显然非同小可，三两下就搞定了这只丑陋的生物')
        time.sleep(2)
        print('在蜘蛛腹部，你发现了未消化的人类头颅')
        input('>')
        time.sleep(1.5)
        print(f'系统提示：玩家{name}发现"死不瞑目的看门人头颅"')
        time.sleep(1.5)
        print('\n(怎么觉得有点慎得慌...)\n')
        time.sleep(1.5)
        head = True
    else:
        print(f'作为{career}，你没有直接攻击能力')
        time.sleep(1.5)
        print('但是无关紧要，高达驾驶员手中的武器显然非同小可，三两下就搞定了这只丑陋的生物')
        time.sleep(2)


def basement1():
    print('基地内部依然光亮整洁，看来没有遭到入侵')
    time.sleep(1.5)
    print('但深入基地不久，你们就看到了身穿白衣的工作人员的尸体')
    input('>')
    time.sleep(1.5)
    print('尸体看上去没有变异的现象，但皮肤奇怪地干瘪，身体毫无水分')
    time.sleep(2)
    print('走廊一路延伸，消失在黑暗的尽头...')
    input('>')
    time.sleep(1.5)
    print('继续往前，走廊里弥漫着血腥味')
    time.sleep(1.5)
    print('走廊尽头传来密集快速的响声，听着不像是丧尸，更不是人类的脚步声')
    time.sleep(2)
    print('一只覆盖棕黑色斑纹与绒毛的巨型蜘蛛冲来，八条近两米长的腿断了三条，面对你们，张开了巨大的口器')
    time.sleep(2)
    giant_spider()
    print('蜘蛛不再是威胁，你们成功地来到走廊尽头')
    time.sleep(1.5)
    print('走廊尽头的玻璃门紧闭着，上有代表机密出入通道的密码面板 ')
    input('>')
    time.sleep(1.5)
    glass_door()
    print('你们成功进入了1号电子通道基地的科研室')
    time.sleep(1.5)
    print('科研室的设备都还在正常运作')
    time.sleep(1.5)
    print('地上散落着四五具身穿白衣的科研人员尸体，身上布满了白色粘液')
    time.sleep(1.5)
    print('通风管道的滤门大开，看起来刚才的巨型蜘蛛可能是从那里进入了科研室，杀光了工作人员')
    time.sleep(2)
    print('不过既然已经解决掉它了，应该不会再有危险')
    input('>')
    time.sleep(1.5)
    print('你们走近了正在运行的电脑')
    time.sleep(1.5)
    print('电脑屏幕上显示着"电子通道1正常运行中"')
    time.sleep(1.5)
    print('桌上有许多文件，你正要看看能不能找到关于这个研究室的线索，上方的通风管道突然传来了轻快密集的脚步声')
    input('>')
    time.sleep(2)
    print('一条细长的舌头从管道口伸了出来，一把将你卷入了腹内')
    time.sleep(1.5)
    print('舌头主人的腹腔里又湿又热，你听到外界传来机枪扫射的声音')
    time.sleep(1.5)
    print('随后是一阵天旋地转，你不知被这怪物带去了哪里')
    input('>')
    time.sleep(1.5)
    print('枪声一路追随着你，你知道这是队友在尝试救你')
    time.sleep(1.5)
    print('但枪声听起来越来越远了，舌头的主人可能已经逃进了通风管道')
    input('>')
    time.sleep(1.5)
    print('皮肤传来灼烧感，胃酸开始腐蚀你的身体了')
    time.sleep(1.5)
    print('更要命的是，这里的氧气严重不足，你已经无法清醒地思考了...')
    time.sleep(1.5)
    if explosion == True:
        print('朦胧间，你听到了爆炸声')
        time.sleep(1.5)
        print('但由于没有直接遭受冲击，你并没有受严重的伤')
        time.sleep(2)
        print('反倒是把你吞下肚的怪物似乎一命呜呼了')
        input('>')
        time.sleep(2)
        print('你从令人作呕的腥臭胃液中爬了出来')
        time.sleep(2)
        print('在不远处，你看到了高达驾驶员的尸体')
        time.sleep(2)
        print('这里似乎发生了一场剧烈的爆炸，道路上满是砾石碎片，两旁的建筑燃烧着坍塌')
        input('>')
        time.sleep(2.5)
        print('待在这样的建筑旁边很危险，你循着破旧的逃生指示牌躲到了地下')
        time.sleep(2.5)
        print('地下似乎有个防空洞之类的避难处')
        time.sleep(1.5)
        input('>')
        print('往避难处深处走去，你见到了醒目的标识：')
        time.sleep(2)
        print('主控室')
        time.sleep(1)
        print('主控室的玻璃门紧闭，旁边有一个密码面板')
        time.sleep(1.5)
        print('\n(又是密码，去他妈的密码)')
        time.sleep(1.5)
        print('(主控室的密码提示总不会直接贴在这里吧？)')
        time.sleep(1.5)
        print('你四处看了看，果然在一旁的墙上看见了密码提示')
        time.sleep(1.5)
        print('\n(妈的，一群智障)')
        time.sleep(1.5)
        control_room_password()
    else:
        print('你的意识逐渐消散，朦胧间见到了一阵白光...')
        time.sleep(1.5)
        print('达成结局 8：那个求助声，果然还是应该去看一眼...'.center(80, '-'))
        time.sleep(1.5)
        print('正在回溯时间...')
        time.sleep(1.5)
        print('已回到时间点：医院/求助声')
        time.sleep(1.5)
        hospital_scream()

    print('但是墙壁上红色的关闭按钮很是醒目')
    time.sleep(1.5)
    basement1_2()


def netbar_password():
    password1 = False
    print('''请在下面句子中的空格处都填入正确的阿拉伯數字，使整句话成立：
『这句話中 0 出现了 ＿ 次，1 出现了 ＿ 次，
　        2 出现了 ＿ 次，3 出现了 ＿ 次，
　        4 出现了 ＿ 次，5 出现了 ＿ 次，
　        6 出现了 ＿ 次，7 出现了 ＿ 次，
　        8 出现了 ＿ 次，9 出现了 ＿ 次。』''')
    time.sleep(1.5)
    print('密码为不带空格、不带标点符号的连续阿拉伯数字'.center(80,'-'))
    time.sleep(1.5)
    print('\n(这里的网管是高考落榜的高斯吗？？？？)')
    time.sleep(1.5)
    print('(我就玩儿个游戏还要做题？？？？)')
    time.sleep(1.5)
    while password1 == False:
        if career == '盗贼':
            input('>')
            print('(不过，我的职业是盗贼，应该对密码类很擅长吧？)')
            time.sleep(1.5)
            print(f'"系统提示：{name}使用主动技能"即使是中世纪的盗贼，也能开27世纪的密码锁"！')
            time.sleep(2)
            print('"系统提示：密码破解成功！"')
            time.sleep(1)
            print('\n(...等等，那个主动技能名字叫什么来着？？)\n')
            time.sleep(1.5)
            password1 = True
        else:
            netbar_password = input('几经思索，你输入了密码\n>')
            if netbar_password == '1732111211' or netbar_password == 'black sheep wall':
                print('密码正确！')
                password1 = True
            elif netbar_password == 'there is no cow level':
                cheating()
            else:
                print('密码错误，再好好想想吧\n请重新输入：')


def tank2():
    if career == '高达驾驶员':
        print('你发现这辆装甲车已经启动了自爆程序，在不到三分钟内，几公里范围内的一切都会随之飞灰烟灭')
        time.sleep(2)
        print('但作为高达驾驶员的你，完全有能力停止这个装置')
        time.sleep(1.5)
        print('除非...')
        time.sleep(1)
        print('\n(靠，需要管理员密码才能终结自爆程序)')
        time.sleep(1.5)
        input('>')
        print('''屏幕上跳出了密码提醒：
        从阿拉伯数字 1 ~ 9 中选取不重复的五个数字，
        假设这五个数分別为：甲、乙、丙、丁、戊，
        且他們必须满足下列条件：

            -甲与戊的和小于丙加5
            -甲、丙与戊的和等于丁
            -甲与丁的和等于乙
            -丁能被丙整除
            -甲与丙的和小于戊
            -丁比6大
        请问甲乙丙丁戊各是多少呢？''')
        print('密码为5位阿拉伯数字'.center(80, '-'))
        time.sleep(1.5)
        print('\n(我对这个世界的居民奇怪的密码提醒方式已经习惯了...)')
        print('(不过还是有理由怀疑是在恶意延长游戏时间)')
        tank_password()

    else:
        print(f'作为{career}，你不知如何驾驶装甲车')
        time.sleep(1.5)
        print('你疑惑地按下几个按钮，屏幕上出现了提示：')
        time.sleep(1.5)
        print(' -自爆プログラムを開始してもよろしいですか?')
        input('>')
        time.sleep(1.5)
        print('看起来像是启动了自毁程序，你尝试取消它')
        time.sleep(1.5)
        print('尝试了几个按钮，提示仍然不变，你决定直接下车')
        time.sleep(1.5)
        print('但是已经太迟了')
        time.sleep(1)
        print('结局 4：如果还有来生，我也想开高达'.center(80,'-'))
        time.sleep(1.5)
        flash_back2()


def netbar():
    print('你和高达驾驶员一起向网吧出发，他手上的武器非常先进，你们有惊无险地到达了网吧')
    time.sleep(2)
    print('正准备使用电脑搜索一些有用信息，你们却发现电脑需要输入密码才能访问')
    time.sleep(1.5)
    print('在网吧里绕了一圈后，你们在网管的位置上发现了贴在桌上的密码提示')
    input('>')
    time.sleep(1.5)
    netbar_password()
    print('\n驾驶员略带敬意地看着你')
    time.sleep(1.5)
    print('你们用电脑看了看最近的新闻，搜索了和现在城市的惨状相关的信息')
    input('>')
    time.sleep(1.5)
    print('这个世界的现状远比你们想象的要复杂')
    time.sleep(1.5)
    print('26世纪后，太阳逐渐冷却，地球上所有能量的来源--太阳停止提供能量')
    time.sleep(1.5)
    print('为了寻找替代的能量，避免人类的消亡，科学家们绞尽脑汁，最终科学家哈兰姆无意发现了实验室中的钨-186会随时间转变成钚-186')
    time.sleep(2.5)
    print('钚-186的质子数与中子数不匹配，是一种地球上从未见过的元素')
    time.sleep(2)
    print('它所携带的电荷是+94，质量是186')
    input('>')
    time.sleep(1.5)
    print('在这样的情况下，原子核里面少了五十多个中子，钚-186是不可能存在的')
    time.sleep(2)
    print('既然它确实存在，而且在最初一段时间内是稳定存在的，那么这种物质就一定存在于某个地方，或某段时间，或自然法则作用不到的某种情况下')
    time.sleep(2.5)
    print('哈兰姆认为，钚-186既然在这个宇宙不可能存在，那一定来自于平行宇宙')
    time.sleep(1.5)
    print('这种物质到了人类的宇宙之后，仍然是稳定的，这是因为它自身仍维持着另一个宇宙的自然法则')
    input('>')
    time.sleep(2)
    print('哈兰姆提出，人类宇宙和钚-186存在的宇宙以此种方式实现了能量置换')
    time.sleep(1.5)
    print('通过能量置换，人类宇宙和平行宇宙都能够得到额外的能源')
    time.sleep(1.5)
    print('横跨"电子通道"就这样建立了起来，它能够连接两个平行宇宙，实现能量的交换')
    input('>')
    time.sleep(2)
    print('作为没有成本、没有污染的能源，钚-186很快被人类用作主要能源')
    time.sleep(1.5)
    print('目前，地球上存在着两个大型"电子通道"基地，不断为两个宇宙提供能源')
    time.sleep(1.5)
    print('然而，数十年内维持着平行宇宙的自然法则、保持稳定的钚-186突然出现了放射性')
    time.sleep(2)
    print('人类宇宙还没能做出反应，就被大范围出现的放射污染感染出现基因变异，变故之快让人始料未及')
    time.sleep(2.5)
    print('不止是人类，地球上所有接触过钚-186的生物都出现了变异的趋势')
    input('>')
    time.sleep(2)
    print('看了电子新闻上的描述，你和驾驶员沉默不语')
    time.sleep(1.5)
    print('你突然听到不远处传来雷鸣地动般的巨大动静，抬头一看，一辆巨型装甲车向网吧冲来')
    time.sleep(2)
    print('还来不及反应，网吧的一半建筑就成了废墟')
    time.sleep(1.5)
    if career == '高达驾驶员':
        print('米利亚尔特·匹斯克拉福特死在了你面前')
        input('>')
        time.sleep(1.5)
    else:
        print('还没来得及问他的名字，你就失去了唯一的队友')
        input('>')
        time.sleep(1.5)

    print('你惊魂未定地环视了四周，在远处发现了第二辆装甲车')
    time.sleep(1.5)
    print('(这个世界似乎还存在其他的幸存者)')
    time.sleep(1.5)
    print('(看起来装甲车比一般民用建筑牢固得多)')
    time.sleep(1.5)
    print('这么想着，你决定向第二辆装甲车出发')
    input('>')
    time.sleep(1.5)
    tank2()


def tank():
    print('无论怎么比，看起来都是装甲车更有吸引力啊...')
    time.sleep(1.5)
    print('你们决定向装甲车出发，驾驶员手上的武器非常先进，你们有惊无险地到达了车旁')
    time.sleep(2)
    print('看他轻车熟路地启动了装甲车，你悬着的心放了下来')
    input('>')
    time.sleep(1.5)
    print('"奇怪，这辆车已经设定好了前进的地点"，驾驶员看了看车载导航')
    time.sleep(1.5)
    print('目的地是一个叫"1号电子通道基地"的地方')
    time.sleep(1.5)
    print('反正对这个世界毫无头绪，你们决定直接前往这个目的地')
    time.sleep(1.5)
    print('驾驶员启动了装甲车')
    input('>')
    time.sleep(1)
    print('虽然道路笔直，但装甲车就像没长眼一样向着两旁的建筑撞去')
    time.sleep(1.5)
    print('\n(这个人真的是开高达的吗？？？？他的开车技术连我幼儿园的表妹都不如！)\n')
    input('>')
    time.sleep(2)
    print('"你长点心！我们撞塌的楼蝙蝠侠和钢铁侠加起来都赔不起！"')
    time.sleep(1.5)
    print('他讪笑了一下，"这玩意儿和开高达好像不是一回事儿啊"')
    time.sleep(1.5)
    print('沿途的建筑物几乎没有幸存，连刚才看到的网吧也成了一片废墟')
    time.sleep(1.5)
    print('你们磕磕绊绊地到达了"1号电子通道基地"')
    time.sleep(1.5)
    basement1()


def netbar_tank():
    choice5 = input('去网吧也许能获得一些关于这个时代的信息，但是装甲车和高达驾驶员一起出现的几率有多少呢？你决定：\n -1. 去网吧\n -2. 当然是去开车！！\n>')
    time.sleep(1.5)
    if '1' in choice5:
        netbar()
    elif '2' in choice5:
        tank()
    else:
        print('究竟应该去哪里呢...只要输入数字1或2就行了吧？')
        netbar_tank()


def hospital():
    print('想到现在自己可能并没有什么战斗能力，你决定先去医院')
    time.sleep(1.5)
    print('亮灯处在3楼，你决定：')
    choice2 = input(' -1. 坐电梯\n -2. 走楼梯\n>')
    time.sleep(1.5)
    if '1' in choice2:
        print('打开电梯门，三五个丧尸向你跑来，还来不及拔出武器你就被吞没了')
        time.sleep(1.5)
        print('达成结局 1：出师不利，出师不利'.center(80, '-'))
        time.sleep(1.5)
        flash_back1()

    elif '2' in choice2:
        print('你认为电梯过于危险，选择走楼梯，成功到达了3楼')
        time.sleep(1.5)
        print('来到了亮着灯的门前，你决定：')
        knock_open()
    else:
        print('你犹豫不决，被路过的丧尸潮吞没')
        time.sleep(1.5)
        print('达成结局 2：优柔寡断，要不得啊'.center(80, '-'))
        time.sleep(1.5)
        flash_back1()


def the_girl():
    global explosion
    explosion=1
    print('你上前，开始帮她移开摩托')
    time.sleep(1.5)
    print('摩托很重，你费劲了力气也只抬起来一点')
    time.sleep(1.5)
    print('正当你全力以赴的时候，后背突然传来枪管的触感')
    input('>')
    time.sleep(1.5)
    print('你举起了双手')
    time.sleep(1)
    print('"看看他包里有什么"')
    time.sleep(1.5)
    print('身后传来了背包被翻开的声音')
    time.sleep(1.5)
    print('"有一把样式很老的手枪...还有一个一脸丧气的观音像"')
    input('>')
    time.sleep(2)
    print('"搜他的身"')
    time.sleep(1)
    print('"老大，他身上除了一条品味很差的连裤袜，什么也没有"')
    time.sleep(2)
    print('\n(不是的，我没有，是系统强制给我装备的，我什么都不知道，你别瞎说)')
    input('>')
    time.sleep(2)
    print('背后传来了倒吸一口凉气的声音，"他是勇者"')
    time.sleep(1.5)
    print('"什么玩意儿？？"')
    time.sleep(1)
    print('"佛像，代表了勇者的信仰。勇者就是不畏艰险拯救万民于水火之中的人"，身后的人解释道')
    time.sleep(2.5)
    print('\n(行啊行啊，你要这么想也可以，快把枪放下)')
    input('>')
    time.sleep(1.5)
    print('"而连裤袜，代表勇者的品味"，身后的人严肃地说')
    time.sleep(2)
    print('"品味越独特，代表勇者装备越好，等级越高"')
    time.sleep(2)
    print('\n(我要怎么解释你们才能相信这双袜子真的不是我要穿的啊啊啊啊啊)')
    input('>')
    time.sleep(1.5)
    print('"多有冒犯，勇者大人"，枪抵在背上的触感消失了')
    time.sleep(2)
    print('你转过身，看到3个身穿黄色防护服的人')
    time.sleep(2)
    print('"您是来拯救这个世界的吧？"，为首的男人恭敬地问道')
    input('>')
    time.sleep(2)
    print('"我其实..."')
    time.sleep(1)
    print('"我就知道您是来拯救我们的！！"，男人激动地接话\n"快上车，我带您去目的地"')
    time.sleep(2)
    print('\n(等一下，就直接去打boss了吗？？我才1级啊！)')
    input('>')
    time.sleep(1.5)
    print('装甲车平稳地行驶在道路上')
    time.sleep(1.5)
    print('"我们这是要去哪里？"')
    time.sleep(1.5)
    print('"去一切的起点，万物的终结"')
    time.sleep(1.5)
    print('\n(...这个人的说辞和我看的几本太监小说的作者一样)')
    input('>')
    time.sleep(1.5)
    print('一路上听着三人的介绍，你大致明白了这个宇宙存在着能和其他宇宙交换物质的通道')
    time.sleep(2)
    print('通道为两个宇宙源源不断地提供0成本、0污染的能源')
    time.sleep(2)
    print('但是那个宇宙所传递过来的物质随时间退役逐渐出现了放射性')
    time.sleep(2)
    print('使得地球上绝大多数接触到放射污染的生物都产生了变异')
    input('>')
    time.sleep(2)
    print('装甲车停在了一幢巨大的白色基地前')
    time.sleep(1.5)
    print('三人的脸色都变了')
    time.sleep(1.5)
    print('基地的门不知被谁打开了，一只奇形怪状的巨型生物攀附在墙壁上')
    input('>')
    time.sleep(1.5)
    print('那生物有着蛇的闪着磷光的皮肤，壁虎的短小四肢，背上生着两只畸形的翅膀')
    time.sleep(1.5)
    print('它吐出的舌头分了岔，口中滴落出白色的粘液')
    input('>')
    time.sleep(1.5)
    print('"看来在放射污染的源头，生物的变异性状更彻底"')
    time.sleep(2)
    print('"那只奇怪的生物堵住了基地入口，我们必须先解决它"')
    time.sleep(2)
    print('坐在一辆装甲车内部的你并不怎么担心')
    input('>')
    time.sleep(1.5)
    print('"我们可以启动装甲车的自爆程序，直接送它上路"，男人斩钉截铁地说道')
    time.sleep(2)
    print('\n(你们这个宇宙都是这么用装甲车的？？？)')
    input('>')
    time.sleep(1.5)
    print('仿佛看穿了你的疑虑，男人苦笑了一下')
    time.sleep(1.5)
    print('"这辆车的弹药早就耗尽了，只能防御不能攻击，而且行驶速度也很慢"')
    time.sleep(2)
    print('"自爆程序定时在5分钟后，我们先躲到那边的掩体后面去"')
    input('>')
    time.sleep(2)
    print('"等一下，如果我们把基地也炸塌了怎么办？"')
    time.sleep(2)
    print('"不要紧，基地的主控室在地下，是专门设计的避难处。不会有事的"')
    time.sleep(2.5)
    print('你们躲到远处，待到爆炸平息后准备进入地下主控室')
    input('>')
    time.sleep(2)
    print('来到入口处，前方的空气中传来一股腥臭味')
    time.sleep(2)
    print('一个人影摇摇晃晃地向你们走来')
    time.sleep(2)
    print('\n(好像有幸存者？)')
    input('>')
    time.sleep(1.5)
    print('人影突然速度极快地朝你冲来，你感到喉咙一阵剧痛...')
    time.sleep(2)
    print('达成结局 12：是谁...杀了我？'.center(80, '-'))
    time.sleep(1.5)
    flash_back3()


def scream():
    print('虽然自己的战斗力大概也不高，但你还是无法对求救声视而不见')
    time.sleep(2)
    print('走近声音源头，你远远地看到一个十二三岁的女孩儿被压在一辆摩托车下')
    input('>')
    time.sleep(2)
    print('"拜托...请帮帮我..."，以她的力量，怎么也推不开压在身上的摩托')
    time.sleep(2)
    print('"我在超市里找到了一些食物，本想把它们运回去的..."，女孩儿说道')
    time.sleep(2)
    print('"但是我不是很会骑摩托..."')
    input('>')
    time.sleep(1.5)
    print('你又走近了些，这个女孩儿看起来对你不是威胁')
    time.sleep(2)
    print('"你是一个人吗？我可以分一些食物给你。拜托，请帮帮我..."')
    time.sleep(2)
    scream_help = input('你决定：\n1. 对她施以援手 \n2. 还是走开吧\n>')
    if scream_help == '1':
        print('怎么看都觉得只是一个遇到困难的女孩儿而已，你实在不忍心走开')
        time.sleep(2)
        the_girl()
    else:
        if career == '圣骑士':
            print('在丧尸围城的危险境况下，一个女孩儿独自行动，看起来太过可疑')
            time.sleep(2)
            print('(还是不要随便相信别人的好)，你想')
            time.sleep(1.5)
            print('耳边突然传来系统提示声："圣骑士从不见死不救，即使对方看起来非常可疑也一样！"')
            time.sleep(2)
            print('\n(这个游戏是不是对职业有什么误解？？？？)')
            time.sleep(1.5)
            print('(系统刚刚不是也承认她看起来非常可疑了吗？？？)\n')
            input('>')
            time.sleep(1.5)
            print('但你的身体还是不受控制地行动了起来')
            time.sleep(1.5)
            the_girl()
        else:
            print('在丧尸围城的危险境况下，一个女孩儿独自行动，看起来太过可疑')
            time.sleep(1.5)
            print('(还是不要随便相信别人的好)，你想')
            time.sleep(1.5)
            print('于是，你转身向医院走去')
            hospital()


def hospital_scream():
    print('\n你看到不远处有一个医院亮着灯光，正要朝那儿走去，又听到了不远处有女性的求助声')
    time.sleep(2)
    choice1 = input('你决定先去：\n -1. 亮着灯的医院\n -2. 求助声源头\n>')
    time.sleep(1)
    if choice1 == '1':
        hospital()
    elif choice1 == '2':
        scream()
    else:
        print('啊...完全没有理解你选了什么，再试一次吧！直接输入1或2就可以啦')
        hospital_scream()


def knock_open():
    choice3 = input(' -1. 敲门\n -2. 推门而入\n>')
    if '1' in choice3:
        print('你敲了敲门，里面传来声音：')
        time.sleep(1.5)
        print('"天王盖地虎"')
        time.sleep(1.5)
        choice7 = input('你想了想，回答道：\n -1. 宝塔镇河妖\n -2. 你是二百五\n>')
        if '1' in choice7:
            print('门开了')
            time.sleep(1)
            print('门内是一个身材魁梧的男人，手握一把看起来像是100世纪以后才会出现的奇怪武器')
            time.sleep(2)
            print('\n（还好提前敲了门，否则一定会死得很奇怪吧？）')
            input('>')
        elif '2' in choice7:
            print('门开了')
            time.sleep(1)
            print('门内是一个身材魁梧的男人，手握一把看起来像是100世纪以后才会出现的奇怪武器')
            time.sleep(2)
            print('\n（还好提前敲了门，否则一定会死得很奇怪吧？）')
            time.sleep(1.5)
            print('"现在的年轻人真没礼貌...."')
            input('>')
        else:
            print('虽然你说了一串不知名的文字，门还是开了')
            time.sleep(1.5)
            print('门内是一个身材魁梧的男人，手握一把看起来像是100世纪以后才会出现的奇怪武器')
            time.sleep(2)
            print('\n（还好提前敲了门，否则一定会死得很奇怪吧？）')
            time.sleep(1.5)
            print('"你就不能老老实实回我一句\'宝塔镇河妖\'吗？？"')
            time.sleep(1.5)
            print('\n(这么低级的暗号你还有脸说....)')
            input('>')

        print('男人扫了你一眼，"第几次任务了？"')
        time.sleep(1.5)
        print('你惊讶道："你也是玩家？你是怎么识破我的身份的？"')
        time.sleep(1.5)
        print('"你装备着新手礼包里的连裤袜..."')
        time.sleep(1.5)
        print('\n(合着新手礼包就这点用处？？)')
        input('>')
        time.sleep(1.5)

        if career == '高达驾驶员':
            print('"至少分清了敌我"，男人向窗外看去，"你选了什么职业？"')
            time.sleep(1.5)
            print(f'{career}，你呢？')
            time.sleep(1.5)
            print('男人看起来表情十分郁闷，"嗨呀，这不是巧了嘛..."')
            time.sleep(1.5)
            print('"我有预感我们俩之间一定会死一个"')
            time.sleep(1.5)
            print('(希望死的是自立Flag的那个...)')
            input('>')
            time.sleep(1.5)
            print('你跟着他来到窗边："驾驶员同志2号，你看起来比我有经验，知道接下来应该干什么吗？"')
            time.sleep(1.5)
            print('"什么2号2号的，我叫米利亚尔特·匹斯克拉福特"')
            time.sleep(1.5)
            print('(........................我就叫你驾驶员好了)')
        else:
            print('"至少分清了敌我"，男人向窗外看去，"你选了什么职业？"')
            time.sleep(1.5)
            print(f'{career}，你呢？')
            time.sleep(1.5)
            print('"我？我是一名高达驾驶员"')
            time.sleep(1.5)
            print('\n(凭什么他的职业这么先进？？？这是充了多少钱？？？我玩的腾讯游戏吗？？？)\n')
            input('>')
            time.sleep(1.5)
            print('你跟着他来到窗边："驾驶员同志，你看起来比我有经验，知道接下来应该干什么吗？"')
            time.sleep(2)

        print('"我在这里观察老半天了，目前为止就你一个活人，情况很不乐观"')
        time.sleep(1.5)
        print('"这次任务很奇怪，系统没有给任何背景介绍，所以我想去东边那个网吧看看，能不能获得一些有用的线索"')
        input('>')
        time.sleep(2)
        print('"不过，旁边那辆装甲车看起来很能打的样子..."')
        time.sleep(1.5)
        print('你随着他的目光看去，西边不远处有一辆大小媲美变形金刚的装甲车')
        time.sleep(1.5)
        netbar_tank()
    else:
        print('你被门后埋伏的枪手一枪击毙')
        time.sleep(1.5)
        print('达成结局 3：别开枪！我是好人！'.center(80,'-'))
        time.sleep(1.5)
        flash_back4()


def door1():
    print('\n')
    print('-' * 80)
    time.sleep(1.5)
    print(f'正在进入门 3'.center(77, '-'))
    time.sleep(2)
    print(f'不好意思打错了，正在进入门 1'.center(72, '-'))
    time.sleep(2)
    print('-' * 80)
    time.sleep(1)
    print('\n')
    print('这是你的第一个任务，因此你想从最简单的开始')
    time.sleep(1.5)
    print('在门 1后，你看到了一片城市的废墟。倒塌的大楼和废弃的汽车随处可见')
    time.sleep(2)
    print('机械残骸与废弃的零件堆积成了一座高山，散发着机油与腐败的恶臭')
    input('>')
    time.sleep(1)
    print(f'(真的吗？最简单的任务就是末日求生？我的职业还是{career}？？？)"')
    time.sleep(1.5)
    hospital_scream()


def door_choose():
    door = input(f'{name}，你选择进入哪一扇门？（请输入数字，不带标点符号）：\n>')
    time.sleep(1.5)

    if '1' in door:
        door1()
    elif '2' in door:
        print('尽管门 2上有故障中的牌子，你还是义无反顾地走了进去')
        time.sleep(1.5)
        print('(勇者，生而无惧)')
        input('>')
        time.sleep(1.5)
        print('你被一片无边无际的黑暗吞没了')
        time.sleep(1.5)
        print('达成结局 6：勇者，死而无憾'.center(80, '-'))
        time.sleep(1.5)
        print('"正在回溯时间..."')
        time.sleep(1.5)
        print('随着一阵白光，你回到了3扇门前')
        time.sleep(1.5)
        print(f'这次好好看看标识吧！{career}{name}！')
        door_choose()
    elif '3' in door:
        print('尽管门 3上有故障中的牌子，你还是义无反顾地走了进去')
        time.sleep(1.5)
        print('(世上本没有路，走的人多了就成了路)')
        input('>')
        time.sleep(1.5)
        print('你被一片无边无际的黑暗吞没了')
        time.sleep(1.5)
        print('达成结局 7：总有几个**不看标识...'.center(80, '-'))
        time.sleep(1.5)
        print('"正在回溯时间..."')
        time.sleep(1.5)
        print('随着一阵白光，你回到了3扇门前')
        time.sleep(1.5)
        print(f'这次好好看看标识吧！{career}{name}！')
        door_choose()
    else:
        print('真的只有3扇门，别四处看啦')
        door_choose()


'''---------------------------------------------The Game-------------------------------------------------'''
# set your name
print('嘿！你是第一位玩这个游戏的玩家！！')
time.sleep(1.5)
print('作为第一位玩家，让我送你点什么吧！')
time.sleep(1.5)
input('请按回车键\n>')
time.sleep(1.5)
print('你获得了：\n -中世纪的连裤袜\n -子弹停产了346年的枪\n -一尊特朗普观音像')
time.sleep(2)
print('\n嗨，我知道它们看起来没什么用')
time.sleep(1.5)
print('事实上，它们确实毫无卵用')
time.sleep(1.5)
print('但是呢，新手礼包，说白了就是一些没用的装饰品，你也知道的吧？')
time.sleep(3)
print('\n好啦好啦，作为一名合格的游戏NPC，我还是得在你卸载游戏之前引导你的')
input('>')
time.sleep(2)
name_character()
print(f"哈！所以'{name}'是你的名字啊!")
time.sleep(1.5)
print('你比我想象得有品味一点嘛')
time.sleep(1.5)
print('当然没有我那么有品位就是了')
input('>')
time.sleep(1.5)

# set your career
print('\n那我们现在开始选职业啦')
time.sleep(1.5)
print(' -1. 圣骑士：骑士教条的守护者，圣骑士绝不做有辱斯文之事。不过这样的操守真的有意义吗？')
time.sleep(3)
print(' -2. 巫师：魔法之主，巫师能用魔法做你能想到的所有事。科学发现他们并不遵守能量守恒定律')
time.sleep(3)
print(' -3. 盗贼：撬锁大师，盗贼绝不放过宝箱！即使宝箱里的道具都是一堆破烂！')
time.sleep(3)
career_choose()

input('那我们就正式开始啦！\n>')

# game starts
print('\n')
print('-'*80)
time.sleep(1.5)
print(f'正在随机生成世界'.center(75,'-'))
time.sleep(1.5)
print('-'*80)
print('\n')

# choose doors
print('你在一间空屋中醒来')
time.sleep(1.5)
print('耳边突然传来了女性的声音：')
time.sleep(1.5)
print('"你好，53847269号参与者。我是系统"，女声说道')
time.sleep(1.5)
print('(什么鬼，我不是一号玩家吗?)')
input('>')
time.sleep(1.5)
print('\n你看了看四周，却找不到声音的来源')
time.sleep(1.5)
print(f'"53847269号玩家现状：\n -姓名：{name}\n -等级：1"')
time.sleep(2)
print('"当玩家成功完成3个任务，即可脱离系统，回到原来的世界"')
time.sleep(2)
print('\n(所以我进入这个世界就是为了出去吗？)')
time.sleep(1.5)
print('"\n每当玩家成功完成一个任务，即可获得相应经验值。经验值随任务难度变化"')
time.sleep(2)
print(f'现在，{name}，你可以开始选择第一个任务了')
input('>')
time.sleep(1.5)
print('\n在空屋的墙上，你看到三扇门：')
time.sleep(1.5)
print(' -门 1：连老奶奶都能通关')
time.sleep(1.5)
print(' -门 2：可能要流一点点血 (故障中，请勿使用)')
time.sleep(1.5)
print(' -门 3：死而无憾！(故障中，请勿使用)')
time.sleep(1.5)
print('\n(你们的物业质量有点差啊...3扇坏了2扇)')
time.sleep(2)
door_choose()


