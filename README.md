# 2-TED para PIX e Padronizacao Nome Banco

-Automação de Processos no TOTVS utilizando Python  
Esses scripts foram desenvolvidos com o objetivo de automatizar tarefas repetitivas dentro do sistema TOTVS, especialmente o processo de padronização e atualização de dados bancários em cadastros de fornecedores.
As automações foram feitas para diferentes situações, como lançamentos via TED, PIX, Banco do Brasil, Itaú Unibanco, entre outros.  

-Principais Tecnologias Utilizadas:
Python  
PyAutoGUI → simulação de cliques, digitação e movimentação do mouse.  
Pyperclip → manipulação da área de transferência (copiar/colar textos de forma confiável).  
Time e OS → controle de tempo e manipulação de caminhos de arquivos.  
Reconhecimento de imagem (via pyautogui.locateOnScreen) para identificar botões, janelas e ícones no sistema.

-O que o código faz:
Localiza imagens específicas da interface do TOTVS (como botões e campos de formulário).  
Realiza cliques automáticos e duplos cliques de forma precisa.  
Edita campos de texto simulando o comportamento humano — inclusive utilizando múltiplos backspace por limitação do sistema.  
Detecta situações de erro, como CPF inválido, e trata automaticamente sem interromper a execução.  
Garante que as ações só avancem quando uma determinada janela for encontrada ou fechada (sincronização por imagem).  
Substitui nomes de bancos e formas de pagamento de forma padronizada.  

-Desafios e Aprendizados:
Durante o desenvolvimento, foram aprendidas e aplicadas boas práticas de automação de interface gráfica:  Criação de funções genéricas para busca de múltiplas imagens e tratamento de exceções.  Controle de fluxo com loops de verificação (aguardar até que uma tela apareça ou desapareça).  Ajuste fino de coordenadas e reconhecimento de padrões visuais em diferentes resoluções e escalas.  Implementação de robustez contra falhas, evitando que o script trave caso uma imagem não seja encontrada imediatamente.  Aprendizado sobre limitações de sistemas legados, como a impossibilidade de usar atalhos universais (Ctrl+A) e a necessidade de simular ações humanas.  

-Resultado:
O uso dessas automações reduziu significativamente o tempo gasto em processos manuais dentro do TOTVS, garantindo mais agilidade, consistência e menor risco de erro humano. Além disso, o projeto reforçou habilidades em automação de processos (RPA), tratamento de exceções, e interação com interfaces gráficas usando Python.
