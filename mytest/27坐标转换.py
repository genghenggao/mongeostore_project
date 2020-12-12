'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-11 20:25:06
LastEditors: henggao
LastEditTime: 2020-12-12 11:27:12
'''
import math


def millerToXY(lon, lat):
    """
    :param lon: 经度
    :param lat: 维度
    :return:
    """
    xy_coordinate = []
    L = 6381372*math.pi*2  # 地球周长
    W = L  # 平面展开，将周长视为X轴
    H = L/2  # Y轴约等于周长一般
    mill = 2.3  # 米勒投影中的一个常数，范围大约在正负2.3之间
    x = lon*math.pi/180  # 将经度从度数转换为弧度
    y = lat*math.pi/180  # 将纬度从度数转换为弧度
    y = 1.25*math.log(math.tan(0.25*math.pi+0.4*y))  # 这里是米勒投影的转换

    # 这里将弧度转为实际距离 ，转换结果的单位是公里
    x = (W/2)+(W/(2*math.pi))*x
    y = (H/2)-(H/(2*mill))*y
    xy_coordinate.append((int(round(x)), int(round(y))))
    return xy_coordinate


test = millerToXY(116, 39)
# test = millerToXY(116.0000014, 38.9999952)
print(test)


def xy_to_coor(x, y):
    lonlat_coordinate = []
    L = 6381372 * math.pi*2
    W = L
    H = L/2
    mill = 2.3
    lat = ((H/2-y)*2*mill)/(1.25*H)
    lat = ((math.atan(math.exp(lat))-0.25*math.pi)*180)/(0.4*math.pi)
    lon = (x-W/2)*360/W
    # TODO 最终需要确认经纬度保留小数点后几位
    lonlat_coordinate.append((round(lon, 7), round(lat, 7)))
    return lonlat_coordinate


data = xy_to_coor(32967282, 6898800)
print(data)
