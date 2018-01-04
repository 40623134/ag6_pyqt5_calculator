# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog
from .Ui_Dialog import Ui_Dialog
 
class Dialog(QDialog, Ui_Dialog):
<<<<<<< HEAD
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
        
        self.changeButton.clicked.connect(self.changeSignClicked)
        
        self.backspaceButton.clicked.connect(self.backspaceClicked)
        
        
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
        pass
        
    def changeSignClicked(self):
        '''變號鍵按下後的處理方法'''
        #pass
        text = self.display.text()
        value = float(text)
 
        if value > 0.0:
            text = "-" + text
        elif value < 0.0:
            text = text[1:]
 
        self.display.setText(text)
        
    def backspaceClicked(self):
        if self.wait:
            return
 
        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.wait = True
 
        self.display.setText(text)
        
    def clear(self):
        '''清除鍵按下後的處理方法'''
        #pass
        # 清除顯示幕, 回復到原始顯示 0
        self.display.setText('0')
        # 重置判斷是否等待輸入運算數狀態
        self.waitingForOperand = True


     def clear(self):
         if self.waitingForOperand:
            return
         #重新顯示 0
         self.display.setText('0')
         self.waitingForOperand = True
     
     #重設所有狀態
     def clearAll(self):
         self.sumSoFar = 0.0
         self.factorSoFar = 0.0
         self.pendingAdditiveOperator = ''
         self.pendingMultiplicativeOperator = ''
         self.display.setText('0')
         self.waitingForOperand = True
     
     def backspaceClicked(self):
         if self.waitingForOperand:
             return
         #取得螢幕上的文字 (拿走最後一項)
         text = self.display.text()[:-1]
         #如果沒有文字
         if not text:
             text = '0'
             self.waitingForOperand = True
         #設定數字到螢幕上
         self.display.setText(text)
     
     def pointClicked(self):
         '''
         如果等待輸入，
         按下小數點，相當於輸入 0.xxx，
         因此自動補零。
         '''
         if self.waitingForOperand:
             self.display.setText('0')
         #若沒有小數點，補上。
         if "." not in self.display.text():
             self.display.setText(self.display.text() + ".")
         self.waitingForOperand = False
     
     def additiveOperatorClicked(self):
         clickedButton = self.sender()
         #取得按鈕符號 (運算子)
         clickedOperator = clickedButton.text()
         #取得螢幕上的文字，轉成小數
         operand = float(self.display.text())
         #如果有乘除運算子
         if self.pendingMultiplicativeOperator:
             #如果計算，且失敗。
             if not self.calculate(operand, self.pendingMultiplicativeOperator):
                 self.abortOperation()
                 return
             #先顯示結果
             self.display.setText(str(self.factorSoFar))
             #儲存結果到 operand 名稱 (name) 裡。
             operand = self.factorSoFar
             self.factorSoFar = 0.0
             self.pendingMultiplicativeOperator = ''
         #如果有加減運算子
         if self.pendingAdditiveOperator:
             #如果計算，且失敗。
             if not self.calculate(operand, self.pendingAdditiveOperator):
                 self.abortOperation()
                 return
             #顯示結果
             self.display.setText(str(self.sumSoFar))
         else:
             #如果沒有加減運算子，儲存乘除的結果。
             self.sumSoFar = operand
         #儲存按鈕符號
         self.pendingAdditiveOperator = clickedOperator
         self.waitingForOperand = True
     
     def multiplicativeOperatorClicked(self):
         clickedButton = self.sender()
         clickedOperator = clickedButton.text()
         operand = float(self.display.text())
         if self.pendingMultiplicativeOperator:
             if not self.calculate(operand, self.pendingMultiplicativeOperator):
                 self.abortOperation()
                 return
             self.display.setText(str(self.factorSoFar))
         else:
             self.factorSoFar = operand
         self.pendingMultiplicativeOperator = clickedOperator
         self.waitingForOperand = True
     
     """
     計算 (被除數, 運算子)，回傳計算結果
     True: 成功
     False: 失敗
     """
     def calculate(self, rightOperand, pendingOperator):
         if pendingOperator == "+":
             self.sumSoFar += rightOperand
         elif pendingOperator == "-":
             self.sumSoFar -= rightOperand
         elif pendingOperator == "*":
             self.factorSoFar *= rightOperand
         elif pendingOperator == "/":
             #防止除零
             if rightOperand == 0.0:
                 return False
             self.factorSoFar /= rightOperand
         return True
     
     #Error 畫面 "####"
     def abortOperation(self):
          self.clearAll()
          self.display.setText("Nope!! Don't copy our calculator.")
     
     def equalClicked(self):
         operand = float(self.display.text())
         if self.pendingMultiplicativeOperator:
             if not self.calculate(operand, self.pendingMultiplicativeOperator):
                 self.abortOperation()
                 return
             operand = self.factorSoFar
             self.factorSoFar = 0.0
             self.pendingMultiplicativeOperator = ''
         if self.pendingAdditiveOperator:
             if not self.calculate(operand, self.pendingAdditiveOperator):
                 self.abortOperation()
                 return
             self.pendingAdditiveOperator = ''
         else:
             self.sumSoFar = operand
         self.display.setText(str(self.sumSoFar))
         self.sumSoFar = 0.0
         self.waitingForOperand = True
