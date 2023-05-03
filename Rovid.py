
import sys
import numpy as np
import glob
import statistics as stat
sys.path.append('C://Users//hallgato//Appdata//Roaming//Python//Python311//site-packages')
import cv2
import time


def main():
    start = time.time()
    #images = [cv2.imread(file) for file in glob.glob("C://Users//hallgato//Documents//dgw//Kepfeldolgozas//beka//beka*.jpg")]
    images = [cv2.imread(file) for file in glob.glob("C://Users//hallgato//Documents//dgw//Kepfeldolgozas//fo//fo*.jpg")]
    #images = [cv2.imread(file) for file in glob.glob("D://programok//kepf//kep//kep*.jpg")]
    img_res =  np.zeros((790, 1053, 3), dtype = "uint8")
    resized,separated,tmpb,tmpg,tmpr,pix = [],[],[],[],[],[]
  
    for i in range(0,len(images)):
        resized.append(cv2.resize(images[i], (1053, 790)))

    for i in resized:
        b,g,r = cv2.split(i)
        separated.append([b,g,r])

    for i in range(0,790):
        for j in range(0,1053):
            for k in range(0,3):
                for l in range(0,len(resized)):
                    if k ==0:
                        tmpb.append(separated[l][k][i][j]) #[[b[790][1053],g[790][1053],r[790][1053]],[b[790][1053],g[790][1053],r[790][1053]],...,[]] 21 db kép
                    elif k ==1:
                        tmpg.append(separated[l][k][i][j])
                    else:
                        tmpr.append(separated[l][k][i][j])
            #pix.append([np.mean(tmpb),np.mean(tmpg),np.mean(tmpr)]) #44,7 sec kb 43.19708228111267
            pix.append([stat.mean(tmpb),stat.mean(tmpg),stat.mean(tmpr)]) #1:40 min kb, de pontosabb 106.53578591346741
            #pix.append([np.median(tmpb),np.median(tmpg),np.median(tmpr)]) #29 sec kb 69.17094326019287
            #pix.append([stat.median(tmpb),stat.median(tmpg),stat.median(tmpr)]) #23 sec kb, gyorsabb és elvileg pontosabb 23.943387031555176
            tmpb,tmpg,tmpr = [],[],[]

    for i in range(0,790):
        for j in range(0,1053):
            if len(pix) > 0:
                img_res[i][j] = (pix[j][0],pix[j][1],pix[j][2]) 
        pix[0:1053] = []

    end = time.time()
    print(end - start)
    cv2.imshow("kép",img_res)
    cv2.waitKey(0)
    
main()
