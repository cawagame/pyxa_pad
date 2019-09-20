flin ="paxa_save/menu"


def opme(fl):
    lo =open(fl)
    lof =lo.readlines()
    lo.close()
    return lof
def svme(fl,data):
    lo =open(fl,'w')
    for i in data:
        lo.write(i+"\n")
    lo.close()

out5 =[]
def modi(data):
    exec(data)
    
    for i in nana:
        nana[i]['m_pos'] ={}
        erra            =[]
        for ib in nana[i]:
        
            if type(ib) ==type(()):
                x,y     =ib
               
                erra.append(ib)
                nana[i]["m_pos"][(x,y)] =nana[i][ib]
        for ib in erra:
            nana[i].pop(ib)
        return 'nana='+str(nana)

#----  m_pos et     x y
lof =opme(flin+".txt")

for i in lof:        
    out5.append(modi(i))
out5.reverse()
svme(flin+"_n.txt",out5)

