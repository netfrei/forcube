
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
