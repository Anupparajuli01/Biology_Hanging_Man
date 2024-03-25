from random import randint
from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.rect.setFill('white')
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.rect.setFill('light grey')
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        
class DisplayText:
    def __init__(self,win, text, point,size):
        self.win =win
        self.text = text
        self.point = point
        self.size = size
        self.txt = Text(self.point,self.text)
        self.txt.setSize(self.size)
        self.txt.draw(self.win)
    
    def undraw_text(self):
        self.txt.undraw()
        
class HangMan:
    def __init__(self,win,flat_line_hint):
         self.win =win
         self.flat_line_hint=flat_line_hint
         self.stand_base= Rectangle(Point(10,8),Point(13,8.2))
         self.stand_base.draw(self.win)
         self.stand= Rectangle(Point(11.6,8),Point(11.8,12))
         self.stand.draw(self.win)
         self.stand_top= Rectangle(Point(10,11.8),Point(11.6,12))
         self.stand_top.draw(self.win)
         self.hanging_rope= Line(Point(10.8,11.8),Point(10.8,11.3))
         self.hanging_rope.draw(self.win)
         self.man_head = Circle(Point(10.8,10.8),0.5)
         self.man_head.setWidth(2)
         self.man_eye = Text(Point(10.8,10.8),"*   *")
         self.man_eye.setSize(20)
         self.man_mouth = Text(Point(10.8,10.8),"_")
         self.man_mouth.setSize(20)
         self.man_spine= Line(Point(10.8,10.3),Point(10.8,9.6))
         self.man_spine.setWidth(2)
         self.man_hand1 = Line(Point(10.8,10.1),Point(10.5,9.7))
         self.man_hand1.setWidth(2)
         self.man_hand2 = Line(Point(10.8,10.1),Point(11.1,9.7))
         self.man_hand2.setWidth(2)
         self.man_leg1 = Line(Point(10.8,9.6),Point(10.5,9.4))
         self.man_leg1.setWidth(2)
         self.man_leg2 = Line(Point(10.8,9.6),Point(11.1,9.4))
         self.man_leg2.setWidth(2)
         
    def drawMan(self,error_count):
        if error_count ==1:
            self.man_head.draw(self.win)
            self.man_eye.draw(self.win)
            self.man_mouth.draw(self.win)
        elif error_count == 2:
            self.man_spine.draw(self.win)
        elif error_count ==3:
            self.hintdisp = DisplayHint(self.flat_line_hint,self.win)
            self.man_hand1.draw(self.win)
            self.man_hand2.draw(self.win)
        elif error_count == 4:
            self.man_leg1.draw(self.win)
            self.man_leg2.draw(self.win)
            
    def undrawMan(self):
            self.man_head.undraw()
            self.man_eye.undraw()
            self.man_mouth.undraw()
            self.man_spine.undraw()
            self.man_hand1.undraw()
            self.man_hand2.undraw()
            self.man_leg1.undraw()
            self.man_leg2.undraw()
            try:
                self.hintdisp.undraw()
            except:
                pass

