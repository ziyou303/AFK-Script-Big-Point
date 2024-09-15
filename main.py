import pyautogui
import time

print('作者:大典')
print('按下Ctrl+C可以停止')

# 等待几秒钟，以便你可以切换到目标窗口
time.sleep(5)

def main():
  # 模拟按下W键
  pyautogui.press('w')
  
  # 等待几秒钟，防止过快导致游戏无反应
  time.sleep(1)
  
  # 模拟按下S键
  pyautogui.press('s')

# 循环
try:
    while True:
      main()
except KeyboardInterrupt:
    print("程序已停止。")
