import pyautogui
import subprocess
import time
import pyperclip

time.sleep(100)
# 메모장 실행
subprocess.Popen(['notepad.exe'])
# 잠시 대기 (메모장이 열릴 때까지 대기)
time.sleep(1)

# 메모장에 'Hello, World!' 입력
ment = ('깜짝 놀랐지? 😄 '
        '하지만 이렇게 예고 없이 찾아오는 놀라움들이 때론 우리의 하루를 특별하게 만들어 주는 법이야! '
        '이제 웃으며 멋진 하루를 시작해봐!')
# 클립보드에 한글 텍스트 복사
pyperclip.copy(ment)
# 붙여넣기 (Ctrl + V)
pyautogui.hotkey('ctrl', 'v')
