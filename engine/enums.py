"""Enums for the simulation engine."""

from enum import Enum

class BoundaryCondition(Enum):
    """Boundary conditions for the simulation grid."""
    PERIODIC = "periodic"
    OPEN = "open"
    FIXED = "fixed"
    ANTI_PERIODIC = "anti_periodic"
    MIXED = "mixed"
    TWISTED = "twisted"
    RANDOM = "random"

class UpdateRule(Enum):
    """Update rules for the simulation."""
    METROPOLIS = "metropolis"
    GLAUBER = "glauber"
    HEAT_BATH = "heat_bath"
    WOLFF = "wolff"
    SWENDSEN_WANG = "swendsen_wang"
    KAWASAKI = "kawasaki"
    MULTI_CLUSTER = "multi_cluster"
    PROJECTED_CLUSTER = "projected_cluster"
    LOOP = "loop"
    HOSHEN_KOPELMAN = "hoshen_kopelman"
    FORTUN_KASTELEYN = "fortun_kasteleyn"
    WANG_LANDAU = "wang_landau"
    PARALLEL_TEMPERING = "parallel_tempering"
    MULTICANONICAL = "multicanonical" 