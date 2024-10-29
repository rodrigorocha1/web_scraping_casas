df_temp = base_apartamento.query(f'bairro == "{bairro}"')
print('=' * 40)
print(f'Bairro: {bairro}')
print(f'Média preço: {round(df_temp["precos"].mean(), 2)}')
print(f'Moda preço: {round(df_temp["precos"].mode(), 2)}')
print(f'Mediana preço: {round(df_temp["precos"].median(), 2)}')
print(f'Desvio Padrão preço: {round(df_temp["precos"].std(), 2)}')
print(f'Preço Máximo: {round(df_temp["precos"].max(), 2)}')
print(f'Preço Minimo: {round(df_temp["precos"].min(), 2)}')
for banheiro in df_temp['banheiros'].unique():

    df_temp = df_temp.query(f'banheiros == {banheiro}')
    if not df_temp.empty:
        print(f'====Análise banheiro {banheiro}=========')
        print(f'Média preço: {round(df_temp["precos"].mean(), 2)}')
        print(f'Moda preço: {round(df_temp["precos"].mode(), 2)}')
        print(f'Mediana preço: {round(df_temp["precos"].median(), 2)}')
        print(f'Desvio Padrão preço: {round(df_temp["precos"].std(), 2)}')
        print(f'Preço Máximo: {round(df_temp["precos"].max(), 2)}')
        print(f'Preço Minimo: {round(df_temp["precos"].min(), 2)}')

    print('=' * 40)
