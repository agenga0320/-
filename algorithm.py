import json
import codecs
import pandas as pd
import numpy as np
import requests
import networkx as nx
import matplotlib.pyplot as plt
# matplotlib 顯示中文字形 ##########################################
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Microsoft JhengHei','sans-serif']
# 代號站名對照表####################################################
Tags = {'0900':'基隆','0910':'三坑','0920':'八堵','0930':'七堵','0940':'百福','0950':'五堵','0960':'汐止','0970':'汐科','0980':'南港','0990':'松山','1000':'臺北','1001':'臺北-環島','1010':'萬華','1020':'板橋','1030':'浮洲','1040':'樹林','1050':'南樹林','1060':'山佳','1070':'鶯歌','1080':'桃園','1090':'內壢','1100':'中壢','1110':'埔心','1120':'楊梅','1130':'富岡','1140':'新富','1150':'北湖','1160':'湖口','1170':'新豐','1180':'竹北','1190':'北新竹','1191':'千甲','1192':'新莊','1193':'竹中','1194':'六家','1201':'上員','1202':'榮華','1203':'竹東','1204':'橫山','1205':'九讚頭','1206':'合興','1207':'富貴','1208':'內灣','1210':'新竹','1220':'三姓橋','1230':'香山','1240':'崎頂','1250':'竹南','2110':'談文','2120':'大山','2130':'後龍','2140':'龍港','2150':'白沙屯','2160':'新埔','2170':'通霄','2180':'苑裡','2190':'日南','2200':'大甲','2210':'臺中港','2220':'清水','2230':'沙鹿','2240':'龍井','2250':'大肚','2260':'追分','3140':'造橋','3150':'豐富','3160':'苗栗','3170':'南勢','3180':'銅鑼','3190':'三義','3210':'泰安','3220':'后里','3230':'豐原','3240':'栗林','3250':'潭子','3260':'頭家厝','3270':'松竹','3280':'太原','3290':'精武','3300':'臺中','3310':'五權','3320':'大慶','3330':'烏日','3340':'新烏日','3350':'成功','3360':'彰化','3370':'花壇','3380':'大村','3390':'員林','3400':'永靖','3410':'社頭','3420':'田中','3430':'二水','3431':'源泉','3432':'濁水','3433':'龍泉','3434':'集集','3435':'水里','3436':'車埕','3450':'林內','3460':'石榴','3470':'斗六','3480':'斗南','3490':'石龜','4050':'大林','4060':'民雄','4070':'嘉北','4080':'嘉義','4090':'水上','4100':'南靖','4110':'後壁','4120':'新營','4130':'柳營','4140':'林鳳營','4150':'隆田','4160':'拔林','4170':'善化','4180':'南科','4190':'新市','4200':'永康','4210':'大橋','4220':'臺南','4250':'保安','4260':'仁德','4270':'中洲','4271':'長榮大學','4272':'沙崙','4290':'大湖','4300':'路竹','4310':'岡山','4320':'橋頭','4330':'楠梓','4340':'新左營','4350':'左營','4360':'內惟','4370':'美術館','4380':'鼓山','4390':'三塊厝','4400':'高雄','4410':'民族','4420':'科工館','4430':'正義','4440':'鳳山','4450':'後庄','4460':'九曲堂','4470':'六塊厝','5000':'屏東','5010':'歸來','5020':'麟洛','5030':'西勢','5040':'竹田','5050':'潮州','5060':'崁頂','5070':'南州','5080':'鎮安','5090':'林邊','5100':'佳冬','5110':'東海','5120':'枋寮','5130':'加祿','5140':'內獅','5160':'枋山','5190':'大武','5200':'瀧溪','5210':'金崙','5220':'太麻里','5230':'知本','5240':'康樂','6000':'臺東','6010':'山里','6020':'鹿野','6030':'瑞源','6040':'瑞和','6050':'關山','6060':'海端','6070':'池上','6080':'富里','6090':'東竹','6100':'東里','6110':'玉里','6120':'三民','6130':'瑞穗','6140':'富源','6150':'大富','6160':'光復','6170':'萬榮','6180':'鳳林','6190':'南平','6200':'林榮新光','6210':'豐田','6220':'壽豐','6230':'平和','6240':'志學','6250':'吉安','7000':'花蓮','7010':'北埔','7020':'景美','7030':'新城','7040':'崇德','7050':'和仁','7060':'和平','7070':'漢本','7080':'武塔','7090':'南澳','7100':'東澳','7110':'永樂','7120':'蘇澳','7130':'蘇澳新','7140':'新馬','7150':'冬山','7160':'羅東','7170':'中里','7180':'二結','7190':'宜蘭','7200':'四城','7210':'礁溪','7220':'頂埔','7230':'頭城','7240':'外澳','7250':'龜山','7260':'大溪','7270':'大里','7280':'石城','7290':'福隆','7300':'貢寮','7310':'雙溪','7320':'牡丹','7330':'三貂嶺','7331':'大華','7332':'十分','7333':'望古','7334':'嶺腳','7335':'平溪','7336':'菁桐','7350':'猴硐','7360':'瑞芳','7361':'海科館','7362':'八斗子','7380':'四腳亭','7390':'暖暖'}
# 下載剩餘車票資訊 #################################################
try:
    seatData = requests.get('http://ods.railway.gov.tw/tra-ods-web/ods/download/dataResource/5a2e672be26f4467a98f121d9ef43885').json()
