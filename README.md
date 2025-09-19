# UML/Mermaid to Code Generation Experiment

## Overview
This project demonstrates automated code generation from UML diagrams using an LLM (Claude Opus 4.1).

## Objective
Explore how diagram specifications translate into working code implementations via LLM interpretation.

## Source Diagrams

### PlantUML (`userSessionDiagrams/plantuml.puml`)
- Class diagram defining User and Session entities
- Specified attributes and methods with types
- Defined 1:1 relationship

### Mermaid (`userSessionDiagrams/mermaid.mmd`)
- Simplified class diagram with same entities
- Basic property and method definitions
- User → Session association

## Generated Code

### From PlantUML → Python
- `userSessionDiagrams/User.py` - User class with SHA-256 password hashing
- `userSessionDiagrams/Session.py` - Session with secure token generation and expiry

### From Mermaid → JavaScript
- `userSessionDiagrams/user.js` - User class with crypto-based authentication
- `userSessionDiagrams/session.js` - Session management with time-based validation

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