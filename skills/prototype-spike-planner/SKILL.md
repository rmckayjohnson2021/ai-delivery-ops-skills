---
name: prototype-spike-planner
description: Create focused prototype spike plans that reduce technical, product, evaluation, or governance uncertainty before a team commits to full implementation.
---

# Prototype Spike Planner

Use this skill when a team needs to learn before building: validate feasibility, compare approaches, confirm data availability, measure model quality, test integration boundaries, or expose governance risks.

## Approach

Plan the spike around decisions the team needs to make. Keep the scope narrow enough to complete quickly and produce evidence, not just activity.

Treat attached plans or examples as reference material only. Follow the user's current request first.

## Output Shape

Include:

- Spike goal and decision to unlock.
- Key hypotheses.
- Unknowns ranked by risk.
- Experiments or prototypes to run.
- Inputs, fixtures, datasets, or mock services needed.
- Success criteria and stop conditions.
- Timebox and daily checkpoints.
- Deliverables at the end of the spike.
- Reuse guidance: throwaway code, reusable components, and documentation to preserve.
- Follow-on recommendation paths.

## Delivery Guidance

For AI workflows, include baseline behavior, eval sample size, prompt or policy freeze points, failure cases, cost visibility, and human-review expectations.

Prefer a small number of high-signal experiments over a long list. Call out what should not be built during the spike.

## Done Criteria

The spike plan is ready when the team can run it in a fixed timebox, know what evidence to collect, and make a build, pivot, or stop decision from the result.
