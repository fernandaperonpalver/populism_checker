import pandas as pd
from googletrans import Translator

# Carregar o arquivo Excel 
df = pd.read_excel('dicionario.xlsx')

# Traduzir palavras
translator = Translator()

def traduzir(texto):
    try:
        if pd.isnull(texto):  # Ignorar valores nulos
            return None
            print('going')
        return translator.translate(texto, src='de', dest='pt').text

    except Exception as e:
        print('exception')
        return f"Erro: {str(e)}"  # Retornar erro como texto

df['Palavra (Português)'] = df['Word'].apply(traduzir)

# Salvar o arquivo com as traduções
output_path = 'dicionario_portuguese.xlsx'
df.to_excel(output_path, index=False)
print("Arquivo traduzido salvo em:", output_path)
