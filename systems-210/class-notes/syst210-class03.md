# SYST 210: SYSTEM DESIGN
## CLASS 03: INTRO TO SYSTEMS AND SYSTEMS ENGINEERING

**Dr. Ali K. Raz**  
Assistant Professor SEOR  
George Mason University  
Copyright © 2025 Ali K. Raz GMU SEOR

---

## LEARNING OBJECTIVES

**Describe:**
- What is a systems engineering
- Why we need systems engineering
- What is a system-life cycle model and how it is used

**Review** definitions in the "Vocabulary" section of the notes

**Explain** how systems engineering can help prevent costly mistakes and system failures

**Utilize** a life-cycle model to organize a logical sequence of activities to manage system life-cycle

---

## SALIENT FEATURES OF A SYSTEM (RECAP)

- A system serves a ________________
- A system performs one or more _______________
- A system is composed of multiple __________________
- A system has a _________________
- A system has a _________________
- A system has a _________________

---

## ENGINEERED VS. NATURAL SYSTEMS (RECAP)

### Engineered Systems

An **engineered system** is a system designed or adapted to interact with an anticipated operational environment to achieve one or more intended purposes while complying with applicable constraints.

### Natural Systems

A **natural system** is an open system whose elements, boundary, and relationships exist independently of human control.

*Source: Systems Engineering Body of Knowledge (SEBoK)*

---

## ATTRIBUTES OF AN ENGINEERED SYSTEM (RECAP)

- **PURPOSE**
- **FUNCTION**
- **STRUCTURE**
- **BEHAVIOR**
- **BOUNDARY**
- **ENVIRONMENT**
- **INTERFACE**
- **HIERARCHY**
- **LIFE CYCLE**

---

## WHAT IS SYSTEMS ENGINEERING?

"Systems Engineering is a **transdisciplinary** and **integrative** approach to enable the successful **realization, use,** and **retirement** of **engineered systems**, using **systems principles and concepts**, and scientific, technological, and management methods."

*INCOSE*

The world around is filled with systems that are technologically complex and interdependent on one another.

These systems are composed of different parts/components that are also technologically complex and interdependent on one another.

Systems Engineering ensures that different parts work together to achieve the objectives of the whole.

---

## LET'S EXAMINE SE DEFINITION WITH AN EXAMPLE

"Systems Engineering is a **transdisciplinary** and **integrative** approach to enable the successful **realization, use,** and **retirement** of **engineered systems**, using **systems principles and concepts**, and scientific, technological, and management methods."

*INCOSE*

**Example: Commercial Aircraft System**

A commercial aircraft contains numerous complex subsystems including:
- Fuel system
- Oxygen systems/passenger service units
- Electrical power distribution
- Interior lighting structures and instruments
- Nacelles
- Cabin connectivity solutions
- Video systems
- Environmental controls
- Crew seats
- Communication, navigation and surveillance systems
- Door actuation
- Wheels and brakes
- Hydraulics
- Emergency power systems
- Galley
- Landing gear
- Pylons
- Actuation system
- Engine controls and sensors
- Exterior lighting
- Trimmable horizontal stabilizer actuator
- Premium, business and economy seating
- Lavatory
- Cargo systems
- Moving map
- Fire protection system
- Evacuation slides
- Electrical power generation

---

## WHY SYSTEMS ENGINEERING IS IMPORTANT!

- **Early examination of entire system life-cycle, before design freeze**
- **Reduce risks associated with new systems or modifications to complex systems**
- **Manage complexity and change**
- **Higher project performance and higher Return on Investment (ROI) (cost and schedule)**

---

## BENEFITS OF SYSTEMS ENGINEERING

**The higher the SE capability, the better the program performance**

Research shows that projects with higher systems engineering capability (Higher SEC) achieve:
- 57% higher performance outcomes
- 24% middle performance
- 20% lower performance

Compared to projects with lower SEC which show:
- 15% higher performance
- 33% middle performance
- 52% lower performance

---

## MANY SUCCESSES OF SYSTEMS ENGINEERING

### Apollo/Saturn V Program used Systems Engineering to manage...

- Government/industry/academic partnership
- 400,000 people at peak
- Hundreds of universities and over 20,000 companies
- Started in July 1960
- Program ended December 1972

---

## WHEN SYSTEMS ENGINEERING GOES WRONG!

### MARS CLIMATE ORBITER
Failed due to unit conversion error (metric vs. imperial)

### Spain S-80 Class Submarine
Design error made submarine too heavy to surface properly

### US ARMY FCS (Future Combat Systems)
$18+ billion program cancelled due to poor systems integration

---

## WHY EARLY AND EFFECTIVE SE IS NEEDED! (1)

Throughout the system lifecycle:

**Cost Committed vs Cost Incurred**

