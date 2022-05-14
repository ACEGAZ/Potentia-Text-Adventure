# Potentia Text Adventure

## Introduction

Potentia text adventure is a text based game that allows the player to make decisions and change how the story plays.
Potentia takes its inspiration from role playing games and other text adventures from the late 1970's and 1980's.
The world, races and lore of Potentia are all my own design and are inspired by Dungeons & Dragons table top Role Playing games.

A: B: C: D: E: F: G: and yes or no are used for the player to make decisions and progress through the game.

Potentia runs in the terminal and uses the code institute template terminal to run in a browser, using Heroku as a hosting platform.

![Recording 2022-05-13 at 09 24 36](https://user-images.githubusercontent.com/97246895/168243359-e47a3cd8-e527-493d-bd55-458863e2cbf0.gif)


## Goals

The main goal of Potentia is to give players a fun experience and to generate intrest in the world and its lore. 

The second goal was to make a playable game using python.

## logic flow

I created a flow chart using lucid chart to show the flow of the game and display how each decision will play out.
Once a decision has been made the terminal will print the next part of the story for the player to make a new choice. 

![Potentia text adventure](https://user-images.githubusercontent.com/97246895/168243401-03dbaeae-6cfc-45e4-ab81-e6bb658932af.png)

## Features 

### Combat 

Potentia features a combat system that allows the player to attack with magic or melee combat. The player and enemy have hitpionts that once
depleted will cause the enemy to die and the game to continue or the player to die and the game to restart. 

### Capture and escape

The game features a one off combat encounter which allows the player to defeat the enemy and escape without being captured or lose the encounter and
be captured. 

### Race Selection

Potentia starts with a race selection, allowing the player to select from 7 different races. 
Each race has unique options for certain situations and unique text when engaged in combat.

Races include:

Vahser
Mortem
Bascula
Hemmel
Human
Arratoi
Fulger

### Character name

The player is able to name their character whatever they want and their character name will be referenced in parts of the story.

### Decisions

Players are able to make decisions that influence how the story plays and what ending the player will see.

### Puzzle

The last section of the game features a puzzle for the player to complete. The puzzle is a series of numbers that equate to letters in the alphabet, A = 1, B = 2, ect.

Here is the puzzle as displayed in the game. The solution is the word Nadaren which can be spelled in all lowercase, all uppercase or with the first letter capitalized.

* 14 = N
* N - 13
* N - 10
* D - 3
* A + N + 3
* D + A
* R - D

## Deployment 

Potentia is deployed on Heroku and can be found here: https://potenta-text-adventure.herokuapp.com/

initially Potentia Text Adventure was going to be deployed using Heroku to connect to Github but this feature has been removed from heroku.
instead it was deployed by using the command heroku login -i and loging in when prompted. Then running the command heroku create Potentia-Text_adventure to create a new app. This created a new Heroku app and linked it to my Gitpod terminal. Then I set up config vars and build packs on Heroku. 
I used heroku/python and heroku/nodejs buildpacks. 

## Testing 

Potentia was tested by a small group of people, including myself. The game was played many times and all feedback was taken and most problems were solved as they 
were discovered.

Once Potentia was hosted on Heroku a link was sent on a messenger chat and each menmber of the chat was able to message me with any issues that they found. 

## Bugs

The only significant bug is enemies skipping thier turn during combat. 
When combat is initiated the player takes thier turn and then if the enemy has hitpoints remaining the code will be run for the enemy to retaliate. 
However, sometimes the eneimes turn will not run and instead the player will get another attack. 

Unfortunatly, I did not have the time to fix this but will be looking to fix it in a future update. 

## Technologies used

Python was primarily used for Potentia and I imported the time and random libraries. 

The Time library was used to pause the game to create the illusion that the enemy was attacking and to allow the player more time to read. 

The Random library was used to return random numbers for player and enemy attacks. 

## Validation 

I ran Potentias code through pep8 with only 3 minor warnings and no major problems. 

## Future updates

I would like to include a complete magic system for utility based magics, such as healing spells. these spells would allow the player to heal during combat.

I would also like to include an experience system were players gain experience (XP) which will increase their power and health. 

## Credits

The intial design concept and layout was taken from Derik Shidler
link: https://www.derekshidler.com/how-to-create-a-text-based-adventure-and-quiz-game-in-python/

The flow chart was designed using lucid charts
Link: https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20charts&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-381457345638:kwd-64262996435&km_CPC_Country=9045120&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjwg_iTBhDrARIsAD3Ib5iJyyR9mzZprdpM9iO9WOfNZS838_JDlskIPm7LKLOwXn1s64vfEx4aAjUsEALw_wcB

### Testers 

* Rachel Lowles
* Charlotte Aling-Case
* lysette Reed
* Aaron Harvey
* Dale Millward
* Natalie March
* Emma Skinner\
