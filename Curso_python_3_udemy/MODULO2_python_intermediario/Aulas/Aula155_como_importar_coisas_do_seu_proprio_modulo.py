# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path


#forma 1
import Aula155_esse_arquivo_e_para_ser_importado

print(Aula155_esse_arquivo_e_para_ser_importado.variavel)


#forma 2   --  se tiver mais de uma coisa pra trazer da pra adicionar no import
from Aula155_esse_arquivo_e_para_ser_importado import variavel, variavel_teste_2

print(variavel)
print(variavel_teste_2)