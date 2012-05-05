# -*- coding: utf-8 -*-
# by Iman Karim (imax@tha-imax.de)
# Released under GPLv2

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
from PyKDE4.kdeui import *
import urllib2
import os
import socket
import eveapi
import eveConfig
import ConfigParser
 
class EveApplet(plasmascript.Applet):
    APIKEY = None
    USERID = None
    CHAR   = None
    timer  = None
    timeResult = None
    timerruns = 0
    html_header = """<html>
    """
    

    
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
        self.imagelabel = Plasma.Label(self.applet)
        self.timelabel = Plasma.Label(self.applet)
        self.namelabel = Plasma.Label(self.applet)
        self.isklabel = Plasma.Label(self.applet)
        self.skilllabel = Plasma.Label(self.applet)
        self.char  = None
        self.skillCache = None

    def init(self):
        self.config = ConfigParser.ConfigParser()
        self.configfile = os.path.expanduser('~/.plasmoEve_config')
        self.config.read(self.configfile)
        if (self.config.has_section("api")):
            self.APIKEY = self.config.get("api", "apikey")
            self.USERID = self.config.get("api", "userid")
            self.CHAR = self.config.get("api", "char")
            
        self.setHasConfigurationInterface(True)
        self.resize(300, 300)
        self.layout = QGraphicsLinearLayout(Qt.Vertical, self.applet)
        self.layout.addItem(self.imagelabel)
        self.layout.addItem(self.namelabel)
        self.layout.addItem(self.isklabel)
        self.layout.addItem(self.skilllabel)
        self.layout.addItem(self.timelabel)
        self.imagelabel.setText("Refreshing...")
        self.namelabel.setText("Refreshing...")
        self.isklabel.setText("Refreshing...")
        self.skilllabel.setText("Refreshing...")
        self.refresh()

    def request(self,url):
        socket.setdefaulttimeout(5)
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'PlasmoEVE/0.1')]
        try:
            ret = opener.open(url).read()
        except Exception, err:
            return(None)
        return(ret)

    def checkUser(self):
        found = False
        try:
            result = self.api.account.Characters(keyID=self.USERID, vCode=self.APIKEY)
            
            
            for c in result.characters:
                if (c.name == self.CHAR):
                    self.char = c
                    found = True
                    break
        except:
            pass
        
        return(found)

    def getImageURL(self):
        return("http://image.eveonline.com/Character/%s_256.jpg" %(self.char.characterID))

    def getSkillInTraining(self):
        result = self.api.char.SkillInTraining(keyID=self.USERID, vCode=self.APIKEY, characterID=self.char.characterID)
        return(result)

    def getISK(self):
        isk = 0
        try:
            auth = self.api.auth(keyID=self.USERID, vCode=self.APIKEY)
            wallet = auth.char.AccountBalance(characterID=self.char.characterID)
            isk = str(wallet.accounts[0].balance) + " ISK"
        except:
            isk = "<html><font color='red'>Failed. Low API Level?"
        return(isk)

    def refresh(self):
        self.api = eveapi.EVEAPIConnection()
        found = self.checkUser()
        
        
        
        if (not found):
            self.imagelabel.setText("<html>No character configured!<br>Please open up the configuration and setup your char.")
            return
        
        
        if (not self.skillCache):
                self.skillCache = self.api.eve.SkillTree(keyID=self.USERID, vCode=self.APIKEY)
        
        imageURL = self.getImageURL()
        ret = self.request(imageURL)
        localImage = "/tmp/.plasmoeve_portrait_" + os.getenv('USER')  + "_" + self.char.name + ".jpg"
        f = open(localImage, "w")
        f.write(ret)
        f.close()
        
        self.timeResult = self.getSkillInTraining()
        self.timerruns = 0
        if (self.timer == None):
            self.timer = QTimer()
            self.connect(self.timer, SIGNAL("timeout()"), self.refreshTime)
        self.timer.start(1000)
            
        skillName = "<font color='red'>Not skilling!</font>"
        skillLevel = 0
        try:
            for skillGroup in self.skillCache.skillGroups:
                for skill in skillGroup.skills:
                    if (skill.typeID == self.timeResult.trainingTypeID):
                        skillName = skill.typeName
                        skillLevel = self.timeResult.trainingToLevel
                        break
        except:
            pass
        
        isk = self.getISK()
        
        self.imagelabel.setText("<html><img src='%s'>" %(localImage))
        self.namelabel.setText("<html><table><tr><td width='128'><b>Pilot:</td><td>%s</b>" %(self.char.name))
        self.isklabel.setText("<html><table><tr><td width='128'><b>Wealth:</td><td>%s" %(isk))
        self.skilllabel.setText("<html><table><tr><td width='128'><b>Skilling:</td><td>%s (L: %d)" %(skillName, skillLevel))
        
        
    def refreshTime(self):
        
        if self.timeResult.skillInTraining:
            timeLeft = self.timeResult.trainingEndTime - self.timeResult._meta.currentTime  - (1000 + self.timerruns)
            if timeLeft < 0:
                complete = True
                timeLeft = -timeLeft
            else:
                complete = False
    
            # make a nice formatted time string
            s = timeLeft % 60
            m = (timeLeft/60) % 60
            h = (timeLeft/3600) % 24
            d = (timeLeft/86400)
            timeString = "%2dd %2dh %2dm %2ds" % (d, h, m, s)
    
            msg = ""
            if complete:
                msg = "<font color='green'>TRAINING COMPLETE (%s ago)</font>" % (timeString)
                self.refresh()
                return
            else:
                msg = "%s" % (timeString)
            
            timelbl = "<html><table><tr><td width='128'><b>Time remaining:</b></td>"
            timelbl += "<td>%s</td>" %(msg)
            timelbl += "</tr>"
            self.timelabel.setText(timelbl)
            
            self.timerruns += 1

            
    
    def createConfigurationInterface(self,parent):
        self.eveConfig = eveConfig.eveConfig(self)
        page = parent.addPage(self.eveConfig,"Eve Char Selection")
        self.connect(parent, SIGNAL("okClicked()"), self.configAccepted)
        self.connect(parent, SIGNAL("cancelClicked()"), self.configDenied)

    def configAccepted(self):
        if (self.timer != None):
            self.timer.stop()
        item = self.eveConfig.lstChars.currentItem()
        if (not item):
            self.label.setText("<html><font color='red'>No Character selected!")
        else:
            self.APIKEY = str(self.eveConfig.txtAPIKey.text())
            self.USERID = str(self.eveConfig.txtUserID.text())
            self.CHAR   = str(item.text())
            self.storeSettingsToFile()
            self.refresh()

    def configDenied(self):
        pass

    def storeSettingsToFile(self):
        if (not self.config.has_section("api")):
            self.config.add_section("api")
        self.config.set("api", "userid", self.USERID)
        self.config.set("api", "apikey", self.APIKEY)
        self.config.set("api", "char", self.CHAR)
        cfg = open(self.configfile, "w")
        self.config.write(cfg)
        cfg.close()

    def showConfigurationInterface(self):
            dialog = KPageDialog()
            dialog.setFaceType(KPageDialog.Plain)
            dialog.setButtons(KDialog.ButtonCode(KDialog.Ok | KDialog.Cancel))
            self.createConfigurationInterface(dialog)
            if (self.APIKEY != None): self.eveConfig.txtAPIKey.setText(self.APIKEY)
            if (self.USERID != None): self.eveConfig.txtUserID.setText(self.USERID)
            dialog.resize(400,400)
            dialog.exec_()
        
def CreateApplet(parent):
    return EveApplet(parent)
