# Computational notebooks

The virtual working environment of NFDI4SD is realised by computational notebooks. Since the 1970s, Donald Knuth's paradigm of literate programming has been based on the narrative description of algorithms as a weave or mixture of explanatory text and executable program. Literate programming environments have been developed for many languages and computational purposes, beginning with Knuth's own $\LaTeX$ typesetting system.

## Jupyter notebooks

The version of the Jupyter notebooks that is widely used today was originally developed by Jernando Perez and Brian E. Granger as "An Open Source Framework for Interactive, Collaborative and Reproducible Scientific Computing and Education" and summarised their objectives in the points: [^2]


> * "Individual exploration: a single investigator tests an idea, algorithm or question, likely with a small-scale test data set or simulation.
>*  Collaboration: if the initial exploration appears promising, more often than not some kind of collaborative effort ensues.
>* Production-scale execution: large data sets and complex simulations often require the use of clusters, supercomputers or cloud resources in parallel.
>* Publication: whether as a paper or an internal report for discussion with colleagues, results need to be presented to others in a coherent form.
>* Education: ultimately, research results become part of the corpus of a discipline that is shared with students and colleagues, thus seeding the next cycle of research."

Researchers use the NFDI4SD services in the form of advanced computational notebooks. The researcher can choose from a range of different running environments of computational notebooks, which are adapted to the development. NFDI4SD develops comprehensive libraries for these environments, providing additional functionality for using research data's computational services, including

- aggregation
- data wrangling
- visualisation
- publication


NFDI4SD follows closely the technological development and intends to support the most important computational notebooks currently used by the small subjects with the support of the steering committee. The following figure shows the implementation of computational notebooks by Jupyter notebooks in the web environment of Jupyterlab [^1].

Die computational Notebooks entwickeln ihre Funktionalität und Bedienungsfreundlichkeit ständig weiter.

- Viele verschiedene vielversprechende Ansätze der kollaborativen Zusammenarbeit von Forschergruppen an einem Dokument sind bereits in fortgeschrittenem Entwicklungsstadium.
- Zukünftige Notebooks kombinieren die Vorzüge aktueller Entwicklungen von Computersprachen und gehen flexibel auf die verschiedenen Kompetenzfelder der Nutzer ein.

[^1]: [Jupyter](https://jupyter.org/), mit [Wiki](https://en.wikipedia.org/wiki/Project_Jupyter) und [Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/).

[^2]: [Perez/Granger](https://ipython.org/_static/sloangrant/sloan-grant.html)


Für die Aufgaben der NFDI4SD werden die Anforderungen an open science research data durch eine erhebliche Erweiterung der Funktionalität von Notebooks übernommen. Das NFDI4SD entwickelt dazu ein Paket "Computational Research Objects" an zusätzlichen Funktionalitäten, in deren Zentrum die Einführung einer neuen Objektklasse *CompResearchObject* steht, deren Instanzen alle relevanten Informationen von Forschungsobjekten alle Attribute beschreibt.

## ObservableHQ

Eine sich sehr schnell verbreitende Form von computational Notebooks sind interaktive Notebooks nach der open source plattform entwickelt von Mike Bostock - ObservableHQ. Aufbauend auf Bostocks "data driven Für die Infographics der New York Time perfektionieren diese Notebooks interaktive Infographiken. ObservableHQ ist ein Repositorium zur kollaborativen Entwicklung, Austausch und Weiterentwicklung von visuellen computational Notebooks. Die herausstechenden Graphiken der d3 Bibliothek sind führend im Design und Funktionalität. ObservableHQ eignen sich ideal zur Visualisierung und Kommunikation von Forschungsdaten. Aus diesem Grund nutzen führende Medienhäuser diese Komponenten, neben der New York Times auch Financial Times Graphics, die in kürzester Zeit mehr als 30 000 Infographiken publizierten. Über die API der NFDI4SD lassen sich Forschungsdaten direkt in die ObservableHQ importieren und visualisieren, ohne zwischengeschaltete deployments und Serverstrukturen.

[Infographics Financial Times](https://www.ft.com/graphics)


# Beispiel Kartenprojektion


### Beispielhaft embedd. Problem: wie ist die Componente zu scalieren?

(1)
  - [Bostocks observable](https://observablehq.com/@mbostock/fullscreen-canvas)
  - [Inspector](https://github.com/observablehq/runtime/blob/master/README.md#_define)
(2) Diagramm mit "embed code" copy/paste

<style>
.fullwidth {
  width: -20vw;
  position: relative;
  left: 0%;
  right: 0%;
  margin-left: -20vw;
  margin-right: 60vw;
  animation: skew 3s infinite;
  transform: scaleX(20);
  animation-direction: alternate;
  opacity: .7;
}
@keyframes skew {
  0% {
    transform: skewX(20deg);
  }
  100% {
    transform: skewX(-20deg);
  }
}

</style>

<div class="fullwidth" id="observablehq-210902eb"></div>

<script type="module">
import {Runtime, Inspector} from "https://cdn.jsdelivr.net/npm/@observablehq/runtime@4/dist/runtime.js";
import define from "https://api.observablehq.com/@mbostock/fullscreen-canvas.js?v=3";
const inspect = Inspector.into("#observablehq-210902eb");
(new Runtime).module(define, name => name === "canvas" ? inspect() : undefined);
</script>

Zuvor ist der Code copy/paste eingefügt worden.


(3) Wie scaliert man die Komponente? es müsste eine screen.width übergeben werden, aber wie?

```js
canvas = {
  const n = 200;
  const height = Math.ceil(width * screen.height / screen.width);
  const margin = 60;
  const context = DOM.context2d(width, height);
  const particles = Array.from({length: n}, () => [Math.random() * width, Math.random() * height, 0, 0]);
  context.canvas.style.background = "#fff";
  context.strokeStyle = "red";
  while (true) {
    const delaunay = new d3.Delaunay.from(particles);
    const voronoi = delaunay.voronoi([0, 0, width, height]);
    context.save();
    context.clearRect(0, 0, width, height);
    context.beginPath();
    delaunay.renderPoints(context);
    context.fill();
    context.beginPath();
    voronoi.render(context);
    context.stroke();
    yield context.canvas;
    for (const p of particles) {
      p[0] += p[2];
      p[1] += p[3];
      if (p[0] < -margin) p[0] += width + margin * 2;
      else if (p[0] > width + margin) p[0] -= width + margin * 2;
      if (p[1] < -margin) p[1] += height + margin * 2;
      else if (p[1] > height + margin) p[1] -= height + margin * 2;
      p[2] += 0.2 * (Math.random() - 0.5) - 0.01 * p[2];
      p[3] += 0.2 * (Math.random() - 0.5) - 0.01 * p[3];
    }
  }
}
```


[Manual](https://observablehq.com/@observablehq/user-manual)

### collaborative writing

One can collaboratively write and program computational notebooks in teams [Teamwork with computational notebooks](https://observablehq.com/@observablehq/fork-share-merge?collection=@observablehq/introduction)

### embedding

ObservableHQ können schnell und ohne weitere Infrastruktur in andere Medien eingebettet werden.

[Embedding](https://observablehq.com/@mbostock/embedded-notebook)
