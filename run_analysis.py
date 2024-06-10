import re
import pandas as pd
import glob
import matplotlib.pyplot as plt
import os


def read_deltaT_from_file(file_path):
    delta_t_values = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = re.search(r'DeltaT="([\d\.]+)"', line)
                if match:
                    delta_t_values.append(float(match.group(1)))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

    df = pd.DataFrame(delta_t_values, columns=['DeltaT'])
    return df


result_folders = 'analysis'
if not os.path.exists(result_folders):
    os.makedirs(result_folders)

all_xml_files = glob.glob('ome_metadata/*.xml')
print("All XML files:")
print(all_xml_files)

for file_path in all_xml_files:
    df = read_deltaT_from_file(file_path)
    if df is not None:
        diff_delta_t = df['DeltaT'].diff()[1:]
        max_duration = df['DeltaT'].max()
        number_frames = len(df)
        average_framerate = max_duration / (number_frames - 1)
        max_delta_t = diff_delta_t.max()
        min_delta_t = diff_delta_t.min()
        max_jitter = max_delta_t - min_delta_t

        output_path = os.path.join(result_folders, os.path.basename(file_path).replace('.xml', '.pdf'))

        title_str = f"File: {file_path}\n\n" \
                    f"Number of frames: {number_frames}\n" \
                    f"Max duration: {max_duration:.3f}s\n" \
                    f"Time/Frame: {average_framerate:.3f}s\n" \
                    f"Max DeltaT: {max_delta_t:.3f}s\n" \
                    f"Min DeltaT: {min_delta_t:.3f}s\n" \
                    f"Max jitter: {max_jitter:.3f}s\n"

        plt.figure(constrained_layout=True, figsize=(10, 6))
        plt.plot(diff_delta_t, 'o-', color='black')
        plt.xlabel('Frame Index')
        plt.ylabel('DeltaT (sec)')
        plt.title(title_str)
        plt.savefig(output_path)
        plt.close()
