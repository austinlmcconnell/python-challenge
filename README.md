# python-challenge

**NOTE: FINAL homework files are located in the newest "python-challenge" folder**
PyBank:
Resources Used:
  1. AskBCS suggested I use "os.path.abspath(os.path.join(...))" to open the CSV file, as I was repeatedly running into a "file not found" issue.
  2. I was running into an error when trying to sum up total profit values from the CSV file, and AskBCS helped identify the issue (I had two separate for loops running instead of one).
  3. I referenced the following link from StackOverflow for help on creating a new line for each print statement in my text file. The result was utitlizing "\n": https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time

Code Breakdown:
  Before I started to loop through the CSV file, I went ahead and defined the first month's totals as variables (total_months = 1, total_profit = 1088983, previous_month = 1088983). I did this because we didn't have any data on the month prior to the initial month in the data set, and since we are trying to calculate the change in profits from month-to-month I wanted to be sure the first month returned change values of "0." I tend to think there are more automated ways to do this, but I was running into issues when trying to start the variables as zero so I went this route.
  While looping through the data, I created two new lists that hold the dates and change in profits from month-to-month. The average change figure that I calculated took the sum of these monthly change totals and divided it by the length of the list. The greatest increase/decrease figures were calculated by taking the max/min of the monthly change list and matching it with the index of the dates list.
  I finished the code out by printing all print statements to a text file using "f.write"

PyPoll:
Resources Used:
  1. The data was not showing up in my CSV file, thus causing errors when trying to run the code. AskBCS suggested I delete and redownload the CSV file, which solved the issue.

Code Breakdown:
  In this for loop, I appended the candidate's name to a separate candidates list every time they appeared. 
  I then created a smaller candidates list designed to list every candidate who received a vote a single time. This condensed list would be helpful if we were unsure of who exactly received votes.
  After identifying the three candidates who received votes, I created variables for each candidate's name, total number of votes, and percent of the total vote they received. The total vote count was retrieved by counting the number of occurrences in the candidates list based on the index number found in the small candidates list. The percent figure was simply calculated by taking each candidates total vote count and dividing it by the length of the candidates list (and then multiplied by 100).
  Lastly, I created a winning list containing the total vote counts for the three candidates. By taking the max of this list, we're able to find which total was the winning amount. I think created an if statement to print the winner based on whose count matched the winning total.
