from flask import Flask
from get_files import get_files
from flask_cors import CORS 
app = Flask(__name__)
CORS(app)
# files= get_files()

# file_dict={}
# file_dict['extension']={}
# for file1 in files:
#     file=file1.split('.')
#     if file[1] in file_dict['extension'].keys():
#         file_dict['extension'][file[1]]+=1
#     else:
#         file_dict['extension'][file[1]]=1
#         file_dict['extension']['file'+file[1]]=[]
#     file_dict['extension']['file'+file[1]].append(file1)
# print(file_dict)

@app.route('/')
def get_files1():
    files= get_files()
    file_dict={}
    file_dict['extension']={}
    
    print(files)
    for file1 in files:
        file=file1.split('.')
        if not file[1] in file_dict['extension'].keys():
            file_dict['extension'][file[1]]={'number of files':1, 'files':[]}
        else:
            file_dict['extension'][file[1]]['number of files']+=1
            
        file_dict['extension'][file[1]]['files'].append(file1)
    print(file_dict)
    return file_dict

if __name__ == '__main__':
    app.run(debug=True)