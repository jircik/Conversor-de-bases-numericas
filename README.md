# Conversor de Bases Numéricas com Integração SQL

Este projeto desenvolvido em Python realiza a conversão de números entre diferentes bases (binário, decimal, hexadecimal, etc.) e utiliza um banco de dados SQL para armazenar resultados já calculados.  
Dessa forma, quando uma conversão já foi feita anteriormente, o programa busca diretamente no banco em vez de recalcular, otimizando a execução, além de disponibilizar um histórico de conversões ao usuário.

---

## 🧠 Funcionalidades

- Conversão entre diferentes bases numéricas.
- Armazenamento das conversões realizadas em um banco SQL.
- Reaproveitamento de resultados já existentes (não recalcula conversões repetidas).
- Disponibiliza ao usuário um histórico de todas as conversões já realizadas.

---

## 🛠 Tecnologias utilizadas

- Python 3
- SQLite

---

## 🚀 Como executar o projeto

Siga os passos abaixo para rodar o programa em sua máquina local:

1. **Clone o repositório** (ou baixe os arquivos manualmente):
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA>

