==> This is the readme file for question 2 regarding 'n' drunk men who start at the origin of a circle and move around in random probability and the purpose is to find the number of drunkards at the end of 'm' steps.
==> For input, first line enter the number of drunk men and press ENTER. In the second line, enter the number of steps taken by them.
==> In the output, you will get a scattered graph corresponding to the experiments.
==> Variables:
	'men' is the number of drunk men
	'steps' is the number of steps taken by them
	'a[j]' is the number of men at radius j
	'signx' and 'signy' show the direction of moving
	'x' and 'y' have the magnitude of movement, assuming the length of each step to be 1 unit.
	'xtot' and 'ytot' will have the magnitude along x and y axis respectively.
==> Explanation:
	We first obtain a random number, which will be x.
	We will get y using pythagoras theorem.
	Other two random numbers are obtained to get the forward or backward direction of both x and y axis.
	At the end of all the steps, we find the radius at which it is located and index it in array.
	The graph has x/y == Radius/Number of drunkmen at radius r.
