---
name: docusaurus-expert
description: Expert knowledge on creating Docusaurus 3.0 sites. Use this for setup, page creation, and configuration.
allowed-tools: [Read, Write, Bash]
---

# Docusaurus Expert Instructions

## 1. Project Structure
- `/docs`: Markdown content (The Book).
- `/src/components`: React components (ChatWidget, etc.).
- `/docusaurus.config.js`: Main config.

## 2. Markdown Rules
- ALWAYS add frontmatter to `.md` files:
  ```md
  ---
  id: [unique-id]
  title: [Readable Title]
  sidebar_position: [Number]
  ---