""" 读取文件 """
from aip import AipOcr

APP_ID = '27462290'  # 这是你产品服务的appid
API_KEY = 'DPjcEwrE8OSpfmVhDPdCGraR'  # 这是你产品服务的appkey
SECRET_KEY = 'a45Ggw7CVW7DC9vbQ38E5RGSpZ4zYITh'  # 这是你产品服务的secretkey
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, "rb") as fp:
        return fp.read()


image = get_file_content('D:/pic1.png')
# url = "https://www.x.com/sample.jpg"
# pdf_file = get_file_content('D:/pic1.png')

# 调用通用文字识别（标准含位置信息版）
res_image = client.general(image)
# res_url = client.generalUrl(url)
# res_pdf = client.generalPdf(pdf_file)
print(res_image)
# print(res_url)
# print(res_pdf)

# 如果有可选参数
options = {}
options["recognize_granularity"] = "big"
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["vertexes_location"] = "true"
options["probability"] = "true"
res_image = client.general(image, options)
# res_url = client.generalUrl(url, options)
# res_pdf = client.generalPdf(pdf_file, options)
print(res_image)
# print(res_url)
# print(res_pdf)