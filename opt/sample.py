from distutils import errors
from email import charset
import imaplib
import email
import pprint
import slackweb
import configparser
from logging import getLogger
import logging
import json
from email.header import decode_header
import base64
import sys
import traceback
from collections import defaultdict
#debug

# 設定ファイルの読み込み
json_file = open('setting.json', 'r')
json_data = json.load(json_file)

#logファイルの読み込み
LOG_FOLDER = "log/Log.log"

#loggerの読み込み
logger = logging.getLogger("logger")    #logger名loggerを取得
# logger.setLevel(logging.DEBUG)  #loggerとしてはDEBUGで
handler = logging.FileHandler(filename=LOG_FOLDER)  #handler2はファイル出力
handler.setLevel(logging.DEBUG)     #handler2はLevel.WARN以上
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))
logger.addHandler(handler)

#slack通知設定
slack = slackweb.Slack(url=json_data["WEBHOOKURL"])
logger.info("設定ファイルの読み込み完了")
logger.info("メールの読み込み開始")

#メールの情報読み込み
def road_email_object() -> dict():
    #gmailの読み込み
    gmail = imaplib.IMAP4_SSL("imap.gmail.com", '993')
    gmail.login(json_data["USERNAME"], json_data["PASSWORD"])
    #BPラベルを取得
    gmail.select()
    gmail.select("INBOX")
    gmail.select("BP")
    try:
        head, data = gmail.search(None, 'ALL')
        emaildata = defaultdict(dict)
        index = 0
        for num in data[0].split():
            h, d = gmail.fetch(num, '(RFC822)')
            raw_email = d[0][1]
            msg = email.message_from_string(raw_email.decode('utf-8'))
            msg_encoding = email.header.decode_header(msg.get('Subject'))[0][1] or 'iso-2022-jp'
            # 件名
            msg_subject = email.header.decode_header(msg.get('Subject'))[0][0]
            #　差出人
            from_ = email.header.decode_header(msg.get('From'))[0][0]
            emaildata[index]['from'] = from_
            # 日付
            date = email.header.decode_header(msg.get('date'))[0][0]
            emaildata[index]['date'] = date
            # エンコーディング
            subject = str(msg_subject.decode(msg_encoding))
            emaildata[index]['subject'] = subject
            index+=1
            #print(subject)
        gmail.close()
        gmail.logout()
        return emaildata
    except Exception as e:
        logger.error(e)
        gmail.close()
        gmail.logout()
        print(traceback.format_exc())

#メールの本文読み込み
def road_email_msg():
    try:
        # 本文の抽出
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            filename = part.get_filename()
            body = base64.urlsafe_b64decode(part.get_payload().encode('ASCII', errors='replace')).decode('utf-8', errors='replace')
            # body = base64.urlsafe_b64decode(part.get_payload().encode('ASCII', errors='replace')).decode('utf-8', errors='replace')
            #body = base64.urlsafe_b64decode(part.get_payload().encode('ASCII', errors='ignore')).decode('utf-8')
            if("希望単価" in body):
                send_text = "件名:" + subject + "\n" + "差出人:" + from_ + "\n" + "日付:" + date + "\n" + "本文" + "\n" + body
            # else:
        # print(body)
    except binascii.Error as be:
        logger.error(be)

        pass
    except Exception as e:
        logger.error(e)
        print(traceback.format_exc())

#スラック通知
def slacksend(text) -> bool():
    try:
        slack.notify(text=text)
    except Exception as e:
        logger.error(e)
        print(traceback.format_exc())

#形態素解析関数



#debug用
hoge = road_email_object()
print("メール読み込み完了")



