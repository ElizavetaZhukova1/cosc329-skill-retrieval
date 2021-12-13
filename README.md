# cosc329-skill-retrieval
## The project is created by Elizaveta Zhukova and Sophia Joseph. 

## The link to the report: https://docs.google.com/document/d/1qULa5P5VO_jSzUdbtJi_ekeJ9mPlObtm3lt1KbPunQk/edit?usp=sharing

## The link to the video: https://drive.google.com/drive/folders/1ZolZJCGhjgRPKTdVlDidTg4HOc-cSUAQ?usp=sharing

## The descriptions for files:
`final_skill_extraction.ipynb` - contains the final version of the skills extraction. Because the original dataset was too big we had to extract the skills by taking only slices of the dataset each time and then merging them. So, if you are willing to try and run the program on the full dataset, remove the slicing from the code in the beginnig and change the name of the  csv file there the dataset gets exported in the end.

`final_test_cases.ipynb`- contains mostly the same content as the previous file, but with test cases and prepared for the demo video.

`NER_and_ling_analysis.ipynb` - contains the NER part of skills extraction (unpolished and ran on the lower sample, because the analysis was performed before mid-project report). Also contains some unsuccessful linguistic analysis, which we decided not to include in the final reprot because it did not yield any significant results. 

`Skill-extraction-sample-demo-v1.ipynb` - the demo notebook for mid-project presentation. This one was made for presentational purposes only so it is run on a very small sample.

`Word2Vec_better.ipynb` - contains KMeans merging (using Word2Vec vectorizations) and final data analysis.

`all_skills_4k.csv` - 4k job postings with skills extracted. We also have 10k dataset, but we decided to also keep this one in the project because a lot of notebooks are using this file (because it is faster to run it).

`jobs_merged_10k.csv` - the final dataset we managed to retrieve from Indeed.ca . Contains 10k job descriptions along with position names. Does not contain extracted skills

`merged_10k_skills.csv` - contains 10k job descriptions with skills extracted

`merging_with_skills.py` - a short Python file there we merge the 3 datasets with extracted skills we had. (We had to break the dataset into 3 and run skills extraction on each of the 3 because the original dataset was too big) 

`scrapeData_with_description.py` - our custom scrapper for Indeed.ca


**Note: Please, use the main branch for exploring the project. Other branches may contain code without proper acknowledgments and the datasets you might consider confusing. So, please, visit at your own risk (or better don't visit at all)**


