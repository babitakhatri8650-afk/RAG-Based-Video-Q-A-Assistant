import whisper 
import json
import os


model=whisper.load_model("large-v2")

audios=os.listdir("audio")

for audio in audios:
    if not audio.endswith(".mp3"):
        continue
    # print(audio)
    number=audio.split("_")[0]
    file_name=audio.split("_")[1][:-4]
    print(number,file_name)


    result =model.transcribe(audio=f"audio/{audio}.mp3",
                                language="hi",
                                task="translate",
                                word_timestamps=False,
        )
    
    chunks=[]
    for segment in result["segments"]:
        chunks.append({"number":number,"file_name":file_name,"start":segment["start"],"end":segment["end"],"text":segment["text"]})

    chunks_with_metadata={"chunks":chunks,"text":result["text"]}
    # create json file separately for separated file
    json_file_name=f"{number}-{file_name}.json"

    json_path=os.path.join("json",json_file_name)

    with open(json_path,"w",encoding="utf-8") as f:
        json.dump(chunks_with_metadata,f,ensure_ascii=False,indent=4)

print("All files Processed Successfully")

