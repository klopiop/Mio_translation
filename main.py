from translation import translation
from ocr import ocr # 待开发
import os

while True:
    print("---------\n1.自带翻译  2.有道云\n3.test\n---------")
    num = int(input())
    input_word = input("please input something:")
    src, tgt = translation.client_choose(num, input_word)
    # 判断翻译结果是否为None
    if tgt is None:
        # 如果是None，打印提示信息，并重新开始循环
        print("翻译失败，请重新选择翻译方式")
        continue
    else:
        # 如果不是None，打印翻译结果，并继续循环
        print(src) # 输入的数据
        print(tgt) # 翻译的结果
