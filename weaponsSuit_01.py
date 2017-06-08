'''
Weapons Match and Female Suit Selection Script 
************ Select Female Skin Suit Color Script ************* 
******************** Weapon matching Script *******************
************************ by Meenu Kaur ************************
Suit Select:
- Select the suit color and press "change"
Weapons Match: 
- Select the source object (the one that has the rotations/translations
  you're trying to copy over) 
- Select the target object (the one that will match the rotation/tranlsation of source object) 
- Run
'''
#Meenu Kaur
import pymel.core as pmc
import maya.cmds as mc

class WS():
    
    def __init__(self):
        
        #get namespace
        namespaces = mc.namespaceInfo(listOnlyNamespaces = True)
        self.namespaces = []
        for name in namespaces:
            if mc.objExists(name+ ":head"):
                self.namespaces.append(name) 
        print self.namespaces
            
            
        #call on the OptionsGUI method
        self.OptionsGUI()

        
        
    def OptionsGUI(self):
        if pmc.window("OptionsWin", exists = True, sizeable = True):
            pmc.deleteUI("OptionsWin") 
        win = pmc.window("OptionsWin",title = "Extra Options", wh = (700,700))
        myMenu = pmc.menuBarLayout()
        pmc.menu(label = "Help", helpMenu = True)
        pmc.menuItem(label = "About")
        
        
        #Female Skin Selection 
        layout = pmc.columnLayout("columnName1", adjustableColumn = True)
        frame1 = cmds.frameLayout(collapsable = True, label = "Female Skins", width = 700)
        pmc.setParent("..")
        pmc.rowColumnLayout( nc = 5)
        OptionsGUI.fRadioButns = mc.radioButtonGrp( label="Select:  \n\n", 
        labelArray4=["Light Blue", "Dark Blue", "Yellow", "White"], numberOfRadioButtons= 4)
        pmc.setParent("..")
        pmc.button(label = "Change", parent = "columnName1", width = 3, align = "center", c= fsuitCol)
       
        #Weapon matching 
        layout3 = pmc.columnLayout("columnName3", adjustableColumn = True)
        frame3 = pmc.frameLayout(collapsable = True, label = "Weapon Position Matching", width = 700) 
        pmc.text(label = "Select Constrols") 
        OptionsGUI.mytextSelection = pmc.textField(text = "")
        pmc.button (label = "<<< Parent Control", width = 30, c = orig_sel, ann="Load in original control.")
        OptionsGUI.mytextSelection2 = pmc.textField(text = "")
        pmc.button (label = "<<< Child Control", w = 30, c = sec_sel, ann="Load in second control.")
        pmc.button(label = "Match Position", c = matchPosition, ann = "Match second control's position to original's position")  
        pmc.setParent("..")
        pmc.showWindow(win) 
        
        pmc.setParent("..")
        pmc.showWindow(win) 
        
    #female skins files     
    def f_applySkinColor(skinColor):
        for name in self.namespaces:
            name_space = name+":"
            
            if (skinColor == "Light Blue"):
                pmc.setAttr(name_space+'file8.fileTextureName', "textures/FM_outfit_textures/female_DM_01.png", type = "string")
            
            elif (skinColor == "Dark Blue"):
                pmc.setAttr(name_space+'file8.fileTextureName', "textures/FM_outfit_textures/female_DM_02.png", type = "string")
        
            elif (skinColor == "Yellow"):
                pmc.setAttr(name_space+'file8.fileTextureName', "textures/FM_outfit_textures/female_DM_03.png", type = "string")
        
            elif (skinColor == "White"):
               pmc.setAttr(name_space+'file8.fileTextureName', "textures/FM_outfit_textures/female_DM_05.png", type = "string")
    
        return skinColor  
    #female radio button selection check      
    def fsuitCol(*args):
        radioSelection = mc.radioButtonGrp(OptionsGUI.fRadioButns, query = True, sl= True)
        if (radioSelection == 1):
            whichColor = "Light Blue"
        elif (radioSelection == 2):
            whichColor = "Dark Blue"
        elif (radioSelection == 3):
            whichColor = "Yellow"  
        elif (radioSelection == 4):
            whichColor = "White"  
        f_applySkinColor(whichColor)
    
    
    
    
    #select original control and put into into text box 
    def orig_sel(*args):
        orig_con = pmc.ls(sl=True)[0]
        textSelection = mc.textField(OptionsGUI.mytextSelection, edit = True, insertText = str(orig_con)) 
        return orig_con
    #select second control and put into text box 
    def sec_sel(*args):
        sec_con = pmc.ls(sl=True)[0]
        textSelection2 = mc.textField(OptionsGUI.mytextSelection2, edit = True, insertText = str(sec_con)) 
        return sec_con
    
    #match second control's translation and rotation to original control 
    def matchPosition(*args):
        orig_con = mc.textField(OptionsGUI.mytextSelection, query = True, tx = True) 
        sec_con = mc.textField(OptionsGUI.mytextSelection2, query = True, tx = True) 
        trans = pmc.xform(orig_con, query = True, t = True, ws = True) 
        rot = pmc.xform(orig_con, query = True, ro = True, ws = True) 
        #transfer translation and rotation 
        pmc.xform(sec_con, t = trans, ro = rot, worldSpace = True)
       
OptionsGUI()
