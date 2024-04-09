programa{
	 funcao inicio() {
	real altura
	real peso
	real IMC
	
		escreva("digite sua altura: ")
		leia(altura)

		escreva("digite seu peso: ")
		leia(peso)

		IMC = peso / (altura * altura)
		

		escreva("\no seu IMC é: ", IMC)
		escreva("\naltura informada: ", altura)
		escreva("\npeso informado: ", peso)

		se(IMC > 30){
			escreva ("\nCUIDADO COM A SAUDE")

		}senao{
			escreva ("\nTudo ok")
		}
		
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 397; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */