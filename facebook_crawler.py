from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import Keys
from openpyxl import Workbook

wb = Workbook()
ws =wb.active
ws.append(['姓名','关注','动态1','动态2','动态3','动态4','动态5','动态6','动态7','动态8','动态9','动态10','动态11','动态12','动态13','动态14','动态15','动态16','动态17','动态18','动态19','动态20','动态21','动态22','动态23','动态24','动态25'])
options = webdriver.ChromeOptions()
# 禁止弹窗
prefs = {
        'profile.default_content_setting_values':
            {
                'notifications': 2
            }
}
# 禁止弹窗加入
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(options)
browser.maximize_window()#浏览器窗口最大化
browser.get("https://www.facebook.com")
browser.find_element(By.ID,'email').clear()
browser.find_element(By.ID,'email').send_keys('xuanyuanling123@outlook.com')
browser.find_element(By.ID,'pass').clear()
browser.find_element(By.ID,'pass').send_keys('azRmtJ4Ys-Z4.AB')
time.sleep(3)
browser.find_element(by=By.XPATH, value='//button[@name="login"]').send_keys(Keys.ENTER)
time.sleep(3)

k=0
name = ['TammyBaldwin','JohnBarrasso','MichaelBennet','MarshaBlackburn','CoryBooker','JohnBoozman','KatieBoydBritt', 'tedbuddforsenate',  'mariacantwell', 'ShelleyMooreCapito', 'billcassidy', 'SusanCollins', 'JohnCornyn', 'SenatorTomCotton', 'senatorkevincramer', 'MikeCrapo', 'senatortedcruz', 'SteveDaines', 'SenDuckworth', 'joniforiowa', 'JohnFettermanPA', 'debfischerforsenate', 'KirstenGillibrand', 'LindseyGrahamSC', 'grassleyworks', 'BillHagertyTN', 'HawleyMO', 'MartinHeinrich', 'cindyhydesmith', 'RonJohnsonWI', 'timkaine', 'SenatorJohnKennedy', 'amyklobuchar', 'lankford.for.america', 'BenRayLujan', 'DrRogerMarshall', 'McConnellForSenate', 'JeffMerkleyOregon', 'mullinforamerica', 'SenLisaMurkowski', 'pattymurray', 'jonossoff', 'alexpadilla4ca', 'RandPaul', 'SenJackReed', 'PeteRickettsNE', 'mittromney', 'SenJackyRosen', 'mikerounds', 'MarcoRubio', 'BrianSchatz', 'SchmittForSenate', 'scottforflorida', 'votetimscott', 'jeanneshaheenNH', 'KyrstenSinema', 'TinaSmithMN', 'stabenow', 'DanSullivanforAlaska', 'jontester', 'SenJohnThune', 'ThomTillis', 'SenatorTuberville', 'MarkRWarner', 'ElizabethWarren', 'PeterWelch', 'SenatorWhitehouse', 'wickerforsenate', 'ToddYoungIndiana','MikeRogersforCongress','RobertAderholt','CongressmanGaryPalmer','RepSewell','Peltola4Congress','repdavidschweikert','RepRubenGallego','repgregstanton','biggsforcongress','peopleforgrijalva','RepDebbieLesko','repgosar','RepWesterman','RepHuffman','assemblymankiley','RepMcClintock','doris.matsui','repgaramendi','RepJoshHarder','RepMarkDeSaulnier','pelosiforcongress','RepBarbaraLee','EricMSwalwell','zoelofgren','RepJimmyPanetta','kevinomccarthy','RepJimCosta','jayobernolte','repsaludcarbajal','RepRaulRuizMD','RepJudyChu','TonyCardenasForCongress','AdamSchiff']
for k in range(0,100):
    ###############爬取关注####################
    url = 'https://www.facebook.com/' + name[k] + '/following'
    browser.get(url)
    time.sleep(1)
    following_path = "//div[@class='xyamay9 x1pi30zi x1l90r2v x1swvt13']/div[3]"
    num = 1
    lists = []
    for num in range(1,15):
        namepath = following_path + "/div[" + str(num) + "]/div[2]/div/a/span"
        try:
            a = browser.find_element(by=By.XPATH,value=namepath).text
        except:
            a = ''
        lists.append(a)
    while '' in lists:
        lists.remove('')

    lenth = len(lists)
    l = 0
    p = ''
    while l < lenth:
        if l==0:
            p = lists[0]
        else:
            p = p + ',' + lists[l]
        l = l + 1
    ###############爬取动态####################
    url = 'https://www.facebook.com/' + name[k]
    browser.get(url)
    time.sleep(1)
    following_path2 = "//div[@class='x9f619 x1n2onr6 x1ja2u2z xeuugli xs83m0k x1xmf6yo x1emribx x1e56ztr x1i64zmx xjl7jj x19h7ccj xu9j1y6 x7ep2pv']"
    x = 1
    list1 = []
    list1.append(name[k])
    list1.append(p)
    for x in range(1, 25):
        namepath0 = following_path2 + "/div[3]/div[" + str(x) + "]"
        namepath1 = following_path2 + "/div[2]/div[" + str(x) + "]"
        y=1
        list2 = []
        browser.execute_script('window.scrollBy(0,700)')
        time.sleep(2)
        for y in range(1,4):
            namepath2 = namepath1 + "/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/span/div[" + str(y) + "]/div"
            namepath3 = namepath0 + "/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/span/div[" + str(y) + "]/div"
            try:
                b = browser.find_element(by=By.XPATH,value=namepath2).text
            except:
                b = ''
            try:
                c = browser.find_element(by=By.XPATH,value=namepath3).text
            except:
                c = ''
            if not b =='':
                list2.append(b)
            if not c =='':
                list2.append(c)
        while '' in list2:
            list2.remove('')
        lenth = len(list2)
        l=0
        p=''
        while l < lenth:
            p += list2[l]
            l = l + 1
        list1.append(p)
    ws.append(list1)
time.sleep(5)
wb.save(r'data.xlsx')