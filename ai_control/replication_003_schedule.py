"""Frozen label schedule for preregistered replication 003.

This module assigns inputs only. It never imports or executes the harness.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json

FIRST_SEED = 421000
LAST_SEED = 421999
COUNT = 1000
HALF = 500
SCHEDULE_NAMESPACE = "replication-003"
EXPECTED_SCHEDULE_SHA256 = "ce49182fda417635d42e32fe38ff9c2df790487eaabe0de5abec9791572d80c2"


@dataclass(frozen=True)
class ReplicationLabel:
    seed: int
    violation_present: bool
    feasible: bool
    first_arm: str


def _selected_half(label: str) -> set[int]:
    seeds = range(FIRST_SEED, LAST_SEED + 1)
    ranked = sorted(
        seeds,
        key=lambda seed: hashlib.sha256(
            f"{SCHEDULE_NAMESPACE}:{label}:{seed}".encode("ascii")
        ).hexdigest(),
    )
    return set(ranked[:HALF])


def frozen_schedule() -> tuple[ReplicationLabel, ...]:
    violation = _selected_half("violation")
    feasible = _selected_half("feasible")
    baseline_first = _selected_half("baseline_first")
    return tuple(
        ReplicationLabel(
            seed=seed,
            violation_present=seed in violation,
            feasible=seed in feasible,
            first_arm="logging_only" if seed in baseline_first else "monitor_enforced",
        )
        for seed in range(FIRST_SEED, LAST_SEED + 1)
    )


def schedule_sha256() -> str:
    payload = json.dumps(
        [asdict(row) for row in frozen_schedule()],
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
