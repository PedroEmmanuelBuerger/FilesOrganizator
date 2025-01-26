# FilesOrganizator

FilesOrganizator é um projeto desenvolvido para organizar arquivos de forma automatizada em um ambiente Linux(possui versão windows tambem), ajudando a manter pastas e diretórios bem estruturados.

## Funcionalidades

O projeto inclui as seguintes funcionalidades:

- Organiza automaticamente arquivos em diretórios com base em sua extensão.
- Cria pastas específicas para cada tipo de arquivo (como documentos, imagens, vídeos, etc.).
- Lida com nomes de arquivos duplicados, garantindo que nenhum arquivo seja sobrescrito.
- Permite personalizar as categorias de organização e os tipos de arquivos associados.
- Registro de logs para acompanhar quais arquivos foram movidos e para onde.
- Estrutura flexível e adaptável para novos tipos de arquivos e configurações.

## Tecnologias

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python**: Linguagem principal para desenvolvimento do projeto.
- **os**: Biblioteca para interagir com o sistema de arquivos.
- **shutil**: Utilizada para mover e copiar arquivos.
- **logging**: Ferramenta para registrar logs detalhados das operações realizadas.
- **Watchdog**: Biblioteca para monitorar movimentos na pasta downloads, garantido que o código só rode caso algo mude la.

## Principais Aprendizados

Os principais aprendizados incluem:

- Utilizar bibliotecas nativas do Python para manipulação de arquivos e diretórios.
- Criar um script que seja eficiente e fácil de usar, mesmo para usuários com pouca experiência técnica.
- Implementar tratamento de erros para lidar com cenários imprevisíveis, como permissões de arquivo.
- Registrar logs para facilitar o monitoramento e depuração do processo de organização.
- Aplicar boas práticas de programação em Python, incluindo modularização e reutilização de código.

## Conclusão

FilesOrganizator é uma ferramenta útil para quem busca automatizar a organização de arquivos em sistemas Linux. O projeto combina conceitos importantes de automação, manipulação de arquivos e registro de logs, oferecendo uma solução eficiente para manter o sistema de arquivos limpo e organizado.
