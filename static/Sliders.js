window.addEventListener("DOMContentLoaded",() => {
  let range0 = new NeumorphicRange({
      element: "#range0",
      tick: 2
    }),
    range1 = new NeumorphicRange({
      element: "#range1",
      tick: 2
    }),
    range2 = new NeumorphicRange({
      element: "#range2",
      tick: 2
    }),
    range3 = new NeumorphicRange({
      element:"#range3",
      tick: 2
    }),
    range4 = new NeumorphicRange({
      element:"#range4",
      tick: 2
    });
});

class NeumorphicRange {
  constructor(args) {
    this.el = document.querySelector(args.element);
    this.min = +this.el.min || 0;
    this.max = +this.el.max || 100;
    this.step = +this.el.step || 1;
    this.tick = args.tick || this.step;
    this.addTicks();
  }
  addTicks() {
    // div to contain everything
    let wrap = document.createElement("div");
    wrap.className = "range";
    this.el.parentElement.insertBefore(wrap,this.el);
    wrap.appendChild(this.el);

    // div to contain the ticks
    let ticks = document.createElement("div");
    ticks.className = "range__ticks";
    wrap.appendChild(ticks);

    // draw the ticks
    for (let t = this.min; t <= this.max; t += this.tick) {
      // zero-width span to allow proper space between each tick
      let tick = document.createElement("span");
      tick.className = "range__tick";
      ticks.appendChild(tick);

      let tickText = document.createElement("span");
      tickText.className = "range__tick-text";
      tick.appendChild(tickText);
      tickText.textContent = t;
    }
  }
}