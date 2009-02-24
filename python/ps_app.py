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

class PsApplication:
    __odeObjects = []
    
    def __init__(self, odeObjects):
        if isinstance(odeObjects, list):
            self.__odeObjects.extend(odeObjects)
        else:
            self.__odeObjects.append(odeObjects)
            
    # For now we assume that all objects have the same step value ...
    def run(self, step, steps):
        for ode in self.__odeObjects:
            ode.setStep(step)
                
        for i in range(steps):
            for ode in self.__odeObjects:
                ode.step()