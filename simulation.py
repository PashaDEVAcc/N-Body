import numpy as np
import pygame


pygame.init()

window_size = (1920,1080)

screen = pygame.display.set_mode(window_size)

# Physical constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
sun_radius = 50
# Time step (s)
dt = 3600

bodies = np.array([
    np.array([1.9855e30,np.array([0,0]),np.array([0,0])]),
    np.array([5.9722e24,np.array([0,29.8e3]),np.array([149.6e9,0]),np.array([173, 216, 230]), 10]),
    np.array([6.39e23, np.array([0,24e3]), np.array([227e9,0]),np.array([165, 42, 42]),5]),
])
def n_body(G, bodies, j, dt):
  # Calculate the net force on body 1
  F_total = []
  for i in range(len(bodies)):
    if i == j:
      continue
    r_2 = bodies[i][2] - bodies[j][2]
    magnitude = np.sqrt(np.sum(r_2**2))
    F = G * bodies[j][0] * bodies[i][0] / magnitude**3 * r_2
    F_total.append(F)
  F_total = np.sum(F_total, axis=0)
  # Update the velocity and position of body 1
  a_1 = F_total / bodies[j][0]
  v_1 = bodies[j][1] + a_1 * dt
  r_1 = bodies[j][2] + v_1 * dt
  #other planets
  # Update the velocity and position of the other bodies
  bodies[j][1] = v_1
  bodies[j][2] = r_1

  return bodies

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 165, 0), (window_size[0] / 2, window_size[1] / 2),sun_radius, 0)
    for i in range(len(bodies)):
      if i == 0 :
         continue
      bodies = n_body(G,bodies,i,dt)
      x, y = int(bodies[i][2][0] / 1e9 + window_size[0] / 2), int(bodies[i][2][1] / 1e9 + window_size[1] / 2)
      x = min(max(x, bodies[i][4]), window_size[0] - bodies[i][4])
      y = min(max(y, bodies[i][4]), window_size[1] - bodies[i][4] )
      pygame.draw.circle(screen, bodies[i][3], (x,y), bodies[i][4], 0)
      
    pygame.display.update()

pygame.quit()
