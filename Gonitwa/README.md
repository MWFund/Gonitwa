### To do

1 graficznie dopasowanie do : Skoczek

2 dodanie ruchu wszystkich figur

3 zmiana szybkości poruszania się planszy np 1-10, obecna to jest 10

4 hosting online

5 przerobić na Astro


10 dodać tryb multi: gra 2 i więcej osób, każda się rusza i może zbijac inne


# Gonitwa/Pursuit

This is the game I created for chess classes

### Concept

The idea was to turn the learning chess pieces movement into fun mini game, making it as a mix of action gamewith strategy game.
For once, I started with the graphical concept, the perspective and the scrolling and tried to make some game out of it.
The result is a little weird, the 'action' part and the 'puzzle' part don't blend so well, but I kinda like it anyway.

### Rules




### Code

I lost a lot of time drawing the checkerboard. My first version used shaky code to compute the projections from checkerboard space to screen space.
While it looked good enough, it was impossible to reverse the projection for computing mouse input, so I had to do it again with a more mathematical approach.

For the pieces, I decided to use SVG in order to have them scale nicely. It was my first contact with SVG and it was quite interesting.
I probably would have saved some time by writing the SVG elements directly in the HTML instead of using JS to generate everything.

As for the rest of the code, it is a little messy, as usual. I should probably have taken some time to write things more cleanly, especially the intro & dialogs part.


### External code

I relied on Mr Doob stats.js lib during debug:
https://github.com/mrdoob/stats.js/

And on jsfx for the sound:
https://github.com/mneubrand/jsfxr

Using code provided by Jack Rugile for the integration of jsfxr:
http://codepen.io/jackrugile/blog/arcade-audio-for-js13k-games
