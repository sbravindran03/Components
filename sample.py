buttons  = [
    {"html":'''<button>{btn1}</button>''',
     "css":'''button {
  --c:  #229091; /* the color*/
  
  box-shadow: 0 0 0 .1em inset var(--c); 
  --_g: linear-gradient(var(--c) 0 0) no-repeat;
  background: 
    var(--_g) calc(var(--_p,0%) - 100%) 0%,
    var(--_g) calc(200% - var(--_p,0%)) 0%,
    var(--_g) calc(var(--_p,0%) - 100%) 100%,
    var(--_g) calc(200% - var(--_p,0%)) 100%;
  background-size: 50.5% calc(var(--_p,0%)/2 + .5%);
  outline-offset: .1em;
  transition: background-size .4s, background-position 0s .4s;
}
button:hover {
  --_p: 100%;
  transition: background-position .4s, background-size 0s;
}
button:active {
  box-shadow: 0 0 9e9q inset #0009; 
  background-color: var(--c);
  color: #fff;
}



body {
  height: 100vh;
  margin: 0;
  display: grid;
  place-content: center;
  grid-auto-flow: column;
  gap: 40px;
  background: #F2DCA2;
}
button {
  font-family: system-ui, sans-serif;
  font-size: 3.5rem;
  cursor: pointer;
  padding: .1em .6em;
  font-weight: bold;  
  border: none;
}''',
     "js":''},{
        "html":'''<button style="--c:#E95A49">{btn1}</button>''',
        "css":'''button {
  --c:  #229091; /* the color*/
  
  box-shadow: 0 0 0 .1em inset var(--c); 
  --_g: linear-gradient(var(--c) 0 0) no-repeat;
  background: 
    var(--_g) calc(var(--_p,0%) - 100%) 0%,
    var(--_g) calc(200% - var(--_p,0%)) 0%,
    var(--_g) calc(var(--_p,0%) - 100%) 100%,
    var(--_g) calc(200% - var(--_p,0%)) 100%;
  background-size: 50.5% calc(var(--_p,0%)/2 + .5%);
  outline-offset: .1em;
  transition: background-size .4s, background-position 0s .4s;
}
button:hover {
  --_p: 100%;
  transition: background-position .4s, background-size 0s;
}
button:active {
  box-shadow: 0 0 9e9q inset #0009; 
  background-color: var(--c);
  color: #fff;
}



body {
  height: 100vh;
  margin: 0;
  display: grid;
  place-content: center;
  grid-auto-flow: column;
  gap: 40px;
  background: #F2DCA2;
}
button {
  font-family: system-ui, sans-serif;
  font-size: 3.5rem;
  cursor: pointer;
  padding: .1em .6em;
  font-weight: bold;  
  border: none;
}''',
    "js":''},{
    "html":'''<button class='glowing-btn'>{btn1}</button>''',
    "css":'''@import url("https://fonts.googleapis.com/css?family=Raleway");

:root {
  --glow-color: hsl(186 100% 69%);
}

*,
*::before,
*::after {
  box-sizing: border-box;
}

html,
body {
  height: 100%;
  width: 100%;
  overflow: hidden;
}

body {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: black;
}

.glowing-btn {
  position: relative;
  color: var(--glow-color);
  cursor: pointer;
  padding: 0.35em 1em;
  border: 0.15em solid var(--glow-color);
  border-radius: 0.45em;
  background: none;
  perspective: 2em;
  font-family: "Raleway", sans-serif;
  font-size: 2em;
  font-weight: 900;
  letter-spacing: 1em;

  -webkit-box-shadow: inset 0px 0px 0.5em 0px var(--glow-color),
    0px 0px 0.5em 0px var(--glow-color);
  -moz-box-shadow: inset 0px 0px 0.5em 0px var(--glow-color),
    0px 0px 0.5em 0px var(--glow-color);
  box-shadow: inset 0px 0px 0.5em 0px var(--glow-color),
    0px 0px 0.5em 0px var(--glow-color);
  animation: border-flicker 2s linear infinite;
}

.glowing-txt {
  float: left;
  margin-right: -0.8em;
  -webkit-text-shadow: 0 0 0.125em hsl(0 0% 100% / 0.3),
    0 0 0.45em var(--glow-color);
  -moz-text-shadow: 0 0 0.125em hsl(0 0% 100% / 0.3),
    0 0 0.45em var(--glow-color);
  text-shadow: 0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.45em var(--glow-color);
  animation: text-flicker 3s linear infinite;
}

.faulty-letter {
  opacity: 0.5;
  animation: faulty-flicker 2s linear infinite;
}

.glowing-btn::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  opacity: 0.7;
  filter: blur(1em);
  transform: translateY(120%) rotateX(95deg) scale(1, 0.35);
  background: var(--glow-color);
  pointer-events: none;
}

.glowing-btn::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  opacity: 0;
  z-index: -1;
  background-color: var(--glow-color);
  box-shadow: 0 0 2em 0.2em var(--glow-color);
  transition: opacity 100ms linear;
}

.glowing-btn:hover {
  color: rgba(0, 0, 0, 0.8);
  text-shadow: none;
  animation: none;
}

.glowing-btn:hover .glowing-txt {
  animation: none;
}

.glowing-btn:hover .faulty-letter {
  animation: none;
  text-shadow: none;
  opacity: 1;
}

.glowing-btn:hover:before {
  filter: blur(1.5em);
  opacity: 1;
}

.glowing-btn:hover:after {
  opacity: 1;
}

@keyframes faulty-flicker {
  0% {
    opacity: 0.1;
  }
  2% {
    opacity: 0.1;
  }
  4% {
    opacity: 0.5;
  }
  19% {
    opacity: 0.5;
  }
  21% {
    opacity: 0.1;
  }
  23% {
    opacity: 1;
  }
  80% {
    opacity: 0.5;
  }
  83% {
    opacity: 0.4;
  }

  87% {
    opacity: 1;
  }
}

@keyframes text-flicker {
  0% {
    opacity: 0.1;
  }

  2% {
    opacity: 1;
  }

  8% {
    opacity: 0.1;
  }

  9% {
    opacity: 1;
  }

  12% {
    opacity: 0.1;
  }
  20% {
    opacity: 1;
  }
  25% {
    opacity: 0.3;
  }
  30% {
    opacity: 1;
  }

  70% {
    opacity: 0.7;
  }
  72% {
    opacity: 0.2;
  }

  77% {
    opacity: 0.9;
  }
  100% {
    opacity: 0.9;
  }
}

@keyframes border-flicker {
  0% {
    opacity: 0.1;
  }
  2% {
    opacity: 1;
  }
  4% {
    opacity: 0.1;
  }

  8% {
    opacity: 1;
  }
  70% {
    opacity: 0.7;
  }
  100% {
    opacity: 1;
  }
}

@media only screen and (max-width: 600px) {
  .glowing-btn{
    font-size: 1em;
  }
}
''',
    "js":'' },{
        "html":'''@import "https://unpkg.com/open-props";

* {
  box-sizing: border-box;
}

body {
  background: var(--gradient-1);
  display: grid;
  place-items: center;
  min-height: 100vh;
}

button {
  font-family: var(--font-sans);
  font-weight: var(--font-weight-6);
  font-size: var(--font-size-5);
  color: var(--gray-8);
  background: var(--gray-0);
  border: 0;
  padding: var(--size-4) var(--size-8);
  transform: translateY(calc(var(--y, 0) * 1%)) scale(var(--scale));
  transition: transform 0.1s;
  position: relative;
}

button:hover {
  --y: -10;
  --scale: 1.1;
  --border-scale: 1;
}

button:active {
  --y: 5%;
  --scale: 0.9;
  --border-scale: 0.9, 0.8;
}

button:before {
  content: "";
  position: absolute;
  inset: calc(var(--size-3) * -1);
  border: var(--size-2) solid var(--gray-0);
  transform: scale(var(--border-scale, 0));
  transition: transform 0.125s;
  
  --angle-one: 105deg;
  --angle-two: 290deg;
  --spread-one: 30deg;
  --spread-two: 40deg;
  --start-one: calc(var(--angle-one) - (var(--spread-one) * 0.5));
  --start-two: calc(var(--angle-two) - (var(--spread-two) * 0.5));
  --end-one: calc(var(--angle-one) + (var(--spread-one) * 0.5));
  --end-two: calc(var(--angle-two) + (var(--spread-two) * 0.5));
  
  mask: conic-gradient(
    transparent 0 var(--start-one),
    white var(--start-one) var(--end-one),
    transparent var(--end-one) var(--start-two),
    white var(--start-two) var(--end-two),
    transparent var(--end-two)
  );
  
  z-index: -1;
}''',
    "js":'',
    },{
    "html":'''<div class={btn1}></div>''',
    "css":''':root {
	--size: 1vmin;
	--bgr-color: #e91e63;
	--ico-color: #4e0a21;
}

body {
	height: 100vh;
	overflow: hidden;
	margin: 0;
	padding: 0;
	display: flex;
	align-items: center;
	justify-content: center;
	background-color: #000000;
	background-image: linear-gradient(147deg, #000000 0%, #2c3e50 74%);
}

.icon-delete {
	width: calc(var(--size) * 20);
	height: calc(var(--size) * 20);
	border: 0;
	border-radius: calc(var(--size) * 1);
	outline: none;
	background: #a4c75a;
	background: var(--bgr-color);
	cursor: pointer;
	position: relative;
}

.icon-delete:before {
	background: 
		linear-gradient(0deg, var(--ico-color) 0 calc(var(--size) * 1), #fff0 0 calc( 100% - calc(var(--size) * 1)), var(--ico-color) 0 100%), 
		linear-gradient(90deg, var(--ico-color) 0 calc(var(--size) * 1), #fff0 0 calc( 100% - calc(var(--size) * 6)), var(--ico-color) 0 100%), 
		linear-gradient(45deg, var(--ico-color) 0 calc(var(--size) * 2.35), #fff0 0 100%);
	width: calc(var(--size) * 12);
	height: calc(var(--size) * 6);
	position: absolute;
	content: "";
	border-radius: calc(var(--size) * 1);
	transform: rotate(-45deg);
	top: calc(var(--size) * 6.5);
	left: calc(var(--size) * 2);
	transition: all 0.5s ease 0s;
}

.icon-delete:after {
	left: calc(var(--size) * 2);
	top: calc(var(--size) * 14.5);
	width: calc(var(--size) * 16);
	height: calc(var(--size) * 0.9);
	position: absolute;
	background: 
		linear-gradient(90deg, var(--bgr-color) 0 45%, #fff0 0 50%, var(--ico-color) 0 100%), 
		repeating-linear-gradient(90deg, var(--bgr-color) 0 3%, var(--ico-color) 0 6%);
	background-position: 86% 0;
	background-size: 200%;
	transition: all 0.5s ease 0s;
	border-radius: 1px;
	content: "";
	border-top: calc(var(--size) * 1) solid var(--bgr-color);
	border-bottom: calc(var(--size) * 1) solid var(--bgr-color);
	content: "ERASE !";
	font-family: Arial, Helvetica, serif;
	font-size: calc(var(--size) * 4);
	text-align: center;
	line-height: calc(var(--size) * 16);
	color: var(--bgr-color);
	text-shadow: -1px -1px 1px var(--ico-color), 1px 1px 1px var(--ico-color);
}

.icon-delete:hover {
	--ico-color: #18222c;
	transition: all 0.5s ease 0s;
}

.icon-delete:hover:before {
	left: calc(var(--size) * 4);
}

.icon-delete:hover:after {
	background-position: 73% 0;
	content: "ERASE?";
}

.icon-delete:active {
	--ico-color: #fff;
	transition: all 0.5s ease 0s;
}

.icon-delete:active:before {
	left: calc(var(--size) * 6);
}

.icon-delete:active:after {
	background-position: 60% 0;
	content: "ERASED";
	color: #fff;
}''',
    "js":''},{
    "html":'''<button onClick={console.log("click")} >
  Click me
  <svg width="79" height="46" viewBox="0 0 79 46" fill="none" xmlns="http://www.w3.org/2000/svg">
  <g filter="url(#filter0_f_618_1123)">
    <path d="M42.9 2H76.5L34.5 44H2L42.9 2Z" fill="url(#paint0_linear_618_1123)"/>
  </g>
  <defs>
    <filter id="filter0_f_618_1123" x="0" y="0" width="78.5" height="46" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
      <feGaussianBlur stdDeviation="1" result="effect1_foregroundBlur_618_1123"/>
    </filter>
    <linearGradient id="paint0_linear_618_1123" x1="76.5" y1="2.00002" x2="34.5" y2="44" gradientUnits="userSpaceOnUse">
      <stop stop-color="white" stop-opacity="0.6"/>
      <stop offset="1" stop-color="white" stop-opacity="0.05"/>
    </linearGradient>
  </defs>
</svg>
</button>''',
    "css":'''@import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap');

body {
	background: #170F1E;
	display: grid;
	height: 100vh;
	place-items: center;
	-webkit-font-smoothing: antialiased;
	width: 100vw;
}

button {
  animation: 1.5s ease infinite alternate running shimmer;
  background: linear-gradient(90deg, #FFE27D 0%, #64E3FF 30%, #9192FF 85%);
  background-size: 200% 100%;
  border: none;
	border-radius: 6px;
  box-shadow: -2px -2px 10px rgba(255, 227, 126, 0.5), 2px 2px 10px rgba(144, 148, 255, 0.5);
  color: #170F1E;
  cursor: pointer;
	font-family: 'Inter', sans-serif;
  font-size: 16px;
	font-weight: 670;
  line-height: 24px;
  overflow: hidden;
  padding: 12px 24px;
  position: relative;
  text-decoration: none;
  transition: 0.2s;
  
  svg {
    left: -20px;
    opacity: 0.5;
    position: absolute;
    top: -2px;
    transition: 0.5s cubic-bezier(.5,-0.5,.5,1.5);
  }
  
  &:hover svg {
    opacity: 0.8;
    transform: translateX(50px) scale(1.5);
  }
  
  &:hover {
    transform: rotate(-3deg);
  }
  
  &:active {
    transform: scale(0.95) rotate(-3deg);
  }

}

@keyframes shimmer {
  to {
    background-size: 100% 100%;
    box-shadow: -2px -2px 6px rgba(255, 227, 126, 0.5), 2px 2px 6px rgba(144, 148, 255, 0.5);
  }
}''',
    "js":''''''
    },{
    "html":'''<div class="container">
      <label>
        <input type="checkbox" class="play-btn" />
        <div class="play-icon"></div>
        <div class="pause-icon"></div>
      </label>
    </div>''',
    "css":'''  *,
      :before,
      :after {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }

      body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background: #000;
      }

      .container {
        width: 120px;
        height: 120px;
        position: relative;
        border-radius: 50%;
      }

      .play-btn {
        position: absolute;
        appearance: none;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: conic-gradient(#ff6347, #ff6347);
        cursor: pointer;
        outline: none;
      }

      .play-btn::before {
        content: "";
        position: absolute;
        width: 93%;
        height: 93%;
        background-color: #000;
        border-radius: 50%;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
      }

      .play-btn:checked {
        animation: borderAnimate 700ms ease-in-out 1;
        animation-fill-mode: forwards;
      }

      @keyframes borderAnimate {
        0% {
          transform: rotate(0);
          background: conic-gradient(#ff6347, transparent 20%);
        }

        80% {
          background: conic-gradient(#ff6347, transparent 90%);
        }

        100% {
          transform: rotate(360deg);
          background: conic-gradient(#ff6347, #ff6347);
        }
      }

      .play-icon {
        position: absolute;
        width: 40px;
        height: 40px;
        left: 60%;
        top: 50%;
        background-color: #ff6347;
        transform: translate(-60%, -50%) rotate(90deg);
        clip-path: polygon(50% 15%, 0% 100%, 100% 100%);
        transition: all 400ms ease-in-out;
        cursor: pointer;
      }

      .play-btn:checked + .play-icon {
        clip-path: polygon(0 100%, 0% 100%, 100% 100%);
      }

      .pause-icon {
        position: absolute;
        width: 40px;
        height: 40px;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        cursor: pointer;
      }

      .pause-icon::before {
        content: "";
        position: absolute;
        width: 0%;
        height: 100%;
        background-color: #ff6347;
        left: 0;
      }

      .pause-icon::after {
        content: "";
        position: absolute;
        width: 0;
        height: 100%;
        background-color: #ff6347;
        right: 0;
      }

      .play-btn:checked ~ .pause-icon::before {
        animation: reveal 300ms ease-in-out 350ms 1;
        animation-fill-mode: forwards;
      }

      .play-btn:checked ~ .pause-icon::after {
        animation: reveal 300ms ease-in-out 600ms 1;
        animation-fill-mode: forwards;
      }

      @keyframes reveal {
        0% {
          width: 0;
        }

        100% {
          width: 35%;
        }
      }''',
      "js":''
    },{
      "html":'''<input type="checkbox" id="cb-pause">
<label class="playButton" for="cb-pause">
  <div class="icon pause">
    <div></div><div></div>
    <div></div><div></div>
  </div>
</label>

<input type="checkbox" id="cb-stop">
<label class="playButton" for="cb-stop">
  <div class="icon stop">
    <div></div><div></div>
  </div>
</label>
''',
    "css":'''*, *::before, *::after {
  padding: 0;
  margin: 0 auto;
  box-sizing: border-box;
}

body {
  background-color: #000;
  color: #fff;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

input[type="checkbox"] {
  appearance: none;
  position: fixed;
  top: -100%; left: -100%;

  &:checked + .playButton {
    --ry: 90deg;
    --clr: maroon;
  }
}

.playButton {
  position: relative;
  width: 160px; height: 80px;
  border-radius: 10% / 20%;
  background-color: var(--clr, red);
  perspective: 320px;
  cursor: pointer;
  margin: 1em auto;
  transition: background-color 0.5s;
}

.icon {
  position: absolute;
  top: 50%; left: 50%;
  transform: rotateY(var(--ry, 0deg));
  transform-style: preserve-3d;
  transition: transform 0.5s;

  &.pause > div {
    position: absolute;
    background-color: #fff;

    @for $i from 0 to 2 {
      &:nth-child(#{$i + 1}) {
        top: -15px; left: -9px;
        width: 30px; height: 30px;
        clip-path: polygon(0 0, 100% 50%, 0 100%);
        transform: translateZ(#{-5 + $i * 20}px);
        background-image:
          linear-gradient(334deg, #0005 12px, #0000 19px),
          linear-gradient(206deg, #0005 12px, #0000 19px),
          linear-gradient(90deg,  #0005, #0000 7px);
      }

      &:nth-child(#{$i + 3}) {
        top: -15px; left: -9px;
        width: 10px; height: 30px;
        transform-origin: left;
        transform: translateZ(#{-15 + $i * 20}px) rotateY(-90deg);
        box-shadow: 0 0 5px #0005 inset;
      }
    }
  }

  &.stop > div {
    position: absolute;
    background-color: #fff;

    &:nth-child(1) {
      top: -15px; left: -9px;
      width: 30px; height: 30px;
      clip-path: polygon(0 0, 100% 50%, 0 100%);
      transform: translateZ(15px);
      background-image:
        linear-gradient(334deg, #0005 12px, #0000 19px),
        linear-gradient(206deg, #0005 12px, #0000 19px),
        linear-gradient(90deg,  #0005, #0000 7px);
    }

    &:nth-child(2) {
      top: -15px; left: -9px;
      width: 30px; height: 30px;
      transform-origin: left;
      transform: translateZ(-15px) rotateY(-90deg);
      box-shadow: 0 0 10px #000a inset;
    }
  }
}''',
    "js":''
    },{
    "html":'''.grid
	a(href="#0").btn Hover me
	a(href="#0").btn.btn--outline Hover me
	a(href="#0").card This is a card''',
    "css":''':root {
	--border-w: 0.25rem;
	--border-r: 1em;
	--angle: 130deg;
}

$color: #6138D8; // so that we can transform it with SCSS
$altColor: saturate(lighten(adjust-hue($color, 25deg), 5), 10);

@mixin neon-outline($c: $color) {
	position: relative;
	
	border-radius: var(--border-r);
	border: var(--border-w) solid $color;

	&:before,
	&:after {
		content: '';
		border-radius: inherit;
		position: absolute;	
		transition: opacity 0.5s, filter 0.5s;
	}
	
	&:before {
		inset: calc(var(--border-w) * -1);
		box-shadow:
			inset 0.0333em 0.0333em 0.2em lighten(adjust-hue($color, 30deg), 15),
			inset -0.0666em -0.0666em 0.15em darken($color, 25),
			inset 0.025em 0.025em 0.1em white,
		;
		mix-blend-mode: hard-light;
	}
	
	&:after {
		inset: 0;
		border-radius: calc(var(--border-r) - var(--border-w));
		box-shadow:
			-0.05em -0.05em 0.05em darken($c, 25),
			0.05em 0.05em 0.05em lighten(adjust-hue($c, 30deg), 15),
		;
		mix-blend-mode: hard-light;
	}
}

body {
	display: flex;
	min-height: 100vh;
	justify-content: center;
	align-items: center;
		
	font-size: 2rem;
	font-family: "objektiv-mk2", sans-serif;
	
	background: rgba(saturate(adjust-hue($color, -20deg), 10), 0.125);
	
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
}

.grid {
	display: inline-grid;
	grid-template-columns: 1fr 30vw;
	grid-template-rows: repeat(2, 1fr);
	gap: 1em;
}

.btn {
	text-decoration: none;
	font-weight: bold;
	line-height: 1;
	
	grid-column: 1;
	
	backface-visibility: hidden;
	
	padding: 0.725em 1.25em 0.8em;
	
	box-shadow:
		0 0.05em 0.5em rgba($color, 0.25),
		0 0.15em 0.3em -0.1em rgba(darken($altColor, 10), 0.25),
		inset 0 0 0.05em 0.0333em rgba($altColor, 0.25),
		inset 0 0.1em 0.2em 0em rgba($altColor, 0.25),
		inset 0 0.1em 0.45em rgba($color, 0.25),
	;
	
	background: linear-gradient(
		var(--angle),
		$color 25%,
		rgba($altColor, 0.9) 40%,
		rgba($altColor, 0.95) 65%,
		$color 85%,
	) no-repeat -1px 50% / 300% calc(100% + 2px);
	color: white;
	
	transition:
		color 0.3s,
		background 0.3s,
		transform 0.75s,
		background-position 0.5s,
		box-shadow 0.5s,
	;
	will-change: background-position, transform, box-shadow;
	
	@include neon-outline;
	
	&:after {
		content: none;
	}
	
	&:hover,
	&:focus {
		// transform: scale3d(1.025, 1.025, 1) translate3d(0, -2px, 0);
		background-position: calc(100% + 1px) 50%;
		
		box-shadow:
			0 0.15em 1.5em rgba(lighten(saturate(adjust-hue($color, 10deg), 10), 5), 0.666),
			0 0.15em 0.333em -0.1em rgba(darken($altColor, 10), 0.666),
			inset 0 0.15em 0.3em -0.1em rgba($altColor, 0),
			inset 0 0 0.05em 0.0333em rgba($altColor, 0.25),
			inset 0 0.1em 0.666em rgba($color, 0.333),
		;
	}
	
	&--outline {
		color: darken($color, 33.3);
		background: linear-gradient(
			var(--angle),
			rgba($color, 0) 33.3%,
			$color 66.6%,
			$color 85%,
			rgba($altColor, 0.9),
		) no-repeat -1px 50% / 300% calc(100% + 2px);
		
		&:after {
			content: '';
		}
		
		&:hover,
		&:focus {
			color: white;
			
			&:after {
				opacity: 0;
			}
		}
	}
}

.card {
	$altColor: saturate(adjust-hue($color, 40deg), 20);
	grid-area: 1 / 2 / 3;
	
	font-size: 0.8em;
	font-weight: bold;
	text-transform: uppercase;
	color: $color;
	text-decoration: none;
	letter-spacing: 0.05em;
	
	display: flex;
	align-items: center;
	justify-content: center;
	
	@include neon-outline;
	
	&:before,
	&:after {
		opacity: 0.25;
		filter: saturate(0) invert(1);
	}
	
	border-color: rgba(desaturate($color, 20), 0.1);
	box-shadow:
		0 0.1em 2.25em -0.5em rgba($altColor, 0),
		0 0.333em .5em -0.25em rgba($altColor, 0),
	; 
	
	transition: 0.5s;
	transition-property: border-color, background, box-shadow, color;
	
	&:hover,
	&:focus {
		color: darken($color, 20);
		border-color: $color;
		background: rgba($altColor, 0.5);
		box-shadow:
			0 0.1em 2.25em -0.5em rgba($altColor, 1),
			0 0.25em 0.25em -0.15em rgba($altColor, 0.333),
		; 
		
		&:before,
		&:after {
			opacity: 1;
			filter: saturate(1) invert(0);
		}
	}
}




























@import url(https://use.typekit.net/ztx1wfr.css);''',
    "js":''''''
    },{
    "html":'''<main>
  <article>

    <button>
      Enter ballot
    </button>
  </article>

</main>''',
    "css":''':root {
  --black: rgb(0 0 0);
  --dark-navy: rgb(26 28 60);
  --navy: rgb(45 54 77);
  --navy-bg: rgb(86 94 115);
  --gray: rgb(167 167 167);
  --white: rgb(255 255 255);
  --yellow: rgb(255 181 0);
  --light-yellow: rgb(255 209 98);
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

main {
  background-image: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.95),
    rgba(26, 28, 60, 0.95) 100%
  );
  display: grid;
  height: 100vh;
  width: 100vw;
  place-items: center;
}

button {
  background-image: url("data:image/svg+xml,%3Csvg viewBox='-39 1 511 511.99897' xmlns='http://www.w3.org/2000/svg' fill='rgb(26,28,60)'%3E%3Cdefs/%3E%3Cpath d='M396.367188 369.371094c-20.109376-12.152344-48.074219-22.054688-80.933594-28.683594-22.523438-29.804688-58.25-49.101562-98.402344-49.101562s-75.878906 19.300781-98.402344 49.101562c-32.820312 6.625-60.757812 16.507812-80.863281 28.644531-2.296875 1.386719-4.445313 2.78125-6.476563 4.183594V210.027344l154.289063-78.820313c5.148437-2.628906 8.390625-7.925781 8.390625-13.707031s-3.242188-11.078125-8.390625-13.707031L31.289062 24.972656v-9.578125C31.289062 6.890625 24.394531 0 15.894531 0S.5 6.890625.5 15.394531v405c0 .097657.011719.191407.015625.289063C.507812 421.023438.5 421.359375.5 421.691406c0 26.851563 24.519531 50.773438 69.046875 67.355469C109.285156 503.847656 161.664062 512 217.03125 512c31.320312 0 64.132812-2.898438 92.390625-8.164062 77.734375-14.472657 124.144531-45.183594 124.144531-82.144532 0-13.613281-6.453125-33.738281-37.199218-52.320312zm6.410156 52.320312c0 3.476563-1.605469 7.300782-4.746094 11.277344-13.730469-11.992188-33.550781-22.308594-58.3125-30.285156-.878906-8.914063-2.714844-17.550782-5.398438-25.8125 45.046876 12.789062 68.457032 31.183594 68.457032 44.820312zm-64.121094 13.167969c13.710938 5.011719 25.171875 10.796875 33.773438 17.015625-11.59375 5.933594-26.414063 11.558594-44.304688 16.261719 5.058594-10.535157 8.621094-21.746094 10.53125-33.277344zM99.746094 376.867188c-2.6875 8.265624-4.523438 16.910156-5.402344 25.832031-24.761719 7.980469-44.699219 18.347656-58.421875 30.375-3.019531-3.890625-4.632813-7.734375-4.632813-11.382813-.003906-13.644531 23.40625-32.035156 68.457032-44.824218zM144.738281 117.5L31.289062 175.457031V59.542969zM61.496094 452.019531c8.648437-6.277343 20.171875-12.105469 33.878906-17.128906 1.90625 11.59375 5.457031 22.804687 10.535156 33.332031-9.0625-2.371094-17.632812-5.050781-25.617187-8.023437-6.894531-2.570313-13.179688-5.320313-18.796875-8.179688zm86.757812 24.554688c-15.300781-17.03125-23.726562-38.859375-23.726562-61.695313 0-51.007812 41.496094-92.503906 92.503906-92.503906s92.503906 41.496094 92.503906 92.503906c0 21.027344-7.304687 41.636719-20.570312 58.035156-.859375 1.0625-1.539063 2.210938-2.070313 3.402344-22.210937 3.140625-46.835937 4.898438-69.863281 4.898438-23.90625 0-47.125-1.59375-68.777344-4.640625zm0 0'/%3E%3Cpath d='M254.625 413.472656c-.558594-.042968-1.085938-.242187-1.535156-.574218-.394532-.296876-.707032-.6875-.910156-1.132813-3.507813-7.746094-12.628907-11.183594-20.375-7.675781-7.742188 3.507812-11.179688 12.628906-7.671876 20.375 2.335938 5.160156 5.96875 9.683594 10.503907 13.078125 5.164062 3.867187 11.292969 6.160156 17.730469 6.632812.382812.027344.765624.042969 1.144531.042969 7.988281 0 14.738281-6.171875 15.335937-14.265625.625-8.480469-5.742187-15.855469-14.222656-16.480469zm0 0M203.050781 376.625c-.558593-.039062-1.089843-.238281-1.53125-.570312-.398437-.296876-.710937-.6875-.914062-1.132813-3.507813-7.746094-12.625-11.183594-20.375-7.675781-7.742188 3.503906-11.179688 12.625-7.671875 20.371094 2.335937 5.160156 5.964844 9.683593 10.503906 13.082031 5.164062 3.867187 11.296875 6.160156 17.726562 6.632812.386719.027344.765626.042969 1.148438.042969 7.988281 0 14.738281-6.171875 15.335938-14.265625.625-8.480469-5.746094-15.859375-14.222657-16.484375zm0 0M255.039062 358.859375c-.558593-.039063-1.089843-.238281-1.535156-.574219-.394531-.292968-.707031-.6875-.910156-1.132812-3.507812-7.746094-12.628906-11.179688-20.375-7.675782-7.742188 3.507813-11.179688 12.628907-7.671875 20.375 2.335937 5.160157 5.96875 9.683594 10.503906 13.078126 5.164063 3.867187 11.292969 6.160156 17.726563 6.632812.386718.027344.765625.042969 1.144531.042969 7.988281 0 14.742187-6.171875 15.335937-14.265625.625-8.480469-5.742187-15.855469-14.21875-16.480469zm0 0'/%3E%3C/svg%3E"),
    url("data:image/svg+xml,%3Csvg viewBox='0 0 609.629 609.629' xmlns='http://www.w3.org/2000/svg' fill='rgb(26,28,60)' %3E%3Cdefs/%3E%3Cg%3E%3Cg%3E%3Cg%3E%3Cpath d='M579.142 419.214V354.96c.034-9.059-3.988-17.659-10.963-23.44l-47.967-40.042c-5.481-4.551-12.383-7.039-19.508-7.031h-5.69l-54.185-162.566h16.389c16.834 0 30.481-13.647 30.481-30.481s-13.647-30.481-30.481-30.481H101.604c-22.446 0-40.642 18.196-40.642 40.642 0 11.223 9.098 20.321 20.321 20.321h10.16v81.283h-20.32c-16.834 0-30.481 13.647-30.481 30.481v83.153c-12.135 4.29-20.267 15.741-20.321 28.612v12.03C8.186 361.729.053 373.18 0 386.051v60.962c0 16.834 13.647 30.481 30.481 30.481 0 39.28 31.843 71.123 71.123 71.123s71.123-31.843 71.123-71.123h294.651c-.041 33.771 23.671 62.914 56.744 69.741s66.388-10.545 79.722-41.571 3.011-67.152-24.702-86.45zm-104.52-131.719c-9.312 4.468-15.72 13.356-17.019 23.603l-82.543-82.533 18.218-18.218c3.85-3.987 3.795-10.324-.124-14.243s-10.256-3.974-14.243-.124l-50.802 50.802c-2.641 2.551-3.701 6.329-2.771 9.881s3.704 6.327 7.256 7.256c3.552.93 7.33-.129 9.881-2.771l18.218-18.218 96.524 96.524v46.595c0 11.223-9.098 20.321-20.321 20.321h-81.283c-11.223 0-20.321-9.098-20.321-20.321v-60.962c0-22.446-18.196-40.642-40.642-40.642h-81.283c-5.611 0-10.16-4.549-10.16-10.16v-60.962c0-16.834-13.647-30.481-30.481-30.481h-20.321V121.88H419.42zm-261.254 17.273h81.283c11.223 0 20.321 9.098 20.321 20.321v18.492l-162.566-27.098V203.164h20.321c5.611 0 10.16 4.549 10.16 10.16v60.962c0 16.835 13.647 30.482 30.481 30.482zM81.283 101.56c0-11.223 9.098-20.321 20.321-20.321h355.613c5.611 0 10.16 4.549 10.16 10.16s-4.549 10.16-10.16 10.16H81.283zm50.802 20.321v193.047h-20.321V121.881zM60.962 233.645c0-5.611 4.549-10.16 10.16-10.16h20.321v20.321H60.962zm0 30.481h30.481v50.802H60.962zm-20.32 81.283c0-5.611 4.549-10.16 10.16-10.16h90.6l173.57 28.927v21.875c.042 7.156 1.992 14.17 5.649 20.321H202.395c-14.788-.024-28.494-7.757-36.161-20.402-5.531-9.3-13.411-16.982-22.851-22.272-9.395-5.322-20.008-8.122-30.806-8.128H40.642zm60.962 182.887c-28.057 0-50.802-22.745-50.802-50.802s22.745-50.802 50.802-50.802 50.802 22.745 50.802 50.802c-.034 28.043-22.759 50.768-50.802 50.802zm368.822-71.123H169.678c-9.078-30.003-36.729-50.524-68.075-50.524s-58.996 20.522-68.075 50.524H30.48c-5.611 0-10.16-4.549-10.16-10.16v-60.962c0-5.611 4.549-10.16 10.16-10.16h82.096c7.293.009 14.46 1.899 20.808 5.487 6.359 3.556 11.668 8.725 15.393 14.987 11.35 18.778 31.675 30.274 53.616 30.329h234.502c22.446 0 40.642-18.196 40.642-40.642v-71.123c0-5.611 4.549-10.16 10.16-10.16h13.005c2.367 0 4.66.819 6.492 2.317l48.008 40.073c2.326 1.918 3.656 4.788 3.617 7.803v54.46c-18.055-5.412-37.521-3.419-54.104 5.539-16.582 8.957-28.919 24.145-34.289 42.212zm68.074 71.123c-28.057 0-50.802-22.745-50.802-50.802s22.745-50.802 50.802-50.802 50.802 22.745 50.802 50.802c-.034 28.043-22.759 50.768-50.802 50.802z'/%3E%3Cpath d='M538.5 447.013c-16.834 0-30.481 13.647-30.481 30.481s13.647 30.481 30.481 30.481 30.481-13.647 30.481-30.481-13.647-30.481-30.481-30.481zm0 40.641c-5.611 0-10.16-4.549-10.16-10.16s4.549-10.16 10.16-10.16 10.16 4.549 10.16 10.16-4.549 10.16-10.16 10.16zM101.604 447.013c-16.834 0-30.481 13.647-30.481 30.481s13.647 30.481 30.481 30.481 30.481-13.647 30.481-30.481-13.647-30.481-30.481-30.481zm0 40.641c-5.611 0-10.16-4.549-10.16-10.16s4.549-10.16 10.16-10.16 10.16 4.549 10.16 10.16-4.549 10.16-10.16 10.16z'/%3E%3C/g%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: calc(0% - 100px), calc(100% - 12px);
  background-color: var(--light-yellow);
  color: var(--dark-navy);
  cursor: pointer;
  display: block;
  position: relative;
  border: 2px solid var(--light-yellow);
  font-size: 14px;
  text-transform: uppercase;
  font-weight: 700;
  padding: 12px 24px 12px 12px;
  width: 250px;
  text-align: center;
  overflow: hidden;
  letter-spacing: 0.08em;
  text-shadow: 0 0 1px rgb(0 0 0 / 20%), 0 1px 0 rgb(0 0 0 / 20%);
  white-space: nowrap;
  transition: background-position 2s ease;

  &:hover {
    background-position: calc(25% - 30px), calc(100% + 100px);
  }
}
'''
    }


]