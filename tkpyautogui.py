import pyautogui
import time

# Give time to switch to target window (like Notepad, Chrome, etc.)
print("⏳ Starting in 5 seconds... Switch to your target window.")
time.sleep(5)

# Move the mouse to (300, 300) over 1 second
pyautogui.moveTo(300, 300, duration=1)
print("🖱️ Mouse moved to (300, 300)")

# Click at current position
pyautogui.click()
print("✅ Clicked")

# Type a message
pyautogui.write("Hello from pyautogui!", interval=0.1)
print("⌨️ Typed message")

# Press Enter
pyautogui.press('enter')
print("↩️ Pressed Enter")





