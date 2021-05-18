#/bin/python3
# practice problem 5

chip_bugger = 0
chip_baver = 0
h_bugger = int(input())
m_bugger = int(input())
l_bugger = int(input())
coke = int(input())
sidar = int(input())

chip_bavar = 0
chip_bugger = h_bugger

if m_bugger < chip_bugger:
	chip_bugger = m_bugger

if l_bugger < chip_bugger:
	chip_bugger = l_bugger

if coke > sidar:
	chip_bavar = sidar
else:
	chip_bavar = coke


print("low set price")
print(chip_bugger + chip_bavar)
