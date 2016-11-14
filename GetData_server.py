# -*- coding: gbk -*-

import urllib2
from time import sleep

def getData(city,ChineseName):

    success = False
    flag_url = 0
    while not success:
        if flag_url >= 5:
            return None  #try this url 5 times, if no response, return 
            break
        try:
            url='http://www.pm25.in'+city
            req = urllib2.Request(url)
            response = urllib2.urlopen(req,timeout = 5)   # deal with timeout 
            html = response.read()
            success=True
        except:
            sleep(1)
            flag_url += 1

    #print html

    time = '\xe6\x95\xb0\xe6\x8d\xae\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4\xef\xbc\x9a'#'���ݸ���ʱ��'
    #time2=time.decode('gbk').encode('utf8')
    indextime = html.find(time)

    temp = html.find(time,indextime+len(time))
    indextime = temp
    
    datetime=html[indextime+len(time):indextime+len(time)+len('2015-09-30 11:00:00')]
    print datetime+' '

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html,"html.parser")
    
    f = open('/home/ec2-user/pm25_wangluyi/pm25.txt','a')   # directory 
    row=1
    countRow=len(soup.tbody.contents)


    while (row<countRow):
    #try:
        f.write(datetime+" ")
        f.write(ChineseName+" ")
        print ChineseName,city
        column=1
        
        while (column<= 3   ):
            try:
                f.write(soup.tbody.contents[int(row)].contents[int(column)].contents[0].encode('gbk')+" ")
            except:
                f.write('error'+' ')
            try:
                print soup.tbody.contents[int(row)].contents[int(column)].contents[0].encode('gbk')
            except:
                print 'error'
            #print soup.tbody.contents[int(row)].contents[int(column)].contents[0].encode('gbk')
            column=column+2

        while (column== 5   ):
            if(len(soup.tbody.contents[int(row)].contents[int(column)])==0):
                f.write('unknown ')
            else:
                try:
                    f.write(soup.tbody.contents[int(row)].contents[int(column)].contents[0].encode('gbk')+" ")
                except:
                    f.write('error'+' ')
                #print soup.tbody.contents[int(row)].contents[int(column)].contents[0].encode('gbk')
            column=column+2

        #����1����Ҫ��Ⱦ��, more than 1 first pollutant 
        while (column==7   ):
            if(len(soup.tbody.contents[int(row)].contents[int(column)])>2): #���3�ּ�������Ⱦ��ı�ǩ�ṹ, record tags for 3 more kinds of pollutant 
                f_special = open('/home/ec2-user/pm25_wangluyi/special_number_of_pollutant.txt','a')   
                f_special.write(soup)
                f_special.write('\n')
                f_special.close()
                f.write('lengthMoreThanTwo ')
                
            if(len(soup.tbody.contents[int(row)].contents[int(column)])==2):  #2����Ҫ��Ⱦ��, 2 critical pollutants 

                if(  str(soup.tbody.contents[int(row)].contents[int(column)]).count('\n')>5  ):
                    f_special = open('/home/ec2-user/pm25_wangluyi/special_number_of_pollutant.txt','a')   
                    f_special.write(soup)
                    f_special.write('\n')
                    f_special.close()

                start=soup.tbody.contents[int(row)].contents[int(column)].contents[0].find('\n',0)
                end=soup.tbody.contents[int(row)].contents[int(column)].contents[0].find('\n',1)
                f.write(soup.tbody.contents[int(row)].contents[int(column)].contents[0][start+1:end].encode('gbk')+",")
            #��Ҫѭ��??? need loop? 

                start = str(soup.tbody.contents[int(row)].contents[int(column)].contents[1]).find('\n',0)
                start += len('                      ')
                end = str(soup.tbody.contents[int(row)].contents[int(column)].contents[1]).find('\n',start)
                f.write( str(soup.tbody.contents[int(row)].contents[int(column)].contents[1])[start+1:end].decode('utf8').encode('gbk')+" ")

            else:
                f.write(soup.tbody.contents[int(row)].contents[int(column)].contents[0].encode('gbk')+" ")
            
            column=column+2

        while ( column<=21 ):
            #������������иø���Ϊ�յ����, if no data in the table cell 
            try:
                if (len(soup.tbody.contents[int(row)].contents[int(column)].contents[0])==0):
                    f.write('nodata'+' ')
                else:
                    f.write(soup.tbody.contents[int(row)].contents[int(column)].contents[0].encode('gbk')+" ")
            except:
                f.write('error'+' ')
                
            column=column+2

        row=row+2
        f.write("\n")

    f.close()


