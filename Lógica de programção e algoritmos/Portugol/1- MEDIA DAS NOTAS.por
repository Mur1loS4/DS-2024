programa{
	 funcao inicio(){
	real nota_1 
	real nota_2
	real nota_3
	real resultado
	real media
	
	escreva("digite a primeira nota: ")
	leia(nota_1)	

	escreva("digite a segunda nota: ")
	leia(nota_2)	

	escreva("digite a tercira nota: ")
	leia(nota_3)	

     limpa()
     
	resultado = nota_1 + nota_2 + nota_3
     escreva("\na soma das notas é: ", resultado)	
     
	media = resultado/3
	escreva("\na media das 3 notas é: ", resultado/3)
	
	se(media >= 7){
	escreva ("\nALUNO APROVADO")
	} senao se(media >= 3 ){
	escreva ("\nALUNO DE RECUPERAÇÃO")} 
	senao se (media < 7 ){
	escreva ("\nALUNO REPROVADO")}
	 }
}

		
	
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 68; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */