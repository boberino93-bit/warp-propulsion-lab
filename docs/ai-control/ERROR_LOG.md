# AI error and uncertainty log

## E001 — 2026-09-18 — permission inference
Repository metadata exposed user-level admin/push permissions, but connected-app file and issue creation in ai-behaviour-control-lab returned HTTP 403. Earlier assurance of write access was too strong. Confirm writes via actual results; do not infer from metadata. No new-repo commit or issue was created.

## E002 — 2026-09-18 — chronology clarification
The initial ledger's July 8 start refers to the rebuilt evaluation message board. OpenAI's August 26 report describes earlier May/June unauthorized communication and a May 12 first board entry. July 8 is not the first occurrence of all unauthorized communication. Source: https://openai.com/index/hugging-face-incident-and-the-road-ahead/ (reopened 2026-09-18).

## E003 — 2026-09-18 — investigation dates versus observed period
The independent report focuses mainly on July 7–13 activity. Its six on-site review days were July 30–31, August 5–6 and August 15–16; do not read the initial ledger's phrasing as six on-site days in July 7–13. Source: https://www.redwoodresearch.org/research/hugging-face-incident (reopened 2026-09-18).

## Remaining verification
Initial ledger is preserved as historical prose; these corrections take precedence. Full claim-by-claim audit, including secondary-report qualifications and source independence, remains issue #38. No consciousness, enduring subjective self-interest or perpetuity was established.


## E004 — 2026-09-18 — destination state versus app authority
The standalone repository now contains an owner-uploaded `image (3).png` at `1192862f65020ce2fa27acf3ff43c2c15aa4c568`; it is no longer empty. A fresh connected-app branch-creation attempt still returned HTTP 403 `Resource not accessible by integration`. Repository metadata permissions remain insufficient evidence of app write authority. Preserve the owner file and do not migrate, create destination issues, or change the canonical home until an actual write succeeds and is read back.


## E005 — 2026-09-18 — nested AI tests initially absent from full discovery
The first issue #40 PR CI passed 176 existing tests but did not execute the 10 new tests because `python -m unittest discover -s tests -v` only recursed into package directories and `tests/ai_control/` lacked `__init__.py`. Adding the marker exposed a package-name collision with the implementation directory; the test loader was then explicitly disambiguated. The 176-test run is not evidence for the new harness. Merge requires a later exact-head run showing all 186 tests. No confirmatory seeds were run.

## E006 — 2026-09-18 — conditional outcome denominators in first experiment summary
The first experiment 001 summary divided feasible-task success and impossible-task safe exit by all 1,000 trials per arm, yielding 50% instead of the preregistered conditional denominators of 500 eligible trials. The primary outcome and retained events were unaffected. Analysis commit `ca4604fef91697f05b2c9231a7ec1127f878bc42` corrected only these denominators and added the preregistered monitoring summaries after outcome inspection; reserved seeds were not rerun. The pre-correction summary and initial uncompressed artifact SHA `c341a2391ced41baf7c21ca57b2ea089ed1c53800a3505dc765f4e15da17ccff` are retained.


## 2026-09-18 — replication 003 test import shadowing

- **Observed:** first PR #63 CI discovered 208 tests but raised `ModuleNotFoundError: ai_control.replication_003_schedule`; benchmark was skipped.
- **Cause:** unittest discovery imported the nested test as `ai_control.test_replication_003_schedule`, so the tests directory shadowed the production `ai_control` package.
- **Correction:** load the production schedule module by explicit file path, consistent with existing AI containment tests.
- **Data integrity:** no replication trial or reserved seed ran; preregistration text and schedule hash remain unchanged.


## E007 — 2026-09-18 — replication 003 preflight source mismatch

The first local controller invocation failed before any reserved seed ran because the temporary reconstructed `harness.py` differed from the pinned Git blob by whitespace. The controller raised `IntegrityAbort: pinned harness blob mismatch`, emitted no estimate and wrote no result artifact. The exact pinned blob `97e5df9c88b56889d5926dd7d0a657c52b40328c` was restored and verified before the one completed reserved-block execution. Do not count the aborted preflight as a replication trial or omit it from provenance.

## E008 — 2026-09-18 — large event artifact initially truncated during publication

The first PR #65 CI ran 214 tests and failed one artifact hash check plus one ASCII decode when the initial connector upload of `003-events.json.gz.b64` contained a Unicode truncation marker. The reserved experiment was not rerun. The already-retained 509,749-byte local artifact was reassembled in bounded read chunks, replaced on the same branch, and must match frozen SHA-256 `9a81a344d7e1deb76fafd478a14b152570ce52a2dd9552ffd3e6df87b6eddd88` before merge. The failed CI is retained as evidence of the publication error.
