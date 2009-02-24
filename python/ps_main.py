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

from ps_app import PsApplication
from ps_solver_euler import PsOdeSolverEuler
from ps_solver_euler_cromer import PsOdeSolverEulerCromer
from ps_ode_falling import PsOdeObjectFalling
from ps_ode_sho import PsOdeObjectSHO

eulerBall = PsOdeObjectFalling([0,1,0,0,500,0,0],[None,0,None,0,None,-9.81,1], PsOdeSolverEuler())
eulerCromerBall = PsOdeObjectFalling([0,1,0,0,500,0,0],[None,0,None,0,None,-9.81,1], PsOdeSolverEulerCromer())
eulerSHO = PsOdeObjectSHO([1, 0, 0],[None, None, 1],PsOdeSolverEuler())
eulerCromerSHO = PsOdeObjectSHO([1, 0, 0],[None, None, 1],PsOdeSolverEulerCromer())

app = PsApplication([eulerBall,eulerCromerBall, eulerSHO, eulerCromerSHO])

dt = 0.1
steps = 100
app.run(dt,steps)
print eulerBall.getState()
print eulerCromerBall.getState()
print eulerSHO.getState()
print eulerCromerSHO.getState()


