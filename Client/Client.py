import pygame
import uuid
from Client.Pieces import Piece
from Client.Network import Network


def redraw(game, col, Player, W, H, T, win):  # w, 0>carry on,1>draw,2>win
    pygame.draw.rect(win, (0, 0, 0), pygame.Rect(0, 0, W, H))
    Font = pygame.font.SysFont("comicsans", 50)

    w = " wins" if game.w == 2 else ""
    colour = (255, 0, 0) if game.p == Player else (255, 255, 255)
    t = Font.render(f"Player {game.p}{w}", 1, colour)

    if game.w == 1:
        t = Font.render("Draw", 1, (255, 0, 255))

    trect = t.get_rect(center=(W / 2, T / 2))
    win.blit(t, trect)

    if game.p == Player:  # highlight
        pygame.draw.rect(
            win, (80, 80, 80), pygame.Rect(col * 100, T, 100, game.rows * 100)
        )

    for i in range(game.cols - 1):
        pygame.draw.rect(
            win, (255, 0, 255), pygame.Rect(99 + 100 * i, T, 2, game.rows * 100)
        )

    for i in range(game.rows):
        pygame.draw.rect(
            win, (255, 0, 255), pygame.Rect(0, 99 + 100 * i, game.cols * 100, 2)
        )

    pieces = []
    for i in range(len(game.l)):
        lst = [x for x in game.l[i] if x != 0]
        for k in range(len(lst)):
            pieces.append(Piece(i * 100, (game.rows - k) * 100, game.l[i][k] - 1))

    for item in pieces:
        item.draw(win)
    pygame.display.update()

    if game.w in (1, 2):
        end = True
        while end:
            a, b = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    end = False


def main(n, game, Player, clock, W, H, T, win):

    run = True
    while run:

        a, b = pygame.mouse.get_pos()
        col = a // 100
        redraw(game, col, Player, W, H, T, win)

        if game.w != 0:
            game = n.send(-3)

        if (
            game.p != Player
        ):  # waiting for other play to make move and return updated game state
            pygame.time.wait(1000)
            game = n.send(-2)
            print("sending: -2")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                n.close()
                pygame.quit()

            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and game.l[col][-1] == 0
                and game.p == Player
                and b > 100
            ):  # 2nd is if there is space in that column
                # if no space then dont break loop
                pygame.time.wait(500)
                print("sending: ", col)
                game = n.send(int(col + 1))  # add,check

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    n.close()
                    run = False
                    return

        clock.tick(30)


def menu_screen(win, clock, session_id, W, H, T):
    run = True

    while run:
        clock.tick(30)
        win.fill((0, 0, 0))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255, 0, 255))
        trect = text.get_rect(center=(W / 2, H / 2))
        win.blit(text, trect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    n = Network(54187)
                    game = n.connect(session_id)
                    Player = n.receive()
                    run = False
                except Exception as e:
                    print("Could not connect:", e)

    main(n, game, Player, clock, W, H, T, win)
    return


def start():

    pygame.init()

    session_id = str(uuid.uuid4())
    print("Session ID:", session_id)

    T = 100  # space for text
    W, H = 700, 600 + T
    win = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Connect Donut")
    clock = pygame.time.Clock()

    while True:
        menu_screen(win, clock, session_id, W, H, T)


if __name__ == "__main__":
    start()
