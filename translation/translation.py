import json
import requests
from translate import Translator

def client_choose(num, input_word):
    if num == 1:
        src, tgt = custom_translate(input_word)
    elif num == 2:
        src, tgt = YD_translate(input_word)
    elif num == 3:
        print("test_ok")
    else:
        print("请输入正确的数字")
        return
    print(src)  # 输入的数据
    print(tgt)  # 翻译的结果

def YD_get_response(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    try:
        response = requests.post(url, data=key)
        # 判断服务器是否相应成功
        response.raise_for_status()
        # 然后相应的结果
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"有道词典调用失败: {e}")
        # 相应失败就返回空
        return None


def YD_translate(word):
    response = YD_get_response(word)
    if response:
        result = json.loads(response)
        # 使用解构赋值简化代码
        src, tgt = result['translateResult'][0][0].values()
        return src, tgt
    else:
        return word, None

    
def custom_translate(word):
    translator = Translator(from_lang="chinese",to_lang="english")
    try:
        response = translator.translate(word)
        # 使用eval或者ast.literal_eval转换字符串为Python对象
        result = eval(response)
        # 使用解构赋值简化代码
        src, tgt = result['translateResult'][0][0].values()
        return src, tgt
    except Exception as e:
        print(f"自定义翻译模块调用失败: {e}")
        return word, None



if __name__ == '__main__':
    # 让用户输入一个数字来选择翻译方式
    num = int(input("请选择翻译方式：1.自定义翻译模块 2.有道词典API "))
    # 让用户输入一个单词或者句子
    word = input("请输入要翻译的内容：")
    # 调用client_choose函数
    client_choose(num, word)
