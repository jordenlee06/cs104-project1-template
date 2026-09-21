# [Project 1]
How well do you know your black history? Law Edition!
## Overview
> This program will quiz users on black history that is related to the law. Based on their answers, users will earn points, their final score will determine how well they did on this quiz and what letter grade they received. 

## Sample Questions and Responses
1. Which 1896 Supreme Court decision famously established the "separate but equal" doctrine, providing legal justification for Jim Crow laws for over half a century?
>1. Plessy V. Ferguson(answer) 
>2. Dred Scott V. Sandford
>3. Cumming V. Richmond County Board of Education
>4. Civil Rights Cases of 1883

2. In the landmark 1954 decision Brown v. Board of Education, the Supreme Court ruled that racial segregation in public schools violated which part of the U.S. Constitution?
>1. The Equal Protection Clause of the Fourteenth Amendment 
>2. The Due Process Clause of the Fifth Amendment 
>3. The Commerce Clause of the Fifth Amendment 
>4. The Privileges and Immunities Clause of Article IV

3. Before his appointment to the Supreme Court, Thurgood Marshall famously served as the chief legal counsel for which civil rights organization?
>1. Southern Christian Leadership Conference(SCLC)
>2. Congress of Racial Equality(CORE)
>3. NAACP Legal Defense and Educational Fund
>4. Urban League

4. The 1967 Supreme Court case Loving v. Virginia unanimously struck down state anti-miscegenation laws, which criminalized what practice?
>1. Interstate travel by interracial couples
>2. Integrated public housing
>3. Voter suppression targeting minorities
>4. Interracial marriage

5. As chief counsel for the NAACP Legal Defense Fund, Thurgood Marshall successfully spearheaded the litigation and oral arguments for which landmark 1954 Supreme Court case?
>1. Brown V. Board of Education
>2. Sweatt v. Painter
>3. Briggs v. Elliot
>4. Bolling v. Sharpe

6. What did the 13th Amendment to the U.S. Constitution accomplish?
>1. It guaranteed equal voting rights regardless of race.
>2. It granted citizenship to all people born in the United States.
>3. It granted women the right to vote.
>4. It abolished slavery and involuntary servitude, except as punishment for a crime.


## Variables 
>   since results are cumulative and only one final score matters.
> - points (int): the points they get per question, which will be 5 points. 
> - Score(int): the total overall points they get at the end: stores the user's response to a question, there are no points deducted if they get the answer wrong, therefore the score will only add points when user inputs the correct answer and will be a total out of 30, since there are 6 questions worth 5 points each.
> - Final_grade: The user will also receive a final letter grade. If they have a score of 0-10 out of 30, they will receive a letter grade of C. If they have a grade of 11-19 out of 30, they will receive a letter grade of B. If they receive a grade of 20-30, they will receive a letter grade of A.
> - Starting score: 0 

## Conditional Logic Outline
> **DELETE AND REPLACE ME:** Outline every conditional statement in your
> program, in the order they appear. For each one, describe it in plain
> language (no code needed): which question/condition it relates to,
> each branch (`if`/`elif`/`else`), the exact condition that triggers
> each branch, the action(s) that happen in each branch, and note any
> nested conditionals and why they're nested.
>
> Example:
> - **Conditional statement 1** — related to "Which 1896 Supreme Court decision famously established the "separate but equal" doctrine, providing legal justification for Jim Crow laws for over half a century? ? 1-Plessy V. Ferguson  2-Dred Scott V. Sandford 3-Cumming V. Richmond County Board of Education 4-Civil Rights Cases of 1883"
>   - `if` response is 1 (Plessy V. Ferguson): display congratulatory message,
>     increment `score` by 5
>   - `else`: display incorrect message and explain the correct answer, and tell the user they earned 0 points for this question.
>
>   
>- **Conditional statement 2** — related to "In the landmark 1954 decision Brown v. Board of Education, the Supreme Court ruled that racial segregation in public schools violated which part of the U.S. Constitution?? ? 1-The Equal Protection Clause of the Fourteenth Amendment  2-The Due Process Clause of the Fifth Amendment  3-The Commerce Clause of the Fifth Amendment 4-The Privileges and Immunities Clause of Article IV"
>   - `if` response is 1 (The Equal Protection Clause of the Fourteenth Amendment): display congratulatory message,
>    increment `score` by 5
>   - `else`: display incorrect message and explain the correct answer, and tell the user they earned 0 points for this question.
> 
> >- **Conditional statement 3** — related to "Before his appointment to the Supreme Court, Thurgood Marshall famously served as the chief legal counsel for which civil rights organization?? ? 1-Southern Christian Leadership Conference(SCLC)  2-Congress of Racial Equality(CORE)  3-NAACP Legal Defense and Educational Fund 4-Urban League"
>   - `if` response is 3 (NAACP Legal Defense and Educational Fund): display congratulatory message,
>    increment `score` by 5
>   - `else`: display incorrect message and explain the correct answer, and tell the user they earned 0 points for this question.
>
> >- **Conditional statement 4** — related to "The 1967 Supreme Court case Loving v. Virginia unanimously struck down state anti-miscegenation laws, which criminalized what practice? 1-Interstate travel by interracial couples   2-Integrated public housing 3-Voter suppression targeting minorities   4-Interracial marriage"
>   - `if` response is 4 (Interracial marriage): display congratulatory message,
>    increment `score` by 5
>   - `else`: display incorrect message and explain the correct answer, and tell the user they earned 0 points for this question.
>
> 
> >- **Conditional statement 5** — related to "As chief counsel for the NAACP Legal Defense Fund, Thurgood Marshall successfully spearheaded the litigation and oral arguments for which landmark 1954 Supreme Court case? ? 1-Brown V. Board of Education  2-Sweatt v. Painter 3-Briggs v. Elliot  4-Bolling v. Sharpe"
>   - `if` response is 1 (Brown V. Board of Education): display congratulatory message,
>    increment `score` by 5
>   - `else`: display incorrect message and explain the correct answer, and tell the user they earned 0 points for this question.
>
>  >- **Conditional statement 6** — related to "What did the 13th Amendment to the U.S. Constitution accomplish? ? 1-It guaranteed equal voting rights regardless of race.   2-It granted citizenship to all people born in the United States.   3-It granted women the right to vote.  4-It abolished slavery and involuntary servitude, except as punishment for a crime."
>   - `if` response is 4 (It abolished slavery and involuntary servitude, except as punishment for a crime.): display congratulatory message,
>    increment `score` by 5
>   - `else`: display incorrect message and explain the correct answer, and tell the user they earned 0 points for this question.
>
> 
> - **Conditional statement 7** — reveals final results based on `final_grade`
>   - `if` score is 20-30: display high-knowledge message
>   - `elif` score is 11-19: display some-knowledge message
>   - `else`: display message encouraging the user to learn more

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
(https://youtu.be/6wedOapcCHk)
