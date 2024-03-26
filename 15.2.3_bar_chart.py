import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc, style

# 폰트 설정
font_name = font_manager.FontProperties(
    fname="C:\\Windows\\Fonts\\HMFMMUEX.TTC"
).get_name()

# 폰트 세팅
rc("font", family=font_name)

# style 변경
plt.style.use("ggplot")

industry = [
    "통신업",
    "의료정밀",
    "운수창고업",
    "의약품",
    "음식료품",
    "전기가스업",
    "서비스업",
    "전기전자",
    "종이목재",
    "증권",
]

fluctuations = [
    1.83,
    1.30,
    1.30,
    1.26,
    1.06,
    0.93,
    0.77,
    0.68,
    0.65,
    0.61,
]

# figure 생성
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

ypos = np.arange(10)  # [0, 1, 2, ... 8, 9]

# plt.barh(각 bar가 그려질 위치, 각 bar에 대한 수치, align=정렬 위치, height=수평 bar 차트 높이)
rects = plt.barh(ypos, fluctuations, align="center", height=0.5)

# pl.yticks(ticker의 위치, 각 위치에서의 label)
plt.yticks(ypos, industry)

# x축 label
plt.xlabel("등락률")

for i, rect in enumerate(rects):  # rect: bar 차트에서 각 bar
    ax.text(
        0.95 * rect.get_width(),  # width: bar 너비의 95%지점
        rect.get_y()
        + rect.get_height() / 2.0,  # height: bar가 출력된 y축 위치 + bar 높이의 절반
        f"{fluctuations[i]}%",  # 출력될 text
        ha="right",  # 가로축 정렬
        va="center",  # 세로축 정렬
    )

plt.show()
