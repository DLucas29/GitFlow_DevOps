# Sistema de Estoque com GitFlow e CI/CD

Sistema de controle de estoque baseado em persistência JSON, gerenciado por meio de uma pipeline automatizada de CI/CD com GitHub Actions, aplicando estratégias de GitFlow e versionamento limpo.

## Arquitetura e Estratégia de Branches

O projeto segue uma estrutura padrão de desenvolvimento dividida em duas branches principais:

- main: Branch de producao, contendo apenas versoes estaveis e testadas do sistema.
- develop: Branch de integracao e homologacao, onde todas as modificacoes, testes e execucoes de pipeline sao validados antes do deploy final na producao.

## Funcionalidades da Pipeline

A pipeline unificada executa o processo de ponta a ponta atraves de tres estagios encadeados:

1. Build: Valida a integridade estrutural e sintatica do arquivo estoque.json.
2. Test: Executa testes unitarios automatizados em Python validando a geracao de IDs sequenciais e regras de remocao.
3. Deploy: Aplica a operacao escolhida no formulario, atualiza o arquivo de estoque e realiza o commit automatico na branch sem poluir o historico de versoes.

## Como Utilizar o Sistema

1. Acesse o repositorio no GitHub e navegue ate a aba Actions.
2. Selecione o workflow Pipeline CI/CD - Sistema de Estoque.
3. Clique no botao Run workflow e escolha a branch de trabalho (develop).
4. Preencha os campos do formulario interativo de acordo com a operacao desejada:
   - ADICIONAR: Informe o Nome, Quantidade e Valor R$. O sistema gerara automaticamente um ID sequencial disponivel (reutilizando lacunas de itens apagados).
   - REMOVER: Informe apenas o ID numerico do item a ser apagado.
   - ATUALIZAR: Informe o ID numerico junto com a Nova Quantidade e o Novo Valor R$.
5. Acompanhe os resultados detalhados e a tabela atualizada do estoque diretamente na aba Summary da execucao da Action.