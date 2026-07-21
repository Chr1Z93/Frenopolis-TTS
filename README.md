# Frenopolis TTS

This repository contains a work-in-progress Tabletop Simulator mod for Frenopolis. It is currently in a prototype / in-progress state. The goal was to build a playable TTS experience with card-driven interactions, turn flow, energy payment, and simple board management.

## Current status

The mod is not a complete or polished implementation of the game. It includes several gameplay systems and UI helpers, but some rules, edge cases, and polish are still missing.

## What is implemented

The current implementation provides a number of core features:

- A global phase tracker with turn and phase progression
- Context-menu actions for cards, including:
  - Play
  - Play as Energy
  - Fren
  - Archive
  - Banish
  - Collect
- Energy-payment flow with color and colorless cost handling
- Fren stacking and card attachment behavior
- Card movement between play zones and shared zones
- Deck spawning from a card bag
- Basic untap and turn-reset helpers

## Project structure

- [src/Global.ttslua](src/Global.ttslua) — main mod logic and game flow
- [src/ColorLib.ttslua](src/ColorLib.ttslua), [src/CoroutineLib.ttslua](src/CoroutineLib.ttslua), [src/DeckLib.ttslua](src/DeckLib.ttslua), [src/MathLib.ttslua](src/MathLib.ttslua), [src/SearchLib.ttslua](src/SearchLib.ttslua), [src/TableLib.ttslua](src/TableLib.ttslua), [src/TtsLuaAdditions.ttslua](src/TtsLuaAdditions.ttslua) — helper libraries used by the main script
- [misc/](misc/) — extra data and utility scripts

## How to use



## Notes

This repository is primarily a code snapshot of a stopped project. It may be useful as a starting point for further development.
