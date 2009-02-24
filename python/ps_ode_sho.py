## physicSim ##
#
# physicSim is a set of tools for doing physic simulations.
# Copyright (C) 2008,2009  Philippe Chretien
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License Version 2
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# You will find the latest version of this code at the following address:
# http://github.com/pchretien
#
# You can contact me at the following email address:
# philippe.chretien@gmail.com

from ps_ode import PsOdeObject

# SHO stands for Simple Harmonic Oscillator
class PsOdeObjectSHO(PsOdeObject):
    # The state of this object is defined as following:
    # x, vx, t
    # x, vx horizontal coordinates and velocity of the projectile
    # t is the time elapsed since the beginning of the simulation
    
    __mass = 1.0
    __K = 1.0
    
    def __init__(self, state, rate, solver, mass=1.0, K=1.0):
        PsOdeObject.__init__(self, state, rate, solver)
        self.__mass = mass
        self.__K = K
       
    def getRate(self):
        F = -1*self.__K*self.getState()[0]
        a = F / self.__mass
        
        # Velocity
        self._rate[0] = self.getState()[1]
        self._rate[1] = a
        
        return self._rate;
    
    def setState(self, state):
        PsOdeObject.setState(self, state)
        
        # Debug stuff ...
        line = ""
        for i in range(int(abs(self._state[0])*20)*2):
            line += "-"
        print line
    
        