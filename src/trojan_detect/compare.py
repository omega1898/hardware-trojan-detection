"""Structural diff of two gate-level netlists.

A netlist here is a dict: {"gates": {gate_name: gate_type}, "wires": [(from_gate, to_gate), ...]}.
"""


def diff_netlists(baseline_netlist, observed_netlist):
    """Return gates and wires present in one netlist but not the other."""
    baseline_gates = set(baseline_netlist["gates"].items())
    observed_gates = set(observed_netlist["gates"].items())
    baseline_wires = set(map(tuple, baseline_netlist["wires"]))
    observed_wires = set(map(tuple, observed_netlist["wires"]))
    return {
        "extra_gates": sorted(observed_gates - baseline_gates),
        "missing_gates": sorted(baseline_gates - observed_gates),
        "extra_wires": sorted(observed_wires - baseline_wires),
        "missing_wires": sorted(baseline_wires - observed_wires),
    }


def is_suspicious(difference):
    """Any extra or missing structure is a deviation worth review."""
    return any(difference[key] for key in difference)
