import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x ,y1, label="sin") # 그래프 생성 "sin"
plt.plot(x, y2, linestyle="--", label="cos") # "cos" 함수는 점선으로 그리기 linestyle
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos") # 제목
plt.legend() # 그래프의 위 정보 출력
plt.show() # 그래프 출력