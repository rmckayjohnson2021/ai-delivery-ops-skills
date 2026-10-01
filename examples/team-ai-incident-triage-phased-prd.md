# Phased PRD: RunbookOps AI Incident Triage

## Summary

- Problem: Operations teams have approved runbooks but inconsistent incident notes, which makes triage quality hard to review and improve.
- Primary users: Data operations analysts, incident reviewers, and AI workflow owners.
- Desired outcome: Turn synthetic data-pipeline incident reports into structured, sourced, reviewable recommendations with clear human-review routing.
- Current phase: Portfolio-ready local application with reusable delivery lessons.

## Context

This artifact shows how `phased-prd-builder` can turn a rough AI workflow idea into a phased delivery plan. It is based on the companion [`team-ai-incident-triage`](https://github.com/rmckayjohnson2021/team-ai-incident-triage) repo and its relationship to [`llm-cost-eval-gateway`](https://github.com/rmckayjohnson2021/llm-cost-eval-gateway).

The workflow is intentionally local and synthetic. It is designed to demonstrate reviewable AI delivery practice, not production incident automation.

## Goals

- Retrieve relevant approved runbook snippets for a synthetic incident.
- Produce validated structured triage output.
- Route uncertain, risky, or unsupported cases to human review.
- Expose evidence, prompt context, route reason, and reviewer feedback.
- Measure behavior with held-out synthetic cases.
- Keep model execution compatible with centralized cost and evaluation controls.

## Non-Goals

- Production incident response automation.
- Real customer data processing.
- Automated remediation.
- Enterprise authentication or authorization.
- Claims of production reliability from the portfolio-scale evaluation.

## Assumptions

- Incident records and runbooks are synthetic.
- Recommendations are advisory.
- Human review is required for ambiguous, risky, or insufficiently supported cases.
- Provider-backed execution may be unavailable; the workflow should still fail clearly.
- Budget, retries, and usage logging belong behind a shared execution layer.

## Constraints

- Time: Optimize for a small, inspectable portfolio demo.
- Budget: Avoid paid model calls for repeatable tests; use mock or fixture paths where possible.
- Data: Use local Markdown runbooks and JSONL incident cases.
- Technical: Keep the app runnable locally with a clear setup path.
- Governance: Do not represent simulated recommendations as operational authority.

## Phased Delivery Plan

| Phase | Objective | Scope | Exit Criteria |
| --- | --- | --- | --- |
| Discovery | Define the incident categories, users, runbook sources, and review expectations | Synthetic incidents, runbook taxonomy, output schema, route policy sketch | Reviewer can explain what the workflow should and should not automate |
| MVP | Produce one validated, sourced triage result from a local UI | Retrieval, prompt construction, structured output validation, deterministic routing, Streamlit result view | One routine case shows recommendation, source evidence, route, and diagnostic details |
| Evaluation | Measure behavior before making quality claims | Development cases, held-out cases, rubric, aggregate metrics, case-level failure notes | Evaluation report compares expected category, severity, source match, and review routing |
| Operationalization | Make the demo reviewable and reusable | Gateway boundary, budget diagnostics, reviewer feedback capture, documentation, demo path | Another reviewer can run the app, inspect decisions, and understand limitations |

## User Workflows

### Workflow 1: Routine Incident Review

1. User selects or enters a synthetic incident.
2. System retrieves relevant runbook snippets.
3. System requests structured triage output through the configured execution path.
4. System validates the output schema.
5. System applies deterministic calibration and routing.
6. User reviews recommendation, severity, evidence, and route reason.
7. User records feedback for future runbook or evaluation updates.

### Workflow 2: Ambiguous Or Risky Incident

1. User submits an incident with unclear evidence, multiple possible causes, or risky operational impact.
2. System retrieves evidence but detects uncertainty or risk signals.
3. System routes to human review rather than presenting an automated recommendation as sufficient.
4. User sees the route reason and supporting context.

### Workflow 3: Provider Or Budget Block

1. User runs triage without valid provider access or under a restrictive budget.
2. Execution layer blocks or fails the provider call clearly.
3. System preserves diagnostics and routes the case to human review.

## Functional Requirements

| ID | Requirement | Priority | Acceptance Criteria |
| --- | --- | --- | --- |
| FR-001 | Retrieve approved runbook snippets for each incident | Must | Result includes ranked source references and matched evidence |
| FR-002 | Produce structured triage output | Must | Output validates against the schema or fails with a clear diagnostic |
| FR-003 | Route uncertain or risky cases to human review | Must | Route reason is visible and testable |
| FR-004 | Display evidence and prompt context for review | Should | Reviewer can inspect runbooks, structured output, and prompt preview |
| FR-005 | Capture reviewer feedback | Should | Feedback records accepted, edited, or rejected outcomes with notes |
| FR-006 | Integrate with a shared execution boundary | Should | Provider calls can flow through gateway controls for budget, retries, and usage logging |

## Data And Integration Requirements

- Inputs: Synthetic incident report, approved runbook Markdown, route policy, provider configuration.
- Outputs: Category, severity, recommendation, source references, route, route reason, review status, workflow version, latency, and estimated cost when available.
- Systems: Local Streamlit app, optional model provider, optional cost/eval gateway.
- Schemas: Pydantic response schema for model output and JSONL case format for incidents.
- Logging: Workflow version, provider diagnostics, route reason, reviewer feedback, evaluation results.

## Evaluation Criteria

| Criterion | Measurement | Target | Notes |
| --- | --- | --- | --- |
| Category quality | Category accuracy on held-out cases | Portfolio target defined in evaluation plan | Report case-level misses |
| Severity quality | Severity match on held-out cases | Portfolio target defined in evaluation plan | Calibrate risky cases conservatively |
| Evidence quality | Source match rate and cited runbook relevance | High enough for reviewer trust | Unsupported recommendations should route to review |
| Review routing | Correct human-review routing | No unsafe automation in known risky cases | Review route false positives are acceptable during MVP |
| Cost visibility | Estimated cost and provider diagnostics | Present when provider data exists | Do not claim billing accuracy |
| Reproducibility | Fresh setup and test commands | Another reviewer can run locally | Avoid paid calls in default tests |

## Risks And Mitigations

| Risk | Impact | Mitigation | Owner |
| --- | --- | --- | --- |
| Synthetic data overstates readiness | Reviewers may infer production reliability | State portfolio claim boundaries in README and reports | Project owner |
| Model output is unsupported by runbooks | User may trust weak recommendations | Require evidence display and human-review route for insufficient support | Workflow owner |
| Provider failures create unclear UX | Demo appears broken rather than safely degraded | Preserve diagnostics and route to review | Engineering |
| Cost controls are bypassed | Budget story weakens across companion repos | Keep provider calls behind shared execution service or gateway | Engineering |
| Reviewer feedback is collected but not used | Learning loop becomes cosmetic | Summarize feedback into backlog candidates | Product owner |

## Open Questions

- Which incidents should become canonical demo scenarios?
- What minimum held-out set is enough for the next portfolio release?
- Should gateway integration be required for every demo run or remain optional?
- What reviewer feedback categories best support future runbook updates?
- Which screenshots or walkthrough clips should be linked from the repo?

## Recommended Next Artifact

- [ ] Prototype spike plan
- [ ] Implementation handoff
- [x] Evaluation plan
- [x] Governance review
