# -*- coding = utf-8 -*-
def phone():
    phonenumber = input("请输入手机号（11位数）：")
    while len(phonenumber) != 11:
        print("输入错误，请重新输入")
        phonenumber = input("请输入手机号（11位数）：")
    else:
        print(f"您输入的手机号码是:{phonenumber}")

phone()