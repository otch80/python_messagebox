import ctypes

def messageBox(title, text, style):
	return ctypes.windll.user32.MessageBoxW(0, text, title, style)

if __name__=="__main__":
    messageBox("Error","에러발생",0)