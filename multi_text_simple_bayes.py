#!-*-coding:utf-8-*-
import sys
import math
import glob
import lib #libフォルダ内のコードをインポート 使用可能な機能は print(lib.__all__)で確認可能
import numpy as np
"""
・知りたい確率
p(spam|meeting)

・ベイズの定理
p(spam|meeting)=p(meeting|spam)*p(spam) / p(meeting)

・p(meeting)
= p(meeting|spam)*p(spam) + p(meeting|ham)*p(ham)
"""

def multi_text( spam , ham , spam_texts ):
    spam_likely,ham_likely = 1,1
    N_spam,N_ham = len(spam),len(ham)
    p_spam = N_spam/( N_spam+N_ham )
    for spam_text in spam_texts:
        text_spam = lib.txt_count( files=spam , text=spam_text , encoding="latin-1" )
        text_ham = lib.txt_count( files=ham , text=spam_text , encoding="latin-1" )

        p_text_spam,p_text_ham = text_spam["freq"]/text_spam["N"]\
        ,text_ham["freq"]/text_ham["N"]

        spam_likely += np.log(p_text_spam*p_spam)
        ham_likely += np.log(p_text_ham*p_spam)

    return {"spam_likely":round(spam_likely,3),"ham_likely":round(ham_likely,3)}


spam_texts = ["meeting","url"] #ここの値を変えると確率が変わる。それ以外は触らないくて良い

#基本情報取得( N_spam , N_ham , N )
spam = glob.glob("datasets/enron1/spam/*")
ham = glob.glob("datasets/enron1/ham/*")

outcome = multi_text( spam=spam , ham=ham , spam_texts=spam_texts )

if outcome["spam_likely"] >= outcome["ham_likely"]:
    print("p(text|spam)p(spam)="+str(outcome["spam_likely"])\
    +">= p(text|ham)p(ham)="+str(outcome["ham_likely"]))
    print("outcome : spam")
else:
    print("p(text|spam)p(spam)="+str(outcome["spam_likely"])\
    +"< p(text|ham)p(ham)="+str(outcome["ham_likely"]))
    print("outcome : ham")
