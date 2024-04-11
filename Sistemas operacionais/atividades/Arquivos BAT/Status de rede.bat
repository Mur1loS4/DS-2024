@echo off
chcp 65001 >nul 

:loopRede
ipconfig

set /p inf= "Testar conctividade, Digite a informação: "

ping %inf%

set /p opcao="deseja continuar? (S/N): "

if "%opcao%"="S" (
	goto loopRede
)