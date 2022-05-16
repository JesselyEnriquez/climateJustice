# Earthquake Damage Modeling
---

## Executive Summary

The project to model and predict earthquake damage in Nepal came in part because of the tragic earthquake named Gorka that occured April 25, 2015 in Nepal. The project aims to support and classify the damage a building is expected to endure given an event with a similar magnitude occurs, in order to inform Nepali locals if retrofitting of a particular building is needed. The research and modeling was done for approximately 11 districts in Nepal. The model can predict and classify the expected damage of a building with an accuracy and F1 Score (macro) of 64%. Considering the baseline percentage for this dataset was 36% this model provides a considerable advantage for the government to accurately determine buildings at risk. </br>

## Notebook Order:
- [earthquake_scrub.ipynb](./Code/Cleaning_N_EDA/earthquake_scrub.ipynb)  </br>
- [muni_geo_encoding.ipynb](./Code/Cleaning_N_EDA/muni_geo_encoding.ipynb) </br>
- [BEGIN_HERE_muni_eda_viz.ipynb](./Code/Cleaning_N_EDA/BEGIN_HERE_muni_eda_viz.ipynb)  </br>
- [muni_eda_viz-prt2.ipynb](./Code/Cleaning_N_EDA/muni_eda_viz-prt2.ipynb) </br>
- [random_forest.ipynb](./Code/Modeling/random_forest.ipynb)</br>
- [xgboost_classifier.ipynb](./Code/Modeling/xgboost_classifier.ipynb) </br>
- [logistic_regression.ipynb](./Code/Modeling/logistic_regression.ipynb) </br>

## Problem Statement
In Nepal there is a need to evaluate where to focus preventative funding but also locals who are knowledgeful of how to retrofit their communities. A model to shed some insight as to what buildings are in need of retrofitting could allow locals to assess if there were any buildings overlooked when undergoing reconstructions from the 2015 Gorkha Earthquake. 

## Data Collection
From the [2015 Nepal Earthquake Open Data Portal](http://eq2015.npc.gov.np/#/)

On April 25, 2015 there was an earthquake that was named the Gorkha Earthquake. Its magnitude was on a scale of 7.8 moment magnitude (mW). Utimately, it cost the world 9,000 lives and 100,000 injuries. So immediately following the event the Nepali Government undertook a massive household survey to identify those in need of government financial assistance. Naturally they collected socio-economic data, in addition to the building characteristics pre/post the earthquake. Another source of information that was gathered is a secondary use flag in which the we can determine if a building was used also as a government office or a hostipital.  

Utimately this data was publicized on the Data Portal linked above, however the geospatial coordines of these locatinos were not provided. So that data had to be gathered from the Nepali govenerment directly([refrence](https://www.nepal.gov.np/)). Mapping these onto one another took quite a bit of time but proved to display some insightful information. It also provides a great foundation for potential future work. 

The features used in the project model contained features from the Building Structure, Ownership, and Damage Assessment datasets that were accessible via the portal and they can be found in the data dictionary below.

The damage grade will be modeled for all eleven districts of Nepal those are named as the following:
- Dhading
- Dolakha
- Gorkha
- Kaverpalanchok
- Makwanpur
- Nuwakot
- Okhaldhunga
- Ramechhap
- Rasuwa
- Sindhuli
- Sindhupalchok



---
## Modeling
A variety of different models and approaches were attempted working through modeling iterations. The different classifier models used in the project were  Random Forest, XGBoost, and Logistic Regression.

After many iterations, the model that performed best based on the F1 Score(macro) was the Logistic Regression Classifier with only minor changes to the default parameters, since it was a multi-class target with severely imbalanced classes of building damage. The feature importances were explored to compare among models, these summaries can be found in the presentation.

The inputs that ultimately were of importance to can be summarized as a form to represent location, age of a building, and buildings structure conditions.
</br>

---

## Conclusion


The final model is able to predict the level of damage a building is expected to experience far more effectively than the baseline. The factors that seem to have the most impact are  location, age of a building, and building structure conditions.  <br>



The Nepali government, as well as locals that the volunteers to survey can utilize this model to attempt to evaluate the expected damage if another earthquake of that magniture were to occur. Given that this was data from a fairly significant earthquake these damage levels is considered a conservative predictions since earthquakes on this scale are not extremely prevelant in Nepal.


<br>

---

## Future Work
Gathering a form of geographical summary of the spacial characteristics on the smallest level possible for each municipality to include sounds to be a good approach to gather a more accurate representation that just the municipality IDs and other spatial IDs that the model is attempting to create connections to damage with.

Once that is made, assuming this is possible on a large scale then the model can be expanded to and even larger scale given that these geospatial representation values actually improve the models performance.


 ---
 ## Data Dictionary
These features were compiled from a third party source ([Data Driven](https://www.drivendata.org/competitions/57/nepal-earthquake/)) since the original data source did not describe all features in their portal.
 | Feature                | Range                | Type: Categories                                                                                                                                                                                                                             |
 |------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 | building_id            | int                  | randomized building identifier                                                                                                                                                                                                               |
 | district_id            |      int              | the district code                                                                                                                                                                                                                            |
 | vdcmun_id              |        int            | the municipality code                                                                                                                                                                                                                        |
 | ward_id                |     int               | the ward code (like a zip code)                                                                                                                                                                                                              |
 | count_floors_pre_eq    |     int          | count of floors before earthquake                                                                                                                                                                                                            |
 | count_floors_post_eq   |      int          | count of floors post earthquake                                                                                                                                                                                                              |
 | age_building           |      int      | age of building in years years                                                                                                                                                                                                                     |
 | plinth_area_sq_ft      |        int        | the property area of a building in square ft                                                                                                                                                                                                 |
 | height_ft_pre_eq       |        int      | height of building before earthquake                                                                                                                                                                                                         |
 | height_ft_post_eq      |     int           | a flag that determines a buildings height post earthquake                                                                                                                                                                                                           |
 | land_surface_condition |       object       | a flag that determines a buildings surface condition of the land where it was built (catergories =n,o,t)|                                                                                                                                                              |roof_type | object             | a flag that determines a buildings type of roof used while building (categories = n, q, x)                         |                                                                                                                                                         
 | ground_floor_type      |       object               | a flag that determines a buildings type of ground floor (categories = f, m, v, x, z)                                                                                                                                                                                            |
 | other_floor_type       |    object                  | a flag that determines a buildings type of constructions used in higher than the ground floors, except roof (categories = j,q,s,x)                                                                                                                                              |
 | position               |        object              | a flag that determines a buildings building (categories = j, o, s, t)                                                                                                                                                                                       |
 | plan_configuration     |          object            | a flag that determines a buildings plan configuration (categories = j,q, s, x)                                                                                                                                                                                         |
 | has_superstructure     | object | a flag that determines if a buildings superstructure was made of the following: adobe_mud, mud_mortar_stone, stone_flag, cement mortar_stone, mud_mortar_brick, cement_mortar_brick, timber, bamboo, rc_non_engineered, rc_engineered, other |
 | legal_ownership_status |           object           | legal ownership status of the land where a building was located (categories = a, r, v, w)                                                                                                                                                    |
 | has_secondary_use      |           object           | a flag to determine if a building was used for any secondary purpose the potential secondary uses are: agriculture, hotel, rental, institution, school, industry, health post, gov office, police, other                                     |
 | count_families         | int                  | the number of families that live in each building                                                                                                                                                                                            |
