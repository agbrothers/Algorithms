import numpy as np

# Approximating Numerical Solutions to ordinary differential equations
# Math 151b - Numerical Analysis

""" FUNCTIONS """ 

def f(t,w):
    return(t*np.exp(3*t)-2*w)

def Euler(w0,t1, t2, h):
    return(w0 + 0.5*h*((t1*np.exp(3*t1)-2*w0) + (t2*np.exp(3*t2) - 2*(w1 + h*(t1*np.exp(3*t1)-2*w0)))))

def Midpoint(w0, t0, h):
    return(w0 + h*f(t0+(h/2), w0 + (h/2)*f(t0,w0)))
    
def RK4(w0, t0, t1, h):
    k1 = h*f(t0,w0)
    k2 = h*f(t0+(h/2), w0+(k1/2))
    k3 = h*f(t0+(h/2), w0+(k2/2))
    k4 = h*f(t1, w0 + k3)
    return(w0 + (1/6)*(k1 + 2*k2 + 2*k3 + k4))

def Y(t):
    return(0.2*t*np.exp(3*t) - (1/25)*np.exp(3*t) + (1/25)*np.exp(-2*t))


""" DATA """

h = 0.5
t = np.linspace(0,1,3)
yy = [y(0), y(0.5), y(1)]
eul = [0, Euler(eul[0],t[0],t[1],h), Euler(eul[1], t[1], t[2], h)]
mid = [0, Midpoint(mid[0], t[0], h), Midpoint(mid[1], t[1], h)]
RK = [0, RK4(RK[0],t[0],t[1],h), RK4(RK[1],t[1],t[2],h)]


""" PLOTS """
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax1.plot(t,eul,'b', t,yy,'r')
ax1.legend(['Mod Euler', 'True Sol'])

ax2 = fig.add_subplot(222)
ax2.plot(t,mid,'b', t,yy,'r')
ax2.legend(['Midpoint', 'True Sol'])

ax3 = fig.add_subplot(223)
ax3.plot(t,RK,'b', t,yy,'r')
ax3.legend(['RK4', 'True Sol'])
