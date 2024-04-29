# Sierpinski envelope fractal
This is a program written in python that uses the "chaos game" method and draws a fractal, which I've named "Sierpinski envelope" because of the way it is formed at a basic level. However, by playing around with the parameters, you can find several different fractals that are closely related and transition into each other.
## Running the script
You will need python 3 installed to run the program. If you have it, go to the repository folder and run the dependency installation with this command:

```pip install -r requirements.txt```

And now you can run the script with the following command:

```python sierpinski_envelope.py```
## Setting parameters
The program allows you to specify 4 parameters on which the image depends:
|Command|Description|
|-------|-----------|
|--draw_count| Specifies the number of points to be drawn per loop. Defaults to 1000.
|--update_count| Specifies the number of drawing loops per one program loop. Defaults to 1.
|--draw_color| Sets the color of the drawing points in hex format. Defaults to #ffffffff (white).
|--background_color| Sets the background color in hex format. Defaults to #000000 (black).

Both ```--draw_count``` and ```--update_count``` affect the drawing speed in one way or another, but also implicitly affect another parameter that determines which fractal will be drawn.
Recommended constraints: ```1 <= draw_count * update_count <= 10^7```
## Explanation
On the standard settings of the program the following happens: 3 nearby vertices of the rectangle are randomly selected and a point is placed in the center of the rectangle. Then at each step one of these 3 vertices is randomly selected and a new point is placed at half the distance between it and the previous point. This happens in one drawing loop. Then the next 3 points are selected and the same thing happens to them and so on. This creates a fractal like this:

![Sierpinski envelope fractal](https://github.com/whode/sierpinski-envelope/assets/60185573/8481a4fb-d0e8-427d-9951-951f67961fb3)

There is almost no information about this fractal on the internet, but you can find references to it by the abstract name “K2 fractal”. It has complex patterns such as elements of Serpinski triangle, the infinite mirror effect and powers of 2. But the way it is constructed doesn't actually go very far from obtaining the Sierpinski triangle itself. Moreover, it incorporates this obtaining:

![The basis of the fractal](https://github.com/whode/sierpinski-envelope/assets/60185573/0badaf73-a215-46af-89ab-9b969029b762)

The algorithm is nothing more than drawing separate Sierpinski triangles, turned in different directions, with them overlapping each other.

But in my picture and by running the program yourself you can see the extra white dots. On a small update speed they may look random, but in fact they are not. You can make sure of it if you increase the update speed via ```--update_count``` command:

![A slightly different fractal](https://github.com/whode/sierpinski-envelope/assets/60185573/f8bfcdc9-c8b6-45b1-80ee-aff2b77f9e51)

It's a slightly different fractal now.
And here we come smoothly to what is perhaps of most interest. Let's see what happens when we use a small ```draw_count``` value:

![Something more interesting](https://github.com/whode/sierpinski-envelope/assets/60185573/c3429b1c-4fcf-4506-a164-d35ea18483b7)

We got a completely new fractal that is not similar to the previous one. This happens because we do point generation for every 3 selected vertices only once. Thus, the chaos game has given us something new. The new fractal resembles an hourglass shape.

Finally, we can see the process of going from one fractal to another. Here is what happens on ```draw_count``` values from 1 to 10:

![Transition from one fractal to another](https://github.com/whode/sierpinski-envelope/assets/60185573/b29ddaf2-4269-42e2-b1d0-604aa230e88e)

## Conclusion
I find it incredible that the simplest randomness-based generation rules yield such complex shapes, and if you think the same way, you might be interested in playing around with this project. Enjoy!
