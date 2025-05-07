from enum import Enum

class BoundaryCondition(Enum):
    PERIODIC = "Periodic"
    FIXED = "Fixed"
    OPEN = "Open"

class UpdateRule(Enum):
    METROPOLIS = "Metropolis"
    GLAUBER = "Glauber"
    HEAT_BATH = "Heat Bath" 