#COTAÇÃO DOLAR  
#IMPORT DATA HTML START
import requests 
from bs4 import BeautifulSoup

url = "https://www.remessaonline.com.br/cotacao/cotacao-dolar"

aquisition_url = requests.get(url)

soup = BeautifulSoup(aquisition_url.content, 'html.parser')

dolar_cotacao_element = soup.find('div', class_= 'style__Text-sc-1a6mtr6-2 ljisZu')
#IMPORT DATA HTML END
#CONVERT DATA IN FLOAT START
if dolar_cotacao_element:
    str_cotacao = dolar_cotacao_element.text.strip("[]")
    str_cotacao = str_cotacao.replace(',', '.').replace('R$', '').strip("Reais")
try:
    float_cotacao = float (str_cotacao)
   
except ValueError:
    print("Erro ao converter a cotação para numero!")
#CONVERT DATA IN FLOAT END
#DAY DATA START  
data_element = soup.find('div', class_='style__Text-sc-1a6mtr6-2 style__Date-sc-1a6mtr6-3 cGCvvZ')

try:
    data_element
    data_cotacao = data_element.text.strip()
  
except ValueError:
    print("Erro ao exibir a data da cotação atual!")
#DAY DATA END 

#COTAÇÃO EURO
#IMPORT DATA HTML START
url_eur = "https://www.remessaonline.com.br/cotacao/cotacao-euro"

aquisition_url_eur = requests.get(url_eur)

soup_eur = BeautifulSoup(aquisition_url_eur.content, 'html.parser')

eur_cotacao_element = soup_eur.find('div', class_= 'style__Text-sc-1a6mtr6-2 ljisZu')
#IMPORT DATA HTML END
#CONVERT DATA IN FLOAT START
if eur_cotacao_element:
    eur_str_cotacao = eur_cotacao_element.text.strip()
    eur_str_cotacao = eur_str_cotacao.replace(',', '.').replace('R$', '').strip("Reais")
try:
    eur_float_cotacao = float (eur_str_cotacao)

except ValueError:
    print("Erro ao converter a cotação para numero!")
#CONVERT DATA IN FLOAT END
#DAY DATA START
eur_data_element = soup_eur.find('div', class_='style__Text-sc-1a6mtr6-2 style__Date-sc-1a6mtr6-3 cGCvvZ')

try:
    eur_data_element
    eur_data_cotacao = eur_data_element.text.strip()
   
except ValueError:
    print("Erro ao exibir a data da cotação atual!")
#DAY DATA END 


print("SEJA BEM VINDO!\n")

#PROG START
print ("\nQual função você deseja?")

print("1 - cotação")
print("2 - conversão \n")

tds = input ("Selecione uma função para ser realizada: (1, 2)\n")
#COTAÇÃO
if tds == ("1"):
     tds_cotacao = print ("Você deseja realizar a cotação de qual moeda?\n")

     print(" 1 - Dólar")
     print(" 2 - Euro")

     funcao = input("\nSelecione uma das moedas para realizar a cotação: (1, 2)\n")

     if funcao == ("1"):
         resp_cotacao = print(f"\n A cotação atual está em: R$ {float_cotacao}\n")
         print("COTAÇÃO REFERENTE A", data_cotacao)

     if funcao == ("2"):
         resp_cotacao_2 = print(f"\n A cotação atual está em: R$ {eur_float_cotacao}\n")
         print("COTAÇÃO REFERENTE A", eur_data_cotacao, "\n")
#CONVERSÃO
if tds == ("2"):
     tds_conversao = print ("\nqual moeda você deseja converter para o real?\n")

     print("1 - Dólar")
     print("2 - Euro")

     funcao_conv = input("\nSelecione uma moeda para realizar a conversão: (1, 2)\n")

     if funcao_conv == ("1"):
         valor_user_usa = input("\nInforme quantos Doláres você deseja converter para o real:\n")
         valor_user_usa = valor_user_usa.replace(',','.').strip()
         valor_user_usa = float (valor_user_usa)

         conv_result_usa = float_cotacao*valor_user_usa
         print(f"\nO valor em REAL é igual a: R$ {conv_result_usa}")
    
     if funcao_conv == ("2"):
         valor_user_eur = input("\nInforme quantos Euros você deseja converter para o real:\n")
         valor_user_eur = valor_user_eur.replace(',','.').strip()
         valor_user_eur = float (valor_user_eur)

         conv_result_eur = valor_user_eur * eur_float_cotacao
         print(f"O valor em REAL é igual a: R$ {conv_result_eur}")




    



      
















