param([string]$Mode='layout',[string]$Tag='r2')
$ErrorActionPreference='Stop'
$rqIntroRoot='E:\PROGETTI\ragequit'
# A server C++ compile in E:\rq-server does not consume the renderer or change
# this project's packages. Do not overlap another editor, cooker or game client.
$rqIntroBusy=@(Get-CimInstance Win32_Process | Where-Object { $_.Name -match '^(UnrealEditor(?:-Cmd)?|Ragequit.*|UnrealPak)\.exe$' -or ($_.Name -eq 'dotnet.exe' -and $_.CommandLine -match 'BuildCookRun|E:\\PROGETTI\\ragequit\\') })
if($rqIntroBusy.Count){ throw ('Renderer occupied: '+(($rqIntroBusy|ForEach-Object {$_.Name+':'+$_.ProcessId}) -join ', ')) }
$rqIntroRun=Join-Path $rqIntroRoot ('.verify\ragequit-unreal\intro-istante-'+$Tag+'-'+(Get-Date -Format yyyyMMdd-HHmmss))
New-Item -ItemType Directory -Path $rqIntroRun | Out-Null
$env:RQ_OUT=$rqIntroRun
$env:RQ_INTRO_MODE=$Mode
$rqIntroExe='C:\Program Files\Epic Games\UE_5.8\Engine\Binaries\Win64\UnrealEditor.exe'
$rqIntroArgs='"E:\PROGETTI\ragequit\unreal\RAGEQUIT.uproject" -ExecutePythonScript="E:\PROGETTI\ragequit\tools\unreal\render-intro-istante.py" -unattended -RenderOffscreen -NoSplash -NoLiveCoding -nosourcecontrol -culture=en -asynctexturecompilationmaxconcurrency=1 -ini:Engine:[DevOptions.Shaders]:ShaderCompilerCoreCountThreshold=999 -ini:Engine:[DevOptions.Shaders]:NumUnusedShaderCompilingThreads=30 -ini:Engine:[DevOptions.Shaders]:NumUnusedShaderCompilingThreadsDuringGame=30 -ini:EditorPerProjectUserSettings:[/Script/UnrealEd.EditorLoadingSavingSettings]:bAutoSaveEnable=False -ExecCmds="au.MuteAudio 1,t.MaxFPS 45" -abslog="'+$rqIntroRun+'\editor.log"'
$rqIntroProc=Start-Process -FilePath $rqIntroExe -ArgumentList $rqIntroArgs -WindowStyle Hidden -PassThru
@{pid=$rqIntroProc.Id;run=$rqIntroRun;mode=$Mode;assets_saved=$false;source_script='tools/unreal/render-intro-istante.py';concurrency='Only unrelated E:/rq-server C++ compile may overlap; no editor, cooker or game client'} | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $rqIntroRun 'runner.json')
Write-Output $rqIntroRun
if(-not $rqIntroProc.WaitForExit(1200000)){ Stop-Process -Id $rqIntroProc.Id; throw 'Owned intro renderer timed out' }
$rqIntroProc.WaitForExit()
if($rqIntroProc.ExitCode -ne 0){throw ('Editor exit '+$rqIntroProc.ExitCode)}
$rqIntroReport=Get-Content -LiteralPath (Join-Path $rqIntroRun 'report.json') -Raw | ConvertFrom-Json
if(-not $rqIntroReport.success){throw ($rqIntroReport.errors -join "`n")}
Write-Output 'Native render complete'
