from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
    html.Br(),

    dcc.Markdown(""" ### Project Goals 

    	After months of sheltering in place due to COVID-19, all 50 states in the US have now reopened to varying degrees.
    	*Now what?* Should we go back to business as usual, as if the pandemic is behind us? Or do we keep inside at all times for another year or two?
    	
    	As a data scientist, I refrain from judging people for their decisions; rather, I wish to provide information 
    	they need to make informed decisions, including: 

    	1. **Infection risk**: How likely is it that you may contract COVID-19, given the state you live in and how many people you socialize with?

    	2. **Outcome severity**: If infected, how likely will you experience severe outcomes such as ICU stays or even death, given your age, sex, medical condition, etc.?

    	To evaluate your risks, you can navigate to the corresponding tabs on top of this page.

    	---

    	"""),

    dcc.Markdown(""" ### Use Cases

    	1. **For yourself**: You can use this app to estimate your own infection risk and outcome severity and decide if it's relatively safe to socialize again and with how many.

    	2. **For your social contacts**: If you wish to socialize with someone who may belong to a vulnerable population (e.g., senior people, people with chronic diseases that 
    	may worsen COVID-19 symptoms, etc.), you can use this app to estimate their risks and watch out for their safety.

    	3. **For state governments**: Public health officials can adjust the recommended social bubble size based on their state's underlying infection rate as well as sending out 
    	warnings to sub-populations that may be subject to severe outcomes if infected.

    	----

    	"""),

    dcc.Markdown(""" ### Under the Hood

    	How do I make these predictions? For full details, you can check out my Jupyter Notebooks ([infection risk](https://github.com/Yuan-Meng/TDI_capstone/blob/master/model/infection_risk.ipynb), [outcome severity](https://github.com/Yuan-Meng/TDI_capstone/blob/master/model/outcome_severity.ipynb)).
    	Below are the main ideas.

    	To predict infection risk, I first assumed that each state's positive viral test rate reflects the underlying infection rate in that state.
    	Do take this estimate with a grain of salt because high positive rates may be a result of insufficient testing rather than high infection rates. 
    	Then, I searched the literature for the infectivity of symptomatic and asymptomatic COVID-19 patients and the percentage of each, based on which 
    	I estimated the probability of a random COVID-19 carrier infecting another person. If someone has prolonged contact with N people, 
    	the probability of getting infected is 1 minus the probability that none of these N people have COVID-19 nor are they infectious. In consequence, your infection risk
    	grows pretty quickly with your "social bubble" size.

    	To predict outcome severity, I used the [COVID-19 case surveillance system database](https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf)
    	provided by CDC, which has over 3 million COVID-19 patients' demographic information (sex, age group, race and ethnicity), medical condition, and their treatment outcomes (e.g., hospitalization, ICU stays, and death).
    	A case is considered severe if either the patient stayed in ICU or died. I built a classification model with [LightGBM](https://lightgbm.readthedocs.io/en/latest/) to predict 
    	outcome severity based on a given user's conditions.

    	*&copy; 2020 Yuan Meng*

    	""")])
