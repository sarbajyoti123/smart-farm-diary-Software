# # import pdb

# # # pdb.set_trace()
# # name=input('enter your name')
# # age=input('enter your age')
# # print(f"your name is {name} and your age is {age}")
# # age=int(age)+5
# # print(f"ypur name is {name} and your age after five year is {age}")
# # import matplotlib.pyplot as plt
# # import matplotlib.animation as animation
# # from matplotlib import style
# # style.use('fivethirtyeight')
# # fig=plt.figure()
# # a=fig.add_subplot(1,1,1)
# # def animate(i):
# #     graph_data=open('example.txt','r').read()
# #     x1=[]
# #     y1=[]
# #     lines=graph_data.split('\n')
# #     for line in lines:
# #         if len(line)>1:
# #             x,y=line.split(',')
# #             x1.append(x)
# #             y1.append(y)
# #     a.plot(x1,y1)
# # ani=animation.FuncAnimation(fig,animate,interval=1000)
# # # animate('i')
# # plt.show()      

# # import numpy as np
# # import matplotlib.pyplot as plt
# # from mpl_toolkits.mplot3d import axes3d
# # from matplotlib import style
# # style.use('fivethirtyeight')
# # fig=plt.figure()
# # a=fig.add_subplot(111,projection="3d")
# # x,y,z=axes3d.get_test_data()
# # # print(axes3d.__file__)
# # a.plot_wireframe(x,y,z)
# # # x=[1,2,3,4,5,6,7]
# # # y=[2,3,4,5,6,7,8]
# # # z=np.ones(7)
# # # dx=np.ones(7)
# # # dy=np.ones(7)
# # # dz=[1,2,3,4,5,6,7]
# # # a.bar3d(x,y,z,dx,dy,dz)
# # # a.scatter(x,y,z)
# # a.set_xlabel("x axis")
# # a.set_ylabel("y axis")
# # a.set_zlabel("z axis")
# # plt.show()
# # Python program for implementation of Quicksort Sort 

# # This function takes last element as pivot, places 
# # the pivot element at its correct position in sorted 
# # array, and places all smaller (smaller than pivot) 
# # to left of pivot and all greater elements to right 
# # of pivot 
# # def partition(arr,low,high): 
# # 	i = ( low-1 )		 # index of smaller element 
# # 	pivot = arr[high]	 # pivot 

# # 	for j in range(low , high): 

# # 		# If current element is smaller than or 
# # 		# equal to pivot 
# # 		if arr[j] <= pivot: 
		
# # 			# increment index of smaller element 
# # 			i = i+1
# # 			arr[i],arr[j] = arr[j],arr[i] 

# # 	arr[i+1],arr[high] = arr[high],arr[i+1] 
# # 	return ( i+1 ) 

# # # The main function that implements QuickSort 
# # # arr[] --> Array to be sorted, 
# # # low --> Starting index, 
# # # high --> Ending index 

# # # Function to do Quick sort 
# # def quickSort(arr,low,high): 
# # 	if low < high: 

# # 		# pi is partitioning index, arr[p] is now 
# # 		# at right place 
# # 		pi = partition(arr,low,high) 

# # 		# Separately sort elements before 
# # 		# partition and after partition 
# # 		quickSort(arr, low, pi-1) 
# # 		quickSort(arr, pi+1, high) 

# # # Driver code to test above 
# # arr = [10, 7, 8, 9, 1, 5] 
# # n = len(arr) 
# # quickSort(arr,0,n-1) 
# # print ("Sorted array is:") 
# # for i in range(n): 
# # 	print ("%d" %arr[i]), 
# # import cx_Freeze
# # import dlib
# # import imutils
# # import argparse
# # import pickle
# # import os
# # f=open("E:\Chem"+"\sss.TXT")
# # with open("sm.TXT","a") as t:
#     # a=t.write("\n"+input())
#     # print(a)
#     # t.close()
#     # sys.exit()
# # os.system("clear")
# # names=['ab','bc','ca']
# # print("original list")
# # print(names)
# # pickle.dump(names,open("smallik.TXT","wb"))
# # f.write("")
# # import os
# # from csv import reader
# # with open('sarbaj.csv','r') as f:
# #     t=reader(f)
# #     next(t)
# #     # print(t)
# #     for i in t :
# #         print(i)

#     # f.write('dont deserve me')
#     # f.close
#     # read=reader(f)
#     # print(read)
# # import sqlite3
# # import json
# # from datetime import datetime
# # timeframe='2017-11'
# # sql_transaction=[]
# # connection=sqlite3.connect('{}.db'.format(timeframe))
# # c=connection.cursor()
# # def create_table():
# #     c.execute("""CREATE TABLE IF NOT EXISTS parent_reply
# #     (parent_id TEXT PRIMARY KEY,comment_id TEXT UNIQUE,parent TEXT, comment TEXT,subreddit TEXT,unix INT,score INT)""")
# #     if __name__=="__main__":
# #         create_table()
# # import httplib2
# # import os
# # import re
# # import sys

# # from apiclient.discovery import build
# # from apiclient.errors import HttpError
# # from oauth2client.client import flow_from_clientsecrets
# # from oauth2client.file import Storage
# # from oauth2client.tools import argparser, run_flow


# # # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# # # the OAuth 2.0 information for this application, including its client_id and
# # # client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# # # the {{ Google Cloud Console }} at
# # # {{ https://cloud.google.com/console }}.
# # # Please ensure that you have enabled the YouTube Data API for your project.
# # # For more information about using OAuth2 to access the YouTube Data API, see:
# # #   https://developers.google.com/youtube/v3/guides/authentication
# # # For more information about the client_secrets.json file format, see:
# # #   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets

# # CLIENT_SECRETS_FILE = "client_secrets.json"

# # # This variable defines a message to display if the CLIENT_SECRETS_FILE is
# # # missing.
# # MISSING_CLIENT_SECRETS_MESSAGE = """
# # WARNING: Please configure OAuth 2.0

# # To make this sample run you will need to populate the client_secrets.json file
# # found at:

# #    %s

# # with information from the {{ Cloud Console }}
# # {{ https://cloud.google.com/console }}

# # For more information about the client_secrets.json file format, please visit:
# # https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
# # """ % os.path.abspath(os.path.join(os.path.dirname(__file__),
# #                                    CLIENT_SECRETS_FILE))

# # # This OAuth 2.0 access scope allows for full read/write access to the
# # # authenticated user's account.
# # YOUTUBE_SCOPE = "https://www.googleapis.com/auth/youtube"
# # YOUTUBE_API_SERVICE_NAME = "youtube"
# # YOUTUBE_API_VERSION = "v3"

# # SECTION_TYPES = ("allPlaylists", "completedEvents", "likedPlaylists",
# #   "likes", "liveEvents", "multipleChannels", "multiplePlaylists",
# #   "popularUploads", "recentActivity", "recentPosts", "recentUploads",
# #   "singlePlaylist", "upcomingEvents",)
# # SECTION_STYLES = ("horizontalRow", "verticalList",)

# # def get_authenticated_service(args):
# #   flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_SCOPE,
# #     message=MISSING_CLIENT_SECRETS_MESSAGE)

# #   storage = Storage("%s-oauth2.json" % sys.argv[0])
# #   credentials = storage.get()

# #   if credentials is None or credentials.invalid:
# #     credentials = run_flow(flow, storage, args)

# #   return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
# #     http=credentials.authorize(httplib2.Http()))

# # def enable_browse_view(youtube):
# #   channels_list_response = youtube.channels().list(
# #     part="brandingSettings",
# #     mine=True
# #   ).execute()

# #   channel = channels_list_response["items"][0]
# #   channel["brandingSettings"]["channel"]["showBrowseView"] = True

# #   youtube.channels().update(
# #     part="brandingSettings",
# #     body=channel
# #   ).execute()

# # def add_channel_section(youtube, args):
# #   channels = None
# #   if args.channels:
# #     channels = re.split("\s*,\s*", args.channels)
# #   playlists = None
# #   if args.playlists:
# #     playlists = re.split("\s*,\s*", args.playlists)

# #   body = dict(
# #     snippet=dict(
# #       type=args.type,
# #       style=args.style,
# #       title=args.title,
# #       position=args.position
# #     ),
# #     contentDetails=dict(
# #       channels=channels,
# #       playlists=playlists
# #     )
# #   )

# #   youtube.channelSections().insert(
# #     part="snippet,contentDetails",
# #     body=body
# #   ).execute()

# # if __name__ == '__main__':
# #   argparser.add_argument("--type", choices=SECTION_TYPES, required=True,
# #     help="The type of the section to be added.")
# #   argparser.add_argument("--style", choices=SECTION_STYLES, required=True,
# #     help="The style of the section to be added.")
# #   argparser.add_argument("--title",
# #     help=("The title to display for the new section. This is only used "
# #           "with the multiplePlaylists or multipleChannels section types."))
# #   argparser.add_argument("--position", type=int,
# #     help=("The position of the new section. "
# #          "Use 0 for the top, or don't set a value for the bottom."))
# #   argparser.add_argument("--playlists",
# #     help="One or more playlist ids, comma-separated (e.g. PL...).")
# #   argparser.add_argument("--channels",
# #     help="One or more channel ids, comma-separated (e.g. UC...).")
# #   args = argparser.parse_args()

# #   youtube = get_authenticated_service(args)
# #   try:
# #     # Before channel shelves will appear on your channel's web page, browse
# #     # view needs to be enabled. If you know that your channel already has
# #     # it enabled, or if you want to add a number of sections before enabling it,
# #     # you can skip the call to enable_browse_view().
# #     enable_browse_view(youtube)

# #     add_channel_section(youtube, args)
# #   except HttpError, e:
#     # print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
# #   else:
#     # print "Added new channel section."    
# # name="sarbajyoti"
# # dots="*****************"
# # print(name.replace('sar','&',)+dots)
# # print(name.center(20,"&"))
# # i=0
# # while i<=10:
#     # print("hello world")
#     # i+=1
#     # print(f"hello world{i}")
# # for i in range(11,-2,-1):
#     # print(i)
# # def new_greater(a,b,c):
# #     if a>b and a>c:
# #         return a
# #     elif b>a and b>c:
# #         return b
# #     else :
# #         return c    
# #     # bigger=greater(a,b)
# #     # return greater(bigger,c)
# # print(new_greater(10,20,30))    
# # mixed=[1,2,3,4,5,6,7,8]
# # mixed[2]='three'
# # del mixed[2]
# # mixed.sort()
# # print(mixed.index(5,1,8))
# # def negetive_list(lis):
# #     neg=[]
# #     for i in lis:
# #         neg.append(-i)
# #     return neg
# # print(negetive_list('sag'))    
# # mixed=('sad','dfg','jkl')
# # # mixed=(1,)
# # mixed1,mixed2,mixed3=mixed
# # print(mixed1)
# # add,multiply=func(2,3)
# # print(add)
# # user={'name':'sagar','father':'gopal'}
# # if 'sagar' in user.values():
# #     print('present')
# # else:
# #     print('false')   
# # user=dict.fromkeys(['sagar','mallik','saiakt'],'unknown')
# # print(user)
# # print(user.clear())
# # name=('sagar','mall','rashidggg')
# # print(max(name))
# # from functools import wraps
# # def decorator_function(a):
# #     @wraps(a)
# #     def wrapper_function(*args,**kwargs):
# #         data_types=[]
# #         for arg in args:
# #             data_types.append(type(arg)==int)
# #         if all(data_types):

# #             return a(*args,**kwargs)
# #         else:
# #             print("invalid statement")    
# #     return wrapper_function()    
# #         # print("this is awsome function")
# #         # return a()
# #     # return wrapper_function()

# # @decorator_function
# # def wrapper1(*args):
# #     total=0
# #     for i in args:
# #         total +=i
# #     return total
# # print(wrapper1('sagar'))    
#         # print(i)
#     # print("hey how are you")
# # decorator_function(4)
# # b()
#     # b()        
# # from csv import     writer
# # with open('sarbaj2.csv','w',newline='') as f:
# #     a=writer(f)
# #     a.writerow(['name','place'])
# #     a.writerow(['sagar','WEST BENGAL'])
# #     a.writerow(['sabya','RANCHI'])
#     # print(a['name'])

