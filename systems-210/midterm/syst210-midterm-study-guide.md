# SYST 210 Midterm Exam Study Guide

**Coverage:** The midterm exam covers until Lecture 11.

**Exam Structure:** The Mid-Term is nearly equally divided between theory and practice

---

## System Design Theory

### 1. Systems and the System Lifecycle

**Key Topics:**
- What is a system
- What are the attributes of a system
- What is systems engineering
- Why systems engineering is needed
- Description of the systems engineering process:
  - Statement of Need
  - Stakeholder Analysis
  - Define the Design Problem
  - Functional Architecture

### 2. Definition/Need For/Purpose Of/Importance Of:

**Need Statement**
- Purpose and importance
- How to write effective need statements

**Operational Concept**
- Components:
  - Vision statement
  - Mission requirements
  - Operational scenarios

**External Systems Diagram**
- Context
- External system
- System boundary

**Objectives Hierarchy**
- Structure and purpose
- How to develop

**Functional Architecture**
- Purpose and components
- Relationship to other artifacts

### 3. Proper Requirements Wording

**Characteristics of Good Requirements:**
- Individual requirement characteristics (8 characteristics):
  1. Unambiguous
  2. Understandable
  3. Correct
  4. Concise
  5. Traced
  6. Traceable
  7. Design independent
  8. Verifiable

- Set characteristics (6 characteristics):
  9. Unique
  10. Complete
  11. Consistent
  12. Comparable
  13. Modifiable
  14. Attainable

**Types of Requirements:**
- Originating requirements (from stakeholders)
- Derived requirements (developed to meet originating requirements)
- Stakeholder need statements vs. requirements

**Writing Requirements:**
- Use "shall" for ordinary requirements
- Use "should" for goals (desirable but not necessary)
- Use "will" for constraints
- Define the system under consideration
- Define positive end results
- Avoid:
  - Ambiguity ('or', 'etc.', 'so on')
  - Escape clauses ('but', 'if', 'when', 'although', 'except')
  - Informal words ('cool', 'user-friendly', 'as much as possible', 'totally')
  - Compounding with 'and', 'also', 'with'
  - Vague words ('usually', 'normally', 'may', 'perhaps', 'could')
  - Incompleteness (TBD, TBR)

### 4. Stakeholders

**What are they?**
- Individuals or groups with interest in the system
- Multiple categories throughout lifecycle

**Why is it important to involve them?**
- Ensure requirements reflect actual needs
- Reduce project failures
- Build support and acceptance

**What can go wrong?**
- If not involved:
  - Missing or incorrect requirements
  - Project failure (35-44% of failures due to requirement issues)
  - Lack of user acceptance
- If involvement not properly managed:
  - Scope creep
  - Conflicting requirements
  - Stakeholder fatigue

**How should they be involved?**
- Activities at different lifecycle stages:
  - Early: Needs identification, vision development
  - Design: Requirements review, feedback on prototypes
  - Development: Testing, validation
  - Deployment: Training, acceptance
  - Operations: Feedback, refinement requests

**Tensions between stakeholders:**
- Why important to identify and address
- Examples: cost vs. performance, user convenience vs. security
- Methods for resolution

### 5. Systems Engineering Artifacts by Lifecycle Stage

**What systems engineers do at each stage:**
- Statement of Need development
- Stakeholder Analysis
- Operational Concept development
- Requirements elicitation and documentation
- Functional Architecture development
- Interface definition
- Verification and validation planning

### 6. Model-Based Systems Engineering (MBSE)

**What is MBSE?**
- Definition: Formalized application of modeling to support system requirements, design, analysis, verification and validation
- Transition from document-centric to model-centric
- Benefits: Single source of truth, traceability, consistency

**MBSE vs. Document-Centric:**
- Old way: Multiple separate documents
- New way: Integrated system model
- Advantages: Faster, savings, authoritative source, collaborative

---

## How to Construct in MBSE

### 1. Operational Concept
- Vision statement
- Mission requirements
- Operational scenarios
- SysML representation: Use Case Diagrams, Sequence Diagrams

### 2. Operational Scenarios
- Sequence Diagrams in SysML
- Actors and interactions
- Message flows

### 3. External Systems Diagram
- System boundary representation
- External systems
- Context elements
- Interfaces

### 4. Use Cases
- Use Case Diagrams
- Actors
- System boundary
- Relationships

### 5. Originating Requirements
- Requirements Diagrams in SysML
- Traceability relationships
- Containment hierarchies

### 6. Functional Architecture
- Activity Diagrams (behavior/flow)
- Block Definition Diagrams (structure)
- Functional decomposition
- Data/signal/energy/matter flows

---

## Systems Design Practice

### Case Study Approach

Many questions will relate to a case study problem describing a system from a stakeholder's point of view. You may be asked to:

### 1. Stakeholder Analysis
- **Who are the stakeholders for the system?**
  - Identify all stakeholder groups
  - Categories: users, operators, maintainers, regulators, etc.
