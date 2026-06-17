# Graph Report - C:\Users\Ronaldinhoo\Desktop\TourUP  (2026-06-16)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 77 nodes · 71 edges · 13 communities (10 shown, 3 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0c5c4e01`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]

## God Nodes (most connected - your core abstractions)
1. `Lugar de la Memoria LUM` - 14 edges
2. `Lima` - 8 edges
3. `Lima` - 7 edges
4. `Cercado de Lima` - 5 edges
5. `Cercado de Lima` - 5 edges
6. `MAC Lima` - 5 edges
7. `MALI` - 5 edges
8. `Miraflores` - 3 edges
9. `Miraflores` - 3 edges
10. `Museo de Sitio Puruchuco` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Ate Vitarte` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Ate Vitarte/Museo de Sitio Puruchuco/Actividades.md → CLAUDE.md
- `Lurin` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Lurin/Museo de Sitio Pachacamac/Actividades.md → CLAUDE.md
- `TourUP` --references--> `Lima`  [EXTRACTED]
  TourUP.md → wiki/Peru/Lima.md
- `Barranco` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Barranco/MAC Lima/Actividades.md → CLAUDE.md
- `Cercado de Lima` --references--> `Lima`  [EXTRACTED]
  wiki/Peru/Lima/Cercado de Lima/MALI/Actividades.md → CLAUDE.md

## Import Cycles
- None detected.

## Communities (13 total, 3 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.13
Nodes (15): Charlas y ciclos de lectura sobre pensamiento social, Miercoles de Filmoteca Ciclo Nora de Izcue, Noche MALI visitas mediadas y actividades especiales, Nueva exposicion en Sala 1 primer piso, Recorrido virtual en visitavirtual.cultura.pe, Recorridos por la casa-museo y exposiciones temporales, Talleres ligados a festividades y danzas tradicionales, Talleres visitas guiadas ferias y presentaciones artisticas (+7 more)

### Community 1 - "Community 1"
Cohesion: 0.14
Nodes (14): 80 anos de Naciones Unidas, Anudando la tierra con Pancho Basurco, Cine Piru. Un viaje de oro, Clausura del Festival de Cine Al Este 2026, Fiesta de la Musica 2026 Orquesta de Camara UNM, Memorias afectivas Husares de Junin, Musica y poesia con Jose Maria Salazar, Musica y poesia con Leda Quintana (+6 more)

### Community 2 - "Community 2"
Cohesion: 0.15
Nodes (14): Ate Vitarte, Barranco, Lima, Lugar de la Memoria LUM, Lurin, MAC Lima, Miraflores, MNAAHP (+6 more)

### Community 3 - "Community 3"
Cohesion: 0.18
Nodes (11): Experiencia sonora con instrumentos originales de mas de 1500 anos, Talleres para familias y experiencias sensoriales, Visitas guiadas a salas de arqueologia, Visitas guiadas al complejo arqueologico, Barranco, Lima, Miraflores, MNAAHP (+3 more)

### Community 4 - "Community 4"
Cohesion: 0.40
Nodes (5): Contemporaneo 1. Materia Alquimia Dispositivo Flujo, El Peru en clave CARETAS. 75 anos de historia fotografica, Semana de la Educacion Artistica 2026, Unsex me La deconstruccion de Lady Macbeth, MAC Lima

### Community 5 - "Community 5"
Cohesion: 0.40
Nodes (5): Cercado de Lima, MALI, Museo de Arte Italiano, Museo Jose Carlos Mariategui, Museo Nacional de la Cultura Peruana

### Community 6 - "Community 6"
Cohesion: 0.50
Nodes (4): Recorridos guiados y talleres de ceramica y tejido, Tramas andinas. Ciencia paisaje arqueologia y saberes ancestrales, Lurin, Museo de Sitio Pachacamac

### Community 7 - "Community 7"
Cohesion: 0.50
Nodes (4): Talleres de educacion patrimonial para ninos y jovenes, Visitas guiadas por el complejo inca, Ate Vitarte, Museo de Sitio Puruchuco

## Knowledge Gaps
- **49 isolated node(s):** `Museo de Sitio Puruchuco`, `MAC Lima`, `MALI`, `Museo de Arte Italiano`, `Museo Jose Carlos Mariategui` (+44 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Lima` connect `Community 3` to `Community 0`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.363) - this node is a cross-community bridge._
- **Why does `Miraflores` connect `Community 3` to `Community 1`?**
  _High betweenness centrality (0.224) - this node is a cross-community bridge._
- **Why does `Cercado de Lima` connect `Community 0` to `Community 3`?**
  _High betweenness centrality (0.212) - this node is a cross-community bridge._
- **What connects `Museo de Sitio Puruchuco`, `MAC Lima`, `MALI` to the rest of the system?**
  _49 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._