except:
    seatFile=open('seat.json', 'r',encoding='utf-8-sig') 
    seatData = json.loads(seatFile.read())
seatTable = pd.DataFrame(seatData,columns=['trnOpDate','trnNo','seatOriStaCode','seatDstStaCode','freeSeats'])
# BaseMap 設定地圖邊界 ####################################################
from mpl_toolkits.basemap import Basemap
minlon, maxlon = 120, 122
minlat, maxlat = 21.5, 25.5
mapExists = 0               #尚未初始化地圖

# 用給定的條件搜尋最短切票路徑，並回傳最短切票路徑 list、最多可訂張數、班次所有剩餘車票 pair 圖
# Parameters:
#   date (string): 'YYYY-MM-DD'
#   trainNo (string): '1234'
#   oriStation (string): '臺北'
#   arrStation (string): '高雄'
# Returns:
#   availPath (list): ['臺北','臺中','高雄']
#   maxTicketCount (int): 5
#   allPairGraph (nx.DiGraph): 
# Example: 
#   availPath, maxTicketCount, allPairGraph = searchByTrainNo('2019-05-24', '123', '臺北', '高雄')

def searchByTrainNo(date, trainNo, oriStation, arrStation):
    query = seatTable.loc[(seatTable['trnNo'] == trainNo) & (seatTable['trnOpDate'] == date)].replace(Tags)
    query['freeSeats'] = query['freeSeats'].astype(int)
    #Construct node information for nx.Digraph()
    availStaPair = list(map(tuple, query.iloc[:,2:4].itertuples(index=False)))
    freeSeatRecord = query.iloc[:,4:5].to_dict('records')
    for i in range(0, len(availStaPair)):
        tmp = list(availStaPair[i])
        tmp.insert(2,freeSeatRecord[i])
        availStaPair[i] = tuple(tmp)
    
    #Make a digraph for query
    allPairsGraph = nx.DiGraph()
    allPairsGraph.add_edges_from(availStaPair)
    allEdgeLabels = {}
    k = 0
    for i in allPairsGraph.edges():
        allEdgeLabels.update({i:query['freeSeats'].iloc[k]})
        k += 1
    try:
        availPath = nx.shortest_path(allPairsGraph, source=oriStation, target=arrStation)
    except:
        availPath = []
    if len(availPath) > 3 or len(availPath) == 0:           #沒票或超過台鐵單次可訂段數
        return [], 0, allPairsGraph
    shortestGraph = allPairsGraph.subgraph(availPath)
    freeSeats = nx.get_edge_attributes(shortestGraph,'freeSeats')
    maxTicketCount, flow_dict = nx.maximum_flow(shortestGraph, oriStation,arrStation, capacity='freeSeats')
    return availPath, maxTicketCount, allPairsGraph

# 把最短切票路徑 list 做成 pair 形式
# Parameter:
#   availPath (list): ['臺北','臺中','高雄']
# Return:
#   pairList (list): [('臺北','臺中'), ('臺中','高雄')]
# Example:
#   pairList = toPairList(['臺北','臺中','高雄'])

def toPairList(availPath):
    pairList = []
    for i in range(len(availPath)-1):
        pairList.append((availPath[i],availPath[i+1]))
    return pairList

