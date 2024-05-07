# Ajuda Rio Grande
Ajuda Rio Grande é um projeto que visa contribuir com a comunidade da cidade do Rio Grande através do sistema hospedado em: https://www.ajudariogrande.com.br. Mapeando possíveis zonas de risco divulgaldas pela prefeitura e instituíções confiáveis bem como agrupar pontos de coleta e abrigos durante o desastre natural que está acontecendo.

[Link do Projeto](https://ajudariogrande.com.br)

## Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Você instalou a versão mais recente do Python
* Você tem uma máquina Windows. (O projeto ainda não foi testado em outros sistemas operacionais)

## Instalando Projeto

Para instalar o Projeto, siga estas etapas:

1. Clone o repositório
```bash
git clone https://github.com/Snizi/AjudaRioGrande
```

2. Navegue até o diretório do projeto
```bash
cd project
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

## Usando Projeto

Para usar Projeto, siga estas etapas:

```bash
python main.py
```

Abra o navegador e visite `http://localhost:5000`

## Contribuindo para Projeto

Para contribuir para Projeto, siga estas etapas:

1. Fork este repositório.
2. Crie uma branch: `git checkout -b <branch_name>`.
3. Faça suas alterações e confirme-as: `git commit -m '<commit_message>'`
4. Envie para a branch original: `git push origin <branch_name>`
5. Crie a pull request.

Alternativamente, consulte a documentação do GitHub em [https://help.github.com/articles/creating-a-pull-request/](https://help.github.com/articles/creating-a-pull-request/).

## 🖇️ Colaborando

Para contribuir com o projeto, basta fazer um fork para sua conta e abrir uma pull request, um review será feito, após aprovado, as atualizações serão jogadas para o site através da pipeline.

No momento, o que mais necessitamos é que as áreas de risco sejam atualizadas conforme divulgações dos órgãos responsáveis bem como a adição de novos pontos de coleta ou abrigos divulgados pela comunidade.

Para editar as áreas de risco, basta pegar o conteúdo do arquivo *riskareas.json* e inserir no site https://geojson.io/. Após isso, editar os polígonos para que se adaptem a situação atual da região, e inserir novamente no arquivo.

Para adicionar novos marcadores de coleta, verificar o arquivo *markers.json* que contém os pontos bem como suas coordenadas geográficas para plotagem no mapa.

Não esqueça de abrir uma pull request!

