cityweather = {
    '北京': '38°',
    '上海': '36°',
    '广州': '35°',
}

cityweather["河北"] = "33°"
print(cityweather)
cityweather["河北"] = "32°"
print(cityweather)
del cityweather["河北"]
print(cityweather)


cityname = input("请输入要查询温度的地区:")
if cityname in cityweather:
    print(cityname + ":"  + cityweather[cityname])
else:
    print("没有这个城市")
