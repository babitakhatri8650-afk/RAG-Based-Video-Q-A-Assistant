# HOW TO USE THIS RAG AI TEACHING ASSISTANT ON YOUR OWN DATA 

## STEP:1 COLLECT YOUR VIDEOS
move all your video files to the video folder

## STEP:2 CONVERT TO MP3
converts all the video files to mp3 by running video_to_mp3.

## STEP:3 
converts all the mp3 files to json by running mp3_to_json.

## STEP:4 CONVERTS JSON FILES TO VECTORS
Use the file preprocess_json to convert the json files to a dataframe with embeddings and save it as a joblib pickel.

## STEP:5 PROMPT GENERATION AND FEEDING TO LLM
Read the joblib file and load it into the memory. Then create a relevant prompt as per the user query and feed it to the LLM.
