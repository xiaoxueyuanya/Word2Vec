import json

# yelp_academic_dataset_review.json has 6990279 lines
filename = "g:/NLP/yelp_dataset/yelp_academic_dataset_review.json"
output_file_prename = "g:/NLP/yelp_dataset_review/yelp_academic_dataset_review_"

file_index = 1;
output_file_name = output_file_prename + "%03d"%file_index + ".json"
print(output_file_name)
ofile = open(output_file_name, 'w')
count = 1
with open(filename, 'r') as ifile:
    for i, line in enumerate(ifile):
        try:
            data = json.loads(line)
            # ofile.write(json.dumps(data, indent=4, ensure_ascii=False))
            ofile.write(json.dumps(data) + "\n")
            count += 1
            if(count == 10000):
                count = 1
                ofile.close()
                file_index += 1
                output_file_name = output_file_prename + "%03d"%file_index + ".json"
                print(output_file_name)
                ofile = open(output_file_name, 'w')            
        except json.JSONDecodeError:
            print(f"Error decoding JSON on line {i+1}")

ofile.close()
print("Split " + filename + " done!\n")





