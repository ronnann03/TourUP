import re
from pathlib import Path

WIKI = Path('wiki/Peru/Lima')

actividades = [
    ('Miraflores','Lugar de la Memoria LUM','Cine Piru. Un viaje de oro','Cine','Jue 4 junio 2026 11:00 a.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Memorias afectivas Husares de Junin','Dialogo','Mie 10 junio 2026 12:00 m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Musica y poesia con Jose Maria Salazar','Musica y Poesia','Jue 11 junio 2026 6:00 p.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Sobreviviendo en azul y tierra','Visita Guiada','Vie 12 junio 2026 11:00 a.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Nico en el barrio con Silvia Bando Landa','Taller','Dom 14 junio 2026 4:00 p.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','80 anos de Naciones Unidas','Visita Guiada','Mie 17 junio 2026 11:30 a.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Presentacion libro Nico de Silvia Bando Landa','Presentacion de Libro','Jue 18 junio 2026 6:00 p.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Shiringa. Genocidio y resistencia en la Amazonia','Cine + Dialogo','Vie 19 junio 2026 7:00 p.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Anudando la tierra con Pancho Basurco','Taller + Dialogo','Sab 20 junio 2026 12:00 m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Fiesta de la Musica 2026 Orquesta de Camara UNM','Concierto','Mie 24 junio 2026 7:00 p.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Musica y poesia con Leda Quintana','Musica y Poesia','Jue 25 junio 2026 6:00 p.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Tupac Amaru El Ultimo Inca de Federico Garcia','Cine + Dialogo','Vie 26 junio 2026 7:00 p.m.','Gratuito'),
    ('Miraflores','Lugar de la Memoria LUM','Clausura del Festival de Cine Al Este 2026','Cine Clausura','Sab 27 junio 2026 6:00 p.m.','Gratuito'),
    ('Pueblo Libre','MNAAHP','Visitas guiadas a salas de arqueologia','Visita Guiada','Todo el mes','S/ 15 Gratis 1er domingo'),
    ('Pueblo Libre','MNAAHP','Talleres para familias y experiencias sensoriales','Taller Familiar','Todo el mes','S/ 15 Gratis 1er domingo'),
    ('Lurin','Museo de Sitio Pachacamac','Tramas andinas. Ciencia paisaje arqueologia y saberes ancestrales','Exposicion Temporal','Vigente junio 2026','S/ 15 Gratis 1er domingo'),
    ('Lurin','Museo de Sitio Pachacamac','Recorridos guiados y talleres de ceramica y tejido','Recorrido + Taller','Todo el mes','S/ 15 Gratis 1er domingo'),
    ('Miraflores','Museo de Sitio Pucllana','Experiencia sonora con instrumentos originales de mas de 1500 anos','Experiencia Sonora','Junio 2026','S/ 15'),
    ('Miraflores','Museo de Sitio Pucllana','Visitas guiadas al complejo arqueologico','Visita Guiada','Todo el mes','S/ 15'),
    ('Ate Vitarte','Museo de Sitio Puruchuco','Visitas guiadas por el complejo inca','Visita Guiada','Todo el mes','S/ 10 Gratis 1er domingo'),
    ('Ate Vitarte','Museo de Sitio Puruchuco','Talleres de educacion patrimonial para ninos y jovenes','Taller Educativo','Todo el mes','S/ 10 Gratis 1er domingo'),
    ('Cercado de Lima','Museo de Arte Italiano','Visitas guiadas a coleccion de arte italiano','Visita Guiada','Todo el mes','Gratuito'),
    ('Cercado de Lima','Museo de Arte Italiano','Recorrido virtual en visitavirtual.cultura.pe','Recorrido Virtual','Permanente','Gratuito'),
    ('Cercado de Lima','Museo Nacional de la Cultura Peruana','Visitas guiadas sobre arte popular y diversidad cultural','Visita Guiada','Todo el mes','S/ 5 Gratis 1er domingo'),
    ('Cercado de Lima','Museo Nacional de la Cultura Peruana','Talleres ligados a festividades y danzas tradicionales','Taller','Todo el mes','S/ 5 Gratis 1er domingo'),
    ('Cercado de Lima','Museo Jose Carlos Mariategui','Recorridos por la casa-museo y exposiciones temporales','Recorrido','Todo el mes','Gratuito'),
    ('Cercado de Lima','Museo Jose Carlos Mariategui','Charlas y ciclos de lectura sobre pensamiento social','Charla','Todo el mes','Gratuito'),
    ('Cercado de Lima','MALI','Miercoles de Filmoteca Ciclo Nora de Izcue','Filmoteca','Mie 3 junio 2026','Variable'),
    ('Cercado de Lima','MALI','Nueva exposicion en Sala 1 primer piso','Exposicion','Del 17 jun al 1 nov 2026','Variable'),
    ('Cercado de Lima','MALI','Noche MALI visitas mediadas y actividades especiales','Evento Nocturno','Vie 27 junio 2026','Variable'),
    ('Cercado de Lima','MALI','Talleres visitas guiadas ferias y presentaciones artisticas','Talleres','Todo el mes','Variable'),
    ('Barranco','MAC Lima','Unsex me La deconstruccion de Lady Macbeth','Exposicion','Hasta 12 julio 2026','S/ 12'),
    ('Barranco','MAC Lima','El Peru en clave CARETAS. 75 anos de historia fotografica','Exposicion','Junio 2026','S/ 12'),
    ('Barranco','MAC Lima','Contemporaneo 1. Materia Alquimia Dispositivo Flujo','Exposicion','Hasta dic 2026','S/ 12'),
    ('Barranco','MAC Lima','Semana de la Educacion Artistica 2026','Festival','Junio 2026','S/ 12'),
]

count = 0
for distrito, museo, nombre, tipo, fecha, costo in actividades:
    slug = re.sub(r'[^a-z0-9]+', '-', nombre.lower())[:50]
    p = WIKI / distrito / museo
    p.mkdir(parents=True, exist_ok=True)
    md_path = p / f'Act - {slug}.md'
    contenido = f"""---
type: actividad
title: "{nombre}"
parent: "{museo}"
museo: "[[{museo}]]"
distrito: "[[{distrito}]]"
ciudad: "[[Lima]]"
pais: "[[Peru]]"
tipo_actividad: "{tipo}"
fecha: "{fecha}"
costo: "{costo}"
tags: [actividad, {distrito.lower().replace(' ','-')}, nivel-6]
---

# {nombre}

| Campo | Detalle |
|-------|---------|
| **Museo** | [[{museo}]] |
| **Distrito** | [[{distrito}]] |
| **Tipo** | {tipo} |
| **Fecha** | {fecha} |
| **Costo** | {costo} |

---
*← [[{museo}]] | [[{distrito}]] | [[Lima]] | [[Peru]]*
"""
    md_path.write_text(contenido, encoding='utf-8')
    count += 1
    print(f"  [ok] {nombre[:40]}")

print(f'\nCreadas {count} notas de actividades individuales')
