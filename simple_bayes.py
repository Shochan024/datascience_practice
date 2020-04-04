#!-*-coding:utf-8-*-
import sys
import math
import glob
import lib #libフォルダ内のコードをインポート 使用可能な機能は print(lib.__all__)で確認可能
"""
・知りたい確率
p(spam|meeting)

・ベイズの定理
p(spam|meeting)=p(meeting|spam)*p(spam) / p(meeting)

・p(meeting)
= p(meeting|spam)*p(spam) + p(meeting|ham)*p(ham)
"""

#基本情報取得( N_spam , N_ham , N )
spam = glob.glob("datasets/enron1/spam/*")
ham = glob.glob("datasets/enron1/ham/*")
text_spam = lib.txt_count( files=spam , text="meeting" , encoding="latin-1" )
text_ham = lib.txt_count( files=ham , text="meeting" , encoding="latin-1" )
N = text_ham["N"] + text_spam["N"]

#各確率の算出( p(spam) , p(ham) )
p_spam = text_spam["N"] / N
p_ham = text_ham["N"] / N

#尤度の算出 p(meeting|spam) p(meeting|ham)
p_meeting_bar_spam = text_spam["freq"] / text_spam["N"]
p_meeting_bar_ham = text_ham["freq"] / text_ham["N"]

#p(meeting) = p(meeting|spam)*p(spam) + p(meeting|ham)*p(ham)
p_meeting = p_meeting_bar_spam*p_spam + p_meeting_bar_ham*p_ham

#p(spam|meeting)
p_spam_meeting = round( (p_meeting_bar_spam*p_spam) / p_meeting ,2 )
print( "p(spam|meeting)="+str(p_spam_meeting)+"≒"+str(round(p_spam_meeting*100))+"%" )
