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

class PsOdeObject:
    _state = []
    _rate = []
    
    __step = 0.0    
    __solver = None
    
    def __init__(self, state, rate, solver):
        self.setState(state)
        self.setRate(rate)
        
        self.__solver = solver
        solver.setOdeObject(self)
        
    def setState(self, state):
        self._state = state
    
    def getState(self):
        return self._state
    
    def setRate(self, rate):
        self._rate = rate
    
    # This method should be overridden by the derived class 
    # so that something happen   
    def getRate(self):
        return self._rate;
    
    def setStep(self, step):
        self.__step = float(step)
        
    def getStep(self):
        return self.__step

    def step(self):
        self.__solver.step()
        
