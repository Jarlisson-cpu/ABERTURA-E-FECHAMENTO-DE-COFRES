# 📉 Métodos Numéricos — Raízes de Funções

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

Script em Python que encontra raízes da função **f(x) = 4 + x·cos(x)** usando três métodos numéricos clássicos e compara o número de iterações de cada um.

## 🔢 Métodos implementados

| Método | Ideia |
|---|---|
| **Bissecção** | Divide o intervalo ao meio até encontrar a mudança de sinal |
| **Newton-Raphson** | Usa a derivada `f'(x) = cos(x) − x·sen(x)` para convergir mais rápido |
| **Secantes** | Aproxima a derivada usando dois pontos anteriores |

Parâmetros: tolerância `1e-5` e no máximo `1000` iterações.

## 🚀 Como executar

```bash
cd "me algebra"
python desenvolvimento.py
```

O programa imprime as raízes encontradas por cada método e o número de iterações.

## 🧠 Conceitos praticados

Cálculo numérico · convergência · tratamento de erros (`ValueError`, `ZeroDivisionError`)

---

👤 Feito por **[Jarlisson Brito](https://github.com/Jarlisson-cpu)** · [LinkedIn](https://www.linkedin.com/in/jarlisson-brito-602909368/)
