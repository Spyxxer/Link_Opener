import mainfile
from selenium import webdriver
import re
import time
import sys



def proceed():
	pattern = str(input("Enter RegExp pattern to find link: "))
	ans = str(input("Are you satisfied Y/N: "))
	if ans.lower() == 'y':
		return pattern
	else:
		proceed()

links_list = []
pat = proceed()
for each in mainfile.BODY:
	links = re.findall(pat, each)
	for e in links:
		links_list.append(e)

print(f'{links_list}')
print(f'\nTOTAL LINKS: {len(links_list)}')
def open_text(link):
	out = None
	try:
		print("\rDo you want to open this link->", link)
		out = str(input("Y/N: "))
		if out.lower() not in ['y', 'n']:
			open_text(link)
		else:
			return out
	except:
		open_text(link)
	else:
		return out

def choose_browser():
	select = None
	try:
	    print("Select the browser you want using the numbers:\n1.Google_Chrome\n2.Firefox\n3.Microsoft_Edge\n4.Safari")
	    select = int(input("Choose number: "))
	except ValueError:
		print("Wrong Input, Try again")
		choose_browser()
	else:
		return select

browser_arr = [webdriver.Chrome, webdriver.Firefox, webdriver.Edge, webdriver.Safari]
val = choose_browser()

def open_links(link_no):
	x = link_no
	BROWSER = browser_arr[val-1]()
	try:
		while x < len(links_list):
			print(f'OPENING LINK: {x}')
			BROWSER.get(links_list[x])
			time.sleep(45); x += 1
	except:
		print(sys.exc_info()[1])
		print('Picking up last phase...')
		open_links(x)

	BROWSER.quit()
	print('OPENED ALL LINKS SUCCESSFULLY.')

open_links(190)
