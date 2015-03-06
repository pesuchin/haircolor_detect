# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import requests
import shutil

def getfiles(path):
  files = []
  for item in os.listdir(path):
    if not os.path.isdir(os.path.join(path,item)):
      files.append(item)
  return files

def cut(x,y,w,h,filename): 
    # 画像取得
    im = cv2.imread(filename)
    figure = False 
    # 画像の切り抜き
    im_trim = im[y:y+h, x:x+w]
    wide = len(im_trim)
    height = len(im_trim[0])
    #print im_trim
    #print wide,height
    freq = {}
    trim = []
    # 頻度を数える辞書(横)
    for coler in im_trim[0:height/6].tolist():
      for c in coler:
        cat = ''
        for rgb in c:
          cat += str(rgb)+":"
        freq[cat[0:-1]] = 0

    # 頻度を数える辞書(縦)
    for coler in im_trim[height/6:height/5].tolist():
      for c in coler[0:wide/10]:
        cat = ''
        for rgb in c:
          cat += str(rgb)+":"
        freq[cat[0:-1]] = 0
    for coler in im_trim[height/6:height/5].tolist():
      for c in coler[wide-wide/10:wide]:
        cat = ''
        for rgb in c:
          cat += str(rgb)+":"
        freq[cat[0:-1]] = 0
    # 頻度を数える(横)
    for coler in im_trim[0:height/6].tolist():
      for c in coler:
        cat = ''
        for rgb in c:
          cat += str(rgb)+":"
        freq[cat[0:-1]] += 1
    # 頻度を数える(縦)
    for coler in im_trim[height/6:height/5].tolist():
      for c in coler[0:wide/15]:
        cat = ''
        for rgb in c:
          cat += str(rgb)+":"
        freq[cat[0:-1]] += 1
    for coler in im_trim[height/6:height/5].tolist():
      for c in coler[0:wide/15]:
        cat = ''
        for rgb in c:
          cat += str(rgb)+":"
        freq[cat[0:-1]] += 1

    #print freq
    # 頻出色の取得
    m = max([(v,k) for k,v in freq.items()])[1].split(":")
    print m
    thres = 0
    flug = False
    # 文字列型から整数型へ変換
    k=[]
    for i in m:
      k.append(int(i))
    # 白かどうかの評価
    for i in m:
      if int(i) >= 240:
        thres += 1
    if min(k) >= 190:
      flug = True
    if flug == True and sum(k) >= 590:
        thres = 3
    if thres == 3:
      predict = True
      print "This is a white hair!"
    else:
      predict = False
      print "This is not a white hair..."
    if figure == True:
    # 画像表示
      cv2.imshow("Show Image",im_trim)
    # キー入力待機
      cv2.waitKey(0)
    # ウィンドウ破棄
      cv2.destroyAllWindows()
    # 切り抜いた画像保存
    #cv2.imwrite("trim.jpg", im_trim)
    return predict

def face_detect(filename):
    print "open:"+filename
    filepath = "./image/"+filename
    # 画像の読み込み
    im = cv2.imread(filepath)
    # 顔探索用の機械学習ファイルを取得
    cascade = cv2.CascadeClassifier("lbpcascade_animeface.xml")
    # 顔探索(画像,縮小スケール,最低矩形数)
    face = cascade.detectMultiScale(im, 1.1, 3)
    pre = []
    # 顔検出した部分を長方形で囲う
    for (x, y, w, h) in face:
        cv2.rectangle(im, (x, y),(x + w, y + h),(0, 50, 255), 3)
        pre.append(cut(x,y,w,h,filepath))
    print pre
    if len(pre)>2 or len(pre)==0:
      os.remove(filepath)
    elif isinstance(im,type(None)):
      os.remove(filepath)
    elif True in pre:
      shutil.move(filepath,"./image/sirokami/")
    else:
      shutil.move(filepath,"./image/gomi/")

if __name__ == '__main__':
    files = getfiles('./image/')
    for file in files:
      face_detect(file)
