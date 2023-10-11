# Cheapest Flights Within K Stops

Existem n cidades conectadas por um certo número de voos. Você recebe uma matriz de voos onde flights[i] = [fromi, toi, pricei] indica que há um voo da cidade fromi para a cidade toi com custo pricei.

Você também recebe três inteiros: src (origem), dst (destino) e k (máximo de paradas). O objetivo é retornar o preço mais barato para viajar de src para dst com no máximo k paradas. Se não houver tal rota, retorne -1.

>    Exemplo 1:
>
>    Entrada: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
>
>    Saída: 700