#     # for i in a:
#         # print(i['words'])
# # import cv2
# # def main():
# #     imgpath=r"D:\python\standard_test_images\lena_color_512.tif"
# #     a=cv2.imread(imgpath,0)
# #     # print(a)
# #     print(type(a))
# #     print(a.dtype)
# #     print(a.shape)
# #     print(a.ndim)
# #     print(a.size)
# #     # outpath=r"D:\python\output photo\img2.jpg"
# #     # cv2.namedWindow('sagar',cv2.WINDOW_AUTOSIZE)
# #     # cv2.imshow('sagar',a)
# #     # cv2.imwrite(outpath,a)
# #     # cv2.imwrite(outpath,a)
# #     # cv2.waitKey(0)
# #     cv2.destroyAllWindows()
# # if __name__=="__main__":
# #     main()
# # import sqlite3
# # import time
# # import random
# # import datetime
# # conn=sqlite3.connect('sagar.db')
# # c=conn.cursor()
# # def create_table():
# #     c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT, keyword TEXT, value REAL)")
# # def data_entry():
# #     c.execute("INSERT INTO stuffToPlot VALUES(1234567,'5-1-2019','python2',9)")
# #     conn.commit()
# #     c.close()
# #     conn.close()


# # def dynamic_data_entry():
# #     unix=int(input("enter unix time"))
# #     date=int(input("input date") 
# #     keywords=str(input("enter akeyword"))
# #     value=int(input("enter a value"))
# #     c.execute("INSERT INTO stuffToPlot(unix,datestamp,keyword,value) VALUES(?,?,?,?)",(unix,date,keywords,value))
# #     conn.commit()
# #     c.close()
# #     conn.close()
    
# # # for i in range(1,10):
# #     # dynamic_data_entry()
# #     # time.sleep(1)
        
# # create_table()
# # dynamic_data_entry()
# # # data_entry()



# import sqlite3
# import time
# import random
# import datetime
# # import matplotlib.pyplot as plt
# # from matplotlib import style
# # style.use('fivethirtyeight')
# conn=sqlite3.connect('sagarmallikk.db')
# c=conn.cursor()
# def create_table():
#     c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT, keyword TEXT, value BLOB)")
# def data_entry():
#     c.execute("INSERT INTO stuffToPlot VALUES(1234567,'5-1-2019','python2',9)")
#     conn.commit()
#     c.close()
#     conn.close()


# # def dynamic_data_entry():
# #     unix=input('enter time')
# #     date=input('enter date')
# #     keywords=input('enter words')
# #     value=input('enter a value')
# #     a=c.execute("INSERT INTO stuffToPlot(unix,datestamp,keyword,value) VALUES(?,?,?,?)",(unix,date,keywords,value))
# #     conn.commit()
# #     c.close()
# #     conn.close()
# # def read_from_db():
# #     keyword=input("enter username")
# #     # password=input("enter password")
# #     # c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='python' ")
# #     c.execute("SELECT keyword FROM stuffToPLot WHERE keyword = ?")
# #     data=c.fetchone()
# #     if c.fetchall():
# #         for i in c.fetchall():
# #             print("excess granted")
# #             break
# #     else:
# #         print("excess denied")    
# #     # print(data)
# #     for i in data:
#         # print(i)

#     # for i in a:
#         # print(i)
# # read_from_db()
# #     
# # for i in range(1,10):
#     # dynamic_data_entry()
#     # time.sleep(1)
        
# # create_table()
# # dynamic_data_entry()
# # data_entry()
# def graph_data():
#     c.execute("SELECT * FROM stuffToPlot LIMIT 1")
#     data=c.fetchall()
#     for i in data:
#         print(i)
#     # dates=[]
#     # values=[]
#     # for i in c.fetchall():
#     #     dates.append(i[0])
#     #     values.append(i[1])
#     # plt.plot_date(dates,values,':')    
#     # plt.show()
# # create_table()
# # read_from_db()
# # graph_data()        


# # import sqlite3
# # import time
# # import random
# # import datetime
# # import matplotlib.pyplot as plt
# # from matplotlib import style
# # style.use('fivethirtyeight')
# # conn=sqlite3.connect('sagar.db')
# # c=conn.cursor()
# # def create_table():
# #     c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT, keyword TEXT, value REAL)")
# # def data_entry():
# #     c.execute("INSERT INTO stuffToPlot VALUES(1234567,'5-1-2019','python2',9)")
# #     conn.commit()
# #     c.close()
# #     conn.close()


