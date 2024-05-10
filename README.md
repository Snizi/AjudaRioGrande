# PROJETO FOI REFATORADO PARA NEXTJS E MIGRADO PARA:
https://github.com/RafaelHuszcza/ajudarg-next


# -Ajuda Rio Grande-
Ajuda Rio Grande é um projeto que visa contribuir com a comunidade da cidade do Rio Grande através do sistema hospedado em: https://www.ajudariogrande.com.br. Mapeando possíveis zonas de risco divulgaldas pela prefeitura e instituíções confiáveis bem como agrupar pontos de coleta e abrigos durante o desastre natural que está acontecendo.

## 🖇️ Colaborando

Para contribuir com o projeto, basta fazer um fork para sua conta e abrir uma pull request, um review será feito, após aprovado, as atualizações serão jogadas para o site através da pipeline.

No momento, o que mais necessitamos é que as áreas de risco sejam atualizadas conforme divulgações dos órgãos responsáveis bem como a adição de novos pontos de coleta ou abrigos divulgados pela comunidade.

Para editar as áreas de risco, basta pegar o conteúdo do arquivo *riskareas.json* e inserir no site https://geojson.io/. Após isso, editar os polígonos para que se adaptem a situação atual da região, e inserir novamente no arquivo.

Para adicionar novos marcadores de coleta, verificar o arquivo *markers.json* que contém os pontos bem como suas coordenadas geográficas para plotagem no mapa. Verifique o "tipo", este determinará o marcador. Tipos: Arrecadação, Abrigo e Ponto de voluntarização

Não esqueça de abrir uma pull request!

