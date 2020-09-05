from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### The Project Goal

Lockdowns due to the COVID-19 pandemic have loosened up everywhere in the US, but is it safe for me and my friends that I go out and socialize again? 
It's difficult to provide a generic answer as it would depend on two critical factors:

1. **Infection risk**: How likely is it that you may contract COVID-19?
2. **Outcome severity**: If infected, how likely might you experience severe outcomes such as staying in the ICU or even dying?

This web app makes personalized predictions for both based on your age, sex, pre-existing medical conditions, and the state you live in.

---
### Use Cases
1. **For yourself**: Enter your information and estimate your own infection risk and outcome severity.
2. **For social contacts**: Enter your social contact's information and estimate their risk of socializing with you.
3. **For state governments**: Adjust safe social bubble size in state guidelines and send out warning to at-risk 
sub-populations.

---

### Data Sources

Infection risk and outcome severity are predicted from the 4 data sources below:

1. **Prevalence**: In a given state, what's the probability that a random person has COVID-19? 
2. **Social bubble size**: For a given user, how many people (themself not included) do they regularly socialize with?
3. **Contagion probability**: If someone has COVID-19, how likely may they infect someone else?  
4. **Outcome severity**: If contracted COVID-19, how likely will the user experience severe outcomes?

Prevalence is estimated from each state's testing data, assuming that the positive rate in diagnostic tests reflects the prevalence of COVID-19 in that state. 
Social bubble size is provided by the user. Contagion probability is taken from published COVID-19 research. Taken 1-3 together, we can estimate the infection risk 
of a user from a certain state socializing with a certain number of people.

Outcome severity is predicted by a LightGBM classifier trained on the CDC case surveillance data with 2 million COVID-19 patients' age, sex, medical conditions, and treatment outcomes
(**mild**: not hospitalized; **moderate**: hospitalized; **severe**: ICU or death).

*&copy; 2020 Yuan Meng*

""")]
