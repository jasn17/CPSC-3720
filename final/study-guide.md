# Final Study Guide

By Jason Lin

## Identify and briefly describe the main parts of a REST API.
- Endpoint (URL/Resource Path)
	- The specific access point for a resource
	- composed of a base URL plus a path (and optionally path or query parameters)
	- identifies which resource or collection you’re addressing 
		`https://api.example.com/users/123?active=true`
- HTTP Method (Verb)
	- Indicates the action to perform on the resource:
	- GET for reading data
	- POST for creating new resources
	- PUT/PATCH for updating existing resources
	- DELETE for removing resources
- Headers
	- Key–value metadata sent with the request or response (e.g. Content-Type, Accept, Authorization, Cookie)
	- informs how to interpret or handle the payload.
- Payload (Body)
	- The actual data sent to the server (in POST/PUT/PATCH requests) or returned from the server (in responses)
	- formatted as JSON to represent the resource’s state or content. ​
- Status code
	- 2xx for success (e.g. 200 OK, 201 Created, 204 No Content)
	- 3xx for redirection
	- 4xx for client errors (e.g. 400 Bad Request, 404 Not Found)
	- 5xx for server errors (e.g. 500 Internal Server Error) 

## What is the OpenAPI Specification and what are the main 	sections of the specification?
- OpenAPI is an open-source standard for describing and documenting RESTful APIs
- Main sections are meta info, path items, and components
	- Meta Information
	- Path Items (Endpoints), Defines each available URL path and its operations.
		- Parameters
		- Request Parameters
		- Responses
	- Components
		- Schemas
		- Parameters
		- Responses

## User stories 
```
You are working for a software company that wants to launch an online used car sale/purchase website.  The product owner has provided the following two Epics:

As a consumer, I can filter my list of cars, so that I can choose from cars that I like and can afford.
As a seller, I can list my car for sale, so that I can get the best price with the least amount of hassle.c
```
#### Epic 1
1. As a broke high school student, I can filter the cars by price range so my purchase can be within my budget. 
	
	AT: The filtered output of the price range should display cars with prices not below the low-end price range and not exceed the high-end price range.

2. As a mechanic, I can filter all cars by model so that I can browse through car models that I like. 
	
	AT: The filtered output should not display any vehicles outside of the queried filter model selected. 

3. As a father, I can filter cars by mileage so that I can find the most reliable vehicle for my high school kid.  
	
	AT: The filtered output should not display any vehicles with total mileage above the queried number. 
 
4. As a environmentalist, I can filter cars by vehicle type so that I can choose my options between an electric, gas, or diesel vehicles. 
	
	AT: The filtered output displays only the vehicles specified in the query or a screen displaying "No results"

5. As a person with no car, I can filter the nearest sellers based on my location so that I don't have to uber long distances to see a potential buying opportunity. 
	
	AT: The all queried results shows how far the seller from me (in miles).

#### Epic 2

1. As a car collector, I can create multiple car listing so that my chances to sell a car increases. 
	
	AT: With every new entry listed, I can see my car under "my current listing" as well as all of the details about the car listed. 

2. As a car enthusiast, I can take and upload photos of my car so people can see the condition of the car before deciding they are interested or not. 
	
	AT: The upload photo button should prompt the seller to select a photo and the photo should be clearly displayed under the listing.

3. As a car salesman, I can edit the vehicle's price under my current listings so I can adjust the price for current market conditions.
	
	AT: Clicking edit, submitting the new price range, the listing displays the new price.

4. As a practical seller, I can view my listing analytics to see how many people have clicked on my listing so I can decided which listings to take down and which ones to keep up.
	
	AT: Clicking the analytics tab and clicking on an individual listing it should show a graph of the number of clicks this particular listing got this month. 

5. As a repo man, I can submit my listings by vehicle type so that my sellers can find exactly what they want. 
	
	AT: With every new listing I can label this listing as a motorcycle, truck, car, or boat. After hitting submit the appropriate listing shows up. 

## Identify at least five microservices that are specific to a used car site (not general services like Accounts and Notifications).
1. A listing manager service which allows adding, modifying, and deleting car listings. 
2. A search and filter service.
3. Analytics and tracking user activities service.
4. Vehicle history service which displays past accidents/records associated with the car. 
5. Pricing service which gives the "best market value" based on car description. 

## Name and briefly describe the roles, ceremonies and artifacts in Agile using Scrum.
#### Roles: 
Scrum Master - remove impediments (servant leadership), enforce scrum values + practices, enforce productivity, shield team from outside distractions, watch all roles and functions

Developers - 4-9 cross functional team, full-time, self-organizing teams, changing teams should only be done between sprints

