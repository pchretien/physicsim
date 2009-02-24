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

class PsOdeSolver:
    __ode = None
    
    def setOdeObject(self, ode):
        self.__ode = ode
        
    def getOdeObject(self):
        return self.__ode
        
    # This function must be overridden by the derived class
    def step(self):
        raise Exception, "OdeSolver.step() must be overridden"