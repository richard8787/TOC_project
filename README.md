# TOC Project 2020

richard8787 for TOC Project 2020
A Line bot based on a finite state machine


## Featutes
* to check whether do the mandatory military service or not
* to give something to remind you


## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
The initial state is set to `user`.

Every time `user` state is triggered to `advance` to another state, it will `go_back` to `user` state after the bot replies corresponding message.

* user
	* Input: "go to state1"
		* Reply: "I'm entering state1"

	* Input: "go to state2"
		* Reply: "I'm entering state2"