- **What are tensions between them?**
  - Identify conflicting interests
  - Prioritization issues

### 2. Need Statement
- **Write a need statement for the system**
  - Clear description of the problem
  - Evidence and facts supporting the need
  - Why the system is needed

### 3. Vision Statement
- **Write a vision statement for the system**
  - High-level view of the system
  - What the system will achieve
  - How it addresses the need

### 4. External Systems Diagram
- **Create an External Systems Diagram**
  - System boundary
  - External systems (interact with system)
  - Context (impacts system but not impacted by it)
  - Interfaces

### 5. Operational Scenarios
- **Write an operational scenario (verbal) for the system**
  - Normal operations
  - Unusual situations:
    - Errors
    - Maintenance operations
    - Emergency situations
  - Training operations

### 6. Sequence Diagrams
- **Develop a sequence diagram corresponding to a verbal operational scenario**
  - Actors
  - System
  - Messages/interactions
  - Timing

### 7. System Boundary
- **Describe the system boundary:**
  - What functions/components/subsystems are **included** in the system
  - What functions/systems are part of the **environment**
  - What functions/systems are part of the **context**

### 8. Critique Diagrams
- **Critique an external systems diagram to find problems and errors**
  - Missing elements
  - Incorrect relationships
  - Unclear boundaries
  - Missing interfaces

### 9. Objectives Hierarchy
- **Develop and/or critique an objectives hierarchy**
  - Cost, schedule, performance measures
  - Hierarchical decomposition
  - Completeness and consistency

### 10. Requirements
- **Write or critique requirements for the system**
  - Check against 14 characteristics
  - Proper wording
  - Traceability
  - Verifiability

---

## Study Strategy

### For Each Lecture, Review:

**1. Learning Objectives**
- Can you meet each objective?
- Practice applying each skill

**2. Vocabulary**
- Define each term
- Understand context and usage

**3. /syst210/TIL Questions**
- Answer each question thoroughly
- Connect concepts across lectures

---

## Key Concepts Summary

### System Definition
A collection of interrelated elements organized to accomplish a specific purpose or set of purposes

### System Attributes
- Purpose/function
- Components/elements
- Relationships/interactions
- Boundary
- Environment
- Emergent properties

### Systems Engineering Process Flow
```
Statement of Need → Stakeholder Analysis
                          ↓
              Define System-level Design Problem
                          ↓
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
Develop Functional Architecture    Develop Physical Architecture
        └─────────────────┬─────────────────┘
                          ▼
              Develop Allocated Architecture
                          ↓
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼
Develop Interface Architecture    Develop Qualification System
```

### Requirements Hierarchy
```
Mission Requirements
        ↓
Stakeholders' Requirements (Originating)
        ↓
System Requirements
        ↓
Component Requirements
        ↓
CI Requirements
        ↓
Derived Requirements
```

### SysML Diagram Types
- **Structure Diagrams:** BDD, IBD, Package, Parametric
- **Behavior Diagrams:** Activity, Sequence, State Machine, Use Case
- **Requirement Diagram**

### Context vs. External Systems vs. System
- **Context:** Impacts the system but is NOT impacted by the system
- **External Systems:** Interact with the system; both impact and are impacted
- **System:** Within the boundary; what we're designing

---

## Practice Questions to Consider

1. Given a scenario, identify all stakeholders and their interests
2. Write a need statement that includes evidence and facts
3. Create a vision statement that addresses stakeholder needs
4. Draw an external systems diagram showing boundary, external systems, and context
5. Write operational scenarios for normal and abnormal situations
6. Convert a verbal scenario into a sequence diagram
7. Write requirements using proper format (system shall...)
8. Critique requirements for the 14 characteristics
9. Develop an objectives hierarchy
10. Create activity diagrams showing functional flow
11. Generate block definition diagrams from functional decomposition

---

## Common Pitfalls to Avoid

### Requirements Writing
- Don't specify HOW (design), specify WHAT (function)
- Avoid ambiguous words
- Don't use negative statements
- One requirement per statement (no "and")

### External Systems Diagrams
- Don't confuse context with external systems
- Show all interfaces
- Clear system boundary

### Stakeholder Analysis
- Don't forget any stakeholder groups
- Consider entire lifecycle
- Identify and address tensions

### Operational Scenarios
- Be specific about interactions
- Include all actors
- Consider edge cases and errors

---

## Final Tips

✓ Review all lecture slides and notes
✓ Practice drawing diagrams by hand
✓ Understand the "why" not just the "what"
✓ Know how concepts connect to each other
✓ Practice with case studies
✓ Review homework problems and solutions
✓ Understand MBSE tools (SysML) concepts
✓ Be able to critique as well as create
✓ Time management: theory and practice are equally weighted

---

# Enjoy studying for the test and all the best of luck on the test!!!

*[Motivational image: "WHO'S GONNA ACE THEIR EXAMS? YOU ARE!"]*

---

*Study Guide for SYST 210 - System Design*  
*George Mason University, SEOR Department*