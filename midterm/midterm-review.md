# Midterm Review

The midterm covers Weeks 1-7 and is on Thursday Feb 27 for 60 minutes using Canvas quizzes with Respondus lockdown browser.  Please make sure your laptop is charged and ready to go for the test. 



## SDLC
- Simple programs vs. larger product systems per Fred Brooks	
	- Single program developed by small team is 3x more complex than garbage code
	- A full product with integration, documentation, and support is 9x more complex
- Benefits of Agile vs Waterfall
	- Agile: iterative development with deliverables every 2-4 weeks
		- embrace chanhge
		- software > documentation
		- interactions and individuals
		- customer collaboration
	- Waterfall
		- sequential requirements → design → coding → testing → maintenance

## Agile:
- Agile roles, artifacts, and ceremonies - make sure you understand each of them
	- Product Owner (defines features & ROI)
	- Scrum Master (servant leader, removes impediments)
	- Developers/Team (4–9 cross-functional members)
	- Product Backlog
	- Sprint Backlog
	- Burndown Chart
	- Impediment Log 
	- Sprint Planning, Daily Scrum (15 min stand-up)
	- Sprint Review (demo)
	- Sprint Retrospective (inspect & adapt)
- How do you gather requirements for user stories?
	- questionnaire
	- observation
	- user interviews
	- story-writing workshops
- Three Cs of user stories
	- Card
	- Conversation
	- Confirmation
- Story hierarchy
	- Product -> Epics -> User stories
- Writing user stories and acceptance tests
	- 
- Estimating in Agile 
	- Sizing: story points + T-shirt size

## Microservices:
- Low coupling and High cohesion - why do you want these in your microservices?
	- Low coupling = less dependencies
	- High cohesion = clarity + reusability
- Characteristics of microservices
	- 
- Benefits of microservices
	- faster time to market
	- agility++
	- continuous integration/development
	- scalability
	- debugging + maintenence

## Teaming:
- Jim McCarthy videos 
	- [Don't Flip the Bozo Bit][1]
		- Don’t permanently label someone as incompetent after one mistake—maintain trust and give people ownership
	- [Beware of the Guy in a Room][2]
		- Warns against isolated decision-making without team input—promote transparency
	- [Don't Go Dark][3]
		- Emphasizes continuous communication—avoid disappearing when challenges arise
- Conway's Law
	- `"Any organization that designs a system will produce a design whose structure mirrors the organization’s communication structure,”`
	- Your team chart often maps directly to your software architecture
 
## REST APIs:
- Four parts: Headers, Methods, Endpoint, Data
	- Endpoint: URL with resource path (e.g., /users/{id})
	- Method: HTTP verb (GET, POST, PUT/PATCH, DELETE)
	- Headers: Metadata (Content-Type, Authorization, etc.)
	- Data: Request payload for POST/PUT/PATCH
- What is the Open API Specification and how is it organized?
	- Meta info (title, version)
	- Paths (endpoints with parameters, request bodies, responses)
	- Components (schemas, parameters, reusable responses) 
- Path vs. Query parameters
	- Path parameters are part of the URL path to identify specific resources 
		`/orders/{orderId}`
	- Query parameters follow ? to filter or sort 
		`?status=shipped&sort=date_asc`

## Quality/Testing:
- Testing types and examples of each
	- Unit Testing: Verify individual modules
	- Integration/System Testing: Validate end-to-end flows
	- Functional Testing: Check features against requirements
	- Exploratory Testing: Ad hoc discovery of issues
	- Regression Testing: Ensure new changes don’t break existing behavior
	- Non-functional Testing: Recovery (chaos), security, stress/soak, performance
- What is cruft? What other term can be use for cruft?
	- Leftover, redundant, or poorly designed code—often called “technical debt”—that accumulates from quick fixes or workarounds
- Agile vs. Waterfall testing
	- Waterfall: Testing at end of development
		- separate QA teams
		- largely manual regression per release
	- Agile	
		- Continuous testing within each sprint
		- shared QA responsibility
		- heavy automation
		- “shift-left” TDD practices

[1]: https://youtu.be/QSKLm8E6KyE
[2]: https://youtu.be/oY6BCHqEbyc
[3]: https://youtu.be/9OJ9hplU8XA