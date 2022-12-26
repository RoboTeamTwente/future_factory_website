/**
 * Used to animate the type writing animation on the main page.
 */
var TxtType = function(el, toRotate, colors) {
        this.toRotate = toRotate;
        this.el = el;
        this.loopNum = 0;
        this.colors = colors
        this.txt = '';
        this.tick();
        this.isDeleting = false;
    };

    TxtType.prototype.tick = function() {
        var i = this.loopNum % this.toRotate.length;
        var fullTxt = this.toRotate[i];
        var color = this.colors[i];

        if (this.isDeleting) {
        this.txt = fullTxt.substring(0, this.txt.length - 1);
        } else {
        this.txt = fullTxt.substring(0, this.txt.length + 1);
        }

        this.el.innerHTML = '<span class="wrap" style="color: '+color+'">'+this.txt+'</span>';

        var that = this;
        var delta = 200 - Math.random() * 100;

        if (this.isDeleting) { delta /= 2; }

        if (!this.isDeleting && this.txt === fullTxt) {
        delta = 2000;
        this.isDeleting = true;
        } else if (this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
        }

        setTimeout(function() {
        that.tick();
        }, delta);
    };

    window.onload = function() {
        var elements = document.getElementsByClassName('typewriter');
        for (var i=0; i<elements.length; i++) {
            var toRotate = elements[i].getAttribute('data-type');
            var colors = elements[i].getAttribute('data-colors');
            if (toRotate) {
              new TxtType(elements[i], JSON.parse(toRotate), JSON.parse(colors));
            }
        }
        // INJECT CSS
        var css = document.createElement("style");
        css.type = "text/css";
        css.innerHTML = ".typewriter > .wrap { border-right: 0.08em solid rgb(71, 71, 71)}";
        document.body.appendChild(css);
    };