class DisplayHint:
    def __init__(self,flat_line_hint,win):
        self.flat_line_hint = flat_line_hint
        self.win =win
        self.hint1 = Text(Point(6.75,6),f"Hint: {self.flat_line_hint[0:85]}-")
        self.hint2 = Text(Point(6.75,5.5),f"-{self.flat_line_hint[85:170]}-")
        self.hint3 = Text(Point(6.75,5),f"-{self.flat_line_hint[170:255]}-")
        self.hint4 = Text(Point(6.75,4.5),f"-{self.flat_line_hint[255:340]}-")
        self.hint5 = Text(Point(6.75,4),f"-{self.flat_line_hint[340:425]}.")
        if len(flat_line_hint)<=85 :
             self.hint1 = Text(Point(6.75,6),f"Hint: {self.flat_line_hint[0:85]}.")
        elif len(flat_line_hint)<=170:
             self.hint2 = Text(Point(6.75,5.5),f"-{self.flat_line_hint[85:170]}.")
        elif len(flat_line_hint)<=255:
             self.hint3 = Text(Point(6.75,5),f"-{self.flat_line_hint[170:255]}.")
        elif len(flat_line_hint)<=340:
             self.hint4 = Text(Point(6.75,4.5),f"-{self.flat_line_hint[255:340]}.")
        
        self.hint1.setSize(15)
        self.hint2.setSize(15)
        self.hint3.setSize(15)
        self.hint4.setSize(15)
        self.hint5.setSize(15)
        self.hint1.setFill("red")
        self.hint2.setFill("red")
        self.hint3.setFill("red")
        self.hint4.setFill("red")
        self.hint5.setFill("red")
        if len(flat_line_hint)<=85 :    
            self.hint1.draw(self.win)
        elif len(flat_line_hint)<=170 :
            self.hint1.draw(self.win)
            self.hint2.draw(self.win)
        elif len(flat_line_hint)<= 255:
            self.hint1.draw(self.win)
            self.hint2.draw(self.win)
            self.hint3.draw(self.win)
        elif len(flat_line_hint)<=340 :
            self.hint1.draw(self.win)
            self.hint2.draw(self.win)
            self.hint3.draw(self.win)
            self.hint4.draw(self.win)
        else:
            self.hint1.draw(self.win)
            self.hint2.draw(self.win)
            self.hint3.draw(self.win)
            self.hint4.draw(self.win)
            self.hint5.draw(self.win)
        
    def undraw(self):
        self.hint1.undraw()
        self.hint2.undraw()
        self.hint3.undraw()
        self.hint4.undraw()
        self.hint5.undraw()
        


