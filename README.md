# Test assignment for Geowox Data Engineer Internship

I implemented a working solution in Test Assignment.py.

Then I implemented an optimized solution in Test Assignment Optimized.py and added snippets of code to both Test Assignment.py and Test Assignment Optimized.py to compare the runtime and memory usage. The optimized solution was generally better in terms of runtime and roughly the same in terms of memory statistics for several trials I ran.

I built a macro in Testing.xlsm that generates 10,000 pairs of random numbers as specified in the test assignment, reverses the digits, sums the reversed digits together and then reverses the sum. The instructions don't explicitly require the integers to be positive, so I left open the possibility that the integers to be summed could be negative. I copied the 10,000 pairs of integers from column A in the 'Output As Values' tab into the file 10,000 cases.txt and used it as input to Test Assignment.py and Test Assignment Optimized.py and then compared the output of both programs to the reversed sum in Testing.xlsm.

One note on the bugs in the output the test assignment PDF: it appears the fish misaligned the input integers with the output integer: the input appears on line N but the output appears on line N-1. And there aren't positive integer N counter variables in the sample input, so I made sure to include those lines in my file 10,000 cases.txt as outlined in the assignment instructions.

Thank you for considering my candidacy!