# def dynamic_data_entry():
#     unix=input('enter time')
#     date=input('enter date')
#     keywords=input('enter words')
#     value=input('enter a value')
#     a=c.execute("INSERT INTO stuffToPlot(unix,datestamp,keyword,value) VALUES(?,?,?,?)",(unix,date,keywords,value))
#     conn.commit()
#     c.close()
#     conn.close()
# def read_from_db():
#     total=0
#     keyword=input("enter username")
#     value=input("enter password")
#     # c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='python' ")
#     # c.execute("SELECT seed FROM app6 ")
#     c.execute("SELECT *  FROM stuffTooPlot WHERE keyword = ? AND value = ?  LIMIT  1")
#     c.execute([(keyword),(value)])
#     # c.execute("SELECT *  FROM stuffTooPlot WHERE keyword = ? AND value = ?  ",[(keyword),(value)])            
#     data=c.fetchall()
#     # print(c.fetchall())
#     # a=data.pop()
#     if data:
#             for i in data:
#                 print("granted")
#                 # print(data)
#                 # from form import Ui_otherwindow
#                 # from python46 import TabbWidget
#                 # self.anotherWindow()
#                 # self.openWindow()
                
#                 # QMessageBox.information(self,"game","excess granted",QMessageBox.Ok,QMessageBox.Ok)
#     else:
#         print("denied")
#             # QMessageBox.information(self,"game","excess denied",QMessageBox.Ok,QMessageBox.Ok)
                
#     # for i in data:
#         # print(i)
#     # c.moveToLast()
#     # cursor.moveToLast
#     # a=("SELECT keyword,value  FROM stuffToPLot WHERE keyword = ? AND value = ? LIMIT 1")
#     # c.execute(a,[(keyword),(value)])

#     # data=c.fetchall()
#     # a=data.pop()
#     # for i in a:
#     #     print(i)



#     # a=[sum(x) for x in zip(*data)]
#     # print(a)
#     # for i in c.fetchall():
#         # total=total+i
#         # [sum(x) for x in zip(*l)]
#         # a=list(i)
#         # print(list(i))
#         # print(sum(5,1))

#         # print(total)
#         # print(sum(i))
#         # print(i)
#         # total=total+i
#         # print(i)
#     # print(data)
#     # if data:
#         # for i in data:
#     #         # c.execute("SELECT keyword,value  FROM stuffToPLot ")
#             # print("excess granted")
#     # else:
#         # print("excess denied")    
#     # print(data)
#     # for i in data:
#         # print(i)

# #     # for i in a:
# #         # print(i)
# # # read_from_db()
# # #     
# # # for i in range(1,10):
# #     # dynamic_data_entry()
# #     # time.sleep(1)
        
# # # create_table()
# # # dynamic_data_entry()
# # # data_entry()
# # def graph_data():
# #     c.execute("SELECT unix,value FROM stuffToPlot")
# #     dates=[]
# #     values=[]
# #     for i in c.fetchall():
# #         dates.append(i[0])
# #         values.append(i[1])
# #     plt.plot_date(dates,values,':')    
# #     plt.show()
# def del_and_update():
#     # a=input('enter time')
#     # b=input('enter date')
#     # c.execute("UPDATE stuffToPlot SET value= 98 WHERE value= 1 ")
#     c.execute("DELETE FROM app10 WHERE seed=55555.0 ")
#     conn.commit()
#     # c.execute("SELECT * FROM stuffToPlot")
#     # [print(i) for i in c.fetchall()]
#     # conn.commit()
#     c.close()
#     conn.close()
# create_table()
# # read_from_db()
# # dynamic_data_entry()
# # dynamic_data_entry()
# del_and_update()
# # graph_data()   
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog,QVBoxLayout,QPushButton
import sys


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "SELECT LANGUAGE"        
        self.top = 100        
        self.left = 100        
        self.width = 680        
        self.height = 500
        layout=QVBoxLayout()
        Button=QPushButton("BENGALI",self)
        # Button.hideEvent(self,)
        Button.clicked.connect(self.bengaliButton)

        layout.addWidget(Button)
        Button2=QPushButton("ENGLISH",self)
        Button2.clicked.connect(self.punjabiButton)
        layout.addWidget(Button2)
        Button3=QPushButton("HINDI",self)
        Button3.clicked.connect(self.hindiButton)
        layout.addWidget(Button3)
        self.setLayout(layout)

        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def bengaliButton(self):
        from python46 import TabbWidget
    def punjabiButton(self):
        from python58 import TabbWidget    
    def hindiButton(self):
        from form import TabbWidget        



App = QApplication(sys.argv)
window = Window()
App.exec()
# sys.exit(App.exec())

     


















