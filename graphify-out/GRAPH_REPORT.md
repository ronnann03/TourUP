# Graph Report - C:\Users\Ronaldinhoo\Desktop\TourUP  (2026-06-16)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 19 nodes · 19 edges · 6 communities (3 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `21a1dda3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]

## God Nodes (most connected - your core abstractions)
1. `Lima` - 8 edges
2. `Cercado de Lima` - 5 edges
3. `Miraflores` - 3 edges
4. `TourUP` - 2 edges
5. `Peru` - 2 edges
6. `Ate Vitarte` - 2 edges
7. `Barranco` - 2 edges
8. `Lurin` - 2 edges
9. `Pueblo Libre` - 2 edges
10. `Museo de Sitio Puruchuco` - 1 edges

## Surprising Connections (you probably didn't know these)
- `TourUP` --references--> `Lima`  [EXTRACTED]
  TourUP.md → wiki/Peru/Lima.md
- `TourUP` --references--> `Peru`  [EXTRACTED]
  TourUP.md → wiki/Peru.md
- `Ate Vitarte` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Ate Vitarte/Ate Vitarte.md → wiki/Peru/Lima.md
- `Lima` --references--> `Barranco`  [EXTRACTED]
  wiki/Peru/Lima.md → wiki/Peru/Lima/Barranco/Barranco.md
- `Lima` --references--> `Lurin`  [EXTRACTED]
  wiki/Peru/Lima.md → wiki/Peru/Lima/Lurin/Lurin.md

## Import Cycles
- None detected.

## Communities (6 total, 3 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.40
Nodes (5): Cercado de Lima, MALI, Museo de Arte Italiano, Museo Jose Carlos Mariategui, Museo Nacional de la Cultura Peruana

### Community 1 - "Community 1"
Cohesion: 0.50
Nodes (5): Lima, MNAAHP, Peru, Pueblo Libre, TourUP

### Community 2 - "Community 2"
Cohesion: 0.67
Nodes (3): Lugar de la Memoria LUM, Miraflores, Museo de Sitio Pucllana

## Knowledge Gaps
- **10 isolated node(s):** `Museo de Sitio Puruchuco`, `MAC Lima`, `MALI`, `Museo de Arte Italiano`, `Museo Jose Carlos Mariategui` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lima` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 5`?**
  _High betweenness centrality (0.882) - this node is a cross-community bridge._
- **Why does `Cercado de Lima` connect `Community 0` to `Community 1`?**
  _High betweenness centrality (0.405) - this node is a cross-community bridge._
- **Why does `Miraflores` connect `Community 2` to `Community 1`?**
  _High betweenness centrality (0.216) - this node is a cross-community bridge._
- **What connects `Museo de Sitio Puruchuco`, `MAC Lima`, `MALI` to the rest of the system?**
  _10 weakly-connected nodes found - possible documentation gaps or missing edges._