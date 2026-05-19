Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c cd /d ""E:\Treino_app\backend"" && ""C:\Program Files\nodejs\node.exe"" server.js >> ""E:\Treino_app\backend\server.log"" 2>&1", 0, False
