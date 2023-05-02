import cv2 
import numpy as np
import glob
import statistics as stat

def main():
    images = [cv2.imread(file) for file in glob.glob("D://programok//kepf//beka//beka*.jpg")]
    #images = [cv2.imread(file) for file in glob.glob("D://programok//kepf//fo//fo*.jpg")]
    #images = [cv2.imread(file) for file in glob.glob("D://programok//kepf//kep//kep*.jpg")]
    img_res =  np.zeros((790, 1053, 3), dtype = "uint8")
    resized = []
    separated = []
    tmpb = []
    tmpg = []
    tmpr = []
    pix = []

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
                        tmpb.append(separated[l][k][i][j])
                    elif k ==1:
                        tmpg.append(separated[l][k][i][j])
                    else:
                        tmpr.append(separated[l][k][i][j])
            pix.append([np.mean(tmpb),np.mean(tmpg),np.mean(tmpr)]) #44,7 sec kb
            #pix.append([stat.mean(tmpb),stat.mean(tmpg),stat.mean(tmpr)]) #1:40 min kb, de pontosabb
            #pix.append([np.median(tmpb),np.median(tmpg),np.median(tmpr)]) #29 sec kb
            #pix.append([stat.median(tmpb),stat.median(tmpg),stat.median(tmpr)]) #23 sec kb, gyorsabb és elvileg pontosabb
            tmpb = []
            tmpg = []
            tmpr = []

    

    for i in range(0,790):
        for j in range(0,1053):
            if len(pix) > 0:
                img_res[i][j] = (pix[j][0],pix[j][1],pix[j][2]) 
        pix[0:1053] = []

    cv2.imshow("kép",img_res)
    cv2.waitKey(0)

main()

#b,g,r = cv.split(image)
#image2 = cv.merge([b,g,r])