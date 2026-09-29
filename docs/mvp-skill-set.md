# MVP Skill Set

## 1. phased-prd-builder

Turns rough requirements into a phased PRD. Best for early product shaping, scope negotiation, and alignment between product, engineering, evaluation, and governance stakeholders.

Key output:

- Problem and user context
- Goals and non-goals
- Phased delivery plan
- Functional requirements
- Evaluation criteria
- Risks and open questions

## 2. prototype-spike-planner

Creates a focused learning plan before a full implementation commitment. Best for unknown integrations, model behavior, data access, or governance feasibility.

Key output:

- Hypotheses
- Risk-ranked unknowns
- Experiments
- Success criteria
- Stop conditions
- Decision paths

## 3. implementation-handoff

Converts a PRD, spike result, or rough plan into engineering-ready work. Best when a team needs PR slices, interfaces, tests, and rollout notes.

Key output:

- Work slices
- Interfaces and contracts
- Implementation notes
- Test plan
- Rollout and rollback
- Open decisions

## 4. evaluation-plan-builder

Creates a reproducible evaluation plan for AI workflows. Best when teams need to compare prompts, model routes, policies, retrieval changes, or workflow versions.

Key output:

- Evaluation question
- Compared configurations
- Dataset or case set design
- Metrics and rubric
- Cost and latency tracking
- Claim boundaries

## 5. governance-review

Reviews a plan for delivery governance concerns. Best before a pilot, launch, or larger investment.

Key output:

- Data and privacy review
- Security and access concerns
- Human oversight requirements
- Auditability requirements
- Cost controls
- Launch gates

## Recommended Flow

```text
rough idea
  -> phased-prd-builder
  -> prototype-spike-planner when uncertainty is high
  -> evaluation-plan-builder before quality claims
  -> governance-review before pilot or launch
  -> implementation-handoff for build execution
```

Not every project needs every artifact. Small projects may start with a spike and handoff. Higher-risk AI workflows should include evaluation and governance artifacts before implementation.
