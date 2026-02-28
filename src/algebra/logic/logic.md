# Logic
## Introduction
- The word logic is derived from the Greek word logos, which may be interpreted as "reason" or "discourse".
ሎጎስ = ርትዒ / መጎት

- The ancient Greeks are usually credited with initiating the study of our reasoning process. The principles discovered by the Greeks were first systematized by Aristotle (384-322 B.C), and Aristotle's type of reasoning constitutes the traditonal logic that has been studied and taught from his time to the present day. 

- Although the modern study of symbolic logic (the subject of this video) finds its roots in the works of such men as the German mathematician Leibniz (1647-1716). Modern symbolism and algebraic type operations were first systematically applied to logic in the works of George Boole (1815-1864). 

- The study of logic has developed at an accelerated pace since Boole's analysis, and considerable progress towards and understanding of logic truth has been made.

- Whether we are tyring to solve a problem or engaged in a debate, we are engaged in a mental activity called "logical reasoning". This reasoning is usually expressed in terms of declarative sentences. And it is to the study of these sentences that we now turn our attentions. 

## Statements and Open Statements
- The sentences (ምሉእ-ሓሳብ) we come across in our every day language are not always declarative sentences. There are also sentences such as questions, commands, suggestions, proposals or exclamations. However, mathematics deals only with declarative sentences. 


1. እዙይ ሕብሪ ፃዕዳ እዩ።
2. በይዛኻ እንዶ ተማላኣኒ!?
3. ፈጣሪ ይሓግዝካ!
4. ናበይ ትኸይድ ኣለኻ?

- Lets' consider the above sentences: Out of all of them, only #1 is a declarative or assertive sentence. In other words, we can assign it a truth value T, when it is true and a truth value F when it is false. 

- Definition: A proposition (or statement) is any meaningful, unambiguous declrative sentence which is either true or false, but not both at the same time.

    - For example, The statement, "Five is less than six" is a proposition. Since this is a true proposition its truth value is T. 
    - The statement "Two plus five is equal to six" is a proposition with a truth value of F. 

- The sentences, "x -3 = 6" and "He is a pilot" become statements when "x" is replaced by a number and the pronoun "He" is replaced by a person. 

- Definition: An open-statement (or open proposition) is a sentence which contains one or more variables or pronouns and becomes a statement when each of its variables or pronouns is replaced by a specific value or an individual. 

## Type of Propositions
- Definition: A simple statement is a complete sentence that conveys one thought with no connecting words like, and , or , not, etc.
- Example:
  - Four is natural number
  - Gebre is a pilot
- We shall denote the simple propositions by small letters such as p,q, r, s etc. 
- 
- Definition: A proposition consisting of two or more simple propositions in the form of a single sentence is called compound (or complex) proposition. 
- Example 
  - The square root of 1 is 1 and 3 > 4. 
  - The day next to Tuesday is Wednesday or 2 + 2 = 4.
- The individual statments in a compound or a complex proposition are called the component propositions. 
- We shall study the determination of truth values of compound propositions from the truth tables of their components. A table that gives truth value of a compound statement is called a truth table. 

## Propositional Connectives
- In order to create a compound proposition, we need to combine simple propositions. And we have five fundamental logical connectives at our disposal. Namely Negation, Conjunction, Disjunction, Implication, and Bi-implication.  Let's discuss them one by one. 
- ### Negation
  - Definition: Let p be any prposition. Then we write the negation of p as ¬p and define it to be the proposition 'it is false that p'. 
  - Examples: Let p be the proposition "the library is closed". Then ¬p, the negation of p, is the proposition "It is false that the library is closed", or "the library is not closed".
  - The connection between p and ¬p can be tabulated by the truth table as follows: 
  - 
- ### Disjunction
  - Any two propositions can be combined by the connective "or" to form a new proposition which is called disjunction of the original propositions. 
  - Definition: Let p and q be two propositions. We define the disjunction of p and q to be the proposition: either p or q or both and we write p ∨ q. We say that p ∨ q is the proposition 'p or q'. p ∨ q is true if p is true or q is true or p and q both are true. 
  - The connection p ∨ q can be tabulated by the true table as follows:  
- ### Conjunction
  - Definition (መብርሂ): Given two propositions q, q we define the conjunction of p and q to be the proposition p and q and we write it p ∧ q. 
  - p ∧ q is true iff the propositions p and q are both true. The truth table of p ∧ q is as follows: 
- ### Implication
  - Definition: A statement of the form "If p then q" where p and q are propositions is called an implication statement (or conditional statement), and it is denoted by p → q. 
  - p → q is false iff p is true and q is false. In all other cases it is true.
  - The truth table of p → q is as follows.    
  - In p → q, the proposition p is called the hypothesis (antecedent) while q is called its conclusion (consequent).
  - Note: p → q does not mean that p causes q. The conditional proposition does not need any logical connection between p and q except that whenever p is true, q is also true. and whenever p is false, q is also false.
    - example: Let p = 2 is less than -2, q = 4 is greater than 1. p → q = if 2 is less than -2, then 4 is greater than 1. Here p → q is true because q is true inspite of the fact that p is false. In fact there is no logical connection between p and q. i.e q cannot be deduced from p. 
  - Definition: if p → q is the direct proposition, then 
    1. q → p is called its converse. 
    2. ¬p → ¬q is called the inverse. 
    3. ¬q → ¬p is called its contrapositive. 
 - ### Bi-Implication (bi conditional)
   - Definition: A bi-implication proposition written in the form of p ↔ q is assigned truth value T iff both propositions have the same truth values.
   - The truth table of p ↔ q is as follows:
   - Note: If there are n-simple statements in a compound or complex proposition, then there are $2^n$ different logical possiblities. 
   - Let's construct a truth table for the proposition (p ∨ ¬q) → r
- ## Tautology and Contradictions
  - Definition: A proposition, which is always true, no matter what truth values are assigned to its component propositions, is called tautology (t). 
  - Let's consider the proposition p ∨ ¬p. As can be seen from its truth value, it is always true regardless of the values of p and ¬p.
  - Definition: A proposition, which is always false, no matter what truth values are assigned to its component proposition is called a contradiction (c). 
  - Let's consider the proposition p ∧ ¬p. As can be seen from its truth value, it is always false regardless of the values of p and ¬p.

## Logical Equivalence
- Definition: Two propositions involving the same component proposition are said to be equivalent iff they have identical truth tables. We will denote logical equivalent by the symbol "≡"
- Let's consider the proposition ¬(p ∧ q) and ¬p ∨ ¬q. As can be seen from their corrosponding truth tables, they are equivalent.
- Given arbitrary propositions p, q, r, the following propositional identities are algebraic laws. 
  - Commutative law: p ∧ q  ≡ q ∧ p
  - Associative law: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)
  - Distributive law: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)    
  - Identity law: p ∧ t ≡ p    
  - Negation law: p ∧ ¬p ≡ c
  - Double Negation law: ¬(¬p) ≡ p 
  - Idempotent law:  p ∧ p ≡ p  
  - De Morgan's law: ¬(p ∧ q) ≡ ¬p ∨ ¬q   
  - Universal bound law: p ∨ t ≡ t
  - Absorption law: p ∧ (p ∨ q) ≡ p
  - Negations of t and c:  ¬t ≡ c
    