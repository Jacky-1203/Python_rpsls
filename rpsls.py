# coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ������
���ڣ�2021/5/31
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��

    if name == "ʯͷ":
        return 0
    elif name == "ʷ����":
        return 1
    elif name == "��":
        return 2
    elif name == "����":
        return 3
    elif name == "����":
        return 4
    else:
        return -1


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

    if number == 0:
        return "ʯͷ"
    elif number == 1:
        return "ʷ����"
    elif number == 2:
        return "��"
    elif number == 3:
        return "����"
    elif number == 4:
        return "����"


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """

    # ���"-------- "���зָ�
    print("----------------")
    print(f"����ѡ��Ϊ:  {player_choice}")
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    player_number = name_to_number(player_choice)
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
    computer_number = random.randrange(0, 5, 1)
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
    computer_name = number_to_name(computer_number)
    # ����Ļ����ʾ�����ѡ����������
    print(f"�������ѡ��Ϊ�� {computer_name}")
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    if player_number == 0:
        if computer_number == 0:
            print("���ͼ��������һ����")
        elif computer_number == 1:
            print("�����Ӯ��")
        elif computer_number == 2:
            print("�����Ӯ��")
        elif computer_number == 3:
            print("��Ӯ��")
        elif computer_number == 4:
            print("��Ӯ��")
    elif player_number == 1:
        if computer_number == 0:
            print("��Ӯ��")
        elif computer_number == 1:
            print("���ͼ��������һ����")
        elif computer_number == 2:
            print("�����Ӯ��")
        elif computer_number == 3:
            print("�����Ӯ��")
        elif computer_number == 4:
            print("��Ӯ��")
    elif player_number == 2:
        if computer_number == 0:
            print("��Ӯ��")
        elif computer_number == 1:
            print("��Ӯ��")
        elif computer_number == 2:
            print("���ͼ��������һ����")
        elif computer_number == 3:
            print("�����Ӯ��")
        elif computer_number == 4:
            print("�����Ӯ��")
    elif player_number == 3:
        if computer_number == 0:
            print("�����Ӯ��")
        elif computer_number == 1:
            print("��Ӯ��")
        elif computer_number == 2:
            print("��Ӯ��")
        elif computer_number == 3:
            print("���ͼ��������һ����")
        elif computer_number == 4:
            print("�����Ӯ��")
    elif player_number == 4:
        if computer_number == 0:
            print("�����Ӯ��")
        elif computer_number == 1:
            print("�����Ӯ��")
        elif computer_number == 2:
            print("��Ӯ��")
        elif computer_number == 3:
            print("��Ӯ��")
        elif computer_number == 4:
            print("���ͼ��������һ����")
    else:
        print("Error. No Correct Name")
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name = input()
rpsls(choice_name)
