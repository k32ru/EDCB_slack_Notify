import slackweb

# -------------------------------
#  config
# 使う時にはconfig.py　に名前を変更してください。
# slack webhookurlの取得については以下のURLを参照のこと
# Python3でslackに投稿する - Qiita https://qiita.com/shtnkgm/items/4f0e4dcbb9eb52fdf316
slack = slackweb.Slack(url="https://hooks.slack.com/services/xxxxxxxxxxxx/xxxxxxxxxxxxxxx")
# slackID メンテンションするときに使用するIDです。
# 自分のIDを調べる時には以下のURLを参考にしてください
# SlackのIncoming Webhooksでメンションを飛ばす方法 - Qiita https://qiita.com/ryo-yamaoka/items/7677ee4486cf395ce9bc
slackID = "@xxxxxx"

# 監視対象のEpgTimerSrvNotify.logがあるパス　先頭にrを付ける必要があります
# 例: watchfilepath=r"C:\Users\k32ru\Documents\MyProgramfiles\EpgDataCap_Bon_EX"
watchfilepath = r"C:\Users\k32ru\Documents\MyProgramfiles\EpgDataCap_Bon_EX"
wathfileName = "EpgTimerSrvNotify.log"

# イベントを受け取る頻度
waitsec = 10

# メンテンションする重要なメッセージ。初期値としては、録画が中途半端に終わった以下2つのメッセージは通知するようにする
MentionMessages = ['ファイル保存で致命的なエラーが発生した可能性があります' , '録画中にキャンセルされた可能性があります']
# slackに転送しないメッセージ
IgnoreMessages = ['予約録画開始準備']
# -------------------------------
