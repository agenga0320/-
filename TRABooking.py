from selenium import webdriver

driver = None


# pairList: (beginID,endID)的list 長度要是[1,3]之間
# day: 格式 YYYYMMDD
# ID: 身分證字號
# trainNo: 車次
# seatNum: 訂票張數
# example: 
# buyTicket([(1020,4220),(4220,4400)],"20190524","A106928562","123",2)
def buyTicket(pairList,day,ID,trainNo,seatNum):
    if len(pairList) not in (1,2,3):
        raise IndexError("pairList 長度不是[1,3]")
        
    if seatNum not in (1,2,3,4,5,6):
        raise IndexError("seatNum 不符合[1,6]")

    
    try:
        url = "https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip123/query"
        global driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        driver = webdriver.Chrome(options=option)
        driver.get(url)
        driver.find_element_by_name("pid").send_keys(ID)
        driver.find_element_by_css_selector("#queryForm > div.basic-info > div:nth-child(2) > div.btn-group > label:nth-child({})".format(len(pairList))).click()
        
        for idx, (begin,end) in enumerate(pairList):
            nowTicketOrderParamList = "ticketOrderParamList[{}]".format(idx)
            driver.find_element_by_name(nowTicketOrderParamList + ".startStation").send_keys(begin)
            driver.find_element_by_name(nowTicketOrderParamList + ".endStation").send_keys(end)
            driver.find_element_by_name(nowTicketOrderParamList + ".rideDate").clear()
            driver.find_element_by_name(nowTicketOrderParamList + ".rideDate").send_keys(day)
            driver.find_element_by_name(nowTicketOrderParamList + ".normalQty").clear()
            driver.find_element_by_name(nowTicketOrderParamList + ".normalQty").send_keys(seatNum)
            driver.find_element_by_name(nowTicketOrderParamList + ".trainNoList[0]").send_keys(trainNo)
            if seatNum==1:
                driver.find_element_by_name(nowTicketOrderParamList + ".chgSeat").find_element_by_xpath("./..").click()
            
        driver.find_element_by_css_selector("#queryForm > div.btn-sentgroup > input").click()
        
        for idx in range(len(pairList)):
            driver.find_element_by_name("selectLoc[{}]".format(idx)).find_element_by_xpath("./..").click()
    except:
        print("Chrome 發生問題")
# 在GUI程式結束的時候call這個function關閉瀏覽器
def closeWebBrowser():
    driver.close()
        
# buyTicket([(1020,4220),(4220,4400)],"20190524","A106928562","123",2)
# closeWebBrowser()