@echo off

:init
 setlocal DisableDelayedExpansion
 set cmdInvoke=1
 set winSysFolder=System32
 set "batchPath=%~0"
 for %%k in (%0) do set batchName=%%~nk
 set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
 setlocal EnableDelayedExpansion

:checkPrivileges
  NET FILE 1>NUL 2>NUL
  if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
  if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)

  ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
  ECHO args = "ELEV " >> "%vbsGetPrivileges%"
  ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
  ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
  ECHO Next >> "%vbsGetPrivileges%"

  if '%cmdInvoke%'=='1' goto InvokeCmd 

  ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
  goto ExecElevation

:InvokeCmd
  ECHO args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
  ECHO UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"

:ExecElevation
 "%SystemRoot%\%winSysFolder%\WScript.exe" "%vbsGetPrivileges%" %*
 exit /B

:gotPrivileges
 setlocal & cd /d %~dp0
 if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)

if exist cmd.exe (
  echo [32mCHECK[0m cmd.exe exists
) else (
  echo [91mCHECK[0m cmd.exe does not exist
  echo:

  pause
  exit
)

if exist register.reg (
  echo [32mCHECK[0m register.reg exists
) else (
  echo [91mCHECK[0m register.reg does not exist
  echo:

  pause
  exit
)

echo:

echo [33mAdding required values to registry...[0m
regedit.exe /S register.reg >nul
echo [32mAdded required values to the registry.[0m

echo:

echo [33mCopying "cmd.exe" to "%HOMEDRIVE%\Protocols\cmd.exe"...[0m
xcopy "cmd.exe" "%HOMEDRIVE%\Protocols\" /E /C /H /R /K /O /Y >nul
echo [32mCopied "cmd.exe" to "%HOMEDRIVE%\Protocols\cmd.exe".[0m

echo:
echo [95mThe "cmd://" protocol has been registered.[0m
echo:

pause
