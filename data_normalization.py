import rpy2.robjects as ro
import os
import pandas as pd

input_folder = "UserNetR/data/"
output_folder = "data_csv/"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".rda"):
        input_path = os.path.join(input_folder, file)

        try:
            ro.r['load'](input_path)
            print(f"Processing: {file}")

            for obj_name in ro.r.ls():
                obj = ro.r[obj_name]

                if hasattr(obj, 'colnames'):
                    df = pd.DataFrame(obj)
                    output_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}_{obj_name}.csv")
                    df.to_csv(output_path, index=False)
                    print(f"Saved: {output_path}")
                else:
                    print(f"Skipped {obj_name}: Not a dataframe")
        except Exception as e:
            print(f"Error processing {file}: {e}")

