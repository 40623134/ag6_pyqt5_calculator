# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_Dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        '''以下為使用者自行編寫程式碼區'''

        num_button = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]
        for i in num_button:
            i.clicked.connect(self.digitClicked)
        self.clearAllButton.clicked.connect(self.clearAll)    
        
        self.wait = True
        #self.plusButton.clicked.connect(self.additiveOperatorClicked)
        
        self.clearButton.clicked.connect(self.clear)
        
        self.clearAllButton.clicked.connect(self.clearAll)
        
        self.clearButton.clicked.connect(self.clear)
        
        
        plus_minus = [self.plusButton,  self.minusButton]
        for i in plus_minus:
            i.clicked.connect(self.additiveOperatorClicked)
        
        #self.pendingAdditiveOperator = ''
        #self.temp=0
        
        self.pendingAdditiveOperator = ''
        self.pendingMultiplicativeOperator = ''
        
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        self.squareRootButton.clicked.connect(self.unaryOperatorClicked)
        
        self.equalButton.clicked.connect(self.equalClicked)
<<<<<<< HEAD
        self.pushButton_22.clicked.connect(self.pointClicked)
=======
    
>>>>>>> eeed6f05ab16d7ffca51a79e79be7e0a55a9feae

    def digitClicked(self):
        '''
        使用者按下數字鍵, 必須能夠累積顯示該數字
        當顯示幕已經為 0, 再按零不會顯示 00, 而仍顯示 0 或 0.0
        
        '''
        #pass
        #self.display.setText(self.display.text() + self.sender().text())
        
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())
        if self.display.text() == '0' and digitValue == 0:
            return
        if self.wait:
            self.display.clear()
            self.wait = False
        self.display.setText(self.display.text() + str(digitValue))
        
    def unaryOperatorClicked(self):
        '''單一運算元按下後處理方法'''
        pass
        
    def additiveOperatorClicked(self):
        '''加或減按下後進行的處理方法'''
        #pass
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        self.pendingAdditiveOperator = clickedOperator
        self.temp=float(self.display.text())
        self.display.clear()
        self.display.setText('0')
        self.wait=True
    def multiplicativeOperatorClicked(self):
        '''乘或除按下後進行的處理方法'''
        pass
        
    def equalClicked(self):
        '''等號按下後的處理方法'''
        #pass
        print(self.temp,self.display.text())
        self.display.setText(str(self.temp  + float(self.display.text())))
       
        
    def pointClicked(self):
        '''小數點按下後的處理方法'''
        #pass
        if self.wait:
            self.display.setText('0')

        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")

        self.waitingForOperand = False
        
    def changeSignClicked(self):
        '''變號鍵按下後的處理方法'''
        pass
        
    def backspaceClicked(self):
        '''回復鍵按下的處理方法'''
        pass
        
    def clear(self):
        '''清除鍵按下後的處理方法'''
        #pass
        # 清除顯示幕, 回復到原始顯示 0
        self.display.setText('0')
        # 重置判斷是否等待輸入運算數狀態
        self.waitingForOperand = True

        
    def clearAll(self):
        '''全部清除鍵按下後的處理方法'''
        #pass
        self.display.clear()
        self.display.setText('0')
        self.wait = True
    def clearMemory(self):
        '''清除記憶體鍵按下後的處理方法'''
        pass
        
    def readMemory(self):
        '''讀取記憶體鍵按下後的處理方法'''
        pass
        
    def setMemory(self):
        '''設定記憶體鍵按下後的處理方法'''
        pass
        
    def addToMemory(self):
        '''放到記憶體鍵按下後的處理方法'''
        pass
        
    def createButton(self):
        ''' 建立按鍵處理方法, 以 Qt Designer 建立對話框時, 不需要此方法'''
        pass
        
    def abortOperation(self):
        '''中斷運算'''
        pass
        
    def calculate(self):
        '''計算'''
        #pass
