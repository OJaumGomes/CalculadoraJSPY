const readline = require('readline');

class Calculadora {
    constructor() {
        // Criamos uma interface para leitura e escrita no terminal
        this.rl = readline.createInterface({ input: process.stdin, output: process.stdout });
    }

    iniciar() {
        // Pergunta ao usuário qual operação deseja realizar
        this.rl.question("Digite a operação (+, -, *, /): ", (operacao) => {
            // Verifica se a operação digitada é válida
            if (!['+', '-', '*', '/'].includes(operacao)) {
                console.log("Operação inválida!");
                return this.rl.close();
            }

            // Solicita o primeiro número ao usuário
            this.rl.question("Digite o primeiro número: ", (num1) => {
                // Solicita o segundo número ao usuário
                this.rl.question("Digite o segundo número: ", (num2) => {
                    // Converte os valores para números decimais
                    num1 = parseFloat(num1);
                    num2 = parseFloat(num2);

                    // Verifica se as entradas são válidas e exibe o resultado
                    console.log(isNaN(num1) || isNaN(num2) 
                    ? "Erro: Entrada inválida. Use apenas números."
                    : `Resultado: ${this.#calcular(operacao, num1, num2)}`);

                    // Fecha a interface de leitura
                    this.rl.close();
                });
            });
        });
    }

    #calcular(operacao, num1, num2) {
        // Mapeamento das operações matemáticas em um objeto
        const operacoes = {
            '+': (a, b) => a + b, // Soma
            '-': (a, b) => a - b, // Subtração
            '*': (a, b) => a * b, // Multiplicação
            '/': (a, b) => (b !== 0 ? a / b : 'Erro: divisão por zero') // Divisão com verificação de zero
        };
        // Retorna o resultado da operação ou uma mensagem de erro se for inválida
        return operacoes[operacao] ? operacoes[operacao](num1, num2) : 'Operação inválida';
    }
}

// Criamos uma nova instância da Calculadora e iniciamos o programa
new Calculadora().iniciar();