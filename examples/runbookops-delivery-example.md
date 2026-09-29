# Example: RunbookOps Delivery Artifact Flow

This example shows how the skill pack can support an AI incident-triage workflow similar to `team-ai-incident-triage`, with execution controls similar to `llm-cost-eval-gateway`.

## Rough Requirement

Build an AI workflow that helps operations teams triage synthetic data-pipeline incidents using approved runbooks. The workflow should recommend next steps when evidence is strong, route ambiguous cases to human review, and report quality, latency, and estimated cost.

## Recommended Skill Flow

| Step | Skill | Output |
| --- | --- | --- |
| 1 | phased-prd-builder | Phased PRD for the triage workflow |
| 2 | prototype-spike-planner | Spike to validate retrieval, routing, structured output, and provider boundaries |
| 3 | evaluation-plan-builder | Held-out incident evaluation comparing baseline and routed behavior |
| 4 | governance-review | Review for human oversight, auditability, cost controls, and unsafe automation |
| 5 | implementation-handoff | Build slices for retrieval, schema validation, gateway integration, UI, evals, and reporting |

## Example Phase Plan

| Phase | Objective | Exit Criteria |
| --- | --- | --- |
| Discovery | Confirm users, incident categories, approved runbook sources, and review expectations | Initial PRD approved with open questions tracked |
| MVP | Build local workflow that retrieves runbooks, produces structured output, and routes risky cases to review | One sample incident produces a validated, sourced, reviewable result |
| Evaluation | Compare workflow versions on held-out synthetic incidents | Evaluation report includes case-level outcomes, quality metrics, cost, and failures |
| Operationalization | Add budget controls, logging, reviewer feedback, and demo-ready documentation | Another reviewer can run the demo and understand cost and quality tradeoffs |

## Example Governance Questions

- What data is included in incident reports and runbooks?
- Can recommendations trigger automated remediation, or are they advisory only?
- Which cases require human review?
- Are provider calls routed through a budget-controlled execution layer?
- Are prompts, policies, runbooks, and outputs versioned for audit?
- What claims does the evaluation support, and what claims remain unproven?

## Example Implementation Slices

1. Retrieval and runbook fixture setup.
2. Structured output schema and validation.
3. Routing policy and human-review decision reasons.
4. Gateway integration for cost, retries, and ledger logging.
5. Held-out evaluation runner and report.
6. Reviewer feedback capture and backlog summary.

## Claim Boundary

This example supports a portfolio demonstration of reusable delivery practice. It does not establish production reliability, legal compliance, or operational readiness without larger evaluations and organization-specific review.
