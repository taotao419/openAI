import requests 
import webbrowser

chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
url = 'https://api.forchange.cn' 
prompt = ''
last_question = ''

while True:
	question_str =  input("\U0001F468 Human: ")
	if question_str == 'pardon' :
		question_str = last_question
	if question_str == 'bye' :
		print("\U0001F916 AI: bye")
		break
	if question_str == 'google' :
		webbrowser.get('chrome').open_new_tab('http://www.google.com/search?q=' + last_question)
		print("\U0001F916 AI: 好的 帮你使用google查询")
		continue
	last_question = question_str
	prompt = prompt + f"Human: {question_str}\nAI:"
	data = {"prompt":prompt,"tokensLength":len(prompt)}
	try: 
		response = requests.post(url, json=data) 
		response_json = response.json()
		answer = response_json['choices'][0]['text'] 
		prompt_history= prompt + answer
		print("\U0001F916 AI: "+ answer)
	except Exception as e:
		print(response.text)
		print(e.message)
