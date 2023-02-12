import numpy as np
import pygame


pygame.init()

window_size = (1920,1080)

screen = pygame.display.set_mode(window_size)

# Physical constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
sun_radius = 30
# Time step (s)
dt = 3600

bodies = np.array([
    np.array([1.9855e30, np.array([0,0]), np.array([0,0])  , np.array([255, 255, 102]), sun_radius]),
    np.array([3.285e23, np.array([0, 47e3]), np.array([579e9, 0]) , np.array([188, 128, 189]), 6.0/100*sun_radius]),
    np.array([4.867e24, np.array([0, 35e3]), np.array([108.2e9, 0])  , np.array([225, 160, 82]), 8.0/100*sun_radius]),
    np.array([5.9722e24,np.array([0,29.8e3]),np.array([149.6e9,0])  ,np.array([173, 216, 230]), 10/100*sun_radius]),
    np.array([6.39e23, np.array([0,24e3]), np.array([227e9,0])  ,np.array([165, 42, 42]),5/100*sun_radius]),
    np.array([1.898e27, np.array([0, 13.1e3]), np.array([778.5e9, 0])  , np.array([216, 179, 101]), 50.0/100*sun_radius]),
    np.array([5.683e26, np.array([0, 9.7e3]), np.array([1.43e12, 0])  , np.array([244, 208, 66]), 40.0/100*sun_radius]),
    np.array([8.681e25, np.array([0, 6.8e3]), np.array([2.87e12, 0])  , np.array([79, 121, 66]), 25.0/100*sun_radius]),
    np.array([1.024e26, np.array([0, 5.4e3]), np.array([4.5e12, 0]) , np.array([48, 128, 154]), 24.0/100*sun_radius])
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
        bodies = n_body(G,bodies,i,dt)
        x, y = int(bodies[i][2][0] / 1e9 + window_size[0] / 2), int(bodies[i][2][1] / 1e9 + window_size[1] / 2)
        x = min(max(x, bodies[i][4]), window_size[0] - 2 * bodies[i][4])
        y = min(max(y, bodies[i][4]), window_size[1] - 2 * bodies[i][4])
        pygame.draw.circle(screen, bodies[i][3], (x,y), bodies[i][4], 0)

      
    pygame.display.update()

pygame.quit()
