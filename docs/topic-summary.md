# Topic summary: DTR27TZ02-NV002

This is a structured summary, not the official text. The official DSIP page could not be read automatically; this summary comes from a consultant's copy that says it reproduces the DSIP text as published Nov 4, 2026. **Confirm every item in DSIP.**

- **Official source:** [DSIP topic search](https://www.dodsbirsttr.mil/topics-app/) (search DTR27TZ02-NV002)
- **Copy read for this summary:** [BW&CO DTR27TZ02-NV002](https://www.bwcoconsulting.com/fod/dtr27tz02-nv002-ai-detection-of-hardware-trojans), read Nov 24, 2026

| Field | Value |
|---|---|
| Topic | DTR27TZ02-NV002 |
| Title | AI/ML Verification of Microelectronic Integrity for High-Assurance Systems |
| Agency | Defense Threat Reduction Agency (DTRA), STTR Phase I |
| Cycle | DoW FY27 Release 2 |
| Technology areas | Information Systems; Sensors |
| ITAR | No (per the copy) |
| CMMC level | Level 1 (per the copy) |
| Proposals due | Jan 6, 2027, 12:00 PM ET |

## Objective

An AI/ML method and prototype for non-destructive verification of integrated-circuit physical and logical integrity, detecting very small adversarial hardware Trojans that evade functional testing, including data-layer subversion and unauthorized RF activation. It is post-silicon verification under a zero-trust posture, positioned against DARPA's AISS program, which works pre-silicon.

## Description

The defense supply chain is global and commercial. The system should ingest a Level 3 technical data package or a model-based systems engineering digital twin as the intended-logic baseline, and apply algorithms to non-destructive evaluation data to find deviations. It should also support digital provenance with unique, verifiable component identifiers. Training data is performer-sourced (synthetic data from design models or generative models, and open benchmarks). Validation data is performer-procured, without relying on government-furnished information unless a known database is proposed, and must include verified Trojan-bearing parts.

## Phase I

Feasibility study covering: architecture and non-destructive inputs; a validation dataset strategy; a framework for correlating scans with the digital twin; data-layer and RF activation vectors; detection modeling for Trojan classes without golden reference chips; an interoperability hook binding attestation to a physically unclonable function for a distributed-ledger chain of custody; and a final report with a preliminary Phase II prototype design.

### Phase I exit metrics (threshold / objective)

- **Architecture:** architecture mapping NDE and data-package ingestion / adds a zero-knowledge enclave design.
- **Detection:** theoretical >85% detection of known functional Trojans on synthetic data / theoretical >95% across multiple Trojan classes with a simulated false-positive rate.
- **Interoperability:** software API for attestation output / PUF-binding method for distributed-ledger integration.
- **Data strategy:** validated acquisition roadmap for Phase II parts / secured procurement channels for Trojan-bearing test structures.

## Phase II

A working prototype validated on the procured dataset for detection accuracy, false positives and speed; adaptive learning against novel insertion methods; a generative model that synthesizes "compound trigger" Trojans; and a transition plan into quality-assurance pipelines and acquisition pathways.

### Phase II exit metrics (threshold / objective)

- **Physical detection:** true-positive rate >90% on the procured set / >99%, including Trojans of 10 or fewer manipulated gates.
- **Efficiency:** false-positive rate <5% on clean chips / <1% while processing a standard microcontroller's NDE data in under 60 minutes.
- **Adaptability:** flag a novel insertion method from an independent team as an anomaly within 72 hours / the performer's own generator creates and defeats a compound-trigger Trojan.

## Phase III and dual use

Integration into the high-assurance acquisition lifecycle (deployable infrastructure, secure communications, command-and-control nodes). Commercial quality-assurance markets such as financial clearinghouses, medical life-support and autonomous systems.

## Keywords

Microelectronics; Hardware Trojans; AI/ML; Supply Chain Risk Management (SCRM); Zero Trust; Integrity Verification; Non-Destructive Evaluation (NDE); Generative Adversarial Networks (GAN)

## Not available

The topic cites an Enclosure 1 (Programmatic Metrics and Data Sourcing) whose text was not in the copy read. Get it from DSIP.