- At Conceptual & Preliminary Design: 5% cost incurred, 60% cost committed
- At Detailed Design & Integration: 20% cost incurred, 80% cost committed
- At Construction or Production: Most costs incurred, nearly all costs committed
- At Use, Refinement & Disposal: 100% cost incurred

**Key Insight:** Most costs are committed early in the lifecycle, but incurred later. Early decisions have massive impact on total cost.

---

## WHY EARLY AND EFFECTIVE SE IS NEEDED! (2)

**Committed Lifecycle Cost against Time**

- **Concept Phase (8%):** Cost to extract defects = 3-6X
- **Design Phase (15%):** Cost to extract defects = 20-100X
- **Develop Phase (20%):** Cost to extract defects increases significantly
- **Prod/test Phase (50%):** Cost = 100%
- **Operations through disposal (95%):** Cost to extract defects = 500-1000X

**Key Insight:** Finding and fixing defects becomes exponentially more expensive as the project progresses.

*Source: SE Handbook v4, 2015; original source DAU*

---

## HOW DOES SE ACHIEVE "SUCCESSFUL REALIZATION, USE, AND RETIREMENT OF ENGINEERED SYSTEMS"

Each system throughout its lifecycle goes through multiple stages.

Life cycle models describe the stages and lay out what activities need to occur at each stage:
- Predictable sequences exist within predictable cycles
- There are many models but most are variations on a few basic themes
- Models differ in emphasis on:
  - Planning ahead (Ready...Aim...FIRE!!!)
  - Learning by doing (Ready...Fire...AIM!!!)

Different models are appropriate for different kinds of project. Key drivers: $, staff, time constraints.

**Examples:**
- Waterfall
- Spiral
- Vee
- Agile

---

## BUILD-AND-FIX (NOT AN SE LIFE CYCLE MODEL)

- Start with an informal general idea
- Build and fix until time or money runs out
- Not a life cycle model
  - Signs of early progress
  - No SE required
  - May work for simple and small projects

---

## LIFE CYCLE MODELS: WATERFALL

**Emphasizes sequential steps in design and development**

**Goal is to plan ahead to minimize rework and redesign:**
- Define before design
- Design before build

**Characteristics:**
- Return to previous steps is viewed as error
- Best for well-understood systems
- Unrealistic and unworkable for new concepts
- Can't expect accurate requirements early in project
- Nothing to see or test until very late in project
- Overhead too costly for small projects

**Sequential Phases:**
1. Systems Requirements
2. Software Requirements
3. Preliminary Design
4. Detailed Design
5. Coding and Debugging
6. Integration and Testing
7. Operations and Maintenance

*Source: Buede, Engineering Design of Systems, Figure 1.6*

---

## LIFE CYCLE MODELS: SPIRAL MODEL

**Recognizes need to "learn by doing"**

**Emphasizes cyclical nature of design activity**

**Uses feedback from previous iterations to improve design:**
- Refine requirements
- Learn what works and what doesn't
- Reduce risks

**Good for new and untried concepts**

**Four Main Quadrants (repeated iteratively):**
1. **Determine Objectives, Alternatives, and Constraints**
2. **Evaluate Alternatives; Identify and Resolve Risks** (with Risk Analysis)
3. **Develop and Verify Next Level Product**
4. **Plan Next Phases** (with Commitment Review)

Each iteration produces prototypes progressing from:
- 1st Prototype
- 2nd Prototype
- 3rd Prototype
- Operational Prototype

**Cumulative Cost** increases with each spiral iteration as progress advances through phases.

---

## LIFE CYCLE MODEL: VEE MODEL OF DESIGN AND INTEGRATION

The Vee Model emphasizes the relationship between development phases (left side) and corresponding verification/validation phases (right side).

**Left Side (Decomposition and Definition):**
- Understand User Requirements, Develop System Concept and Validation Plan
- Develop System Performance Specification and System Validation Plan
- Expand Performance Specifications into CI "Design-to" Specifications and CI Verification Plan
- Evolve "Design-to" Specifications into "Build-to" Documentation and Inspection Plan
- Fab, Assemble and Code to "Build-to" Documentation

**Right Side (Integration and Qualification):**
- Inspect "Build-to" Documentation
- Assemble CIs and Perform CI Verification to CI "Design-to" Specifications
- Integrate System and Perform System Verification to Performance Specifications
- Demonstrate and Validate System to User Validation Plan

**Center:** Systems Engineering / Design Engineering

**Time** flows from left to right along the bottom of the V.

---

## LIFE CYCLE MODEL: VEE MODEL VARIATIONS

### Generic V-Model (Wikipedia)
- Project Definition
- Requirements and Architecture → Verification and Validation
- Detailed Design → Integration, Test, and Verification
- Implementation → System Verification and Validation
- → Operation and Maintenance

