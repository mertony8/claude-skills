# Claude Skills Collection

A curated collection of custom skills for [Claude](https://claude.ai) — extending Claude's capabilities with domain-specific workflows, evaluation frameworks, and automated report generation.

## What Are Skills?

Skills are instruction sets that teach Claude how to perform specialized, multi-step tasks. When you upload a `.skill` file to Claude, it gains the ability to follow structured workflows — crawling websites, analyzing data, generating professional reports, and more.

Skills work best with **Claude in Chrome** (browser automation) and **Computer Use** (file creation, code execution) enabled.

## Available Skills

| Skill | Description | Requirements |
|-------|-------------|-------------|
| [UX Heuristic Evaluator](./ux-heuristic-evaluator/) | Evaluate any website against Nielsen's 10 Usability Heuristics. Crawls the site, scores each heuristic (Pass/Partial/Fail), and generates a professional PDF audit report. Includes 4 example reports. | Claude in Chrome, Python (reportlab) |

## Installation

### Option 1: Upload the `.skill` file

1. Download the `.skill` file from the skill's directory (or from [Releases](../../releases))
2. Open **Claude.ai** → **Customize** → **Skills**
3. Click **Add Skill** and upload the file

### Option 2: Manual installation

1. Clone this repo or download the skill folder
2. Place it in your Claude skills directory
3. The skill will be available in your next conversation

## Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md              ← Main instructions (required)
├── references/           ← Reference docs loaded on demand
│   └── *.md
└── scripts/              ← Executable scripts for automation
    └── *.py
```

- **SKILL.md** — The core instruction file with YAML frontmatter (name, description) and markdown workflow steps
- **references/** — Detailed reference material that Claude reads when needed (keeps the main SKILL.md lean)
- **scripts/** — Python/JS scripts for deterministic tasks like PDF generation

## Contributing

Have a skill idea or want to improve an existing one? Contributions are welcome.

1. Fork this repo
2. Create your skill following the structure above
3. Test it thoroughly with Claude
4. Submit a PR with a description of what the skill does and sample outputs

## License

MIT License — see [LICENSE](./LICENSE) for details.

## Author

Built by [@mertony8](https://github.com/mertony8)
