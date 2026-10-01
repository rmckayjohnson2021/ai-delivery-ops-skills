<p align="center">
  <img src="docs/assets/ai-delivery-ops-logo.png" alt="AI Delivery Ops Skills logo" width="260">
</p>

# AI Delivery Ops Skills

Reusable Codex-style skills and templates for turning rough AI product ideas into phased delivery artifacts that teams can build, evaluate, govern, and review.

Repository: https://github.com/rmckayjohnson2021/ai-delivery-ops-skills

## Project Status

This is an MVP skill pack for portfolio and team enablement use. The first version focuses on five delivery artifacts:

- Phased PRDs
- Prototype spike plans
- Implementation handoffs
- Evaluation plans
- Governance reviews

The skills are intentionally lightweight. They do not replace product judgment, engineering review, legal review, security review, or production approval. They help teams ask the right questions early and leave a clear handoff trail.

## Why This Exists

AI teams often move from a rough idea to a prototype quickly, but the delivery trail can become thin: unclear scope, missing evaluation criteria, vague implementation handoffs, and governance risks discovered too late. This repo provides a reusable operating layer for AI delivery work.

Use it when a team needs to:

- Convert messy requirements into a phased PRD.
- Plan a spike before committing to a full build.
- Hand work to engineering with interfaces, tests, and risks made explicit.
- Define evals before claiming quality improvements.
- Review cost, privacy, security, human oversight, and audit concerns before launch.

## Companion Projects

This repo complements:

- [`team-ai-incident-triage`](https://github.com/rmckayjohnson2021/team-ai-incident-triage), which demonstrates a reviewable AI workflow for synthetic incident triage.
- [`llm-cost-eval-gateway`](https://github.com/rmckayjohnson2021/llm-cost-eval-gateway), which demonstrates budget enforcement, routing, retries, usage logging, and evaluation infrastructure.

Where those repos show concrete AI applications and execution controls, this repo captures the repeatable delivery methods that help teams plan, govern, and hand off similar projects.

## MVP Skill Set

| Skill | Use When | Primary Output |
| --- | --- | --- |
| [`phased-prd-builder`](skills/phased-prd-builder/SKILL.md) | A rough product or workflow idea needs delivery shape | Phased PRD with scope, phases, acceptance criteria, risks, and open questions |
| [`prototype-spike-planner`](skills/prototype-spike-planner/SKILL.md) | The team needs to reduce uncertainty before committing | Spike plan with hypotheses, experiments, decision gates, and evidence to collect |
| [`implementation-handoff`](skills/implementation-handoff/SKILL.md) | A concept or PRD needs to become build-ready | Engineering handoff with slices, interfaces, tests, rollout, and review plan |
| [`evaluation-plan-builder`](skills/evaluation-plan-builder/SKILL.md) | A workflow needs measurable quality and cost criteria | Evaluation plan with datasets, metrics, baselines, rubrics, and reporting format |
| [`governance-review`](skills/governance-review/SKILL.md) | A delivery plan needs risk, oversight, and audit review | Governance review with risks, required controls, owners, and go/no-go gates |

## Repository Structure

```text
ai-delivery-ops-skills/
  .github/
    workflows/
      validate.yml
  skills/
    phased-prd-builder/
      SKILL.md
    prototype-spike-planner/
      SKILL.md
    implementation-handoff/
      SKILL.md
    evaluation-plan-builder/
      SKILL.md
    governance-review/
      SKILL.md
  templates/
    phased-prd-template.md
    prototype-spike-template.md
    implementation-handoff-template.md
    evaluation-plan-template.md
    governance-review-template.md
  docs/
    assets/
      ai-delivery-ops-logo.png
    index.html
    site.css
    artifact-quality-checklist.md
    github-repo-settings.md
    installing-skills.md
    mvp-skill-set.md
    repo-plan.md
    portfolio-positioning.md
  examples/
    runbookops-delivery-example.md
    team-ai-incident-triage-phased-prd.md
  scripts/
    validate_skills.py
```

## Static Skill Browser

The repo includes a zero-build static browser in [`docs/index.html`](docs/index.html) with:

- Skill cards
- Template previews
- Example artifact links
- Copy/install commands
- A recommended flow diagram

To publish it with GitHub Pages, set Pages to deploy from the `main` branch and `/docs` folder. The public URL will be:

```text
https://rmckayjohnson2021.github.io/ai-delivery-ops-skills/
```

See [`docs/github-repo-settings.md`](docs/github-repo-settings.md).

## How To Use

1. Open the relevant skill in `skills/<skill-name>/SKILL.md`.
2. Give Codex the rough requirement, existing plan, or project context.
3. Ask it to use the skill to produce the matching artifact.
4. Save the output using the matching template from `templates/`.
5. Review the artifact with product, engineering, evaluation, and governance stakeholders before execution.

Example request:

```text
Use the phased-prd-builder skill to turn this rough idea into a phased PRD:
We want an AI workflow that triages data pipeline incidents using approved runbooks,
routes uncertain cases to humans, and records quality and cost metrics.
```

## Install Locally

Copy one or more skill folders from `skills/` into your local Codex skills directory. See [`docs/installing-skills.md`](docs/installing-skills.md) for PowerShell examples.

## Examples

- [`examples/runbookops-delivery-example.md`](examples/runbookops-delivery-example.md) shows the recommended artifact flow for a RunbookOps-style AI workflow.
- [`examples/team-ai-incident-triage-phased-prd.md`](examples/team-ai-incident-triage-phased-prd.md) shows a concrete phased PRD produced for the companion incident-triage project.

## Validate

Run the lightweight validator from the repo root:

```powershell
python scripts\validate_skills.py
```

The validator checks that each skill has a `SKILL.md` file with valid `name` and `description` frontmatter, and that the name matches the folder. GitHub Actions runs the same check on pushes and pull requests.

## Public Portfolio Checklist

- Clear README with problem, audience, and companion-project context.
- Concise skill instructions that can be inspected without running code.
- Templates that show the expected artifact shape.
- Example showing how the skills apply to a realistic AI workflow.
- Install guidance for local reuse.
- Automated validation for skill metadata.
- Artifact quality checklist for reviewer-ready outputs.
- No credentials, private customer data, or production-only assumptions.
- Honest boundaries around evaluation, governance, and production readiness.

## Roadmap

- Add examples for cost-gateway planning and AI workflow governance.
- Add optional scripts for packaging the skill pack once the format stabilizes.
- Add release notes for `v0.1.0` after the first GitHub Actions run passes.

## License

MIT. See [`LICENSE`](LICENSE).
