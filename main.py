import cv2 
import numpy as np
import glob
import statistics as stat

def main():
    images = [cv2.imread(file) for file in glob.glob("D://programok//kepf//project//kep//kep*.jpg")]
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
            pix.append([tmpb,tmpg,tmpr])
            tmpb = []
            tmpg = []
            tmpr = []

    res = []
    tmp = []
    for i in range(0,len(pix)):
        for j in range(0,len(pix[0])):
           tmp.append(stat.median(pix[i][j]))
        res.append(tmp)
        tmp = []

    for i in range(0,790):
        for j in range(0,1053):
            if len(res) > 0:
                img_res[i][j] = (res[j][0],res[j][1],res[j][2]) 
        res[0:1053] = []

    cv2.imshow("kép",img_res)
    cv2.waitKey(0)

main()

#b,g,r = cv.split(image)
#image2 = cv.merge([b,g,r])