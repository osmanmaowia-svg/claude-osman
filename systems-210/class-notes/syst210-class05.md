# SYST 210: SYSTEM DESIGN
## CLASS 05: DEFINING SYSTEM LEVEL DESIGN PROBLEM

**Dr. Ali K. Raz**  
Assistant Professor SEOR  
George Mason University  
Copyright © Ali K. Raz GMU SEOR

---

## LEARNING OBJECTIVES FOR TODAY

**State the three elements of Operational Concept:**
- Vision
- Mission Requirements
- Operational Scenarios

**Given a statement of need, develop an operational concept for a system that meets the need**

**Define:**
- Context
- External System
- System Boundary

**Define Objective Hierarchy**

**Given a statement of need, inputs from stakeholders, and a draft operational concept, develop an objectives hierarchy**

**Review vocabulary terms at the end**

---

## STRUCTURE OF THE SYSTEM DESIGN PROCESS

**System Statement of Need** and **Stakeholder Analysis** feed into:

→ **Define System-level Design Problem**

Which branches into:

**Left path:** Develop Functional Architecture

**Right path:** Develop Physical Architecture

Both converge at: Develop Allocated Architecture

Which leads to: Develop Interface Architecture → Develop Qualification System

---

## DEFINE THE DESIGN PROBLEM → WHAT DO WE WANT?

### Major Inputs:
- System Statement of Need
- Stakeholder Analysis

### Major Outputs:
- **Operational Concept of the System**
  - Vision of the system
  - Mission Requirements
  - Operational Scenarios
- **External Systems and System Boundary**
- **Objective Hierarchy**
- **Originating System Requirements**
  - Description of constraints and performance
  - How the system will behave

---

## OPERATIONAL CONCEPT OF THE SYSTEM

**Defines Justification For and Use of the System**

### Vision
- Mission Statement

### Mission Requirements
- Top level description of system purpose

### Operational Scenario
- How the system operates from user's perspective

### Operational Concept (OpsCon) vs. Concept of Operations (ConOps)
- Frequently used interchangeably
- Similar but different
- What are the differences:

---

## OPSCON: VISION

- Succinct statement of essential idea of the system in user language
- Related to system's statement of need/mission statement

### Example:

**Need Statement:**
*Market research indicates that approximately 30,000 buildings of between 10 and 20 stories are constructed each year. Studies show that between 100 and 150 people occupy each floor of a typical building in the target class. There is a need for rapid, safe, reliable, and cost-effective vertical transportation to move people between floors.*

**Vision Statement:**
The new system being designed by the Up and Down Elevator Company is directed at the major market niche of standard 10 to 20 story office buildings being constructed in the U.S. This product is not to address the low end and high ends of the 10 to 20-story office building market, but the center of this market. Marketing estimates are that 100,000 of these buildings are being constructed each year for the next 10 years. Each such building will require six to twenty elevator cars and associated control systems and maintenance/operations support. This market is envisioned to be very price competitive but requiring that basic thresholds of performance and cost be met.

*Buede & Miller, The Engineering Design of Systems*

---

## OPSCON: MISSION REQUIREMENT

- Small number of high-level requirements that capture essential purpose of system (typically no more than 7)
  - Not a comprehensive list of system requirements
  - Capture system vision and need
- Relate to the stakeholder objectives
- Include measurable performance objectives

### Example Mission Requirements

**MR.1.** The system shall capture 20% of the market for vertical transportation in new buildings starting in June 2001.

**MR.2.** The system shall have operational cost of no more than 80% of the operating cost of systems produced by competing vendors.

**MR.3.** The system shall score at least 20% better than systems produced by competing vendors according to the weighted performance index:

0.3 AWT + 0.3 ATT + 0.2 MTBF + 0.2 MTTR

where:
- AWT is a value index that ranges between 0 and 1 for average wait time
- ATT is a value index that ranges between 0 and 1 for average transit time
- MTBF is a value index that ranges between 0 and 1 for mean time between failure
- MTTR is a value index that ranges between 0 and 1 for mean time to repair

