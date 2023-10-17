#include <iostream>

// Definición de la clase Calculadora
class Calculadora {
public:
    // Método para sumar dos números
    double sumar(double num1, double num2) {
        return num1 + num2;
    }

    // Método para restar dos números
    double restar(double num1, double num2) {
        return num1 - num2;
    }

    // Método para multiplicar dos números
    double multiplicar(double num1, double num2) {
        return num1 * num2;
    }

    // Método para dividir dos números
    double dividir(double num1, double num2) {
        if (num2 != 0) {
            return num1 / num2;
        } else {
            // Manejo del caso de división por cero
            std::cout << "Error: División por cero" << std::endl;
            return 0.0;
        }
    }
};

int main() {
    // Creación de una instancia de la clase Calculadora
    Calculadora calculadora;
    double num1, num2;
    char operador;
    char opcion;

    do {
        // Entrada de usuario: primer número
        std::cout << "Ingrese el primer numero: ";
        std::cin >> num1;
        // Entrada de usuario: segundo número
        std::cout << "Ingrese el segundo numero: ";
        std::cin >> num2;
        // Entrada de usuario: operador (+, -, *, /) o 'q' para salir
        std::cout << "Ingrese el operador (+, -, *, /) o 'q' para salir: ";
        std::cin >> operador;

        // Salir del bucle si el usuario elige salir
        if (operador == 'q' || operador == 'Q') {
            break;
        }

        double resultado;

        // Utilizando un switch para determinar la operación a realizar
        switch (operador) {
            case '+':
                resultado = calculadora.sumar(num1, num2);
                break;
            case '-':
                resultado = calculadora.restar(num1, num2);
                break;
            case '*':
                resultado = calculadora.multiplicar(num1, num2);
                break;
            case '/':
                resultado = calculadora.dividir(num1, num2);
                break;
            default:
                // Manejo del caso de un operador no válido
                std::cout << "Operador no valido" << std::endl;
                continue; // Continuar con la siguiente iteración del bucle
        }

        // Mostrar el resultado
        std::cout << "Resultado: " << resultado << std::endl;

        // Preguntar si el usuario desea realizar otra operación
        std::cout << "Desea realizar otra operacion? (S/N): ";
        std::cin >> opcion;
    } while (opcion != 'n' && opcion != 'N');

    // Mensaje de despedida
    std::cout << "¡Gracias por usar la calculadora!" << std::endl;

    return 0; // Salida exitosa
}