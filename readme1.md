==> This is the readme file for question 1 regarding two drunk men and their probabilty to meet at the jth step in n experiments.
==> For input, first line enter the number of experiments and press ENTER. In the second line, enter number of steps taken by them and press ENTER.
==> In the output, you will get a figure corresponding to the result obtained.
==> Variables:
	'n' is the number of experiments
	'm' is the number of steps
	'a[j]' has the number of meeting of both the men at the jth step
	Other variables just help in obtaining the probability
==> Explanation:
	Here, we obtain a random number from the system and check if it is greater than 0.5, then the first man moves forward. Else, he moves backward.
	Same code is applied for second man.
	Then, we check if they are on the same position, then increment a[j] by 1.
	At last, matplotlib is used to plot a scatterred figure.
	It is x/y == number of steps/probability at that step to meet.
