#!/usr/bin/python3.6

#タスクリストファイルのパス
path="/home/sasa/python_task.dir/list.py"

#osモジュールをインポート
import os

#getpassモジュールをインポート
import getpass

#datetimeモジュールをインポート
import datetime

#操作選択
def Start():

    #グローバル変数としてfsize変数を宣言
    global fsize

    #ファイルサイズを取得
    fsize=os.path.getsize(path)

    #メニュー画面を表示
    print("\n* 何をしますか ?\
           \n* 番号を選んでください\
           \n\n1.タスクを追加する\
           \n2.タスクを表示する\
           \n3.タスクを削除する\
           \n4.作業を終了する\n")

    #変数opeに操作番号を格納する
    try:
        ope=input()

    #文字コードエラーを吐いた場合は再入力を促す
    except UnicodeDecodeError:
        print("* エラーが発生しました...\
               \n* もう一度入力してください")
        return Start()

    #1を選んだ場合
    if ope == "1" or ope == "１":
        Add()

    #2を選んだ場合
    elif ope == "2" or ope == "２":

        #ファイルサイズが0より大きい場合
        if fsize > 0:
            View()

        #0の場合
        else:
            print("\n* 登録されているタスクはありません")
            Start()

    #3を選んだ場合
    elif ope == "3" or ope == "３":

        #ファイルサイズが0より大きい場合
        if fsize != 0:
            Delete()

        #0の場合
        else:
            print("\n* 登録されているタスクはありません")
            Start()

    #4を選んだ場合
    elif ope == "4" or ope == "４":
        Finish()

    #1～4以外を選んだ場合
    else:
        print("\n* もう一度入力してください")
        Start()

#タスクを追加する
def Add():

    #タスクリストを表示する
    with open(path,"r") as f:

        #ファイルサイズが0より大きい場合
        if fsize > 0:
            print(f"\n* 現在のタスクを表示します\
                    \n\n=====\n{f.read()}=====")

        #追加画面を表示
        print("\n* 追加するタスクを入力してください\
　　　　　     \n* キャンセル と入力すると選択画面に戻ります\n")

    #追加タスクを格納する
    try:
        add_task=input()

    #文字コードエラーを吐いた場合は再入力を促す
    except UnicodeDecodeError:
        print("* エラーが発生しました...\
             \n* もう一度入力してください")
        return Add()

    #add_taskが"キャンセル"以外の場合
    if add_task != "キャンセル" and add_task != "きゃんせる":

        #タスクリストに追記する
        with open(path,"a") as f:
                   f.write(add_task + "\n")

        #タスクリストを表示する
        with open(path,"r") as f:
            print(f"\n* {add_task} を追加しました !\
                  \n\n=====\n" + f.read() + "=====")

            #Enterで次の画面へ
            input("\n* Enterキーを押すと戻ります")

    #選択画面に戻る
    print("\n* 選択画面に戻ります")
    Start()

#タスクを表示する
def View():

    #タスクリストを表示する
    with open(path,"r") as f:
        print("\n* 現在のタスクを表示します\
               \n\n=====\n" +  f.read() + "=====")

        #Enterで次の画面へ
        input("\n* Enterキーを押すと戻ります")

    #選択画面に戻る
    print("\n* 選択画面に戻ります")
    Start()

#タスクを削除する
def Delete():

    #タスクリストを表示する
    with open(path,"r") as f:
        print("\n* 現在のタスクを表示します\
               \n\n=====\n" + f.read() + "=====\
               \n\n* どのタスクを削除しますか ?\
               \n* キャンセル と入力すると選択画面に戻ります\
               \n* 全て と入力するとタスクを全て削除します\n")

    #タスクリストを読み込む
    with open(path,"r") as f:

        #格納用リスト
        task_word=[]

        #list_wordにタスクを格納していく
        for word in f:
            task_word.append(word.rstrip("\n"))

        #削除タスクを格納する
        try:
            remove_task=input()

        #文字コードエラーを吐いた場合は再入力を促す
        except UnicodeDecodeError:
            print("* エラーが発生しました...\
                 \n* もう一度入力してください")
            return Delete()
        
        #remove_taskが"全て"の場合
        if remove_task == "全て" or remove_task == "すべて" or\
           remove_task == "スベテ":

            #ファイルサイズを0にする
            with open(path,"a") as f:
                f.truncate(0)
                print("\n* 全てのタスクを削除しました !")

        #remove_taskが"キャンセル"以外の場合
        elif remove_task != "キャンセル" and remove_task != "きゃんせる":

            #list_taskにremove_taskがあるかどうか判定する
            try:
                task_word.remove(remove_task)
                bool=True

            #値が無かった場合
            except ValueError:
                print(f"*  {remove_task} は見つかりませんでした...")
                bool=False

            #bool値がTrueの場合
            if bool == True:

                #タスクリストファイルに削除後のタスクリストを書き込む
                with open(path,"w") as f:
                    for word in task_word:
                        f.write(str(word) + "\n")
                    print(f"\n* {remove_task} を削除しました !")

                #削除後にファイルサイズを更新
                fsize=os.path.getsize(path)

                #ファイルサイズが0より大きい場合
                if fsize > 0:

                    #タスクリストを表示する
                    with open(path,"r") as f:
                        print("\n=====\n" + f.read() + "=====" )

                #Enterで次の画面へ
                input("\n* Enterキーを押すと戻ります")

        #選択画面に戻る
        print("\n* 選択画面に戻ります")
        Start()

#作業を終了する
def Finish():

    #hourが0以上8以下の場合
    if 0 <= hour <= 8:
        print(f"\n* またね {username} !\n")

    #hourが9以上16以下の場合
    elif 9<= hour <= 16:
        print(f"\n* おつかれ {username} !\n")

    #hourが上記以外の場合
    else:
        print(f"\n* おやすみ {username} !\n")

#ユーザーネームを取得
username=getpass.getuser()

#時間を取得
now=datetime.datetime.now()
hour=now.hour

#hourが0以上8以下の場合
if 0 <= hour <= 8:
    print(f"\n* おはよう {username} !")

#hourが9以上16以下の場合
elif 9<= hour <= 16:
    print(f"\n* こんにちは {username} !")

#hourが上記以外の場合
else:
    print(f"\n* こんばんは {username} !")

Start()
