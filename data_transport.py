file = open('2.csv', 'r')
file_line = file.readlines()
file.close()
file_after = open("after.csv", "w")
ageAndA1 = [{"男":"1", "女":"2"},{"家人":"1", "独居":"2", "养老院":"3", "999":"."}]
A2dict = {"配偶":1, "子女":2, "子女配偶":3, "孙子女":4, "孙子女配偶":5, "兄弟姐妹":6, "父母或岳父母":7, "其他":8, "(跳过)":9, "999":10}
A3 = {"未上过小学":"1", "小学未毕业":"2", "小学":"3", "初中":"4", "高中":"5", "大专及以上":"6", "999":".", ".":".", "(跳过)":""}
A4 = {"已婚，并与配偶住在一起":"1", "已婚，但不与配偶住在一起":"2", "离婚":"3", "丧偶":"4", "未婚":"5", "999":".", ".":".", "(跳过)":""}
A5 = {"退休金":"1", "配偶":"2", "子女":"3", "孙子女":"4", "其他亲属":"5", "当地政府或社团":"6", "自己劳动或工作":"7", "其他":"8", "999":".", ".":".", "(跳过)":""}
A6 = {"＜100元":"1", "100-200元":"2", "200-300元":"3", "300-500元":"4", "500-1000元":"5", "1000-2000元":"6", "2000元以上":"7", "999":".", ".":".", "(跳过)":""}
A7 = {"企业":"1", "公务员":"2", "事业单位":"3", "离休":"4", "自由职业":"5", "尚未退休":"6", "999":".", ".":".", "(跳过)":""}
A8 = {"很好":"1", "好":"2", "一般":"3", "不好":"4", "很不好":"5", "999":".", ".":".", "(跳过)":""}
A9 = {"是":"1", "否":"2", "999":".", ".":".", "(跳过)":""}
A91 = {"跳过":"", "999":".", ".":".", "(跳过)":""} #key error
A92 = {"跳过":"", "999":".", ".":".", "(跳过)":""} #key error                               
B1ToB10 = {"是":"1", "否":"2", "999":".", ".":".", "(跳过)":""}
B11 = "前所未有的精力旺盛"
B12To13 = {"6-7天":"1", "4-5天":"2", "2-3天":"3", "1天":"4", "从不":"5", "999":".", ".":".", "(跳过)":""}
C1ToC13 = {"能":"1", "有一定困难":"2", "不能":"3", "999":".", ".":".", "(跳过)":""}
D1dict = {"高血压":1, "糖尿病":2, "高血脂":3, "冠心病":4, "痛风":5, "慢阻肺":6, "脑梗塞":7, "风湿病":8, "类风湿等风湿免疫性疾病":8, "风湿免疫性疾病":8, "骨与关节疾病":9, "骨关节炎":9, "肿瘤":10, "其他":11, "无疾病,健康":12, "健康，无疾病":12, "999":13, ".":14, "(跳过)":15}
D2 = {"1-2":"1", "3-5":"2", "6-9":"3", "10种以上":"4", "999":".", ".":".", "(跳过)":""}
D3ToD10 = {"非常同意":"1", "同意":"2", "不同意":"3", "强烈不同意":"4", "非常愿意":"1", "非常想":"1", "非常清楚":"1", "非常相信":"1", "愿意":"2", "想":"2", "清楚":"2", "相信":"2", "不愿意":"3", "不想":"3", "不清楚":"3", "不相信":"3", "强烈不愿意":"4", "4非常不清楚":"4", "4根本不相信":"4", "4强烈不愿意":"4", "999":".", ".":".", "(跳过)":""}
E1ToE3 ={"0":".", "999":".", "无":".", "无数据":"."}
E4 = {"能，不需搀扶或倚靠任何物体":"1", "能，需搀扶或倚靠任何物体":"2", "不能":"3", "999":".", ".":".", "(跳过)":""}
E5ToE10 = {"是":"1", "否":"2", "999":".", ".":".", "(跳过)":"", "w":"."}
E11 = {"没有":"1", "1天":"2", "2-3天":"3", "4-6天":"4", "每天":"5", "999":".", ".":".", "(跳过)":""}
E12 = {"＜1小时":"1", "1-2小时":"2", "3-5小时":"3", "6-10小时":"4", "全天":"5", "999":".", ".":".", "(跳过)":""}
E13 = {"轻微":"1", "中等":"2", "严重":"3", "无法忍受":"4", "999":".", ".":".", "(跳过)":""}
F1 = {"双手":"1", "左手":"2", "右手":"3", "否":"4", "999":".", ".":".", "(跳过)":""}
F2 = {"右":"1", "左":"2", "两只手差不多":"3", "999":".", ".":".", "(跳过)":""}
F31 = {"0":".", "999":".", ".":".", "(跳过)":"", "(空)":"", "":""} #key error
F32 = {"0":".", "999":".", ".":".", "(跳过)":"", "(空)":"", "":""} #key error
F41 = {"0":".", "999":".", ".":".", "(跳过)":"", "(空)":"", "":""} #key error
F42 = {"0":".", "999":".", ".":".", "(跳过)":"", "(空)":"", "":""} #key error
F5 = {"是":"1", "否":"2", "0":".", "999":".", ".":".", "(跳过)":"", "(空)":"", "":""}
F6 = {"(空)":"", "受试者认为不安全":"1", "访问员认为不安全":"2", "受试者拒绝或不愿意测量":"3", "受试者尝试了，但无法完成测量":"4", "受试者无法明白测量的指令":"5", "受试者无不明白测量的指令":"5", "受试者因手术、肿胀或其他原因不能测量":"6", "仪器故障":"7","999":".", ".":".", "(跳过)":""}
G1 = {"没有":"1", "没有明显限制":"1", "是，近期做过手术":"2", "是，外伤":"3", "是，其他健康状况":"3", "999":".", ".":".", "(跳过)":""}
G2 = {"0":".", "999":".", ".":".", "(跳过)":"", "(空)":""} #key error
G3 = {"0":".", "999":".", ".":".", "(跳过)":"", "(空)":""} #key error
G4 = {"无":"1", "拐杖或手杖":"2", "助行器":"3", "其他":"4", "999":".", ".":".", "(跳过)":""}
G5 = {"(空)":"", "受试者认为不安全":"1", "访问员认为不安全":"2", "受试者拒绝或不愿意测量":"3", "受试者尝试了，但无法完成测量":"4", "受试者无法明白测量的指令":"5", "受试者无不明白测量的指令":"5", "受试者因手术、肿胀或其他原因不能测量":"6", "仪器故障":"7","999":".", ".":".", "(跳过)":""}
index = 0
for i in file_line:
    index = index + 1
    after = []
    i = i.split(',')
    i.remove(i[1])
    i.remove(i[1])
    i.remove(i[1])
    i.remove(i[1])
    i.remove(i[1]) 
    i.remove(i[5])
    i.remove(i[6])
    i.remove(i[7])
    i.remove(i[5])
    i.remove(i[5])
    i.remove(i[5])
    i.remove(i[-1])
    i.remove(i[1])
    #print(i)
    after.append({"num":i[0]})
    after.append({"gender":ageAndA1[0][i[1]]})
    after.append({"age":i[2]})
    after.append({"id":i[3][-10:]})
    after.append({"a1":ageAndA1[1][i[4]]})
    _A2 = i[5].split("┋")
    dictA2 = [{"a21":"0"}, {"a22":""}, {"a23":"0"}, {"a24":"0"}, {"a25":"0"}, {"a26":"0"}, {"a27":"0"}, {"a28":"0"}]
    for j in _A2:
        if A2dict[j] == 9:
            for k in dictA2:
                for p in k:
                    k[p] = ''        
            continue
        elif A2dict[j] == 10:
            for k in dictA2:
                for p in k:
                    k[p] = '.'
            continue
        strtmp = str(A2dict[j])
        dictA2[A2dict[j]-1]["a2" + strtmp] = "1"
    for key in dictA2:
        after.append(key)
    after.append({"A3":A3[i[6]]})
    after.append({"A4":A4[i[7]]})
    after.append({"A5":A5[i[8]]})
    after.append({"A6":A6[i[9]]})
    after.append({"A7":A7[i[10]]})
    after.append({"A8":A8[i[11]]})
    after.append({"A9":A9[i[12]]})
    try :
        after.append({"A91":A91[i[13]]})
    except KeyError:
        after.append({"A91":i[13]})
    try :
        after.append({"A92":A92[i[14]]})
    except KeyError:
        after.append({"A92":i[14]})
    after.append({"B1":B1ToB10[i[15]]})
    after.append({"B2":B1ToB10[i[16]]})
    after.append({"B3":B1ToB10[i[17]]})
    after.append({"B4":B1ToB10[i[18]]})
    after.append({"B5":B1ToB10[i[19]]})
    after.append({"B6":B1ToB10[i[20]]})
    after.append({"B7":B1ToB10[i[21]]})
    after.append({"B8":B1ToB10[i[22]]})
    after.append({"B9":B1ToB10[i[23]]})
    after.append({"B10":B1ToB10[i[24]]})
    if i[25] == B11:
         after.append({"B11":"10"})
    else:
        after.append({"B11":i[25]})
    after.append({"B12":B12To13[i[26]]})
    after.append({"B13":B12To13[i[27]]})
    after.append({"C1":C1ToC13[i[28]]})    
    after.append({"C2":C1ToC13[i[29]]})
    after.append({"C3":C1ToC13[i[30]]})
    after.append({"C4":C1ToC13[i[31]]})
    after.append({"C5":C1ToC13[i[32]]})
    after.append({"C6":C1ToC13[i[33]]})
    after.append({"C7":C1ToC13[i[34]]})
    after.append({"C8":C1ToC13[i[35]]})
    after.append({"C9":C1ToC13[i[36]]})
    after.append({"C10":C1ToC13[i[37]]})
    after.append({"C11":C1ToC13[i[38]]})
    after.append({"C12":C1ToC13[i[39]]})
    after.append({"C13":C1ToC13[i[40]]})    
    #after.append({"D1":D1[i[41]]})
    _D1 = i[41].split("┋")
    for j in range(0, len(_D1)):
        if _D1[j].find("其他") != -1:
           _D1[j] = "其他" 
    dictD1 = [{"D11":"0"}, {"D12":"0"}, {"D13":"0"}, {"D14":"0"}, {"D15":"0"}, {"D16":"0"}, {"D17":"0"}, {"D18":"0"}, {"D19":"0"}, {"D110":"0"}, {"D111":"0"}, {"D112":"0"}]
    for j in _D1:
        if D1dict[j] == 13:
            for k in dictD1:
                for p in k:
                    k[p] = '.'
            continue
        elif D1dict[j] == 14:
            for k in dictD1:
                for p in k:
                    k[p] = '.'
            continue
        elif D1dict[j] == 15:
            for k in dictD1:
                for p in k:
                    k[p] = '.'
            continue
        strtmp = str(D1dict[j])
        dictD1[D1dict[j]-1]["D1" + strtmp] = "1"
    for key in dictD1:
        after.append(key)    
    after.append({"D2":D2[i[42]]}) 
    after.append({"D3":D3ToD10[i[43]]}) 
    after.append({"D4":D3ToD10[i[44]]})
    after.append({"D5":D3ToD10[i[45]]})
    after.append({"D6":D3ToD10[i[45]]})
    after.append({"D7":D3ToD10[i[46]]})
    after.append({"D8":D3ToD10[i[47]]})
    after.append({"D9":D3ToD10[i[48]]})
    after.append({"D10":D3ToD10[i[49]]})
    try :
        after.append({"E1":E1ToE3[i[51]]})
    except KeyError:
        after.append({"E1":i[51]})
    try :
        after.append({"E2":E1ToE3[i[52]]})
    except KeyError:
        after.append({"E2":i[52]})
    try :
        after.append({"E31":E1ToE3[i[53]]})
    except KeyError:
        after.append({"E31":i[53]})
    try :
        after.append({"E32":E1ToE3[i[54]]})
    except KeyError:
        after.append({"E32":i[54]})
    after.append({"E4":E4[i[55]]})
    after.append({"E5":E5ToE10[i[56]]})
    after.append({"E6":E5ToE10[i[57]]})
    after.append({"E7":E5ToE10[i[58]]})
    after.append({"E8":E5ToE10[i[59]]})
    after.append({"E9":E5ToE10[i[60]]})
    after.append({"E10":E5ToE10[i[61]]})
    after.append({"E11":E11[i[62]]})
    after.append({"E12":E12[i[63]]})
    after.append({"E13":E13[i[64]]})    
    after.append({"F1":F1[i[65]]})
    after.append({"F2":F2[i[66]]}) 
    try :
        after.append({"F31":F31[i[67]]})
    except KeyError:
        after.append({"F31":i[67]})    
    try :
        after.append({"F32":F32[i[68]]})
    except KeyError:
        after.append({"F32":i[68]})  
    try :
        after.append({"F41":F41[i[69]]})
    except KeyError:
        after.append({"F41":i[69]})          
    try :
        after.append({"F42":F42[i[70]]})
    except KeyError:
        after.append({"F42":i[70]})
    after.append({"F5":F5[i[71]]})
    after.append({"F6":F6[i[72]]})
    after.append({"G1":G1[i[73]]})
    try:
        after.append({"G2":G2[i[74]]})
    except KeyError:
        after.append({"G2":i[74]})
    try:
        after.append({"G3":G3[i[75]]})
    except KeyError:
        after.append({"G3":i[75]})
    if i[76].find("其他") != -1:
        i[76] = "其他"
        after.append({"G4":G4[i[76]]})
    else:
        after.append({"G4":G4[i[76]]})
    after.append({"G5":G5[i[77]]})
    print(len(i))
    print(i)
    print(after)
    print(index)
    afterstr=""
    for index_dict in after:
        for k in index_dict:
            afterstr = afterstr + index_dict[k] + ","
    print(afterstr)
    file_after.writelines(afterstr + "\r\n")
file_after.close()
