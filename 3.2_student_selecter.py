import random

names = [
    "裴浩均",
    "洪梽炫",
    "陈彦臻",
    "吴自欣",
    "陈芸",
    "潘莹",
    "吴杰",
    "梁炫澔",
    "林以乐",
    "李嘉悦",
    "洪沁涵",
    "高琰喆",
    "王孜璟",
    "楼欣晨",
    "徐哿",
    "宋曙延",
    "周欣怡",
    "侯胤竹",
    "黄亦凡",
    "杨洋",
    "张青卉"
]

selected = random.sample(names, 4)
print("抽取的四个人：")
for name in selected:
    print(name)

