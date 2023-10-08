# Property Finding Helpers

* * * * * * * * *
今回は不動産ポータルサイトを開発しました。
## Installation
```
git clone git@github.com:zgalaz/property-finding-helpers.git
cd property-find-helpers
python3 -m virtualenv .venv
source .venv/bin/activate
pip install .
```

## Structure
```
+---helpers
|   +---parsers
|   |   +---portals
|   |   |       base.py
|   |   |       nehnutelnosti.py
|   |   |       
|   |   \---websites
|   |           parser.py
|   |           
|   +---senders
|   |       data_formatter.py
|   |       email_builder.py
|   |       email_sender.py
|   |       
|   +---utils
|   |       common.py
|   |       logger.py
|   |       
|   \---watchdog
|       |   dog.py
|       |   __init__.py
|       |   
|       +---database
|       \---settings
|               watchdog.json
|               
+---settings
|       email.json
```

## 

1. settings/email.json ファイルの email_address、email_password、server、および port フィールドを更新します。
2. helpers/watchdog/settings/watchdog.json ファイルの url フィールドを更新します。
3. ウォッチドッグを実行します: python run.py --email <receiver@email.com>
4. または、以下の内容を含む bash スクリプトを作成し、システムのタスクスケジューラーを定期的に実行します。
このパッケージは、現時点ではウォッチドッグ機能のみをサポートしています（必要に応じて、ヘルパーの機能を更新/拡張することができます）。ウォッチドッグを実行するには、上記の手順に従ってください。


# ライセンス
このプロジェクトはMITライセンスの条件の下でライセンスされています。詳細については、LICENSEファイルを参照してください。