Product Owner - works on product backlog, decide release date, decide on features, finances, dictate which features to work on every sprint, accept/reject work results.

#### Ceremonies:
Daily scrum meeting - 15 minutes standup answering: what did you do yesterday, what did you do today, is there any current impediment.

Sprint planning - teams select items from product BL they can commit to completing adding these items to sprint BL, item broken further down into time

Sprint review - entire team presents what they have completed this sprint, demo of code or features, no slides 

Sprint retrospective - whole team gathers and decides what to start doing, what to stop doing, and what they liked and would like to continue doing (love, loathed, learned)

#### Artifacts:
Product BL - requirements to complete the project listed as epics and stories with story point values

Sprint BL - stories that are chosen to be completed on the current sprint. stories should be broken down into tasks, with story point values assigned, and a timeline 

Burn down Chart - visual chart tracking remaining work (x-axis is time and y-axis is remaining story points)

Impediment Log - scrum master logs all impediments

## Describe the Three Ways to achieve a DevOps culture.  For each "way" specify at least three practices required.
1. The principles of Flow
	- Limit the number of work in progress to finish more and expose bottleneck.
	- Visualize work with Trello board so everything is logged. 
	- Keep non-main branches on git short (do no commit to long to work on a feature)
	- Define environemnts and automate unit/integration tests
2. The principles of Feedback
	- Every change goes through a light code review via pull request 
	- You break it, you fix it
	- Pair programming when the time is appropriate
	- Share collaboration channel (Trello board)

3. The principles of Continual Learning and experimentation
	- Chaos monkey, controlled injection to try and crash your program
	- Incident reviews, what went wrong and what can we do next time?
	- Internal knowledge sharing via a lunch 

## Identfiy three key takeaways, from the the various readings you did in the Mythical Man Month by Fred Brooks.
1. Software by nature is complex much like a tarpit, the more code you add, features you add the harder the system becomes to maintain and understand.
2. Brooke's law states that adding more manpower towards the deadline slows development.
3. Conceptual integrity and prototyping, a system’s quality flows from a unified design vision—best achieved when a small group or lead architect drives the overall concept.
4. Brooks’s rule of thumb allocates roughly 1/3 of project time to detailed planning, 1/6 to coding, 1/4 to component and early system testing, and 1/4 to full system testing

## Describe the difference between functional and non-functional testing and provide at least three examples of each.
- Functional testing verifies what the system does, validating each feature against its specification, ensuring correct behavior for given inputs
	- Unit testing
	- integration testing
	- endpoint testing.
- Non-functional verifies how the system behaves, system qualities and constraints such as performance, reliability, security, and usability
	- Security testing
	- usability testing
	- load testing.

## Before starting a sprint 
```
What is needed to create a release plan for a product? 

How do you estimate and map to a schedule? 

What is needed before you start with the actual story development?

NOTE: Make sure you understand velocity vs story point estimates and how they are used together to create a plan.
```
- Creating a release plan for a product
	- Product Vision
		- high-level goals, target users, major features 
	- Product BL 
		- with stories + epics
	- Sizing & Estimation
		- Estimate each story using relative story-point sizing
		- INVEST: independent, negotiable, valuable, estimatable, small, testable.
	- Sprint Cadence & Velocity
		- 2 weeks per sprint
		- Divide total backlog points by velocity to compute number of sprints, then map to calendar weeks to predict release date
- Estimate and map to a schedule
	- Relative Sizing (Story Points)
		- size stories by complexity/effort
	- Dependency chart for priority
- Story development
	- Sprint 0 / Kickoff
		- Set up dev/test/staging environments
	- Backlog refinement
		- Refine epics into INVEST-compliant stories
	- Define Architecture & Design
		- document system architecture (microservices/APIs, data models, deployment topology)
	- Team Alignment & Ceremonies
		- Clarify roles (Product Owner, Scrum Master, Developers)
		- establish sprint cadence, ceremonies (planning, daily standup, review, retro)

## Tools and SDLC
#### Trello
- Requirements Analysis and Sprint Planning
	- Kanban board for transparent tracking of backlog items and sprint tasks.
	- visualizes bottlenecks for continuous flow.
	- Facilitates collaboration and conversation in daily stand-ups, sprint planning, and retrospectives.
#### Postman
- Define & Design Testing phases
	- refine user-story acceptance criteria
	- parallel development by decoupling front-end and back-end using mocks and examples.
	- shared workspaces for cross-functional collaboration on API design and validation.
#### Git
- Development phase
	- encourages frequent, small commits keeping work incremental and reviewable.
	- pull request for peer reviews, automated builds, and gating quality checks.
	- enables branching strategies (feature branches, release branches) to manage parallel work and releases.
	- enable rapid feedback on code changes, keeping the team’s work aligned and releasable.