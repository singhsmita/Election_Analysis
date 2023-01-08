# Election_Analysis

## Project Overview

A Colorado Board of Elections employee requested help in completing an election audit of a recent local congressional election. The requirement is to automate the process using Python. If this audit is done successfully with Python, the code will be used to audit not only for other congressional districts, but also senatorial districts and local elections.

### Purpose

The election commission has tasked us with reporting the following :-

total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote.

  

-   The voter turnout for each county
    
-   The percentage of votes from each county out of the total count
    
-   The county with the highest turnout
    
-   Total number of votes cast.
    
-   The Total number of votes of each candidate.
    
-   The percentage of votes for each candidate.
    

  

## Election Audit Results

I made use of the Starter_code and the CSV file provided as resources .

Using Python programming I was able to report the election outcomes as follows:-

-   How many votes were cast in this congressional election?
    

-   Total Votes: 369,711
    

![](https://lh3.googleusercontent.com/JFMDoECAwyk2FJ9DFfIAiGJEeiYx2bJtUN0MuIq-X3hn6RCAy_k_hiQpSg9zlgbEgDI0fIBTmLhdnR4k_x2QQqqCA3X7Cbnp7K5fQfXGF93pPozeN0ypzEhJT2QUg2cUlhYKPQysxrWfDcr0z_w2dAvUk9UXA2RG_nqSBCGK38do1I-kmlUwlNy42PRO)

![](https://lh4.googleusercontent.com/UygtCwEfhFkZqtN5mIlPg5IEXdgC_U54kehxp8sQOnpYhNRusIi6bvtiqQW7HMYqmbThZiDMYM7d65SGaJCC7rLns1QthW4cjMcqWNQs9nJbTFuw-P7YQDo5wPYHbNgP2mGyJ2XBZTZZtBQxBlzuB4eScvZkK7KV9KNh31MIOlwkYYFPF-ASVU4pN1ri)

Using a for loop to read each row and tally the votes and increment it by 1 each time the condition is met.

-   Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    

-   County Votes:
    
-   Jefferson: 10.5% (38,855)
    
-   Denver: 82.8% (306,055)
    
-   Arapahoe: 6.7% (24,801)
    

![](https://lh6.googleusercontent.com/B2g4YDxsb32ES9ZRzph9CRq8RBghZ5D-L8yEWbLeXi1A8dLkBtzuzDZ5gGRGFB-a-azPNiVjSOBvEn5cDYtGH3q7eIqSSWvnu9G-OB2ec8m3z1jrhbJuCt5IaUo0yfsygwgF7YnWU7mfT43Llh3g93I2qwE5XrKAEeA3bzDVb3FGPqsumtOTf9Iltdr0)

Using decision statement with a logical operator to check if the county name acquired in county list created.Initializing the county vote to zero which adds a vote to the county’s vote count as you are looping through all the rows.

![](https://lh6.googleusercontent.com/dbYa7DfB1obfuM3iF_i85LFs8OuF8RUF7g7WkseeieoeH_56K5p9dFFhXOn4-so21NztSfYkkQsXNuxLOkBP2KxAtTWGwBONURRF28C367JvuyestNyS22sZstLI4k65QyrbrIqlGBcelJhjwTjaZDbt3Q3NyJjaeNqfmb07iO5K370SLVelLmMcf-hz)

Using repetition statement to get the county from the county dictionary.Created a variable to hold the county’s votes as they are retrieved from the county votes dictionary.Calculated county vote percentage and printed it.

  

-   Which county had the largest number of votes?
    

-   Denver
    

![](https://lh5.googleusercontent.com/xRvJA_4PuRR4kGZADogL2k-sKqVRnmgFuUAdDVAkKo2RujZKgkUVSflagLrgu4kMv4965gdyilN_je-rj8d5w4rGIyQVcrkv_ChIo58s_PozHz-fBUnubPD8gA9ndri33FdAbCocLGiDgq-rg2O-POXVSSP_tsjS37XeJ5G5a7ySTQ2xOZJs-NTJbc_s)

![](https://lh3.googleusercontent.com/HOwX22-fKk4zq0SgWT2pcF8o3cFdKutxn2x2hX5vIyp9linNK4nww567NsTCumrpkJ1vQFC5TpBb2HYXesNO2bJ4KJmj7Fjtp9qnJ6JlfgNb0dxj4iX4y9aLt4ym_C1KGnSWLOIsfkhzbM_PJGP4O6lkbVaeeGobiM_oSNP5OhyZXXwD4DfmuKuUe1_k)

-   Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    

-   Charles Casper Stockham: 23.0% (85,213)
    
-   Diana DeGette: 73.8% (272,892)
    
-   Raymon Anthony Doane: 3.1% (11,606)
    

![](https://lh3.googleusercontent.com/wUA_cGHSUWA3Eak_FrcvUyxUWK03ywpQ7yiKOiBPHKwf61vUCQjUF54EeJURE7Kv10GNRCluh3Ap61vHdfAkBPIEShKAkoaHuWnL3vyKhpHB2BqeQZhNigm7r0AMh4hEe-XGvs8rSJ8tvT2Dhl9vwRmiz8cCyDhZxcLaDceSI0JNZ3jc8bd24eqU3fZP)

Using a for loop to calculate total votes ,the percentage and the number of votes for each of them and printing it.

-   Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    

-   Winner: Diana DeGette
    
-   Winning Vote Count: 272,892
    
-   Winning Percentage: 73.8%
    

![](https://lh3.googleusercontent.com/A6Eh2fxUybNwnJcgRM03QhqwRYk301dkOdOe-mV0yQkRg4UJW_ZcCAfKZp_-eJhx0p84RT5tgFCrPCBSifoDsmpBjs1A47yUpzFTBlvGdzm5Jmg01nqmwEb6BGo_xewysEmGFGvViqyn9Y6eBRMfCww6USqTPXQI0MwBfOV1luMaIRYo1pOBwycG8ZgR)

Using if loop to compare the total votes for each candidate and decide the winner .Also printing the winning candidate name ,vote count and winning percentage to provide clear information.

  

To put it all together ,this is a brief output of the code :-

-   There were 369,711 votes cast in the election.
    
-   The three candidates were:
    

-   Charles Casper Stockham
    
-   Diana DeGette
    
-   Raymon Anthony Doane
    

-   With the candidate results being:
    

-   Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    
-   Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    
-   Candidate 3 received 3.1% of the vote and 11,606 number of votes.
    

-   The winner of the election was:
    

-   Diana DeGette, who received 73.8% of the vote and 272,892 number of votes
    

  

![](https://lh5.googleusercontent.com/ui51_0YZZLLcCg0AoVJnkug2uSUgrBfmSaQwT3_GdG4busf_kIH41GDoG_waTKjwMJvxvfU8sLe4yI6u5f9bgPa5y-isMV39U5H0K_E-GBfGpNtTlOe2YxFWgNSl8MaD7myjPY2u0JKacMGNA8iQCdoMET3BP6PzztbtLHdbLhxN1zlqbLN62CSFWlrY)

## Election Audit Summary

Using Python and reading in the CSV election data set we determined out of the 369,711 votes some patterns and analysis.

This task can usually be done in Excel, but to make it more efficient Election commission wants to know if there's a way to automate the process using Python. Now that we know the audit as done successfully with Python, the code we wrote will be used to audit not only other congressional districts, but also senatorial districts and local elections.

  

The code is efficient enough to run the analysis for either a congressional district , or senatorial districts or even local elections.

  

Few of the business use cases of this code are as follows:-

-   We can use the script in a scenario where we have many candidates running for the elections.
    
candidate_options = []

candidate_votes = {}

candidate_name = row[2]

 # 3: Extract the county name from each row.
county_name = row[1]

     # If the candidate does not match any existing candidate add it to
    
    # the candidate list

    if candidate_name not in candidate_options:

   # Add the candidate name to the candidate list.
    
    candidate_options.append(candidate_name)

   # And begin tracking that candidate's voter count.
    
    candidate_votes[candidate_name] = 0
    
     # Add a vote to that candidate's count

    candidate_votes[candidate_name] += 1

Define a empty list of candidates and a dictionary of candidates votes .As we see the candidate_name can be read from the given row,in this case row[2].We can have any number of candidates and using the conditional statement we can calculate votes for the each candidate without having to make any modifications.

-   Another use case would be if we have to run a report for multiple counties, states.
    
  county_list = []
  
    county_votes = {}
    
	  if county_name not in county_list:
	  
	  #`4b: Add the existing county to the list of counties.`
	  
        county_list.append(county_name)
	
   `# 4c: Begin tracking the county's vote count`.
   
           county_votes[county_name] = 0
	   
            # `5: Add a vote to that county's vote count.`
	    
           county_votes[county_name] += 1

 
Declaring an empty county list and an empty dictionary for county votes,we can calculate total votes for each county.

The similar can be done if we declare list of states/cities and dictinonaries of votes for states/cities.
