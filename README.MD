## 🧪 Casos de testes processados
- test.case.0 - q1sociodemographics.get_all001 ✅
- test.case.1 - notifications.deletetoken.delete_id001 ⚠️
- test.case.2 - educator-missions.get001 ✅
- test.case.3 - food-recognition.get001 ✅
- test.case.4 - gamificationprofiles.post001 ✅
- test.case.5 - foodqs.patch001 ✅
- test.case.6 - users.fitbit.auth.revoke.post001 ✅

## Casos onde todos os testes estão falhando, independente do endpoint:
- notifications ❌
- bodyfats ❌

## 🗂️ Estrutura do projeto
* 📁 data/cpu ➡️ dados de cpu (%) obtidos do Grafana durante a execução dos testes.
* 📁 data/memory ➡️ dados de memória obtidos do Grafana durante a execução dos testes.
* 📁 data/test-logs ➡️ dados de execução dos testes
    * 📁 requests/ ➡️ dados que consideram como sendo o tempo de execução dos testes apenas o tempo das requisições logadas na api-gateway.
    * 📁 total/ ➡️ dados que consideram como sendo o tempo de execução dos testes o processamento feito pelo SPlat mais o tempo das requisições logadas na api-gateway.
* 📁 results ➡️ resultado do processamento dos dados. 
* 📁 utils ➡️ arquivos de suporte que são utilizados no projeto.

## ⚙️ Dependências do projeto
* Python 3.8.11
* Pandas 1.3.3

## ▶️ Execução
Para executar o projeto basta executar o arquivo ```main.py```.
