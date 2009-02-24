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

class PsOdeObjectFalling(PsOdeObject):
    # The state of this object is defined as following:
    # x, vx, y, vy, z, vz, t
    # x, vx and y, vy are the horizontal coordinates and velocity of the projectile
    # z, vz are he vertical position and velocity of the projectile
    # t is the time elapsed since the beginning of the simulation
    
    def getRate(self):
        # Velocity
        self._rate[0] = self.getState()[1]
        self._rate[2] = self.getState()[3]
        self._rate[4] = self.getState()[5]
        
        return self._rate;
    
        