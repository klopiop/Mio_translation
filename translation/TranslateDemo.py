import requests
from utils.AuthV3Util import addAuthParams

# 您的应用ID
APP_KEY = '5b9a0121c84b8c41'
# 您的应用密钥
APP_SECRET = 'P3kqiHRkNzabQHrJhUsL5l9U9B9QNv8v'


def createRequest():
    '''
    note: 将下列变量替换为需要请求的参数
    '''
    q = '待翻译文本'
    lang_from = '源语言语种'
    lang_to = '目标语言语种'
    vocab_id = '您的用户词表ID'

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


# 网易有道智云翻译服务api调用demo
# api接口: https://openapi.youdao.com/api
if __name__ == '__main__':
    result = createRequest()
    translation = result.json().get('translation', [])
    if translation:
        print(translation[0])
    else:
        print('翻译结果不存在')
