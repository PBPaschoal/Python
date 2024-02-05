import pygame
import time
import random

pygame.init()

# Definições iniciais
largura, altura = 600, 400
snake_block = 10
snake_speed = 15

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Configuração da janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Função principal
def jogo():
    game_over = False
    game_close = False

    # Inicialização da cobra
    snake = [{"x": largura / 2, "y": altura / 2}]
    snake_len = 1

    # Inicialização da direção da cobra
    direcao = "RIGHT"
    mudar_direcao = direcao

    # Inicialização da comida
    comida_pos = {"x": round(random.randrange(0, largura - snake_block) / 10.0) * 10.0,
                  "y": round(random.randrange(0, altura - snake_block) / 10.0) * 10.0}

    # Função para desenhar a cobra
    def desenhar_cobra(snake_block, snake):
        for segmento in snake:
            pygame.draw.rect(janela, verde, [segmento["x"], segmento["y"], snake_block, snake_block])

    # Loop principal do jogo
    while not game_over:

        while game_close:
            janela.fill(branco)
            fonte = pygame.font.SysFont(None, 30)
            mensagem = fonte.render("Você perdeu! Pressione Q para sair ou C para jogar novamente.", True, vermelho)
            janela.blit(mensagem, [largura / 6, altura / 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and not direcao == "RIGHT":
                    mudar_direcao = "LEFT"
                elif evento.key == pygame.K_RIGHT and not direcao == "LEFT":
                    mudar_direcao = "RIGHT"
                elif evento.key == pygame.K_UP and not direcao == "DOWN":
                    mudar_direcao = "UP"
                elif evento.key == pygame.K_DOWN and not direcao == "UP":
                    mudar_direcao = "DOWN"

        # Atualização da posição da cobra
        for i in range(snake_len - 1, 0, -1):
            snake[i] = dict(snake[i - 1])

        if mudar_direcao == "LEFT":
            snake[0]["x"] -= snake_block
        elif mudar_direcao == "RIGHT":
            snake[0]["x"] += snake_block
        elif mudar_direcao == "UP":
            snake[0]["y"] -= snake_block
        elif mudar_direcao == "DOWN":
            snake[0]["y"] += snake_block

        # Checar colisões com as bordas
        if snake[0]["x"] >= largura or snake[0]["x"] < 0 or snake[0]["y"] >= altura or snake[0]["y"] < 0:
            game_close = True

        # Checar colisões com o corpo
        for segmento in snake[1:]:
            if snake[0] == segmento:
                game_close = True

        # Checar colisão com a comida
        if snake[0]["x"] == comida_pos["x"] and snake[0]["y"] == comida_pos["y"]:
            comida_pos = {"x": round(random.randrange(0, largura - snake_block) / 10.0) * 10.0,
                          "y": round(random.randrange(0, altura - snake_block) / 10.0) * 10.0}
            snake_len += 1

        # Desenhar a janela
        janela.fill(branco)
        pygame.draw.rect(janela, vermelho, [comida_pos["x"], comida_pos["y"], snake_block, snake_block])
        desenhar_cobra(snake_block, snake)
        pygame.display.update()

        # Controlar a velocidade do jogo
        time.sleep(1 / snake_speed)

    pygame.quit()
    quit()

# Iniciar o jogo
jogo()
