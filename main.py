# -*- coding: UTF-8 -*-
import face_recognition
import os
# 加载示例图片并学习如何识别它。
path ="images"#在同级目录下的images文件中放需要被识别出的人物图
total_image=[]
total_image_name=[]
total_face_encoding=[]
for fn in os.listdir(path): #fn 表示的是文件名
    if fn == 'unknown.jpg':
        continue
    total_face_encoding.append(face_recognition.face_encodings(face_recognition.load_image_file(path+"/"+fn))[0])
    fn=fn[:(len(fn)-4)]#截取图片名（这里应该把images文件中的图片名命名为为人物名）
    print('[+]loading:{0}'.format(fn))
    total_image_name.append(fn)#图片名字列表

#加载未知图片
unknown_image = face_recognition.load_image_file("images/unknown.jpg")
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# 看看面部是否与已知人脸相匹配。
for i,v in enumerate(total_face_encoding):
    match = face_recognition.compare_faces([v], unknown_encoding, tolerance=0.4)
    name = "Unknown"
    if match[0]:
        name = total_image_name[i]
        print('[+]you look like:{0}'.format(name))
