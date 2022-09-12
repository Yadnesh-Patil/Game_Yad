import random as r
import mysql.connector as db

class stonepaperscissor:
    def __init__(self):
        self.stone='Stone'
        self.paper='Paper'
        self.scissors='scissors'

        mydb=db.connect(host='localhost',user='******',passwd='***********')
        cur=mydb.cursor()

        query='''
        create database if not exists yadnesh;
        '''
        cur.execute(query)
        mydb.close()

        

        mydb=db.connect(host='localhost',user='******',passwd='*********',database='*******')
        cur=mydb.cursor()
        query='''
        create table if not exists stonepaperscissors(Id int primary key auto_increment,
        UserName varchar(50) not null,
        Userinput varchar(100) not null,
        Systeminput varchar(100) not null,
        Result varchar(100) not null
        );
        '''

        cur.execute(query)
        
        mydb.close()

    def game(self,username1,uch,data,resultgame):
        mydb=db.connect(host='localhost',user='*****',passwd='*******',database='*****')
        cur=mydb.cursor()

        data1=(username1,uch,data,resultgame)

        query='''
        insert into stonepaperscissors(Username,Userinput,Systeminput,Result) Values(%s,%s,%s,%s);
        '''
        cur.execute(query,data1)
        cur.execute('commit;')
        mydb.close
        return f'Result of following game is {resultgame}'

    def showdata(self,username1):
        mydb=db.connect(host='localhost',user='******',passwd='*********',database='*****')
        cur=mydb.cursor()
        data=(username1,)

        query='''
        select * from table where UserName=%s;
        '''

        cur.execute(query,data)
        userdata=cur.fetchall()
        mydb.close()
        return userdata


a=stonepaperscissor()
while True:
    print('\n*************Welcome to Stone Paper Scissors Game***************\n')

    print('\nSelect one from the given choice.\n1. Play Game\n2. Show Game Data\n3. Exit')

    ch=input('Enter your choice: ')

    if ch=='1':
        while True:

            username1=input('Enter your name: ')

            print('Pick any one the following')
            print('\nSTONE\nPAPER\nSCISSORS\n')
            

            Stone=['STONE','Stone','stone']
            Paper=['PAPER','Paper','paper']
            Scissors=['Scissors','scissors','SCISSORS']

            systemout=['STONE','Stone','stone','PAPER','Paper','paper','Scissors','scissors','SCISSORS']

            uch=input('Enter any one of the above item: ')

            datasample=r.sample(systemout,1)
            data=''
            for m in datasample:
                data+=m
            print(data)

            if (uch in Stone and data in Stone) or (uch in Paper and data in Paper) or (uch in Scissors and data in Scissors):
                resultgame='Draw'
                x=a.game(username1,uch,data,resultgame)
                print(f'\n{x}\n')


            elif (uch in Stone and data in Paper) or (uch in Paper and data in Scissors) or (uch in Scissors and data in Stone):
                resultgame='Lose'
                x=a.game(username1,uch,data,resultgame)
                print(f'\n{x}\n')

            elif (uch in Scissors and data in Paper) or (uch in Stone and data in Scissors) or (uch in Paper and data in Stone):
                resultgame='Win'
                x=a.game(username1,uch,data,resultgame)
                print(f'\n{x}\n')

            else:
                print('*******************Invalid Choice**********************')


    elif ch=='2':
        print('\n************DATA FOR THE YOUR GAME PLAY IS AS GIVEN BELOW************\n')
        username1=input('Enter Your Name : ')
        y=a.showdata(username1)

        for i in y:
            print(i)

        print()

    elif ch=='3':
        print('\n****************Exiting Application***************\n*******************Thankyou*********************\n')
        break

    else:
        print('\n******Invalid Option********\n')
        