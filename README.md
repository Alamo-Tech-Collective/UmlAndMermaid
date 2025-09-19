# UML/Mermaid to Code Generation Experiment

## Overview
This project demonstrates automated code generation from UML diagrams using an LLM (Claude Opus 4.1).

## Objective
Explore how diagram specifications translate into working code implementations via LLM interpretation.

## Key Observations
- LLM inferred security practices (password hashing, secure tokens)
- Added practical features not in diagrams (session expiry, validation)
- Maintained language-appropriate patterns (Python properties, JS prototypes)
- Preserved diagram relationships in code structure

## Generation Details
- **Model**: Claude Opus 4.1
- **Tool**: Claude Code
- **Prompt Used**: "generate the associated code for any plantuml or mermaid files. Put the code in the same directory as the uml or mermaid file it is associated with."
- **Method**: Direct diagram interpretation to idiomatic code from single prompt
