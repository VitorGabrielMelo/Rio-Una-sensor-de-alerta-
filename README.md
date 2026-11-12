# Rio-Una-sensor-de-alerta-

Sistema de monitoramento do Rio Una, em Palmares (PE), criado para alertar os moradores antes das cheias.

## Problema

Palmares fica na Zona da Mata Sul de Pernambuco e já sofreu muito com as cheias do Rio Una. Em 2010, as chuvas fortes provocaram uma das maiores enchentes da região, com mortes, famílias desabrigadas e grandes prejuízos. Muita gente foi pega de surpresa, sem aviso com tempo suficiente para sair de casa.

A ideia do projeto é justamente essa: avisar a população assim que o nível do rio começar a subir de forma perigosa.

## Objetivo

Acompanhar o nível do Rio Una e emitir alertas em diferentes níveis (atenção, alerta e emergência), para que quem mora em áreas de risco consiga se preparar e sair a tempo.

## Como funciona

1. Um sensor simulado mede o nível da água em intervalos regulares. A versão atual é virtual, usada para representar o funcionamento do sistema.
2. Os dados são enviados para um sistema central.
3. Quando o nível passa de limites pré-definidos, o sistema dispara um alerta. docs/creditos
4. Os moradores são avisados por SMS e WhatsApp (nesta versão, o alerta aparece no terminal como simulação).
main

**Importante:** este sistema complementa os alertas oficiais, mas não substitui a Defesa Civil. Em caso de emergência, ligue 199 (Defesa Civil) ou 193 (Bombeiros).

## Funcionalidades

- [x] Leitura do nível da água do rio (sensor simulado)
- [x] Classificação do risco em níveis (normal, atenção, alerta, emergência)
- [ ] Envio de alertas à população
- [ ] Histórico de medições
- [ ] Painel para visualizar o nível atual do rio
- [ ] Mapa com áreas de risco de Palmares

Os itens não marcados são planejados para as próximas versões.

## Tecnologias

- Python 3.10+
- Sensor simulado por script Python (sem hardware físico nesta versão)
- Armazenamento do histórico: planejado para versões futuras

## Instalação

git clone https://github.com/VitorGabrielMelo/Rio-Una-sensor-de-alerta-.git
cd Rio-Una-sensor-de-alerta-

### Pré-requisitos

 docs/creditos
- Python 3.10 ou superior
- Git instalado (`git --version`)
python src/sensor.py
 main

### Passo a passo

```bash
git clone https://github.com/VitorGabrielMelo/Rio-Una-sensor-de-alerta-.git
cd Rio-Una-sensor-de-alerta-
```

### Executando

```bash
python src/sensor.py
```

## Estrutura do projeto

```
├── src/          # Código-fonte (sensor.py, classificacao.py)
├── docs/         # Documentação adicional
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Como contribuir

O projeto usa o fluxo GitHub Flow:

1. A branch `main` deve estar sempre estável e nunca recebe commit direto.
2. Crie uma branch para cada tarefa a partir da `main`.
3. Faça commits pequenos seguindo o padrão Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`).
4. Abra um Pull Request para a `main`.
5. Espere a aprovação de pelo menos um integrante antes de fazer o merge.

### Política de ramificação

- `main`: versão estável
- `feat/*`: novas funcionalidades
- `fix/*`: correções de erros
- `hotfix/*`: correções urgentes na `main`
- `release/*`: preparação de versões (ex.: `release/1.0.0`)
- `docs/*`: mudanças apenas de documentação

## Equipe

| Integrante | Papel |
|---|---|
| Vitor Gabriel | Líder / Mantenedor |
| Guilherme | Documentação e README |
| Renan | Revisão de código |
| João Pedro | Releases e changelog |
| Micaías | Desenvolvimento do sensor |
| Breno | Desenvolvimento do sistema e testes |

## Versões

O projeto segue o [Versionamento Semântico](https://semver.org/lang/pt-BR/). As mudanças de cada versão estão em [CHANGELOG.md](CHANGELOG.md).

## Inspirações e créditos

- Projeto original: https://github.com/sagunpandey/ews-station-client-simulator
- Nosso fork: https://github.com/VitorGabrielMelo/ews-station-client-simulator
- O que aproveitamos: a ideia de simular vários sensores gerando leituras aleatórias do nível do rio, que inspirou o nosso `src/sensor.py`.

## Referências

- SILVA, L. L.; LISTO, F. L. R. Inundações severas no município de Palmares-PE: uma análise comparativa preliminar dos eventos de 2010 e 2017. *GeoUECE*, v. 8, n. 14, 2019. Disponível em: https://revistas.uece.br/index.php/GeoUECE/article/view/1484

- Desastres naturais e percepção de risco da população: um estudo de caso da inundação em Palmares (PE) em 2010. *Revista de Geografia*, Universidade Federal de Pernambuco, 2016. Disponível em: https://periodicos.ufpe.br/revistas/index.php/revistageografia/article/view/229199

- Caso Palmares/PE. Disponível em: https://dialnet.unirioja.es/descarga/articulo/9631896.pdf

- MOREIRA, Manoel Simeão; SILVA, Maria Aparecida da. A enchente de 2010 em União dos Palmares-AL: impactos socioambientais em áreas ribeirinhas do Rio Mundaú. *Revista Eletrônica do Curso de Geografia*, Universidade Federal do Ceará. Disponível em: https://periodicos.ufsm.br/reget/article/download/9086/pdf/48008

## Licença

Este projeto está sob a licença [MIT](LICENSE).
