class Font:
    def __init__(self, name):
        self.letters = {}
	self.name = name

class FontLoader:
    def loadFont(self, directory):
        font = Font("fancy")

        font.letters['G'] = r'''
  ___ 
 / __)
( (_ \
 \___/
'''

		
        font.letters['I'] = r'''
  __  
 (  ) 
  )(  
 (__) 
'''
    
        font.letters['T'] = r'''
 ____ 
(_  _)
  )(  
 (__) 
'''
	return font
	
	
		
