# -*- coding: utf-8 -*-
#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from .Ui_Dialog import Ui_Dialog
import math

class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        '''以下為使用者自行編寫程式碼區'''
        #預設值
        #加減運算子 (Operator)
        self.pendingAdditiveOperator = ''
        #乘除運算子
        self.pendingMultiplicativeOperator = ''
        #記憶體的值
        self.sumInMemory = 0.0
        #上次運算用的值
        self.sumSoFar = 0.0
        self.factorSoFar = 0.0
        #等待運算的狀態
        self.waitingForOperand = True
        #數字
        number = [self.zero, self.one, self.two, self.three, self.four,
            self.five, self.six ,self.seven ,self.eight, self.nine]
        for i in number:
           i.clicked.connect(self.digitClicked)
        #清除鈕
        self.clearButton.clicked.connect(self.clear)
        self.clearAllButton.clicked.connect(self.clearAll)
        #小數點
        self.pointButton.clicked.connect(self.pointClicked)
        #加減號
        for button in [self.plusButton, self.minusButton]:
            button.clicked.connect(self.additiveOperatorClicked)
        #乘除號
        for button in [self.timesButton, self.divisionButton]:
            button.clicked.connect(self.multiplicativeOperatorClicked)
        #等於
        self.equalButton.clicked.connect(self.equalClicked)

        #self.pushButton_22.clicked.connect(self.pointClicked)


        #刪除
        self.backspaceButton.clicked.connect(self.backspaceClicked)
        #變號
        self.changeSignButton.clicked.connect(self.changeSignClicked)
         # 單一運算子
        unaryOperator = [self.squareRootButton, self.powerButton,  self.reciprocalButton ]
        for i in unaryOperator:
            i.clicked.connect(self.unaryOperatorClicked)
        # 設定記憶
        #self.setMemoryButton.clicked.connect(self.setMemory)
        # 加入記憶體
        #self.addToMemoryButton.clicked.connect(self.addToMemory)
    
    def digitClicked(self):
        '''
        使用者按下數字鍵, 必須能夠累積顯示該數字
        當顯示幕已經為 0, 再按零不會顯示 00, 而仍顯示 0 或 0.0
        
        '''
        button = self.sender()
       
        if self.display.text() == '0' and int(button.text())== 0.0:
            return
        #清除螢幕 (運算的時候)
        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False
        #疊加數字
        self.display.setText(self.display.text() + button.text())
    
    def unaryOperatorClicked(self):
        '''單一運算元按下後處理方法'''
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())
 
        if clickedOperator == "Sqrt":
            if operand < 0.0:
                self.abortOperation()
                return
 
            result = math.sqrt(operand)
        elif clickedOperator == "X^2":
            result = math.pow(operand, 2.0)
        elif clickedOperator == "1/x":
            if operand == 0.0:
                self.abortOperation()
                return
 
            result = 1.0 / operand
 
        self.display.setText(str(result))
        self.waitingForOperand = True
        
    def additiveOperatorClicked(self):
        '''加或減按下後進行的處理方法'''
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())
        #乘除運算
        if self.pendingMultiplicativeOperator:
            '''
            計算：self.calculate(乘數或除數, 運算子)
            回傳 bool 以知道運算成功與否
            Python 文法：[if not 結果:] 當失敗時執行 self.abortOperation()。
            '''
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
            #上次的結果
            self.display.setText(str(self.factorSoFar))
            #交換 operand 和 self.factorSoFar
            operand, self.factorSoFar = self.factorSoFar, 0.0
            self.pendingMultiplicativeOperator = ''
        #加減運算
        if self.pendingAdditiveOperator:
            '''
            同上
            '''
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return
            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand
        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True
    def multiplicativeOperatorClicked(self):
        '''乘或除按下後進行的處理方法'''
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())
        #乘除計算
        if self.pendingMultiplicativeOperator:
            '''
            同加減法
            '''
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand
        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True    
    def equalClicked(self):
        '''等號按下後的處理方法'''
        operand = float(self.display.text())
        '''
        同乘除
        '''
        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''
        '''
        同加減
        '''
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
        if self.waitingForOperand:
            return
 
        text = self.display.text()[:-1]
        if not text:
            text = '0'
            self.waitingForOperand = True
 
        self.display.setText(text)
        
    def clear(self):
        '''清除鍵按下後的處理方法'''
        #留著前面的數字
        if self.waitingForOperand:
            #下面不會執行
            return
        #清除
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
     
    def pointClicked(self):
        '''小數點按下後的處理方法'''
        #空白的時候直接按小數點。
        if self.waitingForOperand:
            #加 0。
            self.display.setText('0')
        #沒有小數點再加。
        if "." not in self.display.text():
            self.display.setText(self.display.text() + ".")
        self.waitingForOperand = False
     
    def abortOperation(self):
        '''中斷運算'''
        self.clearAll()
        self.display.setText("####")
    def calculate(self, rightOperand, pendingOperator):
        '''計算'''
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        elif pendingOperator == "-":
            self.sumSoFar -= rightOperand
        elif pendingOperator == "*":
            self.factorSoFar *= rightOperand
        elif pendingOperator == "/":
            #分母不能為零
            if rightOperand == 0.0:
                return False
            self.factorSoFar /= rightOperand
        return True
