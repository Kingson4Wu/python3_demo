# ————————————————
# 版权声明：本文为CSDN博主「小嗨兔」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_43631377/article/details/107577121

def main():     #主程序
    print("开始爬取.....")
    year=2010  #起始年份
    baseurl='https://china.nba.com/static/data/league/playerstats_All_All_All_0_All_false_2018_2_All_Team_points_All_perGame.json'
    #获得数据
    NBAPlayerdatadict=getdata(baseurl,year)
    #所需信息的抬头列表
    cols_index2 = ['displayName',"code", 'position', 'name',"code",'games','points', 'pointsPg', 'rebsPg', 'assistsPg''minsPg', 'fgpct', 'tppct', 'ftpct', 'blocksPg', 'foulsPg', 'height', 'weight'
                   ]
    cols_index1 = ['playerProfile','playerProfile', 'playerProfile', 'teamProfile',
                   'teamProfile',  'statAverage',
                   'statTotal', 'statAverage', 'statAverage', 'statAverage',
                   'statAverage', 'statAverage', 'statAverage', 'statAverage',
                   'statAverage', 'statAverage', 'playerProfile', 'playerProfile'
                   ]
    #保存数据
    savepath='.//'+str(year)+'年-2020年NBA球员数据排行TOP50.xls'
    savedata(NBAPlayerdatadict,savepath,year,cols_index1,cols_index2)
    #数据库位置
    dbpath='.//NBA球员数据库.db'
    #将数据保存到数据库
    saveDB(NBAPlayerdatadict,dbpath,year,cols_index1,cols_index2)
    print('成功爬取并保存数据!')
