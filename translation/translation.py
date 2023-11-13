import json
import requests
from utils.AuthV3Util import addAuthParams
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
    # 您的应用ID
    APP_KEY = '5b9a0121c84b8c41'
    # 您的应用密钥
    APP_SECRET = 'P3kqiHRkNzabQHrJhUsL5l9U9B9QNv8v'
    '''
    note: 将下列变量替换为需要请求的参数
    '''
    q = word
    lang_from = 'auto'
    lang_to = 'auto'
    vocab_id = 'None'

    data = {'q': q, 'from': lang_from, 'to': lang_to, 'vocabId': vocab_id}

    addAuthParams(APP_KEY, APP_SECRET, data)

    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    res = doCall('https://openapi.youdao.com/api', header, data, 'post')
    return res

def doCall(url, header, params, method):
    if method == 'get':
        return requests.get(url, params)
    elif method == 'post':
        return requests.post(url, params, headers=header)

# 有道翻译调用函数
def YD_translate(word):
    response = YD_get_response(word)
    translation = response.json().get('translation', [])
    if translation:
        print(translation[0])
    else:
        print('翻译结果不存在')
    
def custom_translate(word):
    translator = Translator(from_lang="chinese",to_lang="english")
    try:
        response = translator.translate(word)
        # 使用eval或者ast.literal_eval转换字符串为Python对象
        result = eval(response)
        # 使用解构赋值简化代码
        src, tgt = result['translation'][0][0].values()
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

