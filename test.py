import os

def findfile(key, inputdir ='.'):
    found_list = []
    all_files = os.listdir(inputdir)

    for name in all_files:
        full_name = inputdir + '/' + name
        # print(full_name)
        if key in name:
            found_list.append(key)
            print(name)
            print(found_list)
        else:
            try:
                with open(full_name) as f:
                    for l in f:
                        if key in l:
                            found_list.append(full_name + ":" + l.strip())
                            break
            except:
                pass
    return found_list

keyword = input("输入关键字：")
path = input("输入路径：")

if not path.strip():
    path = '.'

result = findfile(keyword, path)


print("===========结果================")

for r in result:
    print(r)
        