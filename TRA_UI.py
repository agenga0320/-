# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:23:47 2019

@author: Vincent Chen
"""

#import TRA_find
import sys
from PyQt5.QtWidgets import QPushButton, QGridLayout ,QWidget ,QCalendarWidget,QLabel,QComboBox,QLineEdit,QTableWidget,QTableWidgetItem
from PyQt5.QtCore import Qt ,QDate
from PyQt5 import QtCore ,QtWidgets ,QtGui
from PyQt5.QtGui import QIntValidator
import algorithm
import odata_api
import TRABooking

    
time=[]
for i in range(0,24):
    time.append(str(i)+":00")
    
Tags = {'0900':'基隆','0910':'三坑','0920':'八堵','0930':'七堵','0940':'百福',
        '0950':'五堵','0960':'汐止','0970':'汐科','0980':'南港','0990':'松山',
        '1000':'臺北','1001':'臺北-環島','1010':'萬華','1020':'板橋','1030':'浮洲','1040':'樹林',
        '1050':'南樹林','1060':'山佳','1070':'鶯歌','1080':'桃園','1090':'內壢',
        '1100':'中壢','1110':'埔心','1120':'楊梅','1130':'富岡','1140':'新富',
        '1150':'北湖','1160':'湖口','1170':'新豐','1180':'竹北','1190':'北新竹',
        '1191':'千甲','1192':'新莊','1193':'竹中','1194':'六家',
        '1201':'上員','1202':'榮華','1203':'竹東','1204':'橫山','1205':'九讚頭',
        '1206':'合興','1207':'富貴','1208':'內灣','1210':'新竹','1220':'三姓橋',
        '1230':'香山','1240':'崎頂','1250':'竹南',
        '2110':'談文','2120':'大山','2130':'後龍','2140':'龍港',
        '2150':'白沙屯','2160':'新埔','2170':'通霄','2180':'苑裡','2190':'日南',
        '2200':'大甲','2210':'臺中港','2220':'清水','2230':'沙鹿','2240':'龍井',
        '2250':'大肚','2260':'追分','3140':'造橋','3150':'豐富','3160':'苗栗',
        '3170':'南勢','3180':'銅鑼','3190':'三義',
        '3210':'泰安','3220':'后里','3230':'豐原','3240':'栗林','3250':'潭子',
        '3260':'頭家厝','3270':'松竹','3280':'太原','3290':'精武',
        '3300':'臺中','3310':'五權','3320':'大慶','3330':'烏日','3340':'新烏日',
        '3350':'成功','3360':'彰化','3370':'花壇','3380':'大村','3390':'員林',
        '3400':'永靖','3410':'社頭','3420':'田中','3430':'二水','3431':'源泉',
        '3432':'濁水','3433':'龍泉','3434':'集集','3435':'水里','3436':'車埕',
        '3450':'林內','3460':'石榴','3470':'斗六','3480':'斗南','3490':'石龜',
        '4050':'大林','4060':'民雄','4070':'嘉北','4080':'嘉義','4090':'水上',
        '4100':'南靖','4110':'後壁','4120':'新營','4130':'柳營','4140':'林鳳營',
        '4150':'隆田','4160':'拔林','4170':'善化','4180':'南科','4190':'新市',
        '4200':'永康','4210':'大橋','4220':'臺南','4250':'保安','4260':'仁德',
        '4270':'中洲','4271':'長榮大學','4272':'沙崙','4290':'大湖',
        '4300':'路竹','4310':'岡山','4320':'橋頭','4330':'楠梓','4340':'新左營',
        '4350':'左營','4360':'內惟','4370':'美術館','4380':'鼓山','4390':'三塊厝',
        '4400':'高雄','4410':'民族','4420':'科工館','4430':'正義','4440':'鳳山',
        '4450':'後庄','4460':'九曲堂','4470':'六塊厝',
        '5000':'屏東','5010':'歸來','5020':'麟洛','5030':'西勢','5040':'竹田',
        '5050':'潮州','5060':'崁頂','5070':'南州','5080':'鎮安','5090':'林邊',
        '5100':'佳冬','5110':'東海','5120':'枋寮','5130':'加祿','5140':'內獅','5160':'枋山','5190':'大武',
        '5200':'瀧溪','5210':'金崙','5220':'太麻里','5230':'知本','5240':'康樂',
        '6000':'臺東','6010':'山里','6020':'鹿野','6030':'瑞源','6040':'瑞和',
        '6050':'關山','6060':'海端','6070':'池上','6080':'富里','6090':'東竹',
        '6100':'東里','6110':'玉里','6120':'三民','6130':'瑞穗','6140':'富源',
        '6150':'大富','6160':'光復','6170':'萬榮','6180':'鳳林','6190':'南平',
        '6200':'林榮新光','6210':'豐田','6220':'壽豐','6230':'平和','6240':'志學','6250':'吉安',
        '7000':'花蓮','7010':'北埔','7020':'景美','7030':'新城','7040':'崇德',
        '7050':'和仁','7060':'和平','7070':'漢本','7080':'武塔','7090':'南澳',
        '7100':'東澳','7110':'永樂','7120':'蘇澳','7130':'蘇澳新','7140':'新馬',
        '7150':'冬山','7160':'羅東','7170':'中里','7180':'二結','7190':'宜蘭',
        '7200':'四城','7210':'礁溪','7220':'頂埔','7230':'頭城','7240':'外澳',
        '7250':'龜山','7260':'大溪','7270':'大里','7280':'石城','7290':'福隆',
        '7300':'貢寮','7310':'雙溪','7320':'牡丹','7330':'三貂嶺',
        '7331':'大華','7332':'十分','7333':'望古','7334':'嶺腳','7335':'平溪','7336':'菁桐',
        '7350':'猴硐','7360':'瑞芳','7361':'海科館','7362':'八斗子','7380':'四腳亭','7390':'暖暖'}

Tags2 = dict(zip(Tags.values(), Tags.keys()))

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import networkx as nx
import json
from mpl_toolkits.basemap import Basemap
import pandas as pd
puyuma = ['1107']
taroko = ['1101']
pp = ['1102','1104','1105','1106','1108','1109','110A','110B','110C']
de = ['1100','1103','110D','110E','110F']
GF = ['1110','1111','1112','1113','1114','1115','1120']
station = open('Station.json', 'r',encoding='utf-8-sig') 
station = station.read()
station = json.loads(station)
staList = pd.DataFrame(station['Stations'])
stu = staList['StationName'].apply(pd.Series)
stv = staList['StationPosition'].apply(pd.Series)
staPosDF = pd.concat([stu['Zh_tw'],stv], axis=1)
Tags2 = dict(zip(Tags.values(), Tags.keys()))
minlon, maxlon = 119.8, 122.3
minlat, maxlat = 21.5, 25.5
m = Basemap(projection='merc', llcrnrlat=minlat, urcrnrlat=maxlat,llcrnrlon=minlon, urcrnrlon=maxlon, lat_ts=30, resolution='h')
print('地圖套件建立完畢')

def IDnumCheck(s):
    a = 0
    num = 0
    try:
        if s[0] == 'A' : a = 10
        elif s[0] == 'B' : a = 11
        elif s[0] == 'C' : a = 12
        elif s[0] == 'D' : a = 13
        elif s[0] == 'E' : a = 14
        elif s[0] == 'F' : a = 15
        elif s[0] == 'G' : a = 16
        elif s[0] == 'H' : a = 17
        elif s[0] == 'I' : a = 34
        elif s[0] == 'J' : a = 18
        elif s[0] == 'K' : a = 19
        elif s[0] == 'L' : a = 20
        elif s[0] == 'M' : a = 21
        elif s[0] == 'N' : a = 22
        elif s[0] == 'O' : a = 35
        elif s[0] == 'P' : a = 23
        elif s[0] == 'Q' : a = 24
        elif s[0] == 'R' : a = 25
        elif s[0] == 'S' : a = 26
        elif s[0] == 'T' : a = 27
        elif s[0] == 'U' : a = 28
        elif s[0] == 'V' : a = 29
        elif s[0] == 'W' : a = 32
        elif s[0] == 'X' : a = 30
        elif s[0] == 'Y' : a = 31
        elif s[0] == 'Z' : a = 33
        num = int(a / 10) + (a % 10) * 9
        print(num)
        for x in range(8) :
            num += int(s[x + 1]) * (9 - x - 1)
        num += int(s[9])
        if num % 10 == 0 :
            return 1
        else :
            return 0
    except:
        return 0 

class TrainBtn(QPushButton):
    def __init__(self,name,id,parent):
        super(TrainBtn,self).__init__(name,parent)
        self.id = id
        self.clicked.connect(self.click)
        self.setIcon(QtGui.QIcon("./booking.png"))
    def click(self):
        path, ticketnum, Graph = algorithm.searchByTrainNo(window.c.selectedDate().toString("yyyy-MM-dd"),self.id,str(window.cb1.currentText()),str(window.cb2.currentText()))
        window3.toplb.setText("<h2>"+str(path)+"<\h2>")
        window3.midlbright.setText(str(ticketnum))
        window.textbox.setText(str(self.id))
        window3.axes.clear()
        window.drawMap(path,ticketnum,Graph)
        window3.mainlb.setText("<h1>"+str(window.c.selectedDate().toString("yyyy-MM-dd"))+" "+str(self.id)+" 車次 最佳切票建議</h1>")
        if len(path) == 0:
            window3.b1.setEnabled(False)
        else:
            window3.b1.setEnabled(True)
        window3.fromWindow2 = 1
        window2.hide()
        window3.show()

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        
        self.title = "臺鐵對號列車切票查詢系統"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        self.labels()
        self.tb()
        self.cal()
        self.cbbox()
        self.btn()
        
    def labels(self):
        self.l = QLabel(self)
        self.l.setText("<h1>請選擇時間及起終點<\h1>")
        self.grid_layout.addWidget(self.l,0,0,1,8)
        self.l.setAlignment(Qt.AlignCenter)
        self.baffer = QLabel(self)
        self.grid_layout.addWidget(self.baffer,4,0,1,8)
        self.text1 = QLabel(self)
        self.text1.setText("<h3>出發站:<\h3>")
        self.grid_layout.addWidget(self.text1,1,4,1,1)
        self.text2 = QLabel(self)
        self.text2.setText("<h3>抵達站:<\h3>")
        self.grid_layout.addWidget(self.text2,1,6,1,1)
        self.text3 = QLabel(self)
        self.text3.setText("<h3>車次:<\h3>")
        self.grid_layout.addWidget(self.text3,2,4,1,1)
        self.text4 = QLabel(self)
        self.text4.setText("<h3>時間:<\h3>")
        self.grid_layout.addWidget(self.text4,3,4,1,1)
        
    def tb(self):
        self.onlyInt = QIntValidator()
        self.textbox = QLineEdit(self)
        self.textbox.setValidator(self.onlyInt)
        self.textbox.setFixedWidth(100)
        self.grid_layout.addWidget(self.textbox,2,5,1,1)
        
    def cal(self):
        self.c = QCalendarWidget(self)
        self.grid_layout.addWidget(self.c,1,0,3,4)
        self.c.setMinimumDate(QDate.currentDate())
        if QDate.currentDate().dayOfWeek() == 5 :
            self.c.setMaximumDate(QDate.currentDate().addDays(16))
        else:
            self.c.setMaximumDate(QDate.currentDate().addDays(14))
        
    def cbbox(self):
        self.cb1 = QComboBox(self)
        self.cb1.addItems(Tags.values())
        self.grid_layout.addWidget(self.cb1,1,5,1,1)
        self.cb2 = QComboBox(self)
        self.cb2.addItems(Tags.values())
        self.grid_layout.addWidget(self.cb2,1,7,1,1)
        self.cb3 = QComboBox(self)
        self.cb3.addItems(time)
        self.grid_layout.addWidget(self.cb3,3,5,1,1)
        
        self.time = str(self.cb3.currentText())
        
    def btn(self):
        self.car = ""
        self.b1 = QPushButton("車次搜尋",self)
        self.b1.clicked.connect(self.clicknumber)
        self.grid_layout.addWidget(self.b1,2,6,1,2)
        self.b2 = QPushButton("時間搜尋",self)
        self.b2.clicked.connect(self.clicktime)
        self.grid_layout.addWidget(self.b2,3,6,1,2)
        
    def clicknumber(self):
        if self.textbox.text() == "" :
            QtWidgets.QMessageBox.warning(self, "警告", "車次未填寫", QtWidgets.QMessageBox.Cancel)
        elif str(self.cb1.currentText()) == str(self.cb2.currentText()) :
            QtWidgets.QMessageBox.warning(self, "警告", "起終點不能相同", QtWidgets.QMessageBox.Cancel)
        else:
            window3.axes.clear()
            path,ticketnum,Graph = algorithm.searchByTrainNo(self.c.selectedDate().toString("yyyy-MM-dd"),str(self.textbox.text()),str(self.cb1.currentText()),str(self.cb2.currentText()))
            self.drawMap(path,ticketnum,Graph)
            window3.toplb.setText("<h2>"+str(path)+"<\h2>")
            window3.mainlb.setText("<h1>"+str(self.c.selectedDate().toString("yyyy-MM-dd"))+" "+str(self.textbox.text())+" 車次 最佳切票建議</h1>")
            window3.midlbright.setText(str(ticketnum))
            self.hide()
            window3.show()
            if len(path) == 0:
                window3.b1.setEnabled(False)
            else:
                window3.b1.setEnabled(True)
                
    def drawMap(self,path, maxTicketNum,Graph):
        Graph = Graph.subgraph(path)
        nodePos={}
        for i in Graph.nodes():
            staName=staPosDF.loc[staPosDF['Zh_tw']==i]['Zh_tw']
            lon=staPosDF.loc[staPosDF['Zh_tw']==i]['PositionLon']
            lat=staPosDF.loc[staPosDF['Zh_tw']==i]['PositionLat']
            try:
                nodePos[staName.iloc[0]]=m(lon.iloc[0],lat.iloc[0])
            except:
                print(i)
        freeSeatDic = algorithm.UpdateEdgeLabel(Graph)
        # draw on map       
        nx.draw_networkx(Graph,pos=nodePos,node_size=80,node_color='green',font_size=12,font_color='r',font_weight='bold',alpha=0.5,ax=window3.axes)
        nx.draw_networkx_edge_labels(Graph,pos=nodePos,edge_labels=freeSeatDic,font_size=10,ax=window3.axes)
        m.drawcoastlines()
        m.drawmapboundary(fill_color='w', linewidth=0)
        m.plot(120,21, latlon=False,ax=window3.axes)
        window3.canvas.draw()
        
    def clicktime(self):
        if str(self.cb1.currentText()) == str(self.cb2.currentText()) :
            QtWidgets.QMessageBox.warning(self, "警告", "起終點不能相同", QtWidgets.QMessageBox.Cancel)
        else:
            self.car = odata_api.timesearch2(self.c.selectedDate().toString("yyyy-MM-dd"),str(self.cb3.currentText()),str(self.cb1.currentText()),str(self.cb2.currentText()))
            self.hide()
            window2.show()
            #print(str(self.car))
            window2.table.setRowCount(self.car.shape[0])
            
            for i in range(self.car.shape[0]):
                window2.table.setRowHeight(i,40)
                for j in range(4):
                    if j == 0 :
                        item = QTableWidgetItem(str(self.car.iloc[i,j]))
                        item.setTextAlignment(Qt.AlignCenter)
                        window2.table.setItem(i,j,item)
                    elif j >= 2:
                        item = QTableWidgetItem(str(self.car.iloc[i,j+1].strftime("%H:%M")))
                        item.setTextAlignment(Qt.AlignCenter)
                        window2.table.setItem(i,j,item)
                    
                    else :
                        if str(self.car.iloc[i,j+1]).find('柴聯') == -1:
                            if str(self.car.iloc[i,1]) in pp:
                                trainIcon = QtGui.QIcon("./3.png")
                            elif str(self.car.iloc[i,1]) in GF:
                                trainIcon = QtGui.QIcon("./4.png")
                            elif str(self.car.iloc[i,1]) in taroko:
                                trainIcon = QtGui.QIcon("./1.png")
                            elif str(self.car.iloc[i,1]) in puyuma:
                                trainIcon = QtGui.QIcon("./2.png")
                            icon = QTableWidgetItem(trainIcon, str(self.car.iloc[i,j+1]))  # 圖片+文字 
                        else:
                            icon = QTableWidgetItem(QtGui.QIcon("./8.png"), str(self.car.iloc[i,j+1])) 
                        window2.table.setItem(i,j, icon)
                        #item = QTableWidgetItem(str(self.car.iloc[i,j+1]))
                        #item.setTextAlignment(Qt.AlignCenter)
                        #window2.table.setItem(i,j,item)
            btn=[]
            for i in range(self.car.shape[0]):
                btn.append(TrainBtn("確認",str(self.car.iloc[i,0]),self))
                window2.table.setCellWidget(i,4,btn[i])
            window2.header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
            window2.title.setText("<h1>"+str(window.cb1.currentText())+" 到 "+str(window.cb2.currentText())+" "+self.c.selectedDate().toString("yyyy-MM-dd")+" "+str(self.cb3.currentText())+" 出發 4小時內可搭乘對號列車</h1>")
            #window2.table.resizeColumnsToContents()
        
class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        
        self.title = "臺鐵對號列車切票查詢系統"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        self.title = QLabel(self)
        self.title.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.title,0,0,1,8)
        
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setVerticalScrollMode
        self.table.setIconSize(QtCore.QSize(24,30))
        self.header = self.table.horizontalHeader()   
        self.table.setHorizontalHeaderLabels(["車次","車種","出發時間","抵達時間","確定"])
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows) 
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.table.setColumnWidth(0,45)
        self.table.setColumnWidth(1,230)
        self.grid_layout.addWidget(self.table,1,1,3,6)
        
        
        self.btn = QPushButton("返回",self)
        self.grid_layout.addWidget(self.btn,4,2,1,4)
        self.btn.clicked.connect(self.back)
        
    def back(self):
        window2.hide()
        window.show()
        
        

class Window3(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.title = "臺鐵對號列車切票查詢系統"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.fromWindow2 = 0
        self.InitWindow()
        
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        
        self.lb()
        self.tb()
        self.cb()
        self.btn()
        
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self.figure)
        self.grid_layout.addWidget(self.canvas,1,2,1,2)
        
    def lb(self):
        self.mainlb = QLabel(self)
        self.mainlb.setText("<h1>建議最佳切票</h1>")
        self.mainlb.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.mainlb,0,0,1,6)
        self.toplb = QLabel(self)
        self.toplb.setText("123")
        self.toplb.setAlignment(Qt.AlignCenter)
        self.grid_layout.addWidget(self.toplb,1,1,1,1)
        self.midlbleft = QLabel(self)
        self.midlbleft.setText("<h2>剩餘數量：<\h2>")
        self.midlbleft.setAlignment(Qt.AlignLeft)
        self.grid_layout.addWidget(self.midlbleft,2,2,1,1)
        self.midlbright = QLabel(self)
        self.midlbright.setText("123")
        self.midlbright.setAlignment(Qt.AlignLeft)
        self.grid_layout.addWidget(self.midlbright,2,3,1,1)
        self.IDlb = QLabel(self)
        self.IDlb.setText("<h2>請輸入身分證字號：<\h2>")
        self.IDlb.setFixedHeight(100)
        self.grid_layout.addWidget(self.IDlb,3,2,1,1)
        self.ticlb = QLabel(self)
        self.ticlb.setText("<h2>訂購張數：<\h2>")
        self.ticlb.setFixedHeight(100)
        self.grid_layout.addWidget(self.ticlb,4,2,1,1)
        
    def tb(self):
        self.textbox = QLineEdit(self)
        self.textbox.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        self.grid_layout.addWidget(self.textbox,3,3,1,2)
        
    def cb(self):
        num=[]
        for i in range(1,7):
            num.append(str(i))
        self.combobox = QComboBox(self)
        self.combobox.addItems(num)
        self.grid_layout.addWidget(self.combobox,4,3,1,1)
        
    def btn(self):
        self.b1 = QPushButton("確認訂票",self)
        self.b1.setFixedHeight(50)
        self.b1.setIcon(QtGui.QIcon("./booking.png"))
        self.b1.setIconSize(QtCore.QSize(40,40))
        self.grid_layout.addWidget(self.b1,5,2,1,1)
        self.b1.clicked.connect(self.send)
        self.b2 = QPushButton("重新選擇",self)
        self.b2.setFixedHeight(50)
        self.grid_layout.addWidget(self.b2,5,3,1,1)
        self.b2.clicked.connect(self.back)
        
    def send(self):
        doc = QtGui.QTextDocument()
        doc.setHtml(self.toplb.text())
        text = doc.toPlainText()
        print(text)
        lst = []
        sw = 0
        temp = ""
        for i in text:
            if i == "'":
                if sw == 0:
                    sw = 1
                else:
                    sw = 0
                    lst.append(temp)
                    temp = ""
                continue
            if sw == 1:
                temp += i
        numlst = []
        for i in lst:
            numlst.append(Tags2[str(i)])
        print(numlst)
        if int(self.combobox.currentText()) > int(self.midlbright.text()) :
            QtWidgets.QMessageBox.warning(self, "警告", "票券不足", QtWidgets.QMessageBox.Cancel)
        elif self.textbox.text() == "":
            QtWidgets.QMessageBox.warning(self, "警告", "請輸入身分證字號", QtWidgets.QMessageBox.Cancel)
        elif len(self.textbox.text()) != 10 :
            QtWidgets.QMessageBox.warning(self, "警告", "身分證字號長度錯誤", QtWidgets.QMessageBox.Cancel)
        elif IDnumCheck(self.textbox.text()) == 0:
            QtWidgets.QMessageBox.warning(self, "警告", "身分證字號格式錯誤", QtWidgets.QMessageBox.Cancel)
        elif (len(numlst)-1)*int(self.combobox.currentText()) > 6:
            QtWidgets.QMessageBox.warning(self, "警告", "超過購買總張數限制", QtWidgets.QMessageBox.Cancel)
        else:
            TRABooking.buyTicket(algorithm.toPairList(numlst),window.c.selectedDate().toString("yyyyMMdd"),self.textbox.text(),window.textbox.text(),int(self.combobox.currentText()))
        
    def back(self):
        if self.fromWindow2 == 0:
            window3.hide()
            window.show()
        else:
            window3.hide()
            window2.show()
            self.fromWindow2 = 0
        
if __name__ == "__main__" :
    app = QtCore.QCoreApplication.instance()
    
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        app_icon = QtGui.QIcon("2.png")
        app.setWindowIcon(app_icon)
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        
    window = Window()
    window.show()
    window2 = Window2()
    window3 = Window3()

    sys.exit(app.exec())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:24:55 2019

@author: Vincent Chen
"""