*Adapted from: Elevator case study from Buede (2009)*

**Mission Requirements commonly also include safety and lifecycle cost**

---

## OPSCON: OPERATIONAL SCENARIOS

- Describe how the system operates or will be used
  - Start at a high-level and include step-by-step explanation/illustration of major steps
  - Often termed as use case and/or mission profile

### How to represent operational scenarios:
- **Illustration** (most common)
- **Text based representation**
- **Model-based representation** (next class – becoming common)

---

## OPSCON: ILLUSTRATION

[Various examples shown in slides including Apollo moon landing trajectories, Artemis I mission map, ventilator systems, and missile defense scenarios]

---

## OPSCON: TEXT-BASED REPRESENTATION – ELEVATOR EXAMPLE

### Preconditions:
- Elevator is operational and ready to respond to requests for service. Passengers are ready to request service.

### Primary scenario: 
Passengers (including mobility, visually, and hearing challenged)
- request up service
- receive feedback that their request was accepted
- receive input that the elevator car is approaching
- receive input that an entry opportunity is available
- enter elevator car, request floor
- receive feedback that their request was accepted
- receive feedback that door is closing
- receive feedback about what floor at which elevator is stopping
- receive feedback that an exit opportunity is available, and
- exit elevator with no physical impediments

### Exceptions:
- Passenger encounters an emergency situation before exit opportunity is presented

### Postconditions:
- Elevator is operational and ready to respond to requests for service

---

## OPSCON: MODEL-BASED REPRESENTATION

**We will cover these in next class**

[Shows sequence diagrams and use case diagrams for elevator system]

---

## SYSTEM BOUNDARY, EXTERNAL SYSTEMS, AND CONTEXT

### Context:
- Impact the system but are not impacted by the system
- Generate originating requirements

### External Systems:
- Interact with the system via external interfaces
- Impact and are impacted by the system
- Play a major role in establishing requirements
- Can be existing (or legacy) systems

### System Boundary:
- Delineates what is inside and outside the system
- Essential input to detailed design

*Buede, The Engineering Design of Systems, Figure 6.2*

---

## DEFINING THE SYSTEM BOUNDARY

- One of the most important design decisions is what functionality is included in the system and what functionality is left to other systems

- Often an early version includes a set of essential functions and additional functions are added in later version

- The system boundary must be agreed upon early in design

- Stakeholder buy-in is essential

- Operational scenarios are an important tool for defining the system boundary
  - Go through operational scenarios with stakeholders
  - Negotiate functionality to include, functionality to exclude, and functionality to defer to a later time
  - Document all decisions and obtain explicit agreement in writing

- External systems diagram shows the system boundary

---

## EXTERNAL SYSTEMS DIAGRAM AND OPERATIONAL CONCEPT

- System Operational Concept is developed for all lifecycle stages

- Examining system boundary from different lifecycle stages helps identify the different interfaces

*Buede & Miller, The Engineering Design of Systems, Figure 1.1*

---

## EXTERNAL SYSTEMS AND OPERATIONAL CONCEPT

[Shows aircraft operational concept with different environments: Flight Environment, Landing Environment, Support Environment, People and Payload Interface, Maintenance Environment]

*Systems Engineering Principles and Practice, 2nd Edition*

---

## OBJECTIVES HIERARCHY

- Represent what stakeholder value
- Hierarchical decomposition of objectives
  - Identify different "buckets" of stakeholder preferences
  - Visualize structure of objectives
- Forms the basis of trade studies
  - Compare alternative design with different cost and performance parameters (Faster, cheaper, durable etc.)
  - Focus design effort on important parts of the trade space

**Objectives Hierarchy Defines Performance Space for Design Solution**

---

## SPECIFYING THE OBJECTIVES

### Objectives
- What stakeholders aim to achieve
- Basis of stakeholder satisfaction
- There are objectives for all lifecycle phases (Production, Manufacturing, Operations, Training, Maintenance, Retirement etc.)