class KeyBoard:
    def __init__(self,win):
        self.win= win
        self.q_bttn = Button(self.win,Point(1,3),1,0.75,'Q')
        self.w_bttn = Button(self.win,Point(2.25,3),1,0.75,'W')
        self.e_bttn = Button(self.win,Point(3.5,3),1,0.75,'E')
        self.r_bttn = Button(self.win,Point(4.75,3),1,0.75,'R')
        self.t_bttn = Button(self.win,Point(6.0,3),1,0.75,'T')
        self.y_bttn = Button(self.win,Point(7.25,3),1,0.75,'Y')
        self.u_bttn = Button(self.win,Point(8.5,3),1,0.75,'U')
        self.i_bttn = Button(self.win,Point(9.75,3),1,0.75,'I')
        self.o_bttn = Button(self.win,Point(11.0,3),1,0.75,'O')
        self.p_bttn = Button(self.win,Point(12.25,3),1,0.75,'P')
        self.a_bttn = Button(self.win,Point(1.5,2),1,0.75,'A')
        self.s_bttn = Button(self.win,Point(2.75,2),1,0.75,'S')
        self.d_bttn = Button(self.win,Point(4.0,2),1,0.75,'D')
        self.f_bttn = Button(self.win,Point(5.25,2),1,0.75,'F')
        self.g_bttn = Button(self.win,Point(6.5,2),1,0.75,'G')
        self.h_bttn = Button(self.win,Point(7.75,2),1,0.75,'H')
        self.j_bttn = Button(self.win,Point(9.0,2),1,0.75,'J')
        self.k_bttn = Button(self.win,Point(10.25,2),1,0.75,'K')
        self.l_bttn = Button(self.win,Point(11.5,2),1,0.75,'L')
        self.z_bttn = Button(self.win,Point(2.75,1),1,0.75,'Z')
        self.x_bttn = Button(self.win,Point(4.0,1),1,0.75,'X')
        self.c_bttn = Button(self.win,Point(5.25,1),1,0.75,'C')
        self.v_bttn = Button(self.win,Point(6.5,1),1,0.75,'V')
        self.b_bttn = Button(self.win,Point(7.75,1),1,0.75,'B')
        self.n_bttn = Button(self.win,Point(9.0,1),1,0.75,'N')
        self.m_bttn = Button(self.win,Point(10.25,1),1,0.75,'M')
        self.q_bttn.activate()
        self.w_bttn.activate()
        self.e_bttn.activate()
        self.r_bttn.activate()
        self.t_bttn.activate()
        self.y_bttn.activate()
        self.u_bttn.activate()
        self.i_bttn.activate()
        self.o_bttn.activate()
        self.p_bttn.activate()
        self.a_bttn.activate()
        self.s_bttn.activate()
        self.d_bttn.activate()
        self.f_bttn.activate()
        self.g_bttn.activate()
        self.h_bttn.activate()
        self.j_bttn.activate()
        self.k_bttn.activate()
        self.l_bttn.activate()
        self.z_bttn.activate()
        self.x_bttn.activate()
        self.c_bttn.activate()
        self.v_bttn.activate()
        self.b_bttn.activate()
        self.n_bttn.activate()
        self.m_bttn.activate()
        
    def deactive_key(self,p):
        if self.q_bttn.clicked(p):
             self.q_bttn.deactivate()
             return 'q'
        if self.w_bttn.clicked(p):
             self.w_bttn.deactivate()
             return 'w'
        if self.e_bttn.clicked(p):
             self.e_bttn.deactivate()
             return 'e'
        if self.r_bttn.clicked(p):
             self.r_bttn.deactivate()
             return 'r'
        if self.t_bttn.clicked(p):
             self.t_bttn.deactivate()
             return 't'
        if self.y_bttn.clicked(p):
             self.y_bttn.deactivate()
             return 'y'
        if self.u_bttn.clicked(p):
             self.u_bttn.deactivate()
             return 'u'
        if self.i_bttn.clicked(p):
             self.i_bttn.deactivate()
             return 'i'
        if self.o_bttn.clicked(p):
             self.o_bttn.deactivate()
             return 'o'
        if self.p_bttn.clicked(p):
             self.p_bttn.deactivate()
             return 'p'
        if self.a_bttn.clicked(p):
             self.a_bttn.deactivate()
             return 'a'
        if self.s_bttn.clicked(p):
             self.s_bttn.deactivate()
             return 's'
        if self.d_bttn.clicked(p):
             self.d_bttn.deactivate()
             return 'd'
        if self.f_bttn.clicked(p):
             self.f_bttn.deactivate()
             return 'f'
        if self.g_bttn.clicked(p):
             self.g_bttn.deactivate()
             return 'g'
        if self.h_bttn.clicked(p):
             self.h_bttn.deactivate()
             return 'h'
        if self.j_bttn.clicked(p):
             self.j_bttn.deactivate()
             return 'j'
        if self.k_bttn.clicked(p):
             self.k_bttn.deactivate()
             return 'k'
        if self.l_bttn.clicked(p):
             self.l_bttn.deactivate()
             return 'l'
        if self.z_bttn.clicked(p):
             self.z_bttn.deactivate()
             return 'z'
        if self.x_bttn.clicked(p):
             self.x_bttn.deactivate()
             return 'x'
        if self.c_bttn.clicked(p):
             self.c_bttn.deactivate()
             return 'c'
        if self.v_bttn.clicked(p):
             self.v_bttn.deactivate()
             return 'v'
        if self.b_bttn.clicked(p):
             self.b_bttn.deactivate()
             return 'b'
        if self.n_bttn.clicked(p):
             self.n_bttn.deactivate()
             return 'n'
        if self.m_bttn.clicked(p):
             self.m_bttn.deactivate()
             return 'm'
            
    def activate_key (self):
        self.q_bttn.activate()
        self.w_bttn.activate()
        self.e_bttn.activate()
        self.r_bttn.activate()
        self.t_bttn.activate()
        self.y_bttn.activate()
        self.u_bttn.activate()
        self.i_bttn.activate()
        self.o_bttn.activate()
        self.p_bttn.activate()
        self.a_bttn.activate()
        self.s_bttn.activate()
        self.d_bttn.activate()
        self.f_bttn.activate()
        self.g_bttn.activate()
        self.h_bttn.activate()
        self.j_bttn.activate()
        self.k_bttn.activate()
        self.l_bttn.activate()
        self.z_bttn.activate()
        self.x_bttn.activate()
        self.c_bttn.activate()
        self.v_bttn.activate()
        self.b_bttn.activate()
        self.n_bttn.activate()
        self.m_bttn.activate()
        

