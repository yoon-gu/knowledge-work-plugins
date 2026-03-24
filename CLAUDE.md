# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is Anthropic's open-source collection of **knowledge work plugins** for [Claude Cowork](https://claude.com/product/cowork) and [Claude Code](https://claude.ai/code). Plugins make Claude a domain expert for specific roles (sales, data, legal, etc.) by bundling skills, commands, connectors, and sub-agents into installable packages.

There is no build system, no tests, and no application code. The entire repo is **Markdown and JSON files only**.

## Plugin Structure

Every plugin follows this layout:

```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest (name, version, description, author)
├── .mcp.json                    # MCP server connections (tool integrations)
├── CONNECTORS.md                # Documents tool categories and ~~placeholder syntax
├── README.md                    # Plugin overview (Korean-translated)
├── commands/                    # Slash commands (explicit user invocation)
│   └── command-name.md
└── skills/                      # Domain knowledge (auto-triggered by Claude)
    └── skill-name/
        ├── SKILL.md             # Main skill definition with YAML frontmatter
        ├── references/          # Supporting reference material
        └── QUICKREF.md          # Optional quick reference
```

### Key file formats

- **SKILL.md**: Has YAML frontmatter (`name`, `description`) followed by Markdown body. The `description` field contains trigger phrases that tell Claude when to activate the skill.
- **plugin.json**: Standard fields are `name`, `version`, `description`, `author`.
- **.mcp.json**: Maps connector names to MCP server URLs. Plugins are tool-agnostic — they reference categories (e.g., `~~CRM`, `~~chat`) rather than specific products.
- **CONNECTORS.md**: Documents the `~~category` placeholder convention and lists which MCP servers are pre-configured vs. alternative options.

## Content Language

The repo has been translated to Korean. All README.md, SKILL.md, and CONNECTORS.md files contain Korean text. The plugin.json `description` fields remain in English.

## Plugins

There are 15 first-party plugins in the root directories and 4 partner-built plugins under `partner-built/`:

- **Root**: bio-research, cowork-plugin-management, customer-support, data, design, engineering, enterprise-search, finance, human-resources, legal, marketing, operations, product-management, productivity, sales
- **Partner-built**: apollo, brand-voice, common-room, slack

The `cowork-plugin-management` plugin is special — it contains skills for creating and customizing other plugins, with reference schemas and examples.

## Contributing

Plugins are just Markdown files. Fork, edit, submit a PR. Licensed under Apache 2.0.
