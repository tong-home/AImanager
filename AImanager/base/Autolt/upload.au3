;把焦点设置在controllID为Edit1的控件中
ControlFocus("打开", "","Edit1")
;等待10秒Class为#32770的窗体
WinWait("[CLASS:#32770]","",10)
;设置该控件的文本为C:\Users\admin\Pictures\Camera Roll\invoice.png
ControlSetText("打开", "", "Edit1", "D:\AImanager\base\file\invoice.png")
Sleep(2000)
;点击controllID为Button1的控件
ControlClick("打开", "","Button1");
