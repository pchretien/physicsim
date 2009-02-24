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
#
# The state vector should be in the form:
#     p1, v1, p2, v2, pn, vn, t
# Where p and v are the position and the velocity and t is the time elapsed 
# since the beginning of the simulation
#
# The rate vector should be in the form:
#     v1, a1, v2, a2, vn, an, t
# Where v and a are the velocity and the acceleration and t is the time since
# the beginning of the simulation
#

from ps_solver import PsOdeSolver

class PsOdeSolverEuler(PsOdeSolver):
    
    # This function must be overridden by the derived class
    def step(self):
        state = self.getOdeObject().getState()
        rate = self.getOdeObject().getRate()
        step = self.getOdeObject().getStep()
        
        # Make sure the rate and the state vectors are same length
        if len(state) != len(rate):
            raise Exeption, "PsOdeSolverEuler.step() - State and Rate vectors must be of the same length"
        
        # Calculate the next step value using Euler algorithm 
        for index in range(len(state)):
            state[index] += rate[index]*step
            
        self.getOdeObject().setState(state)
   
