Set WshShell = CreateObject("WScript.Shell")

' Get the full path of the VBScript file
scriptPath = WScript.ScriptFullName

' Get the directory of the VBScript file
scriptDir = Left(scriptPath, InStrRev(scriptPath, "\"))

' Construct the path to the batch file
batchFilePath = scriptDir & "rbhus_clone.bat"

' Run the batch file
WshShell.Run batchFilePath, 0, False
