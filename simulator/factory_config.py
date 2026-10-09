"""
Factory configuration for the AC Metais plant simulator.

Defines the production stages, machines and materials that the simulator
uses to generate orders and shop-floor events.
All values are realistic assumptions, not real company data.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    code: str
    name: str
    sequence: int     # order in which a production order goes through the stages
    avg_hours: float  # average processing time per production order


@dataclass(frozen=True)
class Machine:
    code: str
    name: str
    stage_code: str   # stage where the machine works


@dataclass(frozen=True)
class Material:
    code: str
    name: str
    density_g_cm3: float  # used later to calculate sheet weight and scrap


STAGES = [
    Stage("CUT", "Laser cutting", 1, 2.0),
    Stage("FAB", "Metalworking / boilermaking", 2, 6.0),
    Stage("FIN", "Finishing", 3, 3.0),
    Stage("SHP", "Shipping", 4, 1.0),
]

MACHINES = [
    Machine("LSR-01", "Fiber laser 01", "CUT"),
    Machine("LSR-02", "Fiber laser 02", "CUT"),
    Machine("BND-01", "Press brake 01", "FAB"),
    Machine("WLD-01", "Welding cell 01", "FAB"),
    Machine("PNT-01", "Paint booth 01", "FIN"),
]

MATERIALS = [
    Material("CS-1020", "Carbon steel SAE 1020", 7.85),
    Material("SS-304", "Stainless steel AISI 304", 8.00),
    Material("AL-5052", "Aluminum 5052", 2.68),
]


def print_summary() -> None:
    """Print the plant configuration in production order."""
    print("AC Metais plant configuration\n")
    for stage in sorted(STAGES, key=lambda s: s.sequence):
        machines = [m.code for m in MACHINES if m.stage_code == stage.code]
        machine_list = ", ".join(machines) if machines else "no machines"
        print(f"{stage.sequence}. {stage.name} (~{stage.avg_hours}h) -> {machine_list}")

    print(f"\nMaterials: {', '.join(m.name for m in MATERIALS)}")


if __name__ == "__main__":
    print_summary()
