with open(r"C:\Users\Michael藤井树\Documents\python_prc\report.txt",\
     encoding='utf-8') as f:
    firstLine = "名次 " + f.readline().strip() + " 总分" + " 平均分"
    list_sub = firstLine.split()
    stu_data = f.readlines()
    data_average = []
    
    for single_stu in stu_data:
        stu_data = single_stu.split()   #每名学生的数据列表
        total = 0     #每名同学的总分
        for s in range(1, 10):
            total += int(stu_data[s])
        average_score = round(total / 9, 2)
        stu_data.extend([str(total), str(average_score)]) 
        data_average.append(stu_data)          
        
    data_average.sort(key= lambda x : x[10], reverse= True)
   
    score_pj = ['0', "平均"]
    for i in range(1, 12):
        score_sub = 0
        for j in data_average:
            score_sub += float(j[i])
        score_sub_pj = round(score_sub / len(data_average), 1)
        score_pj.append(str(score_sub_pj))
    
    score_mc = []
    for i in range(len(data_average)):
        score_sort = data_average[i]
        score_sort.insert(0, str(i + 1))
        score_mc.append(score_sort)    

    for i in range(2, 11):
        for j in score_mc:
            if int(j[i]) < 60:
                j[i] = "不合格"
    score_mc.insert(0, score_pj)
    score_mc.insert(0, firstLine)

with open(r"C:\Users\Michael藤井树\Documents\python_prc\result.txt",\
    'w', encoding='utf-8') as f2:
    for i in score_mc:
        line = ' '.join(i) + '\n'
        f2.write(line)


    

    
   
            
        