class OptionDisplay:
    def __init__(self,win,result):
        self.win =win
        self.result = result
        self.option_rect = Rectangle(Point(3.5,8.5),Point(8.5,11.5))
        self.option_rect.draw(self.win)
        self.result_disp = Text(Point(6,10.5),f"{self.result}")
        self.result_disp.setSize(36)
        self.result_disp.draw(self.win)
        self.Play_agn_bttn = Button(self.win,Point(4.8,9.15),2,0.75,'Play Again')
        self.quit_bttn = Button(self.win,Point(7.2,9.15),2,0.75,'Quit')
        
        self.Play_agn_bttn.activate()
        self.quit_bttn.activate()
    
    def usrchoice(self,p):
        if  self.Play_agn_bttn.clicked(p)== True:
            return True    
        elif self.quit_bttn.clicked(p) == True :
            quit()
        else:
            return None
        
    def undraw(self):
        self.option_rect.undraw()
        self.result_disp.undraw()
        self.quit_bttn.undraw()
        self.Play_agn_bttn.undraw()
        
        
def readLineByLine(filename):
    """Takes a string object filename.
       Return all lines in the file, as a list. """  
    readfile = open(filename, "r")
    list_readfile= readfile.readlines()
    readfile.close()
    return list_readfile

def selectRandomLine(list_readfile):
    """Takes a list file.
       Return a randomly selected line from list. """
    random_line = list_readfile[0]
    random_line = list_readfile[randint(0, len(list_readfile)-1)]
    no_new_line = random_line.split("\n")[0]
    word_and_hint = no_new_line.split(": ")
    flat_line = word_and_hint[0]
    flat_line_hint=word_and_hint[-1]
    return flat_line, flat_line_hint

def maskTheLine(flat_line):
    """Takes a randomly selected line.
       Returns the line by masking all the text with ~ . Character like ,.-' are unmasked """ 
    masked_line= ""
    for i in range(len(flat_line)):
        if flat_line[i]== "'" or flat_line[i]=="-" or flat_line[i]== "," or flat_line[i]== " " or flat_line[i]== "." or flat_line[i]== ";" or flat_line[i]=="(" or flat_line[i]==")" :
            masked_line = f"{masked_line}{flat_line[i]}"
        else:
            try:
                if type(int(flat_line[i]))==type(1):
                   masked_line = f"{masked_line}{flat_line[i]}" 
            except:
                masked_line = f"{masked_line}~"
    return masked_line

def checktheWord(pressed_word,flat_line):
    start_point=0
    if flat_line.lower().find(pressed_word) == -1:
        return False
    else:
        return True
    
def UnmaskCorrectOne(pressed_word,flat_line,masked_line):
    start_point = 0
    for i in range(flat_line.lower().count(pressed_word)):
         index_of_word = flat_line.lower().find(pressed_word,start_point)
         masked_line = masked_line[:index_of_word] + flat_line[index_of_word] + masked_line[(index_of_word+1):]
         start_point =index_of_word+1
    return(masked_line)
    


def main():
    win = GraphWin("HangMan",600,600)
    win.setBackground("white")
    win.setCoords(0,0,13.5,13.5)
    key_board = KeyBoard(win)
    while True:
        list_readfile =readLineByLine("fnl.txt")
        flat_line,flat_line_hint=selectRandomLine(list_readfile)
        hang_man=HangMan(win,flat_line_hint)
        masked_line=maskTheLine(flat_line)
        masked_line_display = DisplayText(win, masked_line, Point(6.75,6.75),23)
        error_count = 0
        while True:
            p = win.getMouse()
            pressed_word= (key_board.deactive_key(p))
            if pressed_word != None:
              if checktheWord(pressed_word,flat_line) == True:
                  masked_line=UnmaskCorrectOne(pressed_word,flat_line,masked_line)
                  masked_line_display.undraw_text()
                  masked_line_display=DisplayText(win, masked_line, Point(6.75,6.75),23)
              else:
                  error_count+=1
                  hang_man.drawMan(error_count)
            
            if error_count == 4 or flat_line ==masked_line:
                if flat_line ==masked_line :
                    result = "You Won!"
                elif error_count == 4:
                    result = "You Lost!"
                break
        if error_count == 4 or flat_line ==masked_line :
            masked_line_display.undraw_text()
            masked_line_display = DisplayText(win, flat_line, Point(6.75,6.75),23)
            options = OptionDisplay(win,result)
            p = win.getMouse()
            while options.usrchoice(p)!= True:
                p = win.getMouse()
            options.undraw()
            hang_man.undrawMan()
            masked_line_display.undraw_text()
            key_board.activate_key()
            
if __name__=="__main__":
    main()
