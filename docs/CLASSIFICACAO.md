# Classificação de risco

O arquivo `src/classificacao.py` transforma o nível do rio (em metros) em uma situação de risco.

| Nível do rio | Situação |
|---|---|
| Abaixo de 3,0 m | NORMAL |
| De 3,0 m a 4,99 m | ATENÇÃO |
| De 5,0 m a 6,99 m | ALERTA |
| 7,0 m ou mais | EMERGÊNCIA |

Os limites são valores de exemplo e devem ser ajustados com dados oficiais da Defesa Civil.
