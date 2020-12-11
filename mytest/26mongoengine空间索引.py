'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-11 09:59:16
LastEditors: henggao
LastEditTime: 2020-12-11 17:22:50
'''
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import DictField, IntField, PointField, StringField
from mongoengine import *
from mongoengine.context_managers import switch_collection, switch_db

connect(alias='drill_system', db='钻孔数据管理子系统',
        host='192.168.55.110', port=20000)


class GeoTest(Document):
    name = StringField()
    location = PointField()
    meta = {'db_alias': 'drill_system'}
    # meta = {'db_alias': 'drill_system',
    #         'indexes': [[("location", "2dsphere"), ("datetime", 1)]]}


# geojson  = GeoTest(name = 'ZK2',location = [0,2])
# geojson.save()
# print(geojson)
# doc = GeoTest.objects(location__geo_within={[[[0, 0], [0, 3], [3,3],[3,0]]]})
# print(doc)
#  多边形查询
# doc = GeoTest.objects(location__geo_within={
#                       "type": "Polygon", "coordinates": [[[0, 0], [0, 3], [3, 3], [3, 0],[0,0]]]})

# 圆形查询
doc = GeoTest.objects(location__geo_within_center=[(0, 0), 2])
print(doc)
# doc = GeoTest.objects(point__near=[0, 0])
# result = GeoTest.objects(location__near=[1,0], location__max_distance=1)

# print(result)
