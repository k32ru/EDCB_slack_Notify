import time
import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import config as config

class FileChangeHandler(FileSystemEventHandler) :

    # ファイル変更時のイベント
    def on_modified(self , event) :
        filepath = event.src_path
        filename = os.path.basename(filepath)
        # print('%s modified' % filename)
        if (filename == config.wathfileName) :
            ReadFile()

def ReadFile() :
    readfilename = config.watchfilepath + "\\" + config.wathfileName

    with open(readfilename , 'r' , encoding="utf-16-le" , ) as f :
        lines = f.read().splitlines()
        last_line = lines[-1]

    for l in config.IgnoreMessages :
        if l not in last_line :
            config.slack.notify(text=last_line)
            for mm in config.MentionMessages :
                if mm in last_line :
                    config.slack.notify(text="<" + config.slackID + "> 重大なエラーを検知しました。" + "内容：「" + mm + "」")

    print(last_line)

if __name__ in '__main__' :

    print(config.watchfilepath + config.wathfileName + 'を監視開始')
    while True :
        event_handler = FileChangeHandler()
        observer = Observer()
        observer.schedule(event_handler , config.watchfilepath , recursive=True)
        observer.start()
        try :
            time.sleep(config.waitsec)
        except KeyboardInterrupt :
            observer.stop()
        observer.join()