if __name__=="__main__":

    ChineseCityName =  ["������",
                        "�����յ���",
                        "��������",
                        "����̩����",
                        "�������",
                        "����",
                        "����",
                        "��ɽ",
                        "��˳",
                        "����",
                        "�׳�",
                        "��ɫ",
                        "��ɽ",
                        "����",
                        "����",
                        "����",
                        "����",
                        "��ɽ",
                        "��ͷ",
                        "�����׶�",
                        "����",
                        "����",
                        "����",
                        "��Ϫ",
                        "�Ͻ�",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "��������",
                        "������",
                        "��ɳ",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "�е�",
                        "�ɶ�",
                        "����",
                        "���",
                        "����",
                        "����",
                        "����",
                        "������",
                        "����",
                        "����",
                        "������",
                        "����",
                        "����",
                        "��ͬ",
                        "���˰����",
                        "���˰������",
                        "����",
                        "�º���",
                        "����",
                        "����",
                        "����",
                        "������",
                        "��ݸ",
                        "��Ӫ",
                        "������˹",
                        "��ʩ��",
                        "����",
                        "���Ǹ�",
                        "��ɽ",
                        "��˳",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "������",
                        "����",
                        "������",
                        "�㰲",
                        "��Ԫ",
                        "����",
                        "���",
                        "����",
                        "����",
                        "������",
                        "��ԭ",
                        "������",
                        "������",
                        "��������",
                        "����",
                        "����",
                        "������",
                        "������",
                        "���ܵ���",
                        "����",
                        "����",
                        "����",
                        "�ױ�",
                        "�ӳ�",
                        "�Ϸ�",
                        "�׸�",
                        "�ں�",
                        "��ˮ",
                        "����",
                        "�������",
                        "��Դ",
                        "����",
                        "����",
                        "�����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "�Ƹ�",
                        "������",
                        "��ɽ",
                        "��ʯ",
                        "���ͺ���",
                        "����",
                        "��«��",
                        "���ױ���",
                        "����",
                        "��ľ˹",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "������",
                        "����",
                        "����",
                        "��ī",
                        "����",
                        "���",
                        "����",
                        "������",
                        "����",
                        "����",
                        "��",
                        "����",
                        "��̳",
                        "����",
                        "����",
                        "�Ž�",
                        "��Ȫ",
                        "����",
                        "����",
                        "����",
                        "��ʲ����",
                        "��������",
                        "����",
                        "�����",
                        "����",
                        "��ɽ",
                        "����",
                        "����",
                        "����",
                        "����",
                        "�ȷ�",
                        "����",
                        "����",
                        "��ɽ",
                        "��ɽ��",
                        "���Ƹ�",
                        "�ĳ�",
                        "����",
                        "��Դ",
                        "����",
                        "�ٰ�",
                        "�ٲ�",
                        "�ٷ�",
                        "������",
                        "����",
                        "��֥����",
                        "��ˮ",
                        "����ˮ",
                        "����",
                        "����",
                        "¤��",
                        "����",
                        "¦��",
                        "����",
                        "���",
                        "����",
                        "����",
                        "����",
                        "����ɽ",
                        "ï��",
                        "üɽ",
                        "÷��",
                        "����",
                        "ĵ����",
                        "�ϲ�",
                        "�ϳ�",
                        "�Ͼ�",
                        "����",
                        "��ƽ",
                        "��ͨ",
                        "����",
                        "��������",
                        "�ڽ�",
                        "����",
                        "����",
                        "ŭ����",
                        "�̽�",
                        "��֦��",
                        "����",
                        "ƽ��ɽ",
                        "ƽ��",
                        "ƽ��",
                        "Ƽ��",
                        "�ն�",
                        "����",
                        "���",
                        "ǭ������",
                        "ǭ����",
                        "ǭ������",
                        "�ൺ",
                        "����",
                        "��Զ",
                        "�ػʵ�",
                        "����",
                        "�������",
                        "��̨��",
                        "Ȫ��",
                        "����",
                        "����",
                        "�տ������",
                        "����",
                        "�ٳ�",
                        "��ɽ",
                        "����Ͽ",
                        "����",
                        "����",
                        "�Ϻ�",
                        "����",
                        "����",
                        "����",
                        "ɽ�ϵ���",
                        "��ͷ",
                        "��β",
                        "�ع�",
                        "����",
                        "����",
                        "����",
                        "����",
                        "ʯ����",
                        "ʯ��ׯ",
                        "ʮ��",
                        "ʯ��ɽ",
                        "�ٹ�",
                        "˫Ѽɽ",
                        "˷��",
                        "��ƽ",
                        "��ԭ",
                        "�绯",
                        "����",
                        "����",
                        "��Ǩ",
                        "����",
                        "����",
                        "���ǵ���",
                        "̩��",
                        "̫��",
                        "̫ԭ",
                        "̨��",
                        "̩��",
                        "��ɽ",
                        "���",
                        "��ˮ",
                        "����",
                        "ͭ��",
                        "ͨ��",
                        "ͨ��",
                        "ͭ��",
                        "ͭ�ʵ���",
                        "��³������",
                        "�߷���",
                        "Ϋ��",
                        "����",
                        "μ��",
                        "�ĵ�",
                        "��ɽ��",
                        "����",
                        "�ں�",
                        "�人",
                        "�ߺ�",
                        "�⽭",
                        "�����",
                        "�����첼",
                        "��³ľ��",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "��̶",
                        "������",
                        "����",
                        "����",
                        "����",
                        "Т��",
                        "���ֹ�����",
                        "�˰���",
                        "��̨",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "��˫������",
                        "����",
                        "����",
                        "����",
                        "�Ű�",
                        "�Ӱ�",
                        "�ӱ���",
                        "�γ�",
                        "����",
                        "��Ȫ",
                        "����",
                        "��̨",
                        "�˱�",
                        "�˲�",
                        "�˴�",
                        "����",
                        "���������",
                        "�����������",
                        "����",
                        "Ӫ��",
                        "ӥ̶",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "����",
                        "�˳�",
                        "�Ƹ�",
                        "������",
                        "��Ϫ",
                        "��ׯ",
                        "�żҸ�",
                        "�żҽ�",
                        "�żҿ�",
                        "����",
                        "��Ҵ",
                        "����",
                        "տ��",
                        "����",
                        "��ͨ",
                        "��Զ",
                        "֣��",
                        "��",
                        "��ɽ",
                        "����",
                        "�ܿ�",
                        "��ɽ",
                        "�麣",
                        "����",
                        "פ����",
                        "����",
                        "�Ͳ�",
                        "�Թ�",
                        "����",
                        "����"]

    nameCity = ["/abazhou",
                "/akesudiqu",
                "/alashanmeng",
                "/aletaidiqu",
                "/alidiqu",
                "/ankang",
                "/anqing",
                "/anshan",
                "/anshun",
                "/anyang",
                "/baicheng",
                "/baise",
                "/baishan",
                "/baiyin",
                "/bengbu",
                "/baoding",
                "/baoji",
                "/baoshan",
                "/baotou",
                "/bayannaoer",
                "/bazhong",
                "/beihai",
                "/beijing",
                "/benxi",
                "/bijie",
                "/binzhou",
                "/boertala",
                "/bozhou",
                "/cangzhou",
                "/changchun",
                "/changde",
                "/changdudiqu",
                "/changjizhou",
                "/changsha",
                "/changshu",
                "/changzhi",
                "/changzhou",
                "/chaoyang",
                "/chaozhou",
                "/chengde",
                "/chengdu",
                "/chenzhou",
                "/chifeng",
                "/chizhou",
                "/chongqing",
                "/chongzuo",
                "/chuxiongzhou",
                "/chuzhou",
                "/dalian",
                "/dalizhou",
                "/dandong",
                "/daqing",
                "/datong",
                "/daxinganlingde",
                "/daxinganlingdiqu",
                "/dazhou",
                "/dehongzhou",
                "/deyang",
                "/dezhou",
                "/dingxi",
                "/diqingzhou",
                "/dongguan",
                "/dongying",
                "/eerduosi",
                "/enshizhou",
                "/ezhou",
                "/fangchenggang",
                "/foshan",
                "/fushun",
                "/fuxin",
                "/fuyang",
                "/fuyangshi",
                "/fuzhou",
                "/fuzhoushi",
                "/gannanzhou",
                "/ganzhou",
                "/ganzizhou",
                "/guangan",
                "/guangyuan",
                "/guangzhou",
                "/guigang",
                "/guilin",
                "/guiyang",
                "/guoluozhou",
                "/guyuan",
                "/haerbin",
                "/haibeizhou",
                "/haidongdiqu",
                "/haikou",
                "/haimen",
                "/hainanzhou",
                "/haixizhou",
                "/hamidiqu",
                "/handan",
                "/hangzhou",
                "/hanzhong",
                "/hebi",
                "/hechi",
                "/hefei",
                "/hegang",
                "/heihe",
                "/hengshui",
                "/hengyang",
                "/hetiandiqu",
                "/heyuan",
                "/heze",
                "/hezhou",
                "/honghezhou",
                "/huaian",
                "/huaibei",
                "/huaihua",
                "/huainan",
                "/huanggang",
                "/huangnanzhou",
                "/huangshan",
                "/huangshi",
                "/huhehaote",
                "/huizhou",
                "/huludao",
                "/hulunbeier",
                "/huzhou",
                "/jiamusi",
                "/jian",
                "/jiangmen",
                "/jiangyin",
                "/jiaonan",
                "/jiaozhou",
                "/jiaozuo",
                "/jiaxing",
                "/jiayuguan",
                "/jieyang",
                "/jilin",
                "/jimo",
                "/jinan",
                "/jinchang",
                "/jincheng",
                "/jingdezhen",
                "/jingmen",
                "/jingzhou",
                "/jinhua",
                "/jining",
                "/jintan",
                "/jinzhong",
                "/jinzhou",
                "/jiujiang",
                "/jiuquan",
                "/jixi",
                "/jurong",
                "/kaifeng",
                "/kashediqu",
                "/kelamayi",
                "/kezhou",
                "/kuerle",
                "/kunming",
                "/kunshan",
                "/laibin",
                "/laiwu",
                "/laixi",
                "/laizhou",
                "/langfang",
                "/lanzhou",
                "/lasa",
                "/leshan",
                "/liangshanzhou",
                "/lianyungang",
                "/liaocheng",
                "/liaoyang",
                "/liaoyuan",
                "/lijiang",
                "/linan",
                "/lincang",
                "/linfen",
                "/linxiazhou",
                "/linyi",
                "/linzhidiqu",
                "/lishui",
                "/liupanshui",
                "/liuzhou",
                "/liyang",
                "/longnan",
                "/longyan",
                "/loudi",
                "/luan",
                "/luohe",
                "/luoyang",
                "/luzhou",
                "/lvliang",
                "/maanshan",
                "/maoming",
                "/meishan",
                "/meizhou",
                "/mianyang",
                "/mudanjiang",
                "/nanchang",
                "/nanchong",
                "/nanjing",
                "/nanning",
                "/nanping",
                "/nantong",
                "/nanyang",
                "/naqudiqu",
                "/neijiang",
                "/ningbo",
                "/ningde",
                "/nujiangzhou",
                "/panjin",
                "/panzhihua",
                "/penglai",
                "/pingdingshan",
                "/pingdu",
                "/pingliang",
                "/pingxiang",
                "/puer",
                "/putian",
                "/puyang",
                "/qiandongnanzhou",
                "/qiannanzhou",
                "/qianxinanzhou",
                "/qingdao",
                "/qingyang",
                "/qingyuan",
                "/qinhuangdao",
                "/qinzhou",
                "/qiqihaer",
                "/qitaihe",
                "/quanzhou",
                "/qujing",
                "/quzhou",
                "/rikazediqu",
                "/rizhao",
                "/rongcheng",
                "/rushan",
                "/sanmenxia",
                "/sanming",
                "/sanya",
                "/shanghai",
                "/shangluo",
                "/shangqiu",
                "/shangrao",
                "/shannandiqu",
                "/shantou",
                "/shanwei",
                "/shaoguan",
                "/shaoxing",
                "/shaoyang",
                "/shenyang",
                "/shenzhen",
                "/shihezi",
                "/shijiazhuang",
                "/shiyan",
                "/shizuishan",
                "/shouguang",
                "/shuangyashan",
                "/shuozhou",
                "/siping",
                "/songyuan",
                "/suihua",
                "/suining",
                "/suizhou",
                "/suqian",
                "/suzhou",
                "/suzhoushi",
                "/tachengdiqu",
                "/taian",
                "/taicang",
                "/taiyuan",
                "/taizhou",
                "/taizhoushi",
                "/tangshan",
                "/tianjin",
                "/tianshui",
                "/tieling",
                "/tongchuan",
                "/tonghua",
                "/tongliao",
                "/tongling",
                "/tongrendiqu",
                "/tulufandiqu",
                "/wafangdian",
                "/weifang",
                "/weihai",
                "/weinan",
                "/wendeng",
                "/wenshanzhou",
                "/wenzhou",
                "/wuhai",
                "/wuhan",
                "/wuhu",
                "/wujiang",
                "/wujiaqu",
                "/wulanchabu",
                "/wulumuqi",
                "/wuwei",
                "/wuxi",
                "/wuzhong",
                "/wuzhou",
                "/xiamen",
                "/xian",
                "/xiangtan",
                "/xiangxizhou",
                "/xiangyang",
                "/xianning",
                "/xianyang",
                "/xiaogan",
                "/xilinguolemeng",
                "/xinganmeng",
                "/xingtai",
                "/xining",
                "/xinxiang",
                "/xinyang",
                "/xinyu",
                "/xinzhou",
                "/xishuangbannazhou",
                "/xuancheng",
                "/xuchang",
                "/xuzhou",
                "/yaan",
                "/yanan",
                "/yanbianzhou",
                "/yancheng",
                "/yangjiang",
                "/yangquan",
                "/yangzhou",
                "/yantai",
                "/yibin",
                "/yichang",
                "/yichun",
                "/yichunshi",
                "/yilihasake",
                "/yilihasakezhou",
                "/yinchuan",
                "/yingkou",
                "/yingtan",
                "/yiwu",
                "/yixing",
                "/yiyang",
                "/yongzhou",
                "/yueyang",
                "/yulin",
                "/yulinshi",
                "/yuncheng",
                "/yunfu",
                "/yushuzhou",
                "/yuxi",
                "/zaozhuang",
                "/zhangjiagang",
                "/zhangjiajie",
                "/zhangjiakou",
                "/zhangqiu",
                "/zhangye",
                "/zhangzhou",
                "/zhanjiang",
                "/zhaoqing",
                "/zhaotong",
                "/zhaoyuan",
                "/zhengzhou",
                "/zhenjiang",
                "/zhongshan",
                "/zhongwei",
                "/zhoukou",
                "/zhoushan",
                "/zhuhai",
                "/zhuji",
                "/zhumadian",
                "/zhuzhou",
                "/zibo",
                "/zigong",
                "/ziyang",
                "/zunyi"]

    
    for i in range(0,len(ChineseCityName)):
        getData(nameCity[i],ChineseCityName[i])
        