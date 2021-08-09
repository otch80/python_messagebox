import ctypes

def msgBox(title, text, style):
	return ctypes.windll.user32.MessageBoxW(0, text, title, style)

if __name__=="__main__":
    msgBox("Error","에러발생",0)