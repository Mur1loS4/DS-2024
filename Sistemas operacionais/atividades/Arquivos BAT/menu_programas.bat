@echo off
chcp 65001 >nul 

:inicio
cls

echo escolha uma opção
echo 1 - abrir calculadora 
echo 2 - abrir bloco de notas
echo 3 - abrir paint

set /p opcao="digite sua opção:"

if "%opcao%" == "1" (
	start calc.exe
)
	
if "%opcao%" == "2" (
	start notepad.exe
)
	
if "%opcao%" == "3" (
	start mspaint.exe
)

goto inicio

pause