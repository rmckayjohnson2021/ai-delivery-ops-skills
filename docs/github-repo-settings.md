# GitHub Repo Settings

These settings are managed in the GitHub UI, not through normal Git files.

## Description

```text
Reusable AI delivery ops skills for PRDs, spikes, handoffs, evals, and governance reviews
```

## Topics

```text
ai
delivery-ops
prd
evaluation
governance
codex-skills
portfolio
```

## Suggested Settings

- Visibility: Public
- Default branch: `main`
- Pages: Deploy from branch `main`, folder `/docs`
- Features: Issues enabled, Discussions optional, Wiki disabled unless needed
- Pull request settings: Allow squash merge
- Branch protection: Optional for v0.1.0; useful after collaborators or external users appear

## Release Checklist

Before creating `v0.1.0`:

- [ ] README links render correctly on GitHub.
- [ ] `Validate skills` GitHub Action passes on `main`.
- [ ] Repo description and topics are set.
- [ ] No secrets, private customer data, or local-only generated files are committed.
- [ ] Examples make clear which claims are portfolio demonstrations versus production claims.
