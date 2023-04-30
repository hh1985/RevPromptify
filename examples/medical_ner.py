from promptify import OpenAI
from promptify.prompts.nlp.prompter import Prompter
from pprint import pprint
import json

sentence = """Metformin is a common drug for the management of type 2 diabetes mellitus; however, 
                it causes various adverse gastrointestinal effects, especially after prolonged treatment.
                It is thus of interest to identify an adjuvant treatment that synergizes with the efficacy 
                of metformin while mitigating its adverse effects. Since previous evidence supports that 
                the gut microbiota is a target of metformin, this study investigated the beneficial effect 
                and mechanism of the coadministration of probiotics with metformin in the management of 
                type 2 diabetes mellitus by conducting a 3-month randomized, double-blind, placebo-controlled
                clinical trial (n = 27 and 21 in the probiotic and placebo groups, respectively, 
                who completed the trial). Clinical results showed that the coadministration of probiotics with 
                metformin significantly reduced glycated hemoglobin compared with metformin taken alone (P < 0.05). 
                Metagenomic and metabolomic analyses showed that the coadministration of probiotics increased 
                the abundance of gut short-chain fatty acid (SCFA)-producing bacteria and bile acids.
                      Significantly or marginally more bile acids and related metabolites were detected in the 
                      probiotic group than in the placebo group postintervention. Taken together, the results of 
                      our study showed that the coadministration of probiotics with metformin synergized with the 
                      hypoglycemic effect in patients with type 2 diabetes mellitus, which was likely through 
                      modulating the gut microbiome and, subsequently, SCFA and bile acid metabolism. Our findings 
                      support that cotreatment with probiotics and metformin is beneficial to patients with type 2 diabetes mellitus."""


model = OpenAI(api_key="",
               model="gpt-3.5-turbo")

prompter = Prompter(model=model,
                    templates_path="../promptify/prompts/text2text/ner/")

output = prompter.fit(template_name="ner_openai.jinja",
                      text_input=sentence,
                      domain="biomedical",
                      labels=["Gene/Protein", "Disease", "Chemical", "Species",
                              "Mutation", "Cell Line", "Cell Type","DNA", "RNA"])

#pprint(eval(output['text']))
pprint(output)
