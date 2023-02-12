# N-Body
N-Body simulation between earth and the sun using pygame
a simulation based on the famous N-Body equation which of where Fg = -Gmi * np.sum(mj/||r12||**3 (r12)), where r12 is the relational vector of r2 - r1
the equation above gives you the forces acting on the body which you can then use to update the acceleration using a_e = -F / mi
the velocity using v_e = v_e + a_e * dt
and finaly the positional vector using r_e = r_e + v_e * dt
this then gives you the new positional vector of the earth which using the while true function and repeating it over and over while updating the velocity,
and the positional vector will replecate an orbit, this N-Body equation is generally used for calculating the position of a satellite after a certain amount of time dt
although I don't have the expertise to do this , if you wanted to you can replace Fg = -Gmi * np.sum9mj/||r12||**3 (r12)) with one of Einstein's field equations 
this would give you a more accurate result and would also let you simulate the position if you were for example orbiting a black hole, using Fg = -Gmi * np.sum9mj/||r12||**3 (r12))
which is basic Newtonian gravity breaks down if you use such large bodies such as black holes.
