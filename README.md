# hardware-trojan-detection

AI-assisted, non-destructive verification of integrated-circuit integrity, built as a starting point for DTRA STTR topic **DTR27TZ02-NV002, AI/ML Verification of Microelectronic Integrity for High-Assurance Systems** (DoW FY27 Release 2).

## The problem

Defense systems rely on chips made in a global commercial supply chain. A hardware Trojan, a small malicious change to a chip's circuitry, can pass every functional test and stay dormant until triggered. The topic asks for an AI/ML method that compares non-destructive scans of a finished chip against its intended design and flags deviations, including Trojans as small as a few gates, without needing a known-good "golden" chip.

## Approach in plain terms

1. **Baseline:** load the intended design (the technical data package or a design model) as a graph of gates and connections.
2. **Observe:** reconstruct the same graph from non-destructive evaluation data of the physical chip.
3. **Compare:** find gates and connections that exist in the chip but not in the design, or the reverse.
4. **Learn:** train models on synthetic Trojan insertions so they can flag subtle or novel ones, and keep false positives low on clean chips.

## Phase I scope

A feasibility study: architecture and inputs, a validation dataset strategy, a framework for correlating scans with the design model, detection modeling without golden reference chips, and an attestation hook. Phase I exit metrics include theoretical detection above 85% of known functional Trojans on synthetic data (threshold). This is an STTR, so it needs a research-institution partner. See [docs/topic-summary.md](docs/topic-summary.md).

## Status

Skeleton only. The first vertical slice (structural diff of two small netlists, no ML yet) is in [docs/architecture.md](docs/architecture.md) and stubbed in `src/`.

## How to run

```bash
python -m unittest discover -s tests -v
```

## Documentation

- [docs/topic-summary.md](docs/topic-summary.md): what the topic asks for
- [docs/topic-qa.md](docs/topic-qa.md): Q&A available so far
- [docs/references.md](docs/references.md): the topic's references
- [docs/submission-requirements.md](docs/submission-requirements.md): dates, award size, partnering, official instructions
- [docs/architecture.md](docs/architecture.md): first vertical slice and design decisions
