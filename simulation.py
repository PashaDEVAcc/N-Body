import numpy as np
import pygame


pygame.init()

window_size = (1920,1080)

screen = pygame.display.set_mode(window_size)

# Physical constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
earth_radius = 10
sun_radius = 50
mercury_radius = 5
# Time step (s)
dt = 3600

bodies = np.array([
    np.array([1.9855e30,np.array([0,0]),np.array([0,0])]),
    np.array([5.9722e24,np.array([0,29.8e3]),np.array([149.6e9,0])]),
    np.array([3.2850e23, np.array([0,47.87e3]), np.array([57.9e6,0])])
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

  # Update the velocity and position of the other bodies
  for i in range(len(bodies)):
    if i == j:
      continue
    a_j = F_total / bodies[i][0]
    v_j = bodies[i][1] + a_j * dt
    r_j = bodies[i][2] + v_j * dt

    bodies[i][1] = v_j
    bodies[i][2] = r_j

  bodies[j][1] = v_1
  bodies[j][2] = r_1

  return bodies

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    bodies = n_body(G,bodies,1,dt)
    pygame.draw.circle(screen, (255, 165, 0), (window_size[0] / 2, window_size[1] / 2),sun_radius, 0)
    x, y = int(bodies[1][2][0] / 1e9 + window_size[0] / 2), int(bodies[1][2][1] / 1e9 + window_size[1] / 2)
    x = min(max(x, earth_radius), window_size[0] - earth_radius)
    y = min(max(y, earth_radius), window_size[1] - earth_radius )
    pygame.draw.circle(screen, (173, 216, 230), (x,y), earth_radius, 0)
    x_mercury, y_mercury = int(bodies[2][2][0] / 1e9 + window_size[0] / 2), int(bodies[2][2][1] / 1e9 + window_size[1] / 2)
    x_mercury = min(max(x_mercury, mercury_radius), window_size[0] - mercury_radius)
    y_mercury = min(max(y_mercury, mercury_radius), window_size[1] -  mercury_radius)
    pygame.draw.circle(screen, (255, 255, 255), (x_mercury,y_mercury), mercury_radius, 0)
    pygame.display.update()

pygame.quit()
