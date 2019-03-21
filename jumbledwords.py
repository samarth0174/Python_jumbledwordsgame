import wx
import random 

count=0
score=0

words = ['GameofThrones','Sherlok','MrRobot','Narcos','PeakyBlinders','Friends','Flash','Arrow','PlanetEarth','BreakingBad','Cosmos','RickandMorty','Firefly','DeathNote','BlackMirror','Seinfeld','HouseofCards','BodyGuard','TheOffice','TheSimpsons','SouthPark','DragonBallZ','StrangerThings','Riverdale','TheCrown','Daredevil','Masum','AdventureTime','Vikings','SiliconValley']
			
						
def choose_arr(arr):
	
	words_new = random.sample(arr,11)
	words_new1 =words_new[:9]
	return words_new1


	
def choose(array,i): 
	 
	pick = array[i-1] 
	return pick 
	
def jumble(word): 
	
	
	random_word = random.sample(word, len(word)) 
	jumbled = ''.join(random_word) 
	return jumbled 
	

word_pick= choose_arr(words) 
  
def next(event):
    # After a person clicks the Start button for the first time, this will happen
    nextButton.SetLabel("Next")
    guessButton.Enable()
    input_word.SetValue("")
   
    global picked_word 
    global count
    picked_word = choose(word_pick,count) 
    qn = jumble(picked_word)
    
    if(count<9):
        question.SetLabel(label="The jumbled word is: "+qn.lower())
        result.SetLabel(label="Waiting for your input...")
    elif(count==9):
        question.SetLabel(label="Game Over!")
        result.SetLabel(label="Yup, the game is finally over!")
        guessButton.Disable()
        nextButton.Disable()
    count=count+1
    
    
    

def  guess(event):
    global score
    ans = input_word.GetValue()
    ans = ans.replace(' ', '')
    if(ans.lower() == picked_word.lower()):
        result.SetLabel(label="Congrats! You got it right.")
        score=score+1
        print(score)
        playerscore.SetLabel(label="player score is: " + str(score))
    else:
        result.SetLabel(label="Sorry, wrong answer. Better luck next time!")
    guessButton.Disable()
   
app = wx.App()
win = wx.Frame(None, title="Jumbled Words Game", size=(460, 345))

#win.SetIcon(wx.Icon('star.ico', wx.BITMAP_TYPE_ICO))
win.CenterOnScreen()
bkg = wx.Panel(win)
guessButton = wx.Button(bkg, label='Guess')

guessButton.Bind(wx.EVT_BUTTON, guess)
guessButton.SetDefault()

# Unless the player has pressed the Start button, the Guess button will be disabled

guessButton.Disable()
nextButton = wx.Button(bkg, label='Start')
nextButton.Bind(wx.EVT_BUTTON, next)
input_word = wx.TextCtrl(bkg)
question = wx.StaticText(bkg, label="Welcome to jumbled words game\nTotal words: 10", style=wx.ALIGN_CENTER)
playerscore = wx.StaticText(bkg, label="player score is: " + str(score))

# fonts
font = wx.Font(pointSize=18, family=wx.DECORATIVE, style=wx.NORMAL, weight=wx.NORMAL)
question.SetFont(font)
font1 = wx.Font(pointSize=15, family=wx.DECORATIVE, style=wx.NORMAL, weight=wx.NORMAL)
playerscore.SetFont(font1)
result = wx.StaticText(bkg, label="Waiting for the initial result...", style=wx.ALIGN_CENTER)
hbox = wx.BoxSizer()	
hbox.Add(input_word, proportion=1, flag=wx.EXPAND)
hbox.Add(guessButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(nextButton, proportion=0, flag=wx.LEFT, border=5)
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(question, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(playerscore, proportion=5, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
vbox.Add(result, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
bkg.SetSizer(vbox)
win.Show()
app.MainLoop()

	
