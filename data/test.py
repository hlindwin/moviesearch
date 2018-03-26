import json
import os, re, codecs

data_path = os.path.normpath(os.path.join(os.getcwd()))
#data_path = os.path.normpath(os.path.join(os.getcwd()))
for root, dirs, files in os.walk(data_path):
    for file in [f for f in files if f.endswith('.html')]:
        file_path = os.path.join(data_path, file)
       # print(file) # quotes-scoop.html
                        #/home/ubuntu/workspace/stormy-lowlands-80953/tutorial/quotes-scoop.html
       # print(file_path)
  
        with open(file) as f:
            #tree = open(f, encoding='utf-8', errors='replace')
            tree=codecs.open(file, 'r')
            tree = tree.read().splitlines()
            for row in tree:
                if row.startswith('	GlobalsObj.CMS_JSON'):
                    #print(row)
                    description = re.findall(r"\= (.+)", row)
                                       #description = re.findall(r"\{([^}]+)\}", row)
                    #print(description[0][:-1])
                    a = []
                    a.append(description[0][:-1])
                    #print(a)
                    #input()
                    #description = description[0][:-1]
        
        name = file[7:]
        name = name[:-5]
        file_name = "%s.json" % name
        #data_path = os.path.normpath(os.path.join(os.getcwd(), 'data'))
        
        with open(file_name, 'w+') as f:
            json.dump({'description': a, 'url': 'focusfeatures.com/'+name, '_type': 'x'}, f)
                
            