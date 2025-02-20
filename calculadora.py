import tkinter as tk  # Importa a biblioteca tkinter para criar a interface gráfica

# Função para somar os números inseridos
def somar():
    try:
        # Tenta somar os valores inseridos nas caixas de texto
        resultado = float(entrada_1.get()) + float(entrada_2.get())
        # Exibe o resultado na tela
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        # Caso algum valor não seja um número, mostra uma mensagem de erro
        label_resultado.config(text="Erro: Entrada inválida")

# Função para subtrair os números inseridos
def subtrair():
    try:
        # Tenta subtrair os valores inseridos nas caixas de texto
        resultado = float(entrada_1.get()) - float(entrada_2.get())
        # Exibe o resultado na tela
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        # Caso algum valor não seja um número, mostra uma mensagem de erro
        label_resultado.config(text="Erro: Entrada inválida")

# Função para multiplicar os números inseridos
def multiplicar():
    try:
        # Tenta multiplicar os valores inseridos nas caixas de texto
        resultado = float(entrada_1.get()) * float(entrada_2.get())
        # Exibe o resultado na tela
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        # Caso algum valor não seja um número, mostra uma mensagem de erro
        label_resultado.config(text="Erro: Entrada inválida")

# Função para dividir os números inseridos
def dividir():
    try:
        # Tenta dividir os valores inseridos nas caixas de texto
        num1 = float(entrada_1.get())
        num2 = float(entrada_2.get())
        if num2 != 0:  # Verifica se o divisor não é zero
            resultado = num1 / num2
            label_resultado.config(text="Resultado: " + str(resultado))
        else:
            # Exibe mensagem de erro se o divisor for zero
            label_resultado.config(text="Erro: Divisão por zero")
    except ValueError:
        # Caso algum valor não seja um número, mostra uma mensagem de erro
        label_resultado.config(text="Erro: Entrada inválida")

# Cria a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")  # Título da janela
janela.geometry("300x300")  # Define o tamanho da janela
janela.config(bg="#f0f0f0")  # Define a cor de fundo da janela

# Rótulo e caixa de texto para o primeiro número
label_1 = tk.Label(janela, text="Primeiro número:", bg="#f0f0f0")
label_1.grid(row=0, column=0, padx=10, pady=5)
entrada_1 = tk.Entry(janela)
entrada_1.grid(row=0, column=1, padx=10, pady=5)

# Rótulo e caixa de texto para o segundo número
label_2 = tk.Label(janela, text="Segundo número:", bg="#f0f0f0")
label_2.grid(row=1, column=0, padx=10, pady=5)
entrada_2 = tk.Entry(janela)
entrada_2.grid(row=1, column=1, padx=10, pady=5)

# Botões para as operações matemáticas
btn_soma = tk.Button(janela, text="+", width=10, command=somar)
btn_soma.grid(row=2, column=0, padx=10, pady=5)
btn_sub = tk.Button(janela, text="-", width=10, command=subtrair)
btn_sub.grid(row=2, column=1, padx=10, pady=5)
btn_mult = tk.Button(janela, text="*", width=10, command=multiplicar)
btn_mult.grid(row=3, column=0, padx=10, pady=5)
btn_div = tk.Button(janela, text="/", width=10, command=dividir)
btn_div.grid(row=3, column=1, padx=10, pady=5)

# Rótulo para exibir o resultado ou mensagens de erro
label_resultado = tk.Label(janela, text="Resultado: ", bg="#f0f0f0")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Inicia o loop da interface gráfica
janela.mainloop()
