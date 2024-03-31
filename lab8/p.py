import pygame

mode = 'draw'
color = (0, 0, 255) 

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    points = []
    
    global mode
    global color

    while True:
        pressed = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.key == pygame.K_r:
                    color = (255, 0, 0) 
                elif event.key == pygame.K_g:
                    color = (0, 255, 0) 
                elif event.key == pygame.K_b:
                    color = (0, 0, 255) 
                elif event.key == pygame.K_y:
                    color = (255, 255, 0)  
                elif event.key == pygame.K_e:
                    mode = 'erase'  
                elif event.key == pygame.K_d:
                    mode = 'draw'  
                elif event.key == pygame.K_c:
                    mode = 'circle' 
                elif event.key == pygame.K_s:
                    mode = 'rectangle' 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if mode == 'draw':
                        radius = min(200, radius + 1)
                    elif mode == 'circle':
                        pygame.draw.circle(screen, color, event.pos, radius)
                    elif mode == 'rectangle':
                        pygame.draw.rect(screen, color, (event.pos[0], event.pos[1], radius*2, radius))
                elif event.button == 3: 
                    if mode == 'draw':
                        radius = max(1, radius - 1)
                    elif mode == 'erase':
                        pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
                
            if event.type == pygame.MOUSEMOTION:
                if mode == 'draw':
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                    
        screen.fill((0, 0, 0))
        
        if mode == 'draw':
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius)
                i += 1
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width):
    global color
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
