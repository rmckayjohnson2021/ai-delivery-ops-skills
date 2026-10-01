# Artifact Quality Checklist

Use this checklist before sharing generated delivery artifacts with product, engineering, evaluation, governance, or portfolio reviewers.

## Phased PRD

- [ ] Names the problem, user, and desired outcome.
- [ ] Separates goals from non-goals.
- [ ] Defines delivery phases with exit criteria.
- [ ] Includes functional requirements with acceptance criteria.
- [ ] Identifies data, integration, and dependency needs.
- [ ] Defines quality, cost, latency, and safety success criteria where relevant.
- [ ] Marks assumptions and open questions instead of inventing certainty.
- [ ] Points to the next needed artifact: spike, eval plan, governance review, or implementation handoff.

## Prototype Spike Plan

- [ ] States the decision the spike should unlock.
- [ ] Lists hypotheses and risk-ranked unknowns.
- [ ] Keeps experiments narrow enough for the timebox.
- [ ] Defines success criteria and stop conditions.
- [ ] Names fixtures, datasets, mocks, or provider access needed.
- [ ] Clarifies what code is throwaway versus reusable.
- [ ] Explains how results lead to build, pivot, or stop decisions.

## Implementation Handoff

- [ ] Summarizes user impact and scope.
- [ ] Breaks work into reviewable slices.
- [ ] Defines interfaces, schemas, APIs, configuration, and logging needs.
- [ ] Covers error handling and fallback behavior.
- [ ] Includes tests for success, failure, and regression paths.
- [ ] Identifies evaluation hooks and operational metrics.
- [ ] Includes rollout, rollback, and review expectations.
- [ ] Leaves unresolved decisions with clear owners.

## Evaluation Plan

- [ ] States the evaluation question and decision it supports.
- [ ] Defines compared configurations and freeze points.
- [ ] Explains dataset or case-set design.
- [ ] Provides a scoring rubric or ground-truth source.
- [ ] Includes quality, cost, latency, and failure metrics where relevant.
- [ ] Covers edge cases and instruction-injection or unsafe-automation attempts when relevant.
- [ ] Produces case-level findings, not only aggregate metrics.
- [ ] States claim boundaries, especially for small portfolio evaluations.

## Governance Review

- [ ] Summarizes intended use, users, and affected stakeholders.
- [ ] Identifies data classification, retention, and export concerns.
- [ ] Reviews authentication, authorization, secrets, and provider access.
- [ ] Defines human oversight and escalation requirements.
- [ ] Requires audit logs, trace identifiers, and versioned prompts or policies where relevant.
- [ ] Checks budget, quota, retry, and abuse controls.
- [ ] Defines launch gates, owners, and unresolved blockers.
- [ ] Gives a clear posture: proceed, proceed with controls, pilot only, or block pending decisions.

## Portfolio Readiness

- [ ] The artifact is specific to the project, not generic filler.
- [ ] Limitations are stated plainly.
- [ ] Claims are backed by evidence or clearly labeled as assumptions.
- [ ] The artifact links to related repos, examples, reports, or templates when useful.
- [ ] A reviewer can tell what should happen next.
