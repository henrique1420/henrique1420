# Personalização e publicação

Este projeto é um README nativo de perfil do GitHub.
Não necessita de servidor, npm, React, banco de dados ou GitHub Pages.

## Identidade e conteúdo

- Nome: Henrique Oliveira.
- Posicionamento: Web Developer & Founder of HenrStudio.
- Idioma público: inglês.
- Localização pública: Portugal.
- Os cartões são ilustrações conceituais, não screenshots.
- Nenhum repositório privado é referenciado ou alterado.
- Nenhuma experiência, certificação, cliente ou resultado foi inventado.
- Os ícones tipográficos são desenhos locais próprios, não logotipos oficiais.

## Links configuráveis

Edite `profile.config.json`.

Campos vazios permanecem invisíveis no README.

- `website`: website público confirmado do HenrStudio.
- `email`: endereço profissional que pode ser publicado.
- `linkedin`: URL pública do perfil.
- `projects`: URLs públicas autorizadas para cada projeto.
- `snake_enabled`: mantenha `false` até a primeira execução bem-sucedida.

Depois execute, a partir da raiz deste repositório:

```bash
python scripts/customize.py
```

O script não executa Git nem faz pedidos de rede.
Apenas atualiza os blocos delimitados do README.

Use somente URLs HTTPS públicas. Nunca insira tokens, URLs privadas,
dados de infraestrutura, telefone ou WhatsApp neste arquivo.

## Publicar o perfil

1. Revise todos os arquivos.
2. Crie manualmente um NOVO repositório público chamado
   `henrique1420`, pertencente à conta `henrique1420`.
3. Não altere a visibilidade dos repositórios dos produtos.
4. Envie o conteúdo desta pasta para a raiz do novo repositório.
5. Garanta que README.md está na branch padrão.

Apenas o repositório do perfil precisa ser público.
Não publique a pasta como um site.

Se usar Git localmente, pode iniciar somente esta pasta com:

```bash
git init -b main
git add .
git commit -m "feat: add HenrStudio GitHub profile"
```

Adicionar o remoto e executar git push são etapas manuais posteriores.
Nenhum script deste pacote cria repositórios remotos ou executa esses passos.

## Ativar o Snake

1. Publique `.github/workflows/snake.yml` na branch padrão.
2. Abra Settings > Actions > General.
3. Garanta que Actions está habilitado.
4. Se a política restringir ações, permita especificamente
   actions/checkout e Platane/snk nos commits fixados no workflow.
5. O workflow declara `contents: write` apenas no job que publica.
   A política da conta/organização precisa permitir essa declaração.
   Não é necessário criar um PAT nem permitir aprovação de pull requests.
6. Abra Actions > Update contribution snake > Run workflow.
7. Execute na branch padrão.
8. Aguarde sucesso e confirme os quatro SVGs na branch output.
9. No profile.config.json, altere snake_enabled para true.
10. Execute `python scripts/customize.py`.
11. Publique a atualização do README e da configuração.

Executar o workflow autoriza a publicação dos gráficos na branch output.
O workflow nunca faz push para a branch do README.

O agendamento é diário, às 04:23 UTC. Execuções agendadas podem atrasar.
O GitHub pode desativar agendamentos após 60 dias sem atividade no
repositório público; se isso ocorrer, reative o workflow na aba Actions.

## Falhas e recuperação

- Uma falha na geração ou validação impede a etapa de publicação.
- O push não usa force.
- A última versão publicada permanece disponível em caso de falha.
- Uma primeira execução com falha mantém o Snake ausente do README.
- Não há serviços públicos de cartões estatísticos no carregamento do perfil.
- O link para a atividade nativa do GitHub permanece disponível.
- Se output tiver regras que bloqueiem o bot, ajuste apenas essa branch
  ou continue usando a atividade nativa; não crie um PAT para contornar regras.
- Os SVGs podem demorar a atualizar devido ao cache do GitHub.

## Movimento e compatibilidade

banner.svg usa CSS interno para:

- entrada discreta do texto;
- cursor com três ciclos;
- movimento de uma linha decorativa com três ciclos.

Os textos possuem estado estático visível.
A animação não exige JavaScript, fontes externas ou foreignObject.

O README também usa picture para escolher banner-static.svg quando
prefers-reduced-motion for respeitado pelo navegador.

O pós-processamento do Snake produz versões estáticas e inclui uma
regra prefers-reduced-motion nas versões animadas.

A aparência exata pode variar entre navegadores e interfaces móveis.
A validação final deve ser feita no README renderizado do GitHub;
abrir o SVG diretamente não é suficiente para confirmar esse contexto.

Para desativar permanentemente o movimento do hero, altere no README
o src do banner para ./assets/banner-static.svg.

Para remover o Snake, defina snake_enabled como false e execute
scripts/customize.py. Isso mantém o link para as contribuições reais.

## Temas claro e escuro

O hero e os cartões têm fundo próprio e texto claro.
O corpo do README utiliza as cores nativas do GitHub.
O Snake possui paletas específicas para tema claro e tema escuro.
A preferência do navegador usada por picture pode diferir de um tema
selecionado manualmente nas configurações do GitHub.

## Estatísticas e linguagens

Não foram incluídos contadores, streaks ou totais estáticos.

O Snake utiliza dados obtidos do GitHub pelo Platane/snk.
A disponibilidade e a visibilidade dos dados dependem da API e das
configurações do GitHub; não se promete exibir toda a atividade privada.

Um cartão de linguagens só deve ser adicionado depois de verificar
que existem repositórios públicos e dados suficientes. Ele deve ser
identificado como linguagens de código público, não como medida de
experiência ou domínio técnico.

## Imagens futuras

Screenshots não são necessários para publicar esta versão.

Quando houver imagens autorizadas:

1. Remova nomes, mensagens e dados pessoais.
2. Exclua URLs, credenciais e detalhes privados.
3. Salve as imagens em assets/.
4. Troque a referência do cartão correspondente no README.
5. Atualize o texto alternativo.

Não substitua cartões por screenshots confidenciais.

## Verificação final

O gerador verifica XML, referências locais, atributos alt e contraste
dos pares de texto usados nos assets.

Essas verificações não substituem:

- validação do YAML por actionlint;
- execução real do workflow;
- revisão visual no GitHub em tema claro e escuro;
- revisão em largura de celular;
- teste de movimento reduzido;
- teste dos links públicos adicionados posteriormente.

Nenhuma dessas verificações remotas foi executada pelo gerador.

## Referências oficiais

- https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- https://docs.github.com/en/actions/reference/security/secure-use
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- https://github.com/Platane/snk
- https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_as_an_image
