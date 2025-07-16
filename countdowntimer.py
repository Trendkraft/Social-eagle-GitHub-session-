import time

# Countdown from 10 to 0
print("⏳ Countdown Timer Starting...\n")

for i in range(10, -1, -1):
    print(f"🕒 {i}")
    time.sleep(1)

print("\n🚀 Time's up!")
