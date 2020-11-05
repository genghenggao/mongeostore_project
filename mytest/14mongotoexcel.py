from openpyxl import Workbook
import pymongo


# 读取mongoDB数据库相应的表，每条数据取出数个字段存入一个dict，再将所有的dict存入一个list
# def read_mongoDB():
    # 连接mongoDB数据库，读取 db 库 table 表中的数据
client = pymongo.MongoClient("192.168.55.110", 20000)
db = client['segyfile']
table = db['excel_data']

# 创建list用于存储从mongoDB中读取到的数据
mongo_data_list = []
# 从table中读取的数据为整个documents内容
documents = table.find()
# print(documents[1].keys())
list_keys = documents[1].keys()
# print(list_keys)
# 遍历 documents 表中的每一个document
for document in documents:
    # 创建dict用于存储各条数据的各个字段名称及内容
    # print(document.keys())
    mongo_data_dict = {}
    for list_key in list_keys:
        print(list_key)
        list_key_tmp = document.get(str(list_key))
        # 为了处理ObjectId
        if list_key == "_id":
            list_key_tmp = str(list_key_tmp)
        mongo_data_dict.update({str(list_key): list_key_tmp})
    # rid = document.get("rid")
    # vip = document.get("vip")
    # rank = document.get("?rank")
    # costMoney = document.get("costMoney")
    # 将查询到的的数据字段内容以更新添加的方式添加到每个dict中
    # mongo_data_dict.update({"rid": rid})
    # mongo_data_dict.update({"vip": vip})
    # mongo_data_dict.update({"rank": rank})
    # mongo_data_dict.update({"costMoney": costMoney})
    print("mongo_data_dict:", mongo_data_dict)
    mongo_data_list.append(mongo_data_dict)
    # print("mongo_data_dict:", mongo_data_list)
    # return mongo_data_list


# 保存至本地excel表格
# def save_to_excel(mongoDB_data):
outwb = Workbook()
outws = outwb.worksheets[0]
# 字段写入
# header_list = ["rid", "vip", "rank", "costMoney"]
header_list = list(list_keys)
# print(type(header_list))
outws.append(header_list)
# 遍历外层列表
for new_dict in mongo_data_list:
    a_list = []
    # 遍历内层每一个字典dict，把dict每一个值存入list
    for item in new_dict.values():
        # print(item)
        a_list.append(item)
        # print(a_list)
    # sheet直接append list即可
    outws.append(a_list)

outwb.save(r'./mongeostore_env/upload/excel_data.xlsx')
print('数据存入excel成功')


# def main():
#     mongoDB_data = read_mongoDB()
#     # print(mongoDB_data)
#     save_to_excel(mongoDB_data)


# if __name__ == '__main__':
#     main()
