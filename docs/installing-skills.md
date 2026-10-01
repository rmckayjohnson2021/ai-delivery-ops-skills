# Installing Skills

This repo is a Markdown skill pack, not a Python package. To use one or more skills locally, copy the desired skill folders into your Codex skills directory.

## Install One Skill

PowerShell example:

```powershell
$repo = "C:\Dev\repos\ai-delivery-ops-skills"
$skills = "$env:USERPROFILE\.codex\skills"

New-Item -ItemType Directory -Force -Path $skills | Out-Null
Copy-Item -Recurse -Force "$repo\skills\phased-prd-builder" "$skills\phased-prd-builder"
```

Then start a new Codex chat and ask for the skill by name:

```text
Use phased-prd-builder to turn this rough feature idea into a phased PRD.
```

## Install All MVP Skills

```powershell
$repo = "C:\Dev\repos\ai-delivery-ops-skills"
$skills = "$env:USERPROFILE\.codex\skills"

New-Item -ItemType Directory -Force -Path $skills | Out-Null
Copy-Item -Recurse -Force "$repo\skills\*" $skills
```

## Verify The Skill Files

From the repo root:

```powershell
python scripts\validate_skills.py
```

If `python` is not on PATH, use any available Python 3.12+ interpreter. The validator uses only the Python standard library.

## Update Installed Skills

After pulling repo updates, rerun the copy command for the skills you use. Existing folders will be replaced with the repo version.

## Notes

- These skills produce planning and delivery artifacts; they do not call external services by themselves.
- Templates are optional. They are starter formats for saving generated outputs.
- Human review is still required before using generated artifacts for product, engineering, security, legal, or compliance decisions.
