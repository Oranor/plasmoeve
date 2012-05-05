# -*- coding: utf-8 -*-
# by Iman Karim (imax@tha-imax.de)
# Released under GPLv2
from PyQt4.QtGui import QWidget
from config_ui import Ui_Dialog
from PyQt4.QtCore import QTimer, QString, Qt, SIGNAL, QRect
import eveapi


class eveConfig(QWidget,Ui_Dialog):
    def __init__(self,parent,defaultConfig = None):
        QWidget.__init__(self)
        self.parent = parent
        self.setupUi(self)
        self.txtStatus.setText("Hit 'Retrieve Characters' to continue.")
        
        self.connect(self.cmdRetrieveChars, SIGNAL("clicked()"), self.retrieveChars)
        
    def retrieveChars(self):
        self.lstChars.clear()
        
        found = False
        try:
            api = eveapi.EVEAPIConnection()
            result = api.account.Characters(keyID=self.txtUserID.text(), vCode=self.txtAPIKey.text())
            
        
            for c in result.characters:
                self.char = c
                found = True
                self.lstChars.addItem(c.name)
        except (Exception):
            pass
        
        if (found):
            self.txtStatus.setText("<html><font color='green'>Select your character in the List and click OK.")
        else:
            self.txtStatus.setText("<html><font color='red'>No characters found! Maybe invalid UserID\\API key?")
        
 