;�ѽ���������controllIDΪEdit1�Ŀؼ���
ControlFocus("��", "","Edit1")
;�ȴ�10��ClassΪ#32770�Ĵ���
WinWait("[CLASS:#32770]","",10)
;���øÿؼ����ı�ΪC:\Users\admin\Pictures\Camera Roll\invoice.png
ControlSetText("��", "", "Edit1", "D:\AImanager\base\file\invoice.png")
Sleep(2000)
;���controllIDΪButton1�Ŀؼ�
ControlClick("��", "","Button1");