### MIT Systems Engineering V-Model
Integrates 11 key processes:
1. Stakeholder Analysis
2. Requirements Definition (SRR)
3. System Modeling Languages - MBSE
4. System Architecture Concept Generation
5. Tradespace Exploration Concept Selection (PDR)
6. Design Definition Multidisciplinary Optimization
7-10. System Integration Interface Management
11. Lifecycle Management (PFR)
12. Prototyping Manufacturing

With key reviews: SRR, PDR, CDR, FRR

---

## LIFE CYCLE MODELS: AGILE DEVELOPMENT

Developed by Software Engineers; Increasing application in SE

**Principles:**
- Continuous Collaboration
- Continuous Updates
- Short cycle (weekly basis)
- Value participation and interactions
- Emphasize simplicity

**Scrum Construction Lifecycle:**

1. **Product Backlog** (Highest-Priority Requirements)
2. **Sprint Backlog** (Planning session to select requirements for current Sprint and to identify work tasks)
3. **30-day Sprint** with Daily Work
4. **Daily Scrum Meeting** (Share status and identify potential issues)
5. **Working System** produced
6. **Sprint review** (Demo system to stakeholders and gain funding for next sprint)
7. **Sprint Retrospective** (Learn from your experiences)
8. **Funding & Feedback** loop back to requirements

*Source: http://www.ambysoft.com/essays/agileLifecycle.html*  
*Copyright 2005-2008 Scott W. Ambler*  
*Original Diagram Copyright Mike Cohn*

---

## LIFE CYCLE MODEL: REFERENCE AND ADDITIONAL READING

**For more information, see:**

https://www.sebokwiki.org/wiki/System_Life_Cycle_Process_Models:_Vee

**Comparison of Life Cycle Models:**

### Generic Life Cycle (ISO 15288:2008)
- Exploratory Stage
- Concept Stage
- Development Stage
- Production Stage
- Utilization Stage (with Support Stage)
- Retirement Stage

### Typical High-Tech Commercial Systems Integrator
**Study Period:**
- User Requirements Definition Phase
- Concept Definition Phase
- System Specification Phase
- Acq Prep Phase
- Source Select Phase

**Implementation Period:**
- Development Phase
- Verification Phase

**Operations Period:**
- Deployment Phase
- Operations and Maintenance Phase
- Deactivation Phase

### Typical High-Tech Commercial Manufacturer
Similar phases adapted for manufacturing context

### US Department of Defense (DoD) 5000.2
- User Needs
- Tech Opport Resources
- Pre-Systems Acquisition: Materiel Solution Analysis
- Technology Development
- Systems Acquisition: Engineering and Manufacturing Development
- Production and Deployment
- Sustainment: Operations and Support (including Disposal)

### NASA
- Formulation: Pre-Phase A (Concept Studies) → Phase A (Concept & Technology Development)
- Approval: Phase B (Preliminary Design & Technology Completion)
- Implementation: Phase C (Final Design & Fabrication) → Phase D (System Assembly Integration & Test, Launch)
- Phase E (Operations & Sustainment)
- Phase F (Closeout)

### US Department of Energy (DoE)
**Project Planning Period:**
- Pre-Project
- Preconceptual Planning
- Conceptual Design
- Preliminary Design
- Final Design

**Project Execution:**
- Construction

**Mission:**
- Acceptance
- Operations

---

## WHAT YOU NEED TO DO!

### Readings:
- Buede & Miller: Chapter 1
- Buede & Miller: 2.1, 2.2, 2.3, 6.3, 6.10 and 6.11
- INCOSE: Chapter 1.1 to 1.3

### Homework:
- Homework 0: Due August 29th, 2025
- Homework 1: Due Sept 12th, 2025 (Available later next week)

### Discover Systems Assignment Online
- Preferences due Sept 10th, 2025
- Let's review this on CANVAS

---

## IN CLASS EXERCISE!

Get together with your team and revisit the offshore oil platform exercise.

Discuss answers to the following questions in your group:

**Can this system benefit from systems engineering? Why? Why Not?**
- Identify at least three disciplines evident in this system
- What could go wrong if SE is not applied?

---

## PROJECT TEAMS

Teams have been organized based on favorite topics including:
- Defense System 1 & 2
- Space
- Aircraft
- Computer/Software
- Robotics/Gadgets
- Automobiles
- Medical

(See full team roster in original document)

---

## VOCABULARY

**System:** set of components, including hardware, software, people, facilities, and procedures, acting together to achieve a set of common objectives

**Life Cycle:** phases of systems' existence from initial concept through refinement and disposal

**Life Cycle Model:** description of stages in system life cycle and the activities at each stage. Examples include waterfall, spiral, vee.

**Integration:** process of assembling a system from components and subsystems

---

## /SYST210/TIL

Today I Learned:

- What is systems engineering?
- Explain the kind of problems systems engineering can prevent and how it prevents them.
- Describe different life cycles models and what kind of a system each one is best suited for.

---

*Copyright © 2025 Ali K. Raz GMU SEOR*