### To define an objective, we specify:
- A metric to establish how well an objective is met
- Minimum acceptable threshold
- Desired performance

---

## EXAMPLE OF OBJECTIVES HIERARCHY

**Operational Objectives** branches into:

1. **Monthly Operating Costs** ($1,500 - $1,000, Wt = 0.1)

2. **Operational Performance Objectives** (Wt = 0.9)
   - **Time in System Objectives** (Wt = 0.35)
     - Average Wait (Routine): 35 - 27 sec, Wt = 0.3
     - Average Wait (Priority): 35 - 30 sec, Wt = 0.35
     - Average Transit Time: 90 - 60 sec, Wt = 0.35
   
   - **Ride Quality Objectives** (Wt = 0.30)
     - Max'm Acceleration: 1.5 - 1.25 m/s², Wt = 0.3
     - Max'm Accel'n Change: 2 - 1.5 m/s³, Wt = 0.5
     - Floor Leveling Error: 0.7 - 0.3 cm, Wt = 0.2
   
   - **Availability Objectives** (Wt = 0.35)
     - Operational MTBF: 1 - 1.5 yrs, Wt = 0.5
     - Operational MTTR: 8 - 4 hrs, Wt = 0.5

---

## CHARACTERISTICS OF OBJECTIVES AND TYPES

### Characteristics of Objectives
- Complete
- Consistent
- Measurable
- Non-overlapping
- Hierarchically arranged in logical groupings
- Each group has 7 (typically) or fewer objectives

### Types of Objectives:
- **Fundamental Objectives** – essential to system purpose
  - Objectives hierarchy recognizes fundamental objectives
- **Means Objectives** – helps achieve fundamental objectives
  - Not part of objectives hierarchy
  - Implicit in derived requirements

---

## CATEGORIES OF OBJECTIVES

### Operational Phase
- Operating Cost
- **Operational Performance**
  - Include objective for each aspect of system main mission
- **Suitability or Quality Attributes**
  - Sometimes called the "ilities" (see https://sebokwiki.org/wiki/Systems_Engineering_and_Quality_Attributes)
  - E.g: reliability, maintainability, useability, safety, etc.

### Throughout the system life cycle
- Total lifecycle cost: development, operations, disposal
- Manufacturability
- Schedule: design, development, manufacturing
- Environmental impact at all lifecycle phases
- Safety at all lifecycle phases
- Ease of Training
- Etc.

---

## WHAT YOU NEED TO DO SOON!

### Reading for next week:
- A Practical Guide to SysML: Chapter 2.1 and 3.1,3.2, 4.1, 4.2, 4.3.1-4.3.7

### Homework 2 Available Now
- Due Sept 19th, 2025

---

## VOCABULARY

**Operational Concept:** describes how system will be used
- **Vision statement:** succinct statement of essential idea of system
- **Mission requirements:** small number of high-level requirements capturing essential purpose of system
- **Operational scenario:** step-by-step description of how system is used (also called use case)

**Context (of a system):** set of entities that can impact the system but are not impacted by the system

**External system:** system that interacts with system via external interfaces

**System boundary:** separates the system from external systems with which it interacts; inputs and outputs must flow across the boundary

**External systems diagram:** displays interactions of system with other (external) systems, thus providing a definition of the system boundaries

**Objectives hierarchy:** hierarchical decomposition of objectives valued by stakeholders
- **Fundamental objective:** objective that is essential to the system purpose
- **Means objective:** objective that is important because it helps to meet fundamental objectives

---

## /SYST210/TIL

Today I Learned:

- What are the six major steps of the systems engineering design process?
- What is the purpose, inputs and outputs of each step of the systems engineering design process?
- **What are the elements of an operational concept?**
- What is the purpose of each of these elements?
- What is an external systems diagram and what is its purpose in helping to define a system design?
- Why is it important to provide a measure when specifying an objective?
- Objectives should be broken into what categories?
- What are system "ilities"?

---

*Copyright © Ali K. Raz GMU SEOR*