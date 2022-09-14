# 百度ocr提供了模板，我们直接复制就ok
# 下载通用文字识别的python sdk,一定要放在你写的代码的文件夹下面
from aip import AipOcr
from os import path


def baiduOCR(picfile):  # picfile:图片文件名 outfile:输出文件
    filename = path.basename(picfile)  # 图片名称
    print(filename)
    # 百度提供
    """ 你的 APPID AK SK """
    APP_ID = '27462290'  # 这是你产品服务的appid
    API_KEY = 'DPjcEwrE8OSpfmVhDPdCGraR'  # 这是你产品服务的appkey
    SECRET_KEY = 'a45Ggw7CVW7DC9vbQ38E5RGSpZ4zYITh'  # 这是你产品服务的secretkey
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    i = open(picfile, 'rb')
    img = i.read()

    print("正在识别图片：\t" + filename)
    """ 调用通用文字识别（高精度版） """
    message = client.basicAccurate(img)
    # message = {
    #     'words_result': [{
    #         'words': '9×8='
    #     }],
    #     'words_result_num': 1,
    #     'log_id': 1569926993987192414
    # }
    print("识别成功！", message)

    i.close()

    text = message.get('words_result')
    print(text)
    print(text[0])
    print(type(text[0]))
    my_str = text[0].get('words')[:-1]
    print(my_str)
    print(type(my_str))
    if '×' in my_str:
        rmy_str = my_str.replace('×', '*')
        print(rmy_str)
    elif '÷' in my_str:
        rmy_str = my_str.replace('÷', '/')
    else:
        rmy_str = my_str
    res = eval(rmy_str)
    print(res)
    return res


# with open(outfile, 'a+') as fo:  # 这边是写进.txt文件
#     fo.writelines("*" * 60 + '\n')  # 搞点花里胡哨的做区分
#     fo.writelines("识别图片：\t" + filename + "\n" * 2)
#     fo.writelines("文本内容：\n")
#     # 输出文本内容
#     for text in message.get('words_result'):  # 识别的内容
#         fo.writelines(text.get('words') + '\n')
#     fo.writelines('\n' * 2)
# print("文本导出成功！")
# print()


if __name__ == '__main__':
    baiduOCR('D:/pic1.png')