# 把各剩餘車票數加到對應的 pair 上
# Parameter:
#   Graph (nx.DiGraph): 要添加的圖
# Return:
#   pairFreeSeat (dictionary): 各 pair 對應到的剩餘座位
# Example:
#   freeSeat = UpdateEdgeLabel(Graph)

def UpdateEdgeLabel(Graph):
    freeSeats = nx.get_edge_attributes(Graph,'freeSeats')
    fs = {}
    k = 0
    for i in Graph.edges():
        fs.update({i:freeSeats[i]})
        k += 1
    return fs

# 畫出所有 pair 的剩餘車票圖
# Parameters:
#   Graph (nx.DiGraph)
#   date (string): Graph 對應到的日期
#   trainNo (string): Graph 對應到的車次
# Output:
#   plt (matplotlib.pyplot): 剩餘車票對總圖
# Returns:
#   none
# Example: drawGraph(Graph, '2019-05-24', '123')

def drawGraph(Graph, date, trainNo):
    picture = plt.figure(1)
    picture.canvas.set_window_title("剩餘車票對總圖")
    freeSeatDic = UpdateEdgeLabel(Graph)
    nx.draw_networkx(Graph, node_size=1000, pos=nx.circular_layout(Graph), node_color='b', font_color='w', with_labels=True)
    nx.draw_networkx_edge_labels(Graph, pos=nx.circular_layout(Graph), edge_labels=freeSeatDic, font_size=8)
    plt.title(date+'  '+trainNo+' 次 剩餘車票總圖')
    plt.axis('off')
    #plt.savefig(str(date)+'_'+str(trainNo)+'.pdf',format='pdf')
    plt.show()

# 把最短切票路徑及可訂座位數畫到 BaseMap 上
# Parameters:
#   Graph (nx.DiGraph)
#   date (string): Graph 對應到的日期
#   trainNo (string): Graph 對應到的車次 
#   oriStation (string): 出發站
#   arrStation (string): 目的地
#   maxTicketCount (int): 最多可訂座位數
# Output:
#   plt (matplotlib.pyplot): 以地圖呈現資訊
# Return:
#   None

def drawOnMap(Graph, date, trainNo, oriStation, arrStation, maxTicketCount):
    station = open('station.json', 'r',encoding='utf-8-sig') 
    station = station.read()
    station = json.loads(station)
    staList = pd.DataFrame(station['Stations'])
    stu = staList['StationName'].apply(pd.Series)
    stv = staList['StationPosition'].apply(pd.Series)
    staPosDF = pd.concat([stu['Zh_tw'],stv], axis=1)
    if mapExists == 0:
        m = Basemap(projection='merc', llcrnrlat=minlat, urcrnrlat=maxlat,llcrnrlon=minlon, urcrnrlon=maxlon, lat_ts=30, resolution='h')
    # convert lat and lon to map projection: mx,my=m(lons,lats)
    # put map projection coordinates in pos dictionary
    nodePos={}
    for i in Graph.nodes():
        staName=staPosDF.loc[staPosDF['Zh_tw']==i]['Zh_tw']
        lon=staPosDF.loc[staPosDF['Zh_tw']==i]['PositionLon']
        lat=staPosDF.loc[staPosDF['Zh_tw']==i]['PositionLat']
        try:
            nodePos[staName.iloc[0]]=m(lon.iloc[0],lat.iloc[0])
        except:
            print(i)
    freeSeatDic = UpdateEdgeLabel(Graph)
    # draw on map
    mapPicure = plt.figure(2)
    mapPicure.canvas.set_window_title("最短切票圖")
    nx.draw_networkx(Graph,pos=nodePos,node_size=100,node_color='green',font_color='r',font_weight='bold',alpha=0.5)
    nx.draw_networkx_edge_labels(Graph,pos=nodePos,edge_labels=freeSeatDic,font_size=10)
    m.drawcoastlines()
    m.drawmeridians(np.arange(minlon, maxlon, 0.5), labels=[0, 0, 0, 1])
    m.drawparallels(np.arange(minlat, maxlat, 0.5), labels=[1, 0, 0, 0])
    m.plot(120,21, latlon=False)
    plt.title(date+'  '+trainNo+' 次 '+oriStation+' 到 '+arrStation+' 最多可訂 '+str(maxTicketCount)+' 張')
    plt.savefig('remaining.pdf',format='pdf')
    plt.show()