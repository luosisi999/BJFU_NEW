import re
# 以写的方式打开文件，如果文件不存在，就会自动创建
f = open("./data/jibing.txt","r", encoding='utf-8')   #设置文件对象
line = f.readline()
line = line[:-1]
arr=[]
while line:             #直到读取完文件
    line = f.readline()  #读取一行文件，包括换行符
    line = line[:-1]     #去掉换行符，也可以不去
    if(line.find('[疾病名称]')!=-1 or line.find('[同义词]') != -1):
        if(line.find('[疾病名称]')!=-1):
            ind = line.find('[疾病名称]')
        else:
            ind = line.find('[同义词]')
        jibing=line[ind+6:].replace('\ue007',"(")
        jibing=jibing.replace('\ue008',")")
        jibing=jibing.replace('\ue00d',"[")
        jibing=jibing.replace('\ue00e',"]")
        index=jibing.find("www")
        if(index!=-1):
            jibing=jibing[0:index]
        jibing = re.sub(u"\\(.*?\\)", "", jibing)
        jibing=jibing.lstrip()

        # 处理[]
        if (jibing.find('[')!=-1):
            ide2_s=jibing.find('[')
            ide2_e=jibing.find(']')
            temp=jibing
            jibing = re.sub(u"\\[.*?\\]", "", jibing)
            arr.append(jibing.replace(" ",""))
            temp2=temp[0:ide2_s-(ide2_e-ide2_s-1)]
            jibing2=temp2+temp[ide2_s+1:ide2_e]+temp[ide2_e+1:]
            arr.append(jibing2.replace(" ",""))
        else:
            arr.append(jibing.replace(" ",""))
            # 开始处理[]
        # if(jibing):
        #     if (len(jibing)<2):
        #         print(jibing)
f.close() #关闭文件
print(arr)
# 以写的方式打开文件，如果文件不存在，就会自动创建
file_write_obj = open("dest.txt", 'w',encoding='utf-8')
for var in arr:
    if(var!=""):
      file_write_obj.writelines(var)
      file_write_obj.write('\n')
file_write_obj